# Q59 — Stage 4 methods

## Ensemble and controls

- **Panel:** Sixteen aligned one-sided bijective parity ceiling pairs from Q55–Q56 (`one_sided_ceiling()`).
- **Reuse:** Q58 `norm_cut_utils.py` (min-norm partition detail, `cut_ones`, `partition._cut_matrix`);
  Q57 `direction_mip_utils.py` (recipient/non-recipient cut identification, topology classes).
- **Q59 extension:** `cut_edge_utils.py` (directed-edge extraction from cut matrices, cross-edge
  identification from connectivity matrix, symmetric-difference templates).
- **Instrument control:** Canonical triad `[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]` must
  read triadic, max_phi=2.0, MIP first line `2 parts: {W,SC}`. Abort if control fails.

## Directed-edge extraction

For each min-norm at-system-Phi partition representative (Q58 `min_norm_detail`):

- `cut_matrix` — `numpy.array(partition._cut_matrix)`, shape 3×3, rows/cols indexed W,S,C.
- `severed_edges` — sorted list of directed edges `X→Y` where `cut_matrix[i,j]=1` for
  `LABELS[i]=X`, `LABELS[j]=Y`.
- `cross_edge` — from `cm_from_rules`: `W→C` if `cm[0,2]=1`, else `C→W` if `cm[2,0]=1`.
- `only_tied` — edges in tied severed set minus excluded severed set; `only_excl` the converse.
- `adj_cut_ones` — `cut_ones - int(cut_matrix[cross_src, cross_tgt])` per cut.

Recipient (tied) and non-recipient (excluded) cuts follow Q57 `expected_tied_cut` / `excluded_outer_cut`.

## H1 test — cross-edge shared severance

- **Measure:** whether `cross_edge ∈ severed_tied` and `cross_edge ∈ severed_excl`.
- **Decision rule:** Confirmed if 16/16 pairs have cross-edge in both sets; partial if 15/16; refuted if
  any pair has cross-edge in only one set or in neither.

## H2 test — symmetric-difference size

- **Measure:** `|only_tied|`, `|only_excl|`, and `|only_tied| + |only_excl|`.
- **Decision rule:** Confirmed if 16/16 pairs have |only_tied|=3, |only_excl|=1, total symdiff=4; partial
  if 15/16; refuted otherwise.

## H3 test — cross-edge subtraction equalizes counts

- **Measure:** `adj_tied = cut_ones_tied - cross_in_tied`, `adj_excl = cut_ones_excl - cross_in_excl`;
  test equality `adj_tied == adj_excl`.
- **Decision rule:** Confirmed if 16/16 equal; partial if 15/16; refuted if 0/16 equal (expected refutation).

## H4 test — mediator edges in recipient-only difference

- **Measure:** count of edges in `only_tied` where S appears as source or target; `adj_ratio =
  adj_tied / adj_excl`.
- **Decision rule:** Confirmed if 16/16 have mediator count 2 and adj_ratio 3.0 with spread 0; partial if
  mediator count 2 on 15/16; refuted otherwise.

## H5 test — recipient-template gate invariance

- **Measure:** compare `only_tied` and `only_excl` frozensets against fixed templates:
  - worker: only_tied=`{S→W, W→C, W→S}`, only_excl=`{C→S}`
  - counterpart: only_tied=`{C→S, C→W, S→C}`, only_excl=`{W→S}`
- **Decision rule:** Confirmed if 8/8 worker and 8/8 counterpart match; partial if one mismatch; refuted if
  two or more mismatches or gate polarity swaps templates.
