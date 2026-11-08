---
key: villalobos2018enactive
apa: "Villalobos, M., & Dewhurst, J. (2018). Enactive autonomy in computational systems. *Synthese*, *195*(5), 1891–1908. https://doi.org/10.1007/s11229-017-1386-z"
authors: "Villalobos, Mario; Dewhurst, Joe"
year: 2018
registered_year: 2017
title: "Enactive autonomy in computational systems"
venue: "Synthese"
volume: "195"
issue: "5"
pages: "1891–1908"
doi: "10.1007/s11229-017-1386-z"
url: ""
type: article
facets: [F2]
claims: [c4]
role: contrast
load: load-bearing
read_depth: full_text
object_read: "Publisher version of record (Springer open-access PDF, CC BY 4.0, 18 pp. plus a blank page), and its text layer villalobos2018enactive.txt at ~/iit-playground/pt_ai_animation_local/pdfs/villalobos2018enactive/, fetched by S4 from link.springer.com (FETCH_LOG.tsv); read in full 2026-11-08 (pp. 1891–1908, including footnotes and reference list); sha256 7f136dddd81f51d678b696809d6ef03fed3b12aa7aa06ab3218fe8951989829e (PDF; recomputed with shasum -a 256, matches sha256.txt)"
verified: verified
verified_against: "crossref.json; Springer VoR PDF sha256 recomputed; full text layer, 15 quotations traced"
prior_cards: []
status: cited
added: 2026-11-08
run: pta-lib-2026-11
---

# Villalobos & Dewhurst (2018), Enactive autonomy in computational systems

## What it argues

Mario Villalobos and Joe Dewhurst argue that a computational system can meet the criteria for autonomy
that classical enactivism (CE) sets out. CE, in Thompson's canonical form, treats autonomy as the mark
that sets living and cognitive systems apart from machines. An autonomous system is self-determining,
organizationally and operationally closed, and precarious. A heteronomous system, by contrast, works by
input–output information flow and external control; Thompson's example is the automatic bank machine.
Villalobos and Dewhurst take the first two criteria back to Maturana's autopoietic theory. Maturana's
*functional closure* says that a sensor–effector circuit closed through its environment, like a
thermostat with both parts in one house, has no intrinsic inputs or outputs. On this view an observer
assigns them for her own purposes. Maturana's *structural determinism* says that external events only
trigger changes in any physical system, living or not; they never instruct it.

The authors then apply both ideas to a physically built Turing machine, following Wells's reading of
the tape as the machine's environment. The head reads and writes; the tape loops the effector's work back
to the sensor; so the machine is functionally closed and shows organizational-operational autonomy
(OA, §5). Its own configuration decides what a mark on the tape triggers, so it is structurally
determined and shows self-determination autonomy (SDA, §6). For precariousness (§7), they imagine a
mobile Turing machine whose computations find the chemical energy that powers those computations. That
loop of enabling conditions would give it "at least some degree" of precarious autonomy. They concede
the sketch proves nothing conclusive and leaves aside normativity, teleology and individuation. They
also stay neutral throughout: they defend neither enactivism nor computationalism, and they claim only
that CE's autonomy criterion alone need not rule out computational systems.

## What the paper uses it for

