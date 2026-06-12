export const meta = {
  name: 'question-pipeline',
  description: 'Run one research question through the six-stage protocol to a finished paper',
  whenToUse: 'Take a queued research question to a complete quantitative paper, per org_frontier/protocol/RESEARCH_PROTOCOL.md',
  phases: [
    { title: 'Review', detail: 'place the question against the logbook' },
    { title: 'Deep research', detail: 'web literature via the deep-research workflow' },
    { title: 'Hypotheses', detail: 'five falsifiable hypotheses fixed before computation' },
    { title: 'Methods', detail: 'per-hypothesis test specs' },
    { title: 'Run', detail: 'write + run probes, capture results' },
    { title: 'Paper', detail: 'assemble the paper and de-slop' },
  ],
}

// args = { id: "43", slug: "thompson_interdependence", question: "<full question text>", startProbe: 135 }
// args may arrive as an object or as a JSON string depending on the runtime.
let Q = args || {}
if (typeof Q === 'string') {
  try { Q = JSON.parse(Q) } catch (e) { throw new Error('args must be a JSON object or JSON string: ' + e.message) }
}
const id = String(Q.id)
const slug = Q.slug
const question = Q.question
const startProbe = Q.startProbe || null
const dir = `org_frontier/questions/q${id}_${slug}`

if (!id || !slug || !question) {
  throw new Error('args must include {id, slug, question[, startProbe]}')
}

const HYP_SCHEMA = {
  type: 'object',
  required: ['hypotheses'],
  properties: {
    hypotheses: {
      type: 'array', minItems: 5, maxItems: 5,
      items: {
        type: 'object',
        required: ['name', 'claim', 'null', 'predicted', 'slug'],
        properties: {
          name: { type: 'string' },
          claim: { type: 'string' },
          null: { type: 'string' },
          predicted: { type: 'string' },
          slug: { type: 'string', description: 'short snake_case id for the probe script' },
        },
      },
    },
  },
}

const METHODS_SCHEMA = {
  type: 'object',
  required: ['tests'],
  properties: {
    tests: {
      type: 'array', minItems: 5, maxItems: 5,
      items: {
        type: 'object',
        required: ['hypothesis', 'slug', 'spec'],
        properties: {
          hypothesis: { type: 'string' },
          slug: { type: 'string' },
          spec: { type: 'string', description: 'form/ensemble, measure, controls, decision rule — reproducible without code' },
        },
      },
    },
  },
}

const RESULT_SCHEMA = {
  type: 'object',
  required: ['hypothesis', 'verdict', 'numbers', 'probe_file', 'probes_row'],
  properties: {
    hypothesis: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'partial', 'refuted'] },
    numbers: { type: 'string', description: 'the key numeric results' },
    probe_file: { type: 'string' },
    probes_row: { type: 'string', description: 'a one-line PROBES.md-style result row for this test (required, never empty)' },
  },
}

phase('Review')
const review = await agent(
  `Stage 1 review for research question Q${id}: "${question}".
Read org_frontier/probes/PROBES.md and org_frontier/STRUCTURAL_FINDINGS.md. Find the prior probes that bear on this question (cite by number), what they found, and the specific gap this question opens. If a prior probe already answers it, say so. Write the review to ${dir}/review.md following the layout of org_frontier/protocol/template/review.md. Return a three-sentence summary of the gap.`,
  { phase: 'Review', label: 'review' })

phase('Deep research')
const research = await workflow('deep-research',
  `Research the question: "${question}", in the context of organization/coordination theory and integrated information. Map what the literature establishes and whether anyone has answered it. Return ~15-30 sources with DOIs/arXiv IDs and open-access status, an explicit open-gap statement, and honest caveats. Write the report to ${dir}/literature/deep_research_report.md and a bibliography to ${dir}/literature/references.bib, in the format of org_frontier/landscape/literature/deep_research_report.md.`)

phase('Hypotheses')
const hyps = await agent(
  `Stage 3 for Q${id}. Using the review at ${dir}/review.md and the deep-research report at ${dir}/literature/deep_research_report.md, write FIVE distinct, falsifiable working hypotheses, each with its structurally-expected null and the outcome it predicts, fixed before any computation. Write them to ${dir}/hypotheses.md following org_frontier/protocol/template/hypotheses.md. They must be genuinely distinct, not rephrasings. Return the five hypotheses.`,
  { phase: 'Hypotheses', label: 'hypotheses', schema: HYP_SCHEMA })

