# Hypotheses — reproducibility signaling in management research

*Committed before any corpus is harvested or coded. The question: how often do recent
management and organization empirical papers signal reproducibility practices — open data, code
availability, pre-registration, or shared materials — and is that signaling rising over time?
This is a descriptive review. Each hypothesis names the knowledge claim it tests (in the
knowledge-weaving typology), its operationalization, and the outcome that would support versus
challenge it.*

The open-science movement reached management research later than it reached psychology. Journals
in the field have added data-availability policies, badge programs, and registered-report tracks
over the past decade. Whether authors act on those policies — and say so where a reader can see it
— is a measurable question. This review measures the visible signal in titles and abstracts (and
any data-availability statement text present), which is what a reader or a screening tool sees
first.

## H1 — Signaling is uncommon overall
- **Knowledge claim (stylized fact):** most management empirical papers do not signal any
  reproducibility practice; open data, shared code, and pre-registration remain minority behaviors
  in the field.
- **Operationalization:** the share of empirical papers coded `yes` on at least one of `open_data`,
  `code_available`, `preregistered`, measured on the adjudicated dataset.
- **Predicts:** any-signal papers are a minority — well under half of the corpus.
- **Challenged if:** a majority of empirical papers signal at least one practice.

## H2 — Signaling has risen over 2015–2025
- **Knowledge claim (key assumption):** open-science norms have diffused into management research
  over the decade, so signaling should be more common in recent years than in the mid-2010s.
- **Operationalization:** the any-signal rate by year period (2015–2019 vs 2020–2025), on the
  adjudicated dataset joined to corpus year.
- **Predicts:** the later period's any-signal rate exceeds the earlier period's.
- **Challenged if:** the later rate is equal to or below the earlier rate.

## H3 — Quantitative papers signal more than qualitative ones
- **Knowledge claim (enduring critique):** the open-science apparatus (data repositories,
  pre-registration, code) was built around quantitative work, so quantitative papers signal
  reproducibility more often than qualitative papers, whose data (interviews, field notes) are
  harder to share and whose traditions did not adopt pre-registration.
- **Operationalization:** the any-signal rate for `method_type=quantitative` versus
  `method_type=qualitative`, on the adjudicated dataset.
- **Predicts:** quantitative any-signal rate exceeds qualitative any-signal rate.
- **Challenged if:** qualitative signaling equals or exceeds quantitative signaling.

## Method fixed in advance
- Corpus boundary and search: `methods.md` (substantive + procedural gates; semantic-search harvest).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`.
- Reliability reported (Fleiss' κ). Any hypothesis the data contradict is reported as challenged.
- **Load-bearing limitation, fixed here:** coding is from title + abstract (plus any
  data-availability statement text present in the record). Many journals place data-availability
  statements in the paper body, not the abstract, so abstract-only coding undercounts real
  practice. Every signaling rate this review reports is a **lower bound**.
