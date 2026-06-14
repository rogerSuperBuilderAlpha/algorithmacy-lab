"""Q83 forms: two recipient-side gating agents over the outreach triad (E, M, R, T1, T2).

Base triad E'=M, M'=E&R, R'=M. Two triage agents T1,T2 gate delivery to R. Each agent reads the message
(Ti'=M, bidirectional candidate). 'Both-required' gating: R'=M & T1 & T2. 'Either-suffices': R'=M & (T1|T2).
Single-agent control reuses the Q68 bidirectional triage (one agent).
"""
import os, sys
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

# indices E=0,M=1,R=2,T1=3,T2=4
LABELS5 = ("E", "M", "R", "T1", "T2")
BOTH_REQUIRED = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3] & x[4], lambda x: x[1], lambda x: x[1]]
EITHER_SUFFICES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & (x[3] | x[4]), lambda x: x[1], lambda x: x[1]]

# single bidirectional gating agent (Q68 bidirectional), E,M,R,T indices 0..3
LABELS4 = ("E", "M", "R", "T")
SINGLE_BIDIR = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[1]]