phase('Methods')
const methods = await agent(
  `Stage 4 for Q${id}. Write ${dir}/methods.md specifying one test per hypothesis from ${dir}/hypotheses.md. Use the reusable infrastructure: org_frontier/classifier/classifier.py (classify_rules, tpm_from_rules, cm_from_rules), org_frontier/probes/lib.py (verdict, major_complex, max_phi_float), org_frontier/probes/_info.py, proxy_audit/exact_phi.py. Each test states the exact form/ensemble, the measure, the controls, and a decision rule fixed before the run, plus an instrument control (a form whose verdict is already known). Follow org_frontier/protocol/template/methods.md. Return the five test specs.`,
  { phase: 'Methods', label: 'methods', schema: METHODS_SCHEMA })

phase('Run')
const results = await parallel(methods.tests.map((t, i) => () =>
  agent(
    `Stage 5 for Q${id}, hypothesis "${t.hypothesis}". Implement ${dir}/probe_${t.slug}.py per its spec in ${dir}/methods.md: ${t.spec}
Ensure the package path works: create empty org_frontier/questions/__init__.py and ${dir}/__init__.py and ${dir}/results/.gitkeep if they do not exist. The probe module must insert the repo root onto sys.path at the top (compute it from __file__) and import from org_frontier.* and proxy_audit.*, so it also runs as a direct script. FIRST assert an instrument control passes (a known form reproduces its known verdict, e.g. the strict-mediation triad reads triadic at Φ=2.0); abort if it fails. Then run the test, print exact numbers, and write any CSV to ${dir}/results/. Run it with: ~/iit-playground/venv-4.0/bin/python ${dir}/probe_${t.slug}.py 2>&1 | grep -v "Welcome to PyPhi\\|pyphi.config". If imports fail, fix the sys.path insertion and retry. Report the exact numbers, the verdict (confirmed/partial/refuted — report refutation honestly), the probe file path, and a one-line PROBES.md result row.`,
    { phase: 'Run', label: `run:${t.slug}`, schema: RESULT_SCHEMA })
)).then(r => r.filter(Boolean))

phase('Run')
const logged = await agent(
  `Append result rows to org_frontier/probes/PROBES.md for Q${id}, continuing the global probe numbering${startProbe ? ` starting at ${startProbe}` : ' (read the last probe number in the file and continue from there)'}. Add a section header "### Question Q${id} — ${slug}" and one table row per test using these rows: ${JSON.stringify(results.map(r => r.probes_row))}. Then add a short reading paragraph synthesizing the five. Do not renumber existing probes. Report the probe-number range used.`,
  { phase: 'Run', label: 'log' })

phase('Paper')
const paper = await agent(
  `Stage 6 for Q${id}. Write ${dir}/paper.md (Abstract, Introduction, Related work from the deep research, Hypotheses, Methods, Results, Discussion, Limitations, References) and a compact ${dir}/FINDINGS.md, from the results: ${JSON.stringify(results)}. Use org_frontier/protocol/template/paper.md. Every number must trace to ${dir}/results/ or the logged probes. Report refuted hypotheses as refuted. Write in the CLAUDE.md house style (no first person, plain, section titles as short noun phrases).`,
  { phase: 'Paper', label: 'paper' })

const deslop = await agent(
  `De-slop pass on ${dir}/paper.md and ${dir}/FINDINGS.md per org_frontier/CLAUDE.md: cut the antithesis machine (", not X", "X rather than Y", "is not a/the/an"), self-narration of rigor, and metronomic short openers; enforce no first person and short-noun-phrase section titles. Edit the files in place. Report the per-1000-word grep counts (em-dashes, antithesis constructions, banned openers) and confirm they are under threshold.`,
  { phase: 'Paper', label: 'deslop' })

return {
  dir,
  gap: review,
  hypotheses: hyps.hypotheses.map(h => h.name),
  results: results.map(r => ({ h: r.hypothesis, verdict: r.verdict, numbers: r.numbers })),
  probes: logged,
  deslop,
}