- **c4** (an organizational account of life fits the system around the LLM): contrast, as DECISIONS
  assigns it (it replaces Thompson 2007 as the self-production counter). The source in fact cuts both
  ways, and the paper should use both edges.
  - *Where it helps c4.* Villalobos and Dewhurst show that the heteronomy objection, that machines are
    "determined and controlled from the outside", does not follow from CE's own criteria for closure and
    self-determination. They also show that the system's boundary depends on its functional loop, not on
    its casing: the tape links effector to sensor, "thus becoming a part of the computing system as a whole"
    (p. 1902; the sentence starts on p. 1901).
    The same move could draw an LLM's harness, tools and memory inside the system the paper calls the AI.
    That extension is the paper's, not theirs.
  - *What it would object to.* (1) The paper's thesis needs a *life* account. Villalobos and Dewhurst
    address only CE's *autonomy* criterion. They bracket whether autopoietic or biological systems are
    Turing computable (fn. 4), they say precariousness is shown only "in a modest sense", and they leave
    out self-production entirely. On their reading, closure and structural determinism are cheap: a
    thermostat has both. So meeting them does not make the system around the LLM living. (2) Their
    precariousness test cuts against c4 directly. CE counts a system as precarious only if its processes
    would stop without the closed network. Villalobos and Dewhurst note that engineers usually build the
    reverse: a machine as "robust and durable as possible", with an energy supply independent of its
    computations, solving "a problem that is relevant for us as users, not for the machine itself"
    (p. 1906). A deployed LLM system with harness, VMs and data-centre power fits that description. Its
    operators keep it running whatever it computes. Under CE's criteria, then, it fails precariousness,
    and the organizational account the paper wants would not apply unless the paper drops or reworks
    that criterion. (3) Their autonomy is a property of the machine with its tape. The paper's "system
    around the LLM" includes developers, studio and platform. Those are the outside controllers whose
    presence CE treats as the mark of heteronomy.

## Loci

Locators: printed journal pages (the PDF is the version of record; printed page = PDF page + 1890).
Section and footnote numbers are the printed ones. Every quotation was matched against
`villalobos2018enactive.txt`, the text layer of the held PDF (sha256 above), after joining line-end
hyphens ("func-tional", "organiza-tional", "com-putationalism") and collapsing line breaks. No quotation
here has inner double quotation marks.

