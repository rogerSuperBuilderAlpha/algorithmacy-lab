"""Probe 464: does the extremes-only quorum law survive input observation errors?

Hypotheses: noisy OR/AND keep the full core, majority keeps zero whole-system
Phi, and weighted boundary forms keep their smaller cores with zero whole Phi.
Method: exact observation-error TPMs for five forms at eta=0, 0.1, 0.5;
controls and decision rules are in weighted_quorum/input_noise/hypotheses.md.
Run: python -m org_frontier.probes.probe_quorum_input_noise
Add --write to regenerate the state-profile artifact in weighted_quorum/input_noise.
"""

from org_frontier.probes.weighted_quorum.input_noise.probe_input_noise import main


if __name__ == "__main__":
    main()
