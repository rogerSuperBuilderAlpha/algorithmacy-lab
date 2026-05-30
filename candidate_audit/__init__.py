"""Candidate-measure audit: do the published 'candidate Φ' measures track exact
IIT-4.0 Φ?

Audits the family of practical integrated-information measures compared in
Mediano, Seth & Barrett (2019), *Measuring Integrated Information: Comparing
Candidate Measures* / *Evaluating Approximations and Heuristic Measures of
Integrated Information* — against the exact IIT-4.0 Φ that those measures were
never benchmarked against (because exact Φ was intractable for them).
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
