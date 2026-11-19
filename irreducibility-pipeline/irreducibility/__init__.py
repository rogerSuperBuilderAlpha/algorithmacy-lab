"""irreducibility: exact irreducibility analysis of coordinative structures with PyPhi (IIT 4.0)."""

from .core import (PHI_EPS, Verdict, classify, classify_rules, cm_from_rules, major_complex,
                   tpm_from_rules, verdict)
from .regime import regime
from .contingency import contingency_test
from .spread import spread
from .rules import compile_rule, compile_rules

__version__ = "0.1.0"