- "In this paper we will demonstrate that a computational system can meet the criteria for autonomy laid down by classical enactivism." — p. 1891 (PDF p. 1), Abstract; matched against villalobos2018enactive.txt
- "Our aim in this paper is to challenge the assumption that computational systems are necessarily heteronomous systems" — p. 1891 (PDF p. 1), Abstract; matched against villalobos2018enactive.txt
- "Enactivists, to the best of our knowledge, have never said that computational systems can be autonomous systems, but they have never explicitly denied such a possibility either." — p. 1892 (PDF p. 2), §1; matched against villalobos2018enactive.txt
- "Our purpose is to dissolve an alleged conceptual incompatibility between the notions of computation and autonomy, not to make a defence of any theory in particular." — p. 1893 (PDF p. 3), §1; matched against villalobos2018enactive.txt
- "On the one hand, a living cell, a multicellular animal, an ant colony, or a human being behaves as a coherent, self-determining unity in its interactions with its environment. An automatic bank machine, on the other hand, is determined and controlled from the outside (Thompson 2007, p. 37)" (block quotation of Thompson; Thompson's page as the authors give it, unchecked against Thompson) — p. 1894 (PDF p. 4), §2; matched against villalobos2018enactive.txt
- "Thus, to qualify a system as genuinely autonomous, the system must also be precarious." — p. 1895 (PDF p. 5), §2; matched against villalobos2018enactive.txt
- "Similarly, a physical Turing machine will have the tape as its computationally relevant environment, and the wider physical environment as enabling conditions (e.g., energy supply, ambient temperature, humidity, etc.)." — p. 1900 (PDF p. 10), fn. 6; matched against villalobos2018enactive.txt
- "this does not reveal any features that are intrinsic to a functionally closed system, but is rather a descriptive convention adopted by the observer according to her interests." — p. 1902 (PDF p. 12), §5; matched against villalobos2018enactive.txt
- "A conventional physically implemented Turing machine, insofar as its functional dynamics are concerned, lacks input and output in the systemic (organizational/operational) sense that is relevant for CE, and therefore exhibits OA." — p. 1902 (PDF p. 12), §5; matched against villalobos2018enactive.txt
- "A physically instantiated Turing machine, through its structure and configuration, specifies its own domain of interactions (perturbations) and meets the environment on its own terms." — p. 1905 (PDF p. 15), §6; matched against villalobos2018enactive.txt
- "Usually, if we think of implementing a computing system, we try to make it as robust and durable as possible." — p. 1906 (PDF p. 16), §7; matched against villalobos2018enactive.txt
- "A computing machine, typically, is conceived of to solve a problem that is relevant for us as users, not for the machine itself." — p. 1906 (PDF p. 16), §7; matched against villalobos2018enactive.txt
- "The machine’s computations are enabled by the energy supply, and the energy supply, in turn, is enabled by the computations." — p. 1906 (PDF p. 16), §7; matched against villalobos2018enactive.txt
- "Of course, merely visualizing the possibility of such a physical Turing machine does not demonstrate, in any conclusive way, that a physical computing system can exhibit, in the full sense that matters to CE, precariousness." — p. 1906 (PDF p. 16), §7; matched against villalobos2018enactive.txt
- "What we have not done is attempted to argue for or defend either position (enactivism or computationalism)." — p. 1907 (PDF p. 17), §8; matched against villalobos2018enactive.txt

## Caution

- **Registered year (record correction from DECISIONS).** The key and APA take the volume year, 2018
  (*Synthese* 195(5), Crossref published-print 2018-05). Crossref's `issued` and published-online date is
  2017-04-06, and the PDF says "Published online: 6 April 2017" and "© The Author(s) 2017". The card sets
  `registered_year: 2017`.
- **"Autonomy", not "life".** The authors' target is CE's autonomy criterion for *cognitive* systems
  (the nervous system), not a definition of life. Footnote 2 says CE has other reasons, such as the
  phenomenological life–mind continuity, to resist computational accounts, and that their result does not
  touch those. A draft must not cite them as saying a computer can be alive.
- **Thompson, Maturana and Di Paolo & Thompson at second hand.** The block quotations of Thompson (2007),
  Maturana (1987, 2003) and Di Paolo & Thompson (2014) are seen here only as Villalobos and Dewhurst quote
  them. The card does not vouch for the original pages.
- **Maturana & Varela (1980) at second hand.** On p. 1898 the authors say Maturana and Varela (1980)
  argued that an organism's sensorimotor system is functionally closed. Their reference list gives the book
  as "Dordrecht, Holland: Kluwer Academic Publisher". The Open Library edition record I saw for
  `maturana1980autopoiesis` gives D. Reidel, Boston. See that card.
- **Machine type.** The argument is about a special-purpose Turing machine with discrete states. The
  authors say only in passing (fn. 3, fn. 5) that unsupervised connectionist networks "might" already be
  partly autonomous. Nothing here is about LLMs or deep learning, so any application to an LLM system is
  the paper's own extension.
- **What the paper may not claim from it:** that any actual machine has been shown precarious, that
  enactivists accept the result, or that the authors endorse computationalism.

## Verification

- date: 2026-11-08; agent: S6 verifier (opus), batch W1 group 1
- verdict: verified
- checked: frontmatter against crossref.json (authors, volume year 2018 with registered_year 2017 from issued/online 2017-04-06, Synthese 195(5) 1891-1908, DOI, journal-article); PDF sha256 recomputed and matches sha256.txt; all 15 quotations found verbatim on the stated printed pages (printed = PDF + 1890 confirmed from the running heads); section and footnote locators checked against the heading lines (§5 quotations on p. 1902 precede the §6 heading; §7 quotations on p. 1906 precede the §8 Conclusion heading; fn. 6 on p. 1900); the p. 1901-1902 tape sentence, "in a modest sense", fn. 2 (life-mind continuity), fn. 4 (Turing computability), fn. 5, normativity/teleology/individuation, the Maturana & Varela (1980) report on p. 1898 and the Kluwer reference on p. 1908 all confirmed.
- changed: nothing
