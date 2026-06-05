"""Learned surrogate: can a model combine cheap features to predict exact Φ?

The proxy and candidate audits showed that no single cheap measure tracks exact
IIT-4.0 Φ well. This experiment asks the constructive follow-up: does a learned
model that *combines* the cheap features recover Φ? It also produces a reusable
exact-IIT-4.0 feature dataset (the kind of ground truth Hosaka et al.'s GNN work
lacked for the 4.0 formalism).
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
