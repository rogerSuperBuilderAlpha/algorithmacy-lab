const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel,
  PageNumber, Header,
} = require("docx");

const FONT = "Times New Roman";
const SIZE = 24; // half-points; 24 = 12pt
const LINE = 480; // double (240 = single)

function t(text, extra = {}) {
  return new TextRun({ font: FONT, size: SIZE, ...extra, text });
}

function p(runs, extra = {}) {
  return new Paragraph({
    spacing: { after: 0, line: LINE },
    ...extra,
    children: Array.isArray(runs) ? runs : [runs],
  });
}

function empty() {
  return p([]);
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0, line: LINE },
    children: [t(text, { bold: true })],
  });
}

function body(runs) {
  return p(runs, { indent: { firstLine: 720 } });
}

function hanging(runs) {
  return p(runs, { indent: { left: 720, hanging: 720 } });
}

const header = new Header({
  children: [
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      spacing: { line: LINE },
      children: [new TextRun({ font: FONT, size: SIZE, children: [PageNumber.CURRENT] })],
    }),
  ],
});

const titlePage = [
  empty(), empty(), empty(), empty(), empty(), empty(),
  p([t("Algorithmacy as a Human Factors Problem: Re-coding Digitally Induced Altered States", { bold: true })], {
    alignment: AlignmentType.CENTER,
  }),
  empty(),
  p([t("Roger Hunt")], { alignment: AlignmentType.CENTER }),
  p([t("Ph.D. Program, Bentley University")], { alignment: AlignmentType.CENTER }),
  p([t("PHD1750-3: Independent Research Project")], { alignment: AlignmentType.CENTER }),
  p([t("Ericson")], { alignment: AlignmentType.CENTER }),
  p([t("October 6, 2026")], { alignment: AlignmentType.CENTER }),
];

const pageBreak = new Paragraph({
  children: [],
  pageBreakBefore: true,
});

