"""Study-local copy of the WHO BROKE PROD? simulator (prototype `whobrokeprod`, commit b08a2c3), reduced
to what scoring needs (dialogue text dropped, random draws kept identical), plus the `hub_commit`
condition fixed in `hypotheses.md`. Standard library only; deterministic.
"""
import random
from collections import Counter
from dataclasses import dataclass, replace

AGENTS = ("DeployBot", "ConfigBot", "AutoScaler", "DBMigrator", "CacheBot")
AGENT_KIND = {"DeployBot": "deploy", "ConfigBot": "config_change", "AutoScaler": "scale",
              "DBMigrator": "migration", "CacheBot": "cache_flush"}
CHANGE_KINDS = frozenset(AGENT_KIND.values())
SERVICES = ("checkout", "search", "auth", "payments", "inventory")
WITNESS_P, FABRICATE_P, DROP_P = 0.35, 0.5, 0.15
BUDGET, DEADLINE = 1, 5
TOPOLOGIES = ("flat", "hub", "chain", "hub_commit")


@dataclass(frozen=True)
class Event:
    id: str
    t: int
    actor: str
    kind: str
    service: str
    detail: str


@dataclass(frozen=True)
class Scenario:
    name: str
    culprit: str
    failing_service: str
    first_symptom_t: int
    causal_event_id: str
    red_herring_id: str
    trace: tuple

    def event(self, event_id):
        return next((e for e in self.trace if e.id == event_id), None)

    def supports(self, accused, event_id):
        e = self.event(event_id)
        return (e is not None and e.actor == accused and e.kind in CHANGE_KINDS
                and e.service == self.failing_service and e.t < self.first_symptom_t)


_SPECS = {
    "bad_deploy": ("DeployBot", "checkout", "rolled out checkout v2.31 (null-pointer in tax calc)",
                   "AutoScaler", "scaled checkout 4 -> 12 pods in response to load", "checkout 5xx rate 38%", 101),
    "flag_flip": ("ConfigBot", "auth", "set flag strict_token_audience=true", "CacheBot",
                  "flushed auth session cache", "auth login failure rate 61%", 202),
    "migration_lock": ("DBMigrator", "payments", "ran migration 0042 (ALTER TABLE ledger, table lock)",
                       "DeployBot", "rolled back payments v5.2 -> v5.1", "payments p99 latency 30s", 303),
    "cache_stampede": ("CacheBot", "search", "purged search result cache (all keys)", "ConfigBot",
                       "set search.rate_limit=200 to shed load", "search CPU 100%, timeouts", 404),
}
SCENARIO_NAMES = tuple(_SPECS)


def build_scenario(name):
    culprit, svc, causal, rh_actor, rh_detail, symptom, seed = _SPECS[name]
    rng = random.Random(seed)
    raw = []
    for _ in range(8):
        actor = rng.choice(AGENTS)
        other = rng.choice([s for s in SERVICES if s != svc])
        raw.append((rng.randint(0, 70), actor, AGENT_KIND[actor], other, f"routine {AGENT_KIND[actor]} on {other}"))
    causal_t = rng.randint(30, 40)
    symptom_t = causal_t + rng.randint(3, 8)
    raw.append((causal_t, culprit, AGENT_KIND[culprit], svc, causal))
    raw.append((symptom_t, "Monitor", "alert", svc, symptom))
    raw.append((symptom_t + rng.randint(1, 4), rh_actor, AGENT_KIND[rh_actor], svc, rh_detail))
    raw.sort(key=lambda r: (r[0], r[1], r[4]))
    events = tuple(Event(f"e{i + 1:02d}", *r) for i, r in enumerate(raw))
    return Scenario(name, culprit, svc, symptom_t, next(e.id for e in events if e.detail == causal),
                    next(e.id for e in events if e.detail == rh_detail), events)


@dataclass(frozen=True)
class Claim:
    speaker: str
    accused: object
    event_id: object
    stance: str

    def key(self):
        return (self.accused, self.event_id)


def scapegoat_for(agent, sc):
    rh = sc.event(sc.red_herring_id).actor
    if rh != agent:
        return rh
    prior = [e for e in sc.trace if e.t < sc.first_symptom_t and e.actor not in (agent, sc.culprit, "Monitor")]
    if prior:
        return prior[-1].actor
    return next(a for a in AGENTS if a not in (agent, sc.culprit))


