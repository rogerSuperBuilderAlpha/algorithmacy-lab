"""Independent probability anchors for the observation-error TPM."""

import unittest

import numpy as np

from .probe_input_noise import input_tpm
from org_frontier.probes.weighted_quorum.probe_weighted_quorum import table_of


class InputNoiseTests(unittest.TestCase):
    def test_ten_percent_probabilities_by_active_count(self):
        # Hand-calculated binomial probabilities, indexed by true active count.
        expected = {
            1: (0.271, 0.919, 0.991, 0.999),
            2: (0.028, 0.172, 0.828, 0.972),
            3: (0.001, 0.009, 0.081, 0.729),
        }
        for quota, probabilities in expected.items():
            tpm = input_tpm(table_of((1, 1, 1), quota), 3, 0.1)
            for state in range(16):
                with self.subTest(quota=quota, state=state):
                    self.assertAlmostEqual(tpm[state, 0], probabilities[(state >> 1).bit_count()])
                    np.testing.assert_array_equal(tpm[state, 1:], [state & 1] * 3)

    def test_endpoint_can_be_biased_but_input_independent(self):
        # Fair independent observations yield OR=7/8 and AND=1/8, not 1/2.
        for quota, expected in ((1, 7 / 8), (2, 1 / 2), (3, 1 / 8)):
            tpm = input_tpm(table_of((1, 1, 1), quota), 3, 0.5)
            np.testing.assert_array_equal(tpm[:, 0], np.full(16, expected))


class MajorityCounterexampleTests(unittest.TestCase):
    def test_whole_system_phi_with_independent_golden_tpm(self):
        # Build from hand-calculated probabilities, without input_tpm/table_of/cm_numeric.
        from org_frontier.classifier.classifier import classify
        probabilities = (0.028, 0.172, 0.828, 0.972)
        tpm = np.array([[probabilities[(state >> 1).bit_count()]] + [state & 1] * 3
                        for state in range(16)], dtype=float)
        cm = np.array([[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]])
        result = classify(tpm, cm, labels=("S", "P1", "P2", "P3"))
        self.assertAlmostEqual(result.max_phi, 0.026980608910464783, places=9)
        self.assertEqual(result.structure, "triadic")


if __name__ == "__main__":
    unittest.main()
