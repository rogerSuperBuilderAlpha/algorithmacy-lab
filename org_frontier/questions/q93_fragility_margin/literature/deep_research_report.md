# Q93 literature — a robustness gradient under a binary verdict

## The gap

The verdict is binary at Φ_MIP = 0: a form is triadic or dyadic, with nothing said about how close a
triadic form sits to the dyadic boundary. The corpus repeatedly finds that a single edge, read function,
or party toggles the verdict (the `classifier` minimal test cases, Finding 1), which suggests the verdict
is structurally fragile but does not measure the fragility. A margin-to-dyadic metric — the smallest
structural perturbation that collapses a triadic form — turns the binary verdict into a gradient.

## Why a structural margin might predict noise survival

Q71 found the outreach verdict degrades gracefully under stochastic noise, with Φ falling smoothly rather
than snapping to zero. Two notions of robustness are in play: a structural one (how many single-bit edits
preserve the verdict) and a dynamical one (how much Φ survives added noise). They need not agree —
structural distance in rule space and attenuation under output noise are different operations. Whether the
cheap structural margin predicts the dynamical survival is the question; a positive result would let a
form's robustness be read off its structure without simulating noise.

## The parity connection

Finding 4 showed parity determinations (XOR, XNOR) yield triadic forms twice as often as monotone ones.
Whether parity also yields the more *robust* triads is a separate claim — frequency and robustness are
distinct — and a natural extension of that finding.

## Method context

The perturbation is exhaustive over single-bit flips of the eight-bit form encoding; the noise model is
the repo's standard output-noise mix (`proxy_bridge.bridge.add_noise`), with exact Φ recomputed on the
noisy TPM.
