"""Unit tests for cycle-ordering covariates on forms with known answers.

Run:  python -m org_frontier.ergodicity.test_cycle_order
  or: python org_frontier/ergodicity/test_cycle_order.py

No Φ. Definitions match studies/ergodic_cycle_ordering/hypotheses.md.
"""

from __future__ import annotations

import itertools
import os
import sys
import unittest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from org_frontier.ergodicity.eoa import (
    bit_observable,
    control_full_cycle_n3,
    control_identity_single,
    control_two_absorbing,
    rules_to_next_map,
    trajectory_time_average,
    uniform_ensemble,
)
from org_frontier.ergodicity.settling import (
    circular_mean_abs_remainder,
    cofilip_sync_of_cycle,
    control_chain_to_fixed,
    control_two_step_cycle,
    exact_basin_gap,
    finite_T_time_average,
    flip_signature,
    hamming_party_rate_of_cycle,
    lag1_autocorr,
    most_clumped_binary,
    most_spread_binary,
    order_components,
    order_excess_of_sequence,
    order_index_of_sequence,
    phase_lag_of_cycle,
    summarize_cycle_ordering,
)


class TestPhaseRemainderKnownAnswers(unittest.TestCase):
    def test_complete_periods_are_zero(self):
        """r = 0 ⇒ remainder is 0 at every phase, any values."""
        values = [1, 1, 0, 0]
        self.assertAlmostEqual(circular_mean_abs_remainder(values, 8), 0.0, places=12)
        self.assertAlmostEqual(circular_mean_abs_remainder(values, 4), 0.0, places=12)

    def test_clumped_versus_spread_at_T6(self):
        """Period 4, T=6, r=2. Clumped 1100 has mean |R|=1/12; spread 1010 has 0."""
        clump = [1, 1, 0, 0]
        spread = [1, 0, 1, 0]
        self.assertAlmostEqual(circular_mean_abs_remainder(clump, 6), 1.0 / 12.0, places=12)
        self.assertAlmostEqual(circular_mean_abs_remainder(spread, 6), 0.0, places=12)
        self.assertAlmostEqual(order_index_of_sequence(clump, 6), 1.0, places=12)
        self.assertAlmostEqual(order_index_of_sequence(spread, 6), 0.0, places=12)
        self.assertAlmostEqual(order_excess_of_sequence(clump, 6), 1.0 / 12.0, places=12)
        self.assertAlmostEqual(order_excess_of_sequence(spread, 6), 0.0, places=12)

    def test_window_of_one_does_not_see_order(self):
        """r=1: mean |R| depends only on the weight, so the order index is 0."""
        clump = [1, 1, 0, 0]
        spread = [1, 0, 1, 0]
        self.assertAlmostEqual(
            circular_mean_abs_remainder(clump, 5),
            circular_mean_abs_remainder(spread, 5),
            places=12,
        )
        self.assertAlmostEqual(order_index_of_sequence(clump, 5), 0.0, places=12)

    def test_two_step_on_cycle_T3(self):
        """000↔100, bit 0, T=3: each phase has |R|=1/6."""
        nxt = control_two_step_cycle()
        summary = summarize_cycle_ordering(nxt, party_indices=(0,), horizon=3)
        self.assertAlmostEqual(summary.pred_gap_cycle, 1.0 / 6.0, places=12)
        self.assertAlmostEqual(lag1_autocorr([0.0, 1.0]), -1.0, places=12)
        self.assertAlmostEqual(summary.lag1_autocorr, -1.0, places=12)
        self.assertAlmostEqual(summary.hamming_party_rate, 1.0, places=12)
        self.assertAlmostEqual(summary.cofilip_sync, 0.0, places=12)

    def test_two_step_T64_on_cycle_remainder_zero(self):
        """Period 2 divides 64, so the on-cycle predicted gap is 0."""
        nxt = control_two_step_cycle()
        summary = summarize_cycle_ordering(nxt, party_indices=(0,), horizon=64)
        self.assertAlmostEqual(summary.pred_gap_cycle, 0.0, places=12)
        self.assertAlmostEqual(summary.order_index, 0.0, places=12)
        self.assertAlmostEqual(summary.order_excess, 0.0, places=12)

    def test_full_cycle_bit_average_at_T6(self):
        """Hand-computed mean |R| on the Hamiltonian cycle, parties (0, 2), T=6.

        Bit 0 (0,1,1,0,0,1,1,0) has mean |R| = 1/12.
        Bit 2 (0,0,0,0,1,1,1,1) has mean |R| = 1/8.
        Equal average is 5/48. The cycle is the whole state space.
        """
        nxt = control_full_cycle_n3()
        summary = summarize_cycle_ordering(nxt, party_indices=(0, 2), horizon=6)
        self.assertAlmostEqual(summary.pred_gap_cycle, 5.0 / 48.0, places=12)
        self.assertEqual(summary.n_attractors, 1)
        self.assertEqual(summary.n_starts, 8)

    def test_identity_all_zero(self):
        rules = control_identity_single()
        summary = summarize_cycle_ordering(rules, party_indices=(0, 2), horizon=64)
        self.assertAlmostEqual(summary.pred_gap_cycle, 0.0, places=12)
        self.assertAlmostEqual(summary.remainder_allstarts, 0.0, places=12)
        self.assertAlmostEqual(summary.order_index, 0.0, places=12)
        self.assertAlmostEqual(summary.cofilip_sync, 0.0, places=12)
        self.assertAlmostEqual(summary.phase_lag, 0.0, places=12)
        self.assertAlmostEqual(summary.hamming_party_rate, 0.0, places=12)
        self.assertAlmostEqual(summary.lag1_autocorr, 0.0, places=12)
        self.assertEqual(summary.n_attractors, 8)

    def test_fixed_point_chain_predicted_gap_zero(self):
        """The unique attractor is the fixed point 000, so the cycle remainder is 0."""
        nxt = control_chain_to_fixed()
        summary = summarize_cycle_ordering(nxt, party_indices=(0, 2), horizon=64)
        self.assertAlmostEqual(summary.pred_gap_cycle, 0.0, places=12)
        # Transients still move the all-start remainder off the cycle mean.
        self.assertGreater(summary.remainder_allstarts, 0.0)


