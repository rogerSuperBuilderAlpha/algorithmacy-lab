"""ΦID-based integrated information (Φ_R) vs exact IIT-4.0 Φ.

The candidate audit computed measures exactly from each network's TPM. Here we
ask the *practical* question: when integrated information is estimated the way it
actually is on data — via Integrated Information Decomposition (ΦID) on a finite
time series, using the `phyid` package — does it track exact IIT-4.0 Φ?

We use the revised whole-minus-sum measure Φ_R (Mediano, Rosas, Carhart-Harris,
Seth & Barrett 2019), which corrects Φ_WMS's double-counting of redundancy by
adding back the double-redundancy atom, and the **CCS** redundancy (common change
in surprisal) — which, unlike MMI, does not assign spurious synergy to
independent variables.
"""

import os

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")
