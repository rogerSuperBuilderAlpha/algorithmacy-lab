"""q217 probe: human-autopilot shared control of a robot (H, P, R)."""
from org_frontier.probes.lib import verdict, major_complex

LABELS = ("H", "P", "R")
MODELS = [
    ("1 teleoperation            H'=R, P'=R, R'=H  ", [lambda x: x[2], lambda x: x[2], lambda x: x[0]]),
    ("2 full autonomy            H'=R, P'=R, R'=P  ", [lambda x: x[2], lambda x: x[2], lambda x: x[1]]),
    ("3 shared control           H'=R, P'=R, R'=H&P", [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[1]]),
    ("4 shared, human fb cut     H'=H, P'=R, R'=H&P", [lambda x: x[0], lambda x: x[2], lambda x: x[0] & x[1]]),
]

if __name__ == "__main__":
    for name, rules in MODELS:
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        print(f"{name} -> {v.structure}  Φ_MIP max={v.max_phi:.4f}  major complex={core} φ={phi:.4f}")
