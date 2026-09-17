"""Probe exact IIT-4.0 Φ on a MultivaluedNetwork; report M2 blocker locus."""

from __future__ import annotations

import traceback
from typing import Any

from pyphi import Subsystem, exceptions, new_big_phi

from .network import MultivaluedNetwork
from .tpm import MultivaluedTPMError


def probe_exact_phi_blocker(
    network: MultivaluedNetwork, state: tuple[int, ...]
) -> dict[str, Any]:
    """Attempt stock ``new_big_phi`` / ``Subsystem`` on an M1 network.

    Returns a structured report. Does not invent proxy Φ.
    """
    report: dict[str, Any] = {
        "attempted": True,
        "phi": None,
        "blocked": True,
        "locus": "",
        "error_type": "",
        "error": "",
        "traceback_tail": "",
    }
    try:
        Subsystem(network, state)
        mc = new_big_phi.maximal_complex(network, state)
        if isinstance(mc, new_big_phi.NullPhiStructure):
            report["blocked"] = False
            report["phi"] = 0.0
            report["locus"] = "NullPhiStructure (no irreducible complex)"
        else:
            report["blocked"] = False
            report["phi"] = float(mc.phi)
            report["locus"] = "phi_computed"
    except MultivaluedTPMError as e:
        report["error_type"] = type(e).__name__
        report["error"] = str(e)
        report["locus"] = (
            "Subsystem.__init__ → network.tpm.condition_tpm "
            "(non-empty background; M2 mixed-radix conditioning)"
        )
    except exceptions.StateUnreachableError as e:
        report["error_type"] = type(e).__name__
        report["error"] = str(e)
        report["locus"] = "validate.state_reachable / binary SBN assumptions"
    except ValueError as e:
        report["error_type"] = type(e).__name__
        report["error"] = str(e)
        msg = str(e)
        if "zeros and ones" in msg:
            report["locus"] = (
                "validate.node_states — stock pin allows only binary "
                "state tuples (M2 must accept alphabet digits)"
            )
        elif "current_state must have length" in msg:
            report["locus"] = (
                "Subsystem.__init__ → tpm.backward_tpm → "
                "probability_of_current_state — treats SBS matrix as "
                "binary SBN (last axis = nodes); M2 needs SBS-native "
                "backward TPM / cause repertoire"
            )
        else:
            report["locus"] = f"ValueError in stock Subsystem/new_big_phi: {e}"
    except Exception as e:  # noqa: BLE001 — probe must surface any locus
        report["error_type"] = type(e).__name__
        report["error"] = str(e)
        report["locus"] = f"unexpected: {type(e).__name__}"
        report["traceback_tail"] = "".join(
            traceback.format_exception(type(e), e, e.__traceback__)[-4:]
        )
    return report