class TestOrderingFeatures(unittest.TestCase):
    def test_coflip_staggered_versus_synchronous(self):
        staggered = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        sync = [(0, 0, 0), (1, 1, 0)]
        parties = (0, 1)
        self.assertAlmostEqual(cofilip_sync_of_cycle(staggered, parties), 0.0, places=12)
        self.assertAlmostEqual(cofilip_sync_of_cycle(sync, parties), 1.0, places=12)
        self.assertAlmostEqual(hamming_party_rate_of_cycle(staggered, parties), 0.5, places=12)
        self.assertAlmostEqual(hamming_party_rate_of_cycle(sync, parties), 1.0, places=12)

    def test_phase_lag_in_phase_and_anti_phase(self):
        # Period 4. Bit 0 and bit 1 identical ⇒ lag 0. Bit 1 flipped ⇒ anti-phase.
        in_phase = [(1, 1), (1, 1), (0, 0), (0, 0)]
        anti = [(1, 0), (1, 0), (0, 1), (0, 1)]
        self.assertAlmostEqual(phase_lag_of_cycle(in_phase, (0, 1)), 0.0, places=12)
        self.assertAlmostEqual(phase_lag_of_cycle(anti, (0, 1)), 1.0, places=12)

    def test_lag1_clump_positive_alternate_negative(self):
        self.assertGreater(lag1_autocorr([1, 1, 1, 0, 0, 0]), 0.0)
        self.assertAlmostEqual(lag1_autocorr([1, 0, 1, 0, 1, 0]), -1.0, places=12)
        self.assertIsNone(lag1_autocorr([1, 1, 1]))

    def test_flip_signature_canonical_rotation(self):
        cycle = [(0, 0, 0), (1, 0, 0)]
        sig = flip_signature(cycle, (0, 1, 2))
        self.assertEqual(sig, "100-100")
        # A rotation of the same masks must canonicalize to the same string.
        rotated = [(1, 0, 0), (0, 0, 0)]
        self.assertEqual(flip_signature(rotated, (0, 1, 2)), sig)

    def test_spread_and_clump_bound_binary_necklaces(self):
        """For every binary cycle with period ≤ 12 and the horizons below,
        R_spread ≤ R_obs ≤ R_clump, so the order index lies in [0, 1] up to
        1e-8 on that grid. The definition remains the ratio if a longer
        cycle ever exits the interval.
        """
        horizons = (1, 6, 16, 64, 128)
        for period in range(1, 13):
            for bits in itertools.product((0, 1), repeat=period):
                for horizon in horizons:
                    observed, spread, clump = order_components(bits, horizon)
                    self.assertLessEqual(spread, observed + 1e-9)
                    self.assertLessEqual(observed, clump + 1e-9)
                    # The named placements attain the bounds.
                    weight = sum(bits)
                    self.assertAlmostEqual(
                        circular_mean_abs_remainder(
                            most_spread_binary(period, weight), horizon
                        ),
                        spread,
                        places=12,
                    )
                    self.assertAlmostEqual(
                        circular_mean_abs_remainder(
                            most_clumped_binary(period, weight), horizon
                        ),
                        clump,
                        places=12,
                    )


class TestClosedFormMatchesTrajectory(unittest.TestCase):
    def test_finite_T_matches_trajectory_time_average(self):
        forms = [
            control_chain_to_fixed(),
            control_two_step_cycle(),
            control_full_cycle_n3(),
            rules_to_next_map(control_identity_single()),
            rules_to_next_map(control_two_absorbing()),
        ]
        horizons = (1, 2, 3, 5, 7, 8, 16, 64)
        for nxt in forms:
            n = len(next(iter(nxt)))
            for start in uniform_ensemble(n):
                for bit in range(n):
                    obs = bit_observable(bit)
                    for horizon in horizons:
                        closed = finite_T_time_average(nxt, start, obs, horizon)
                        walked = trajectory_time_average(
                            nxt, start, obs, horizon=horizon, noise=0.0
                        )
                        self.assertAlmostEqual(
                            closed, walked, places=9, msg=(start, bit, horizon)
                        )

    def test_exact_basin_gap_matches_instrument(self):
        from org_frontier.ergodicity.eoa import REFERENCE_BASIN, run_eoa_parties

        forms = [
            ("chain", control_chain_to_fixed()),
            ("two", control_two_step_cycle()),
            ("cycle", control_full_cycle_n3()),
            ("id", rules_to_next_map(control_identity_single())),
        ]
        for _name, nxt in forms:
            for horizon in (3, 6, 16, 64):
                closed = exact_basin_gap(nxt, (0, 2), horizon=horizon)
                instrument = run_eoa_parties(
                    nxt,
                    (0, 2),
                    horizon=horizon,
                    noise=0.0,
                    reference_mode=REFERENCE_BASIN,
                )
                self.assertAlmostEqual(
                    closed, instrument.gap_mean, places=9, msg=(_name, horizon)
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
