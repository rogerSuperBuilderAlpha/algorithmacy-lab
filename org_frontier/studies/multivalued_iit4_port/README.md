# pyphi_iit4_mv M1 overlay

Vendored SBS-native multivalued TPM path for IIT-4.0, on the stock pin
`feature/iit-4.0` at `b78d0e342`. The same port is on
`rogerSuperBuilderAlpha/pyphi@feat/multivalued-iit4-radix-k` (`3d96339a`,
pull request #1). Upstream PyPhi 2.0 (`wmayner/pyphi` `main` at `134a8f31`,
tag `v2.0.0rc4`) matches this overlay under `pyphi.iit4_2023()`. See
[`third_party/pyphi_iit4_mv/README.md`](../../../third_party/pyphi_iit4_mv/README.md)
and [`INSTRUMENT_GAP.md`](INSTRUMENT_GAP.md).

```
python third_party/pyphi_iit4_mv/smoke_m1.py
python org_frontier/studies/multivalued_iit4_port/analyze_port.py
```
