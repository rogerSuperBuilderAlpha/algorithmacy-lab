# Q123 — Stage 2 literature: reproducibility of an IIT verdict

## The question in context

The critical review's T6 charges that "exact IIT-4.0 Φ" is one config of an unpinned, mutable build. The
charge has three parts: the build is not pinned (a moving branch, no commit), the config is unreported, and a
reviewer read SYSTEM_CUTS = 3.0_STYLE as evidence the verdict is a 3.0-style variant rather than canonical
4.0. Each part is checkable.

## What the field and the build establish

- **Computational reproducibility needs a pinned environment.** A moving Git branch is not a reproducible
  dependency; the remedy is a commit hash plus a config dump (the standard for computational claims). The
  build here is installable at a fixed commit, and PyPhi's config is fully introspectable.
- **PyPhi separates the IIT-3.0 and IIT-4.0 computations.** The system integrated information of IIT 4.0 is
  computed by `pyphi.new_big_phi` over the 4.0 system partitions; the legacy `big_phi` is the 3.0 quantity.
  SYSTEM_CUTS is a legacy option documented as controlling "traditional IIT 3.0 cuts" for the legacy
  computation, so whether it touches the 4.0 verdict is a matter of which code path reads it.
- **The repertoire distance is the substantive measure choice.** IIT 4.0's small-Φ is built on the intrinsic
  difference; other distances (EMD, KLD, L1) belong to other formulations and are not interchangeable on the
  4.0 path. Whether any alternative even runs there bounds how much the verdict is a free config choice.
- **Versions can disagree.** Whether IIT 3.0 and IIT 4.0 return the same verdict is an open question the
  program's agenda already lists (#8). The legacy 3.0 computation is a separate path, not a config toggle.

## The gap Q123 fills

The program reported verdicts without pinning the build, recording the config, or testing config-invariance.
Q123 does all three, and isolates which config choices the verdict depends on and which it does not.