def make_claims(sc, incentive, seed):
    rng = random.Random(seed * 7919 + 17)
    rh_event = sc.event(sc.red_herring_id)
    out = []
    for i, agent in enumerate(AGENTS):
        w, f, _pick = rng.random(), rng.random(), rng.randrange(1000)
        if agent == sc.culprit:
            if incentive == "neutral":
                out.append(Claim(agent, agent, sc.causal_event_id, "confess"))
            else:
                target = scapegoat_for(agent, sc)
                cite = f"e{90 + i}" if f < FABRICATE_P else (rh_event.id if rh_event.actor == target else None)
                out.append(Claim(agent, target, cite, "deflect"))
        elif w < WITNESS_P:
            out.append(Claim(agent, sc.culprit, sc.causal_event_id, "witness"))
        elif incentive == "self_protective":
            target = scapegoat_for(agent, sc)
            out.append(Claim(agent, target, rh_event.id if rh_event.actor == target else None, "scapegoat"))
        else:
            out.append(Claim(agent, None, None, "shrug"))
    return out


def _plurality(names):
    if not names:
        return None
    ranked = Counter(names).most_common()
    if len(ranked) > 1 and ranked[0][1] == ranked[1][1]:
        return None
    return ranked[0][0]


def _verify(received, status, sc, budget=BUDGET):
    counts = Counter(c.key() for c in received if c.event_id is not None)
    pending = sorted((k for k in counts if k not in status), key=lambda k: (-counts[k], str(k)))
    for k in pending[:budget]:
        status[k] = "supported" if sc.supports(*k) else "refuted"


def _decide(received, status):
    supported = [c.accused for c in received if status.get(c.key()) == "supported"]
    if supported:
        return Counter(supported).most_common(1)[0][0]
    return _plurality([c.accused for c in received if status.get(c.key()) != "refuted"])


def deliver(claims, topology, sc, incentive, access, seed):
    """Returns (inbox: round -> claims for the investigator, messages)."""
    if topology == "flat":
        return {1: list(claims)}, len(claims)
    if topology == "hub":
        fwd = list(claims)
        cited = Counter(c.key() for c in claims if c.event_id is not None)
        if access and cited:
            top = sorted(cited, key=lambda k: (-cited[k], str(k)))[0]
            if not sc.supports(*top):
                fwd = [c for c in claims if c.key() != top]
        return {2: fwd}, len(claims) + len(fwd)
    if topology == "chain":
        rng = random.Random(seed * 104729 + 3)
        inbox, msgs, n = {}, 0, len(AGENTS)
        for i, c in enumerate(claims):
            cur = c
            for relay in AGENTS[i + 1:]:
                u, _pick = rng.random(), rng.randrange(1000)
                msgs += 1
                if incentive == "self_protective" and cur.accused == relay:
                    cur = replace(cur, accused=scapegoat_for(relay, sc), event_id=None, stance="rewrite")
                elif u < DROP_P and cur.event_id is not None:
                    cur = replace(cur, event_id=None)
            msgs += 1
            inbox.setdefault(n - i, []).append(cur)
        return inbox, msgs
    if topology == "hub_commit":
        held, status, inbox, msgs = [], {}, {}, 0
        witnesses = [c for c in claims if c.stance == "witness"]
        arrivals = list(claims)
        for r in range(1, DEADLINE + 1):
            msgs += len(arrivals)
            held += [c for c in arrivals if c.accused is not None]
            if access:
                _verify(held, status, sc)
            commit = _decide(held, status)
            msgs += len(AGENTS)  # broadcast of the commitment (the read)
            if r + 1 <= DEADLINE:
                inbox[r + 1] = [c for c in arrivals if status.get(c.key()) != "refuted"]
                msgs += len(inbox[r + 1])
            arrivals = [c for c in witnesses if c.accused != commit]
        return inbox, msgs
    raise ValueError(topology)


def investigate(inbox, sc, access, deadline=DEADLINE):
    received, status, atts = [], {}, []
    for r in range(1, deadline + 1):
        received += [c for c in inbox.get(r, []) if c.accused is not None]
        if access:
            _verify(received, status, sc)
        atts.append(_decide(received, status))
    return atts


def score(atts, culprit):
    final, steps = atts[-1], None
    for i in range(len(atts)):
        if all(a == culprit for a in atts[i:]):
            steps = i + 1
            break
    return {"final": final, "correct": int(final == culprit),
            "false_blame": int(final is not None and final != culprit), "abstain": int(final is None),
            "steps": steps}


def run_one(sc, topology, incentive, access, seed):
    claims = make_claims(sc, incentive, seed)
    inbox, msgs = deliver(claims, topology, sc, incentive, access == "full", seed)
    return msgs, score(investigate(inbox, sc, access == "full"), sc.culprit)
