"""Q73 keystone forms: one representative per pillar of the outreach-coordination law (q63-q72)."""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

# joint determination + liveness (q63): read_recipient triadic, broadcast dyadic, one_shot dyadic
READ_RECIPIENT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]          # ("E","M","R")
BROADCAST = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]
ONE_SHOT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]
# non-substitutability (q64/q70): all_required triadic, substitutable dyadic  ("E","M","R1","R2")
ALL_REQUIRED = [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]]
SUBSTITUTABLE = [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]]
# depth (q66): closed ring binds all  ("E","A1","A2","R")
RING4 = [lambda x: x[3] & x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2] & x[0]]