const doc = new Document({
  creator: "Roger Hunt",
  title: "Algorithmacy as a Human Factors Problem: Re-coding Digitally Induced Altered States",
  description: "PHD1750-3 Independent Research Project paper proposal, Ericson, Fall 2026.",
  styles: {
    default: {
      document: {
        run: { font: FONT, size: SIZE },
        paragraph: { spacing: { line: LINE } },
      },
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickStyle: true,
        paragraph: {
          spacing: { before: 0, after: 0, line: LINE },
          alignment: AlignmentType.CENTER,
        },
        run: { font: FONT, size: SIZE, bold: true, color: "000000" },
      },
    ],
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      headers: { default: header },
      children: [
        ...titlePage,
        pageBreak,
        p(
          [t("Algorithmacy as a Human Factors Problem: Re-coding Digitally Induced Altered States", { bold: true })],
          { alignment: AlignmentType.CENTER }
        ),
        empty(),
        h1("Topic and Rationale"),
        body([
          t("The paper asks how science-fiction narratives depict parties reading and rewriting a shared algorithmic third party, and what patterns of access, interface, and competence those depictions make visible. "),
          t("Belousov et al. (2027) analysed 25 novels for digitally induced altered states of consciousness (DIAL) and produced an eight-type framework of user–technology interaction. "),
          t("They treat the brain–computer interface as the frontier, input discrepancy as the mark of an altered state, and the user as the person who receives what a designer made. "),
          t("The unit that now decides most coordination is a triad: a party, an algorithmic mediator with commitments of its own, and a counterpart who meets what that mediator has become."),
        ]),
        body([
          t("That triad is the construct my dissertation names "),
          t("algorithmacy", { italics: true }),
          t("—the competence of coordinating with a counterpart through an interested algorithmic third party. "),
          t("The course paper re-codes Belousov et al.’s published corpus against that construct and extends it by six catalogued screen and platform works ("),
          t("The Matrix", { italics: true }),
          t(", "),
          t("The Feed", { italics: true }),
          t(", "),
          t("Upload", { italics: true }),
          t(", the embodied co-pilot of semi-autonomous vehicles, the recommender-as-oracle, and algospeak). "),
          t("It moves a current HCI framework from literacy’s producer–consumer ontology onto the triadic form the rest of the dissertation measures, and it treats speculative interfaces as a human-factors laboratory."),
        ]),
        h1("Connection to Course Concepts"),
        body([
          t("Perception. ", { italics: true }),
          t("Folk theories of algorithmic systems are perceptual models of an invisible rule, inferred from outputs rather than from structure (Eslami et al., 2016). "),
          t("Belousov et al. (2027) take a related cut: an altered state is a discrepancy between sensory input and experienced content. "),
          t("That criterion tests the periphery of perception and fails where the input is itself authored by a mediator. "),
          t("Literacy already rebuilds perceptual cortex; Dehaene and Cohen (2007) showed that reading recycles a region of ventral occipitotemporal cortex as the visual word form area. "),
          t("Designed signs alter minds. The brain–computer interface changes the sensorimotor channel. Algorithmacy changes the activity of the mediator."),
        ]),
        body([
          t("Action. ", { italics: true }),
          t("Every qualifying scene is coded as a read or a write on the mediator’s commitments. "),
          t("Sanctioned writes include training a recommender by lingering and intervening on a semi-autonomous vehicle whose intervention becomes fleet policy. "),
          t("Subversive writes include gaming a stimulator’s feedback rule and shipping a coded protocol over a classifier. "),
          t("Human–agent teaming appears as the embodied co-pilot: the handoff is not a trust-calibration display but a development act whose product other drivers later meet."),
        ]),
        body([
          t("Cognition. ", { italics: true }),
          t("Algorithmacy is a competence, not a literacy upgrade. "),
          t("Integrated Information Theory supplies the criterion for an altered state: a reconfiguration of the cause–effect structure a system specifies for itself (Albantakis et al., 2023). "),
          t("No Φ is computed on fiction; the borrowing is formal. "),
          t("Irreducibility of cause–effect structure is the right kind of thing to mean by a change of state once input discrepancy has done its taxonomic work."),
        ]),
        body([
          t("Human factors and design. ", { italics: true }),
          t("Ananny and Crawford (2018) showed that seeing a system is not knowing it, and that raw backend access can overload working memory. "),
          t("The paper accepts the load claim and rejects the pastoral conclusion that novices should receive abstracted heuristics while experts receive structural variables. "),
          t("Abstracting the steering surface from a party who is already steering hides her contribution while keeping it available to the operator. "),
          t("The design object is the "),
          t("engagement layer", { italics: true }),
          t("—where reading and rewriting the shared mediator is the ordinary mode of use—not a product layer that hides the mediator behind a stable surface."),
        ]),
        h1("Preliminary Position or Direction"),
        body([
          t("The final paper is a secondary analysis, not a new sample. "),
          t("I hold Belousov et al.’s 25 novels fixed so that differences of result are differences of criterion and frame, and I extend the corpus with six works already catalogued for algorithmic mediation. "),
          t("The inclusion criterion is "),
          t("cooptive commit", { italics: true }),
          t(": a scene qualifies when an algorithmic mediator sits between a party and a counterpart, and the scene depicts the party reading or writing that mediator’s commitments."),
        ]),
        body([
          t("Two aspects, fixed before coding, combine into eight interaction types. "),
          t("Reach", { italics: true }),
          t(" asks whose later state the read or written mediator state is met by (internal or external). "),
          t("Act", { italics: true }),
          t(" asks whether the party reads the commitments, interpretively from behaviour or structurally from the rule, or writes them through a sanctioned channel or a subverted one. "),
          t("The eight types are folk theorizing, backend reading, shared folk theory, audit, training by response, subversive affordance, operator commit, and protocol shipping. "),
          t("Five themes follow: write access is stratified by licence rather than literacy; engagement is the operator’s development material; the self is a node others can rewrite; truth is a mediator commitment; pastoral design should give way to collective algorithmacy. "),
          t("The framework is offered to designers inverted: each cell is a cooptive regime, not an experience genre."),
        ]),
        h1("Preliminary Literature Review"),
        hanging([
          t("Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. "),
          t("PLOS Computational Biology, 19", { italics: true }),
          t("(10), Article e1011465. https://doi.org/10.1371/journal.pcbi.1011465"),
        ]),
        body([
          t("Albantakis et al. state IIT 4.0 in physical terms: a system’s experience is identical to the cause–effect structure it specifies over its own parts, irreducible to any partition of those parts. "),
          t("The paper uses this as the conceptual criterion for an altered state, replacing Belousov et al.’s input discrepancy, and as the formal warrant for calling the algorithmic mediator a party. "),
          t("No Φ is computed on fiction; the laboratory’s exact-Φ results on Boolean models are cited, not re-derived."),
        ]),
        hanging([
          t("Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability. "),
          t("New Media & Society, 20", { italics: true }),
          t("(3), 973–989. https://doi.org/10.1177/1461444816676645"),
        ]),
        body([
          t("Ananny and Crawford argue that seeing a system is not knowing it, and that the transparency ideal can fail as an accountability practice. "),
          t("The paper takes that limit as the load half of the transparency paradox and as the reason audit, a structural read of a shared mediator, is rare in the field. "),
          t("Their argument is the foil for the design claim: the remedy is not more explanation of a finished product but an operable engagement layer."),
        ]),
        hanging([
          t("Belousov, A., Macey, J., Bujić, M., Ojell-Järventausta, T., & Hamari, J. (2027). Designing the future of consciousness: A components framework and speculative implications. "),
          t("International Journal of Human–Computer Studies, 218", { italics: true }),
          t(", Article 103926. https://doi.org/10.1016/j.ijhcs.2026.103926"),
        ]),
        body([
          t("Belousov et al. analyse 25 science-fiction novels for DIAL, construct an eight-type framework from context × purpose, and draw five themes about identity, autonomy, and hypercompetition. "),
          t("Their published extracts, Table 1, and Table A.1 are the fixed corpus the paper re-codes. "),
          t("Their method, reflexive thematic analysis of diegetic prototypes, transfers; their UX-first coding layer and their discrepancy criterion do not."),
        ]),
        hanging([
          t("Dehaene, S., & Cohen, L. (2007). Cultural recycling of cortical maps. "),
          t("Neuron, 56", { italics: true }),
          t("(2), 384–398. https://doi.org/10.1016/j.neuron.2007.10.004"),
        ]),
        body([
          t("Dehaene and Cohen show that literacy recycles a region of left ventral occipitotemporal cortex originally tuned for invariant visual recognition, producing the visual word form area. "),
          t("The finding grounds the claim that designed signs already alter minds, so that BCI is a change of channel rather than the start of mind-altering design. "),
          t("It also supplies the engagement-layer analogy: the answer to cognitive load was a change of interface ("),
          t("scriptio continua", { italics: true }),
          t(" to word separation), not a reservation of reading for those who could bear the load."),
        ]),
        hanging([
          t("Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I “like” it, then I hide it: Folk theories of social feeds. In "),
          t("Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems", { italics: true }),
          t(" (pp. 2371–2382). Association for Computing Machinery. https://doi.org/10.1145/2858036.2858494"),
        ]),
        body([
          t("Eslami et al. document the folk theories users construct of algorithmic social feeds: working models of an invisible ranking rule, built from its outputs. "),
          t("Those theories populate two cells of the paper’s framework, folk theorizing and shared folk theory, and are the fielded analogue of characters who infer a mediator they cannot inspect. "),
          t("The article is the human-factors warrant for coding interpretive read as a competence rather than as error."),
        ]),
        h1("References"),
        hanging([
          t("Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., Mayner, W. G. P., Zaeemzadeh, A., Boly, M., Juel, B. E., Sasai, S., Fujii, K., David, I., Hendren, J., Lang, J. P., & Tononi, G. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. "),
          t("PLOS Computational Biology, 19", { italics: true }),
          t("(10), Article e1011465. https://doi.org/10.1371/journal.pcbi.1011465"),
        ]),
        hanging([
          t("Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the transparency ideal and its application to algorithmic accountability. "),
          t("New Media & Society, 20", { italics: true }),
          t("(3), 973–989. https://doi.org/10.1177/1461444816676645"),
        ]),
        hanging([
          t("Belousov, A., Macey, J., Bujić, M., Ojell-Järventausta, T., & Hamari, J. (2027). Designing the future of consciousness: A components framework and speculative implications. "),
          t("International Journal of Human–Computer Studies, 218", { italics: true }),
          t(", Article 103926. https://doi.org/10.1016/j.ijhcs.2026.103926"),
        ]),
        hanging([
          t("Dehaene, S., & Cohen, L. (2007). Cultural recycling of cortical maps. "),
          t("Neuron, 56", { italics: true }),
          t("(2), 384–398. https://doi.org/10.1016/j.neuron.2007.10.004"),
        ]),
        hanging([
          t("Eslami, M., Karahalios, K., Sandvig, C., Vaccaro, K., Rickman, A., Hamilton, K., & Kirlik, A. (2016). First I “like” it, then I hide it: Folk theories of social feeds. In "),
          t("Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems", { italics: true }),
          t(" (pp. 2371–2382). Association for Computing Machinery. https://doi.org/10.1145/2858036.2858494"),
        ]),
      ],
    },
  ],
});

const out = process.argv[2];
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(out, buf);
  console.log("wrote", out);
});
