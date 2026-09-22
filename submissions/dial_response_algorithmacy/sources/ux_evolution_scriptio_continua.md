# The UX of Evolution: From Scriptio Continua to Triadic Algorithmacy

Ingested verbatim from Google Docs (file id `1wlUWN0MlkGotceDcLfN3HHibFJIzqkyMzuVuxXQmBBA`, Drive
title "Text UX and Algorithmacy Evolution"), owner `regorhunt02052@gmail.com`, created 2026-09-20,
last edited 2026-09-20. Source of truth stays the Doc — re-pull before quoting it verbatim.

**Overlap note.** This essay's core argument — *scriptio continua* as high-friction interface,
word separation and the codex as the literacy-era fix, the transparency paradox, folk theories
(Spotify, AV drivers, dating apps), subversive affordances, algospeak — is already fully present
in `../draft.md` §2.3 ("Reading already reorganises the brain") and in
[`../corpus/essay.md`](../corpus/essay.md), which makes the same argument through the same sources
(Dehaene, Saenger, Ananny & Crawford). Nothing here should be treated as new argument material for
the article.

What is **not** already used elsewhere in this submission:

- The deeper information-architecture history — cuneiform tablets and colophons, papyrus scrolls,
  broadsides as "notifications of the early modern era," and the Gutenberg/Eisenstein/Manutius
  print-culture chapter (italic type, the octavo pocket-book, standardized punctuation). `draft.md`
  §2.3 stays brief (scriptio continua → word separation → codex) by design; this doc's fuller
  pre-history could seed a longer companion piece on interface history but is not needed for the
  IJHCS article's argument.
- A citation to Douyin (TikTok's Chinese counterpart) studies of "infrapolitical" algorithmic
  resistance — oscillation between pushback and digital resignation under state censorship and
  commercial exploitation. `draft.md` cites Klug et al. (2023) and Steen et al. (2023) on TikTok
  algospeak and Sun (2019) on gig-worker coordination, but not a Douyin-specific source.

Neither addition changes the article's substance; both are logged here in case the lab wants a
longer history-of-interfaces treatment later.

---

## The UX of Evolution: From Scriptio Continua to Triadic Algorithmacy

The evolution of human communication is fundamentally a history of cognitive ergonomics, sociotechnical negotiation, and interface design. Long before the advent of digital screens, the physical structures of texts—from Mesopotamian clay tablets to printed codices and ephemeral broadsheets—functioned as complex user interfaces that mediated information transfer. The progression of these textual interfaces reveals a continuous, centuries-long struggle to manage cognitive load, optimize spatial arrangement, and negotiate the power dynamics between the creator of information and its consumer. Historically, the transition from oracy (face-to-face dyadic communication) to literacy (author-to-reader dyadic communication mediated by a static object) represented an ontological shift in human coordination and cognition. Today, as digital environments become increasingly mediated by artificial intelligence, society is undergoing another profound transition toward "algorithmacy".

Unlike the passive mediums of parchment or early graphical user interfaces, algorithmic systems operate as active third parties, transforming human-computer interaction into a framework of triadic cooptive coordination. In this triadic form, an algorithm sits between two human parties, acting upon their inputs in pursuit of its own programmed objectives. To understand the user experience challenges of this algorithmic era—including cognitive friction, the transparency paradox, the development of user folk theories, and the emergence of subversive algorithmic resistance—it is imperative to examine the historical development of reading technologies. By analyzing how humanity successfully navigated the cognitive hurdles of ancient texts, modern interface designers, information architects, and sociotechnical researchers can glean vital lessons for designing the complex, algorithmic architectures of the future.

## The Neurobiology of the Reading Interface

To comprehend the user experience of ancient texts and draw parallels to modern algorithmic cognitive load, one must first understand the biological constraints of the human brain. Reading is not an evolutionary given; it is a cultural invention that requires the human brain to fundamentally repurpose existing neural circuitry through a process known as neuronal recycling.

### The Visual Word Form Area and Neuronal Recycling

According to the neuronal recycling hypothesis, the acquisition of literacy forces the brain to repurpose a specific region of the left ventral occipitotemporal (VOT) cortex. This area, originally evolved in primates for the invariant visual recognition of objects, tools, and faces, becomes the Visual Word Form Area (VWFA), frequently referred to in cognitive neuroscience as the brain's "letterbox". The VWFA adapts to recognize the shapes of letters and words, acting as an interface that links visual perception to the brain's preexisting phonological and semantic networks.

In pre-literate or early-literate children, this neural real estate is broadly dedicated to navigating the physical environment. As humans begin interacting with written interfaces, the VWFA engages in a competition for cortical space. Longitudinal neuroimaging studies reveal that during reading acquisition, visual words invade a sector of the cortex that is initially weakly specialized for tools and close to face-responsive areas. This competition subtly displaces face recognition capabilities, pushing them more strongly into the right hemisphere to accommodate textual decoding in the left hemisphere. Furthermore, the brain must actively "unlearn" mirror invariance—an evolutionary trait that allows humans to recognize a face or object regardless of its left-right orientation—because reading requires strict adherence to fixed directional orientations for characters.

### Cognitive Load, Bouma Shapes, and Serial Processing

The efficiency with which the VWFA can process visual symbols directly dictates the cognitive load experienced by the user. Historically, typography and information architecture relied on the "Bouma shape" model of word recognition, named after Dutch psychologist Herman Bouma, which posited that readers recognize words by their overall physical outline (the distinct patterns of ascenders and descenders in lowercase text). This theory was supported by the Word Superiority Effect discovered by James Cattell in 1886, which demonstrated that humans process whole words faster than individual letters, and that lowercase text is read faster than all-caps text.

However, modern cognitive neuroscience has shifted toward the parallel letter recognition model, indicating that the VWFA processes the individual letters within a word simultaneously rather than relying solely on the external silhouette. The brain develops a compositional neural code tuned to individual letters, bigrams, and their ordinal positions. When textual interfaces degrade—whether through the omission of causal information, semantic dissimilarities, or poor identifier naming in software code—comprehension slows dramatically. Functional magnetic resonance imaging (fMRI) studies show that degraded text forces readers out of automatic processing and into controlled processing, triggering increased N400 electrophysiological responses that reflect severe semantic processing demands. This neurological baseline underscores that any interface—whether a papyrus scroll or an Explainable AI dashboard—that fails to optimize visual parsing will impose a debilitating cognitive tax on the user.

## The UX of Early Textual Formats: Clay Tablets and Papyrus Scrolls

The earliest functional user interfaces emerged in Mesopotamia in the form of cuneiform clay tablets. Primarily used for administrative, accounting, medical, and divinatory purposes, these tablets were highly structured data repositories designed for institutional tracking rather than casual reading.

### Cuneiform and the Origins of Information Architecture

Scribes functioning as early information architects utilized physical layout features, such as horizontal and vertical rulings, to create columns and tables that organized data into digestible hierarchies. The user experience of a cuneiform tablet was highly tactile and spatially constrained, prioritizing durability and bureaucratic classification over linear narrative flow. To facilitate navigation across massive physical databases and temple archives, scribes developed sophisticated metadata systems. Colophons—appended to the edges or ends of tablets—provided summary information, line counts, and titles. Clay "envelopes" and lozenge-shaped shelf tags allowed users to identify contents without needing to extract and read the entire tablet, serving as the ancient equivalent of file directories. Even in antiquity, the sheer volume of information necessitated robust wayfinding systems.

### Papyrus and the Burden of *Scriptio Continua*

As communication shifted toward extended narratives, poetry, and philosophical discourse, the physical medium transitioned to the papyrus scroll. While papyrus allowed for longer texts, the scroll format imposed a severe user experience limitation: it forced strictly sequential navigation. A reader could not easily "jump" to a specific section without unrolling and rerolling the entire document, making cross-referencing nearly impossible.

More significantly, Greek and Roman texts were characteristically written in *scriptio continua*—a continuous stream of letters without spaces, capitalization, or standardized punctuation. From a modern cognitive ergonomics perspective, *scriptio continua* represents an interface with exceptionally high cognitive friction. Because the visual boundaries of words were hidden, the VWFA could not instantly execute parallel letter recognition.

Consequently, ancient reading was almost exclusively an oral, performative act. Readers had to subvocalize—sounding out the syllables aloud to allow their auditory processing centers to identify word breaks and extract syntactical meaning. This continuous cognitive decoding consumed significant working memory, making reading a slow, taxing endeavor relegated to a highly trained elite. The ancient world viewed this high barrier to entry not as a flaw, but as a feature of a culture that valued rhetorical performance over mass information consumption. The interface of *scriptio continua* required the user to do the computational heavy lifting that the text's layout refused to provide, much like modern users forced to parse unformatted data dumps.

## The Typographical Revolution: White Space, Syntax, and the Codex

The transition from the heavy cognitive load of oral reading to the efficient, internal process of silent reading represents one of the most profound user experience enhancements in human history. This shift was entirely driven by changes in the visual architecture of the page.

### Word Separation as Cognitive Offloading

In the seventh and eighth centuries, Irish and Anglo-Saxon monks—whose native languages were entirely foreign to Latin—struggled immensely to parse *scriptio continua*. To alleviate this cognitive burden, these Insular scribes introduced a radical design intervention: they inserted physical space between words.

Historian Paul Saenger details how this simple spatial manipulation drastically reduced cognitive load. By visually isolating words, the text aligned perfectly with the parallel processing capabilities of the human visual system. Readers no longer had to rely on auditory feedback to decode syntax; the visual shape of the word delivered meaning directly to the semantic centers of the brain. This graphical reduction of prior cognitive processing facilitated the birth of silent reading. The introduction of white space transformed reading from a localized, vocalized performance into an autonomous, internal, and highly accelerated cognitive process.

### The Evolution of Punctuation

Simultaneous to the development of word separation was the evolution of punctuation, which served as an early form of digital markup and structural syntax. In antiquity, Aristophanes of Byzantium had introduced a system of dots (the *théseis*) to indicate pauses for breath during rhetorical delivery. These dots were arranged by height: a high dot (*stigmḕ teleía*) for a full sentence, a mid-height dot (*stigmḕ mésē*) for a clause, and a low dot (*hypostigmḗ*) for a minor pause.

However, as the written word shifted from a mere script for speech to an autonomous information repository, punctuation evolved to indicate syntactical logic rather than just breath control. In the seventh century, Archbishop Isidore of Seville resurrected and updated Aristophanes' system, assigning distinct grammatical meanings to the placement of dots, separating clauses and indicating the termination of thoughts. Later medieval scribes added marks like the *punctus elevatus* (a major pause) and the *virgula suspensiva* (a slash) to provide visual cues regarding sentence structure. This structural syntax acted as a mental wayfinding system, guiding the eye's saccades and preventing cognitive missteps.

### The Codex and Random Access Navigation

The evolution of text was further accelerated by the triumph of the codex over the scroll. The bound book provided a fixed, manageable spatial layout that revolutionized information architecture. Unlike the sequential scroll, the codex enabled "random access" navigation, calculating and ordering space in advance according to levels of meaning and hierarchy.

This hardware upgrade facilitated complex software innovations. Scribes developed pagination, tables of contents, and indices. Cross-referencing systems, most notably the Eusebian Canons—a complex set of numerical tables aligning parallel passages across the four Gospels—transformed the book into a highly interactive, non-linear database. The codex allowed readers to flip back and forth, compare texts, and synthesize information at an unprecedented scale, vastly increasing the user's agency over the information flow.

## Mass Communication and Print Culture: From Books to Broadsheets

If the Middle Ages provided the structural innovations of the codex and word separation, the Renaissance and the advent of the printing press introduced standardization, scalability, and the beginnings of mass-market UX design.

### Print Culture and Typographical Standardization

The invention of the movable-type printing press by Johannes Gutenberg catalysed what historian Elizabeth Eisenstein termed "print culture". Prior to print, scribal culture was plagued by high costs, slow reproduction, and inevitable textual corruption during copying, which fostered a reliance on secrecy and limited distribution.

The printing press mechanized the preservation of symbolic reality, creating textual "fixity". Exact reproductions of charts, diagrams, and data allowed scholars across Europe to compare identical datasets, fueling the Scientific Revolution. From a cognitive standpoint, standardization reduces friction. Because readers encountered identical typefaces and layouts, they developed automated visual processing habits, allowing the brain to focus entirely on higher-order comprehension rather than low-level decoding.

The refinement of print UX was heavily influenced by Venetian printer Aldus Manutius in the late 15th and early 16th centuries. Seeking to make classical texts portable, he introduced the octavo "pocket-book" format. To maximize the amount of text that could fit on these smaller pages without sacrificing legibility, Manutius commissioned Francesco Griffo to design the first italic typeface. The italic font was narrower, allowing for dense but highly readable text blocks. Furthermore, Manutius standardized modern punctuation, defining the rules for the comma and introducing the modern semicolon to delineate complex ideas within a single sentence.

### Broadsides: The Architecture of Public Attention

While bound books catered to sustained, deep reading, the printing press also birthed the broadside (or broadsheet)—large, single-sided sheets of paper plastered in public squares. Broadsides functioned as the notifications and social media feeds of the early modern era, disseminating news, proclamations, ballads, and advertisements.

Because they were designed to be read from a distance by a passing public, broadsides required a completely different UX paradigm. Printers utilized oversized wood type, crude illustrations, and high-contrast layouts to grab attention. This ephemeral medium prioritized immediacy and emotional impact over sustained narrative. Broadsides, chapbooks, and *pashkevils* (propaganda posters used in specific religious communities) represent early experimentation in visual hierarchy and scannability—techniques that directly precede modern web design and feed-based algorithmic curation.

| Interface Era | Medium | Key UX Innovation | Cognitive Impact |
| :-: | :-: | :-: | :-: |
| **Antiquity** | Clay Tablet, Papyrus | Hierarchical grids, Colophons, Metadata tags | High working memory load due to *scriptio continua* and strictly sequential access. |
| **Medieval** | Manuscript Codex | Word separation, Punctuation, Pagination, Indices | Enabled silent reading; VWFA optimization; allowed non-linear random access. |
| **Early Modern** | Printed Book, Broadside | Typographic standardization, Italic fonts, Visual hierarchy | Reduced decoding friction via textual fixity; mass dissemination; rapid visual scanning. |

## The Paradigm Shift to Algorithmacy and Triadic Coordination

Just as the transition from oracy to literacy rewired human cognition and societal structures, the current digital age is driving an ontological shift toward "algorithmacy". For centuries, the ultimate goal of information architecture was to structure static data so that humans could navigate it efficiently. The user was the active agent; the medium was a passive conduit.

### Defining Algorithmacy and Triadic Cooptive Coordination

With the integration of Artificial Intelligence and machine learning, the paradigm has fundamentally shifted. Algorithmacy is defined as the communication competency through which a worker or user coordinates with another human party through an algorithmic third party. This creates a model of "triadic cooptive coordination."

In classical computer-mediated communication (CMC), a human sends a message through a passive digital channel to a receiver. In triadic coordination, the algorithm is an independent, irreducible actor. It processes inputs from both sides, filters content, alters visibility, and makes autonomous recommendations based on its own optimized objectives (e.g., maximizing engagement, revenue, or specific platform metrics). This represents a profound disruption in user experience. The user is no longer navigating a static taxonomy; they are negotiating with a dynamic, opaque system that co-opts their behavioral data to alter the very environment they are navigating.

This dynamic extends into Human-Agent Teaming (HAT) configurations. Research into triadic interactions—such as a human therapist interacting with two clients, or a human collaborating with both another human and an AI agent—reveals that coordination relies less on fine-grained temporal synchrony and more on interoceptive-affective scaffolding under divided attention. Capturing eye-gaze synchrony in these triadic environments demonstrates that humans must constantly redistribute their cognitive load and trust between human and algorithmic agents.

### System 0 Cognition and Epistemic Offloading

The integration of AI into decision-making has introduced what researchers term "System 0" cognition. Building on Daniel Kahneman's dual-process theory (System 1: fast/intuitive; System 2: slow/analytical), System 0 represents the outsourcing of cognitive tasks to AI systems capable of processing vast amounts of data beyond human capacity.

In modern interfaces, algorithms act as cognitive pre-processors, structuring the informational environment and scaffolding decisions before the user even engages in conscious deliberation. While this drastically reduces the mechanical workload of gathering data, it introduces a dangerous form of "cognitive surrender," wherein users adopt AI outputs without critical evaluation. The UX challenge of algorithmacy is that the interface is so seamless—so devoid of traditional friction—that the user loses awareness of the epistemic mediation taking place. The algorithm embeds external interests within the architecture of the self, acting prior to conscious deliberation to shape the very pre-attentive infrastructures through which agency is negotiated.

## The Transparency Paradox and Cognitive Overload in XAI

As society grapples with the pervasive influence of opaque algorithms—what legal scholar Frank Pasquale famously termed the "Black Box Society"—there has been a massive regulatory and ethical push for Explainable AI (XAI) and algorithmic transparency. The prevailing assumption among policymakers and software engineers is that by exposing the inner workings of an algorithm, users will regain autonomy, calibrate their trust appropriately, and detect biases.

### The Cognitive Costs of Transparency

However, recent empirical research in Human-Computer Interaction reveals a counterintuitive phenomenon: the "Transparency Paradox". Studies demonstrate that providing highly detailed explanations of AI reasoning (e.g., chain-of-thought outputs, multi-layered decision trees) often reduces perceived user autonomy and diminishes overall decision quality.

When users are confronted with extensive, transparent AI rationales, it triggers severe cognitive overload. The user's working memory capacity is overwhelmed by the need to parse, verify, and integrate the machine's complex logic. Rather than empowering the user, excessive transparency forces them into a state of cognitive depletion. Paradoxically, when the cognitive cost of processing the explanation exceeds its actual decision value, users disengage, feel dominated by the system, and their sense of agency collapses.

This dynamic creates an inverted-U relationship where moderate transparency fosters trust and certainty, but excessive transparency induces skepticism and reduces AI adoption. The Human Identity and Autonomy Gap (HIAG) framework explains that transparency triggers higher-order evaluations, prompting users to question their own reasoning; when information load exceeds capacity, users experience autonomy depletion.

Interestingly, this effect is highly moderated by individual personality traits. Individuals with high "Openness to Experience" tend to use detailed rationales as intellectual scaffolding, extracting useful information while maintaining decision ownership. Conversely, highly extroverted or action-oriented users experience the strongest autonomy reduction, as detailed explanations force deliberative processing that conflicts with their natural intuitive decision-making style.

### The *Scriptio Continua* of the Algorithmic Age

The Transparency Paradox highlights a profound historical parallel in user experience. Providing a user with an unfiltered, raw dump of an AI's decision-making weights and logic trees is the algorithmic equivalent of handing an ancient reader a papyrus scroll written in *scriptio continua*. It is technically legible, but cognitively hostile.

Just as ancient readers were exhausted by the lack of physical spaces between words, modern users are exhausted by uncurated algorithmic transparency. To achieve true algorithmacy, designers cannot simply "open the black box." They must invent the algorithmic equivalent of word separation and punctuation. Information must be structurally formatted, adaptively paced based on real-time cognitive state, and presented within an "information budget" that respects human working memory limits. Trust in AI systems is not built through maximum data exposure, but through UX design that balances clarity, usability, and cognitive ergonomics.

## User Agency: Folk Theories in the Algorithmic Era

When interfaces fail to align with user expectations, or when algorithmic power becomes overly oppressive and opaque, users do not remain passive. Because the technical operations of modern recommender systems and automated management tools are hidden, users are forced to construct their own mental models—known as "folk theories"—to navigate the digital environment.

### Constructing Mental Models of Opaque Systems

Folk theories are intuitive, informal explanations that laypeople construct to interpret the behavior of complex systems. Because users cannot see the code, they rely on experiential feedback, media coverage, and social networks to map the algorithm's boundaries.

For instance, studies of Spotify users revealed two primary, competing folk theories: some users conceptualized the algorithm as a "social being" that heavily surveils their behavior to provide recommendations, while others viewed it as a "computational machine" brimming with resources that could be specifically trained through intentional interaction.

Similarly, drivers interacting with semi-autonomous vehicles (AVs) construct anthropomorphic folk theories to interpret algorithmic behavior that contradicts their expectations. When an AV brakes unexpectedly on a highway or hesitates at a complex intersection, drivers lack the informational resources to validate the system's logic. In response, they describe the system using metaphors like it "sees," "hesitates," or becomes "overwhelmed". In the realm of dating apps, users differentiate between "algorithmic pairing" (where compatibility scores are explicitly presented) and "algorithmic filtering" (where the algorithm curates a deck of profiles invisibly in the background), developing distinct strategies to navigate each paradigm.

These theories, while often technically inaccurate, are highly functional; they serve as symbolic resources that guide behavior, restore a sense of perceived control, and allow users to strategize around algorithmic filtering. Folk theories offer a productive way to broaden our understanding of what agency means in relation to algorithms, revealing the social annotations behind how people interact with technology.

## Algorithmic Resistance and Subversive Affordances

When folk theories reveal that an algorithm's objectives conflict with the user's goals—such as exploiting personal data, pushing addictive content, enforcing unfair managerial metrics, or implementing rigid political censorship—users transition from mere sensemaking to active algorithmic resistance. This resistance rarely involves abandoning the platform entirely, due to the monopolistic nature of modern digital environments and the social costs of disconnection. Instead, it manifests as continuous, everyday micro-rebellions woven into regular usage.

### The Repertoires of Digital Resistance

Researchers have conceptualized this pushback through the lens of "subversive affordances"—the strategic repurposing of platform engagement mechanisms to disrupt dataveillance and reclaim digital autonomy. To quantify these behaviors, the Social Media Algorithmic Resistance Scale (SM-ARS) categorizes them into specific behavioral repertoires. The two most prominent are avoidant resistance, which involves limiting structural exposure to the algorithm, and obfuscatory resistance, which involves strategic data pollution to confuse the system's profiling mechanisms.

A prime example of obfuscatory resistance is "algospeak"—the use of subversive orthography, intentional typos, or coded emojis to bypass automated content moderation and algorithmic filtering. By deliberately altering the visual and textual data fed into the system, users effectively break the AI's pattern recognition capabilities. Just as ancient scribes created ligatures and abbreviations to manage physical space on parchment, modern users manipulate orthography to evade the panoptic gaze of the algorithm.

### Cooperative Affordances and Infrapolitical Action

In the realm of platform labor, gig workers facing algorithmic management routinely enact "cooperative affordances." Food delivery couriers, for example, recognize that the delivery apps are designed with affordances that encourage gamified, competitive behavior while discouraging worker solidarity. In response, workers enact cooperative affordances by utilizing external instant messaging apps to organize, share knowledge about algorithmic behaviors, and coordinate collective action. They supplement and circumvent the isolating UX designed by the delivery platforms from below.

Similarly, studies of users on Douyin (the Chinese version of TikTok) reveal complex "infrapolitical" algorithmic resistance. Users experience a paradox between their reliance on the platform for sociocultural gratification and their frustration with algorithmic simplification, commercial exploitation, and state censorship. Their resistance oscillates between limited pushback and digital resignation, evolving into a subtly reflexive practice that challenges the power structures embedded in algorithmic governance without triggering outright bans.

These practices demonstrate that users interacting with triadic algorithmic systems are not merely passive data sources. Much like medieval scholars who filled the margins of rigid codices with disruptive glosses and annotations to challenge the main text, modern digital citizens are actively hacking the algorithmic architecture. They are forcing a negotiation of power, utilizing the platform's own interface to establish pockets of autonomy within a tightly controlled triadic system.

## Conclusion

The historical progression of texts reveals that human cognition is highly elastic but fundamentally constrained by the realities of interface design. From the heavy cognitive toll of reading *scriptio continua* on papyrus to the navigational elegance of the printed codex and the immediate visual impact of the broadsheet, usability breakthroughs have always relied on structuring information to align with the brain's visual and semantic processing capabilities.

As society navigates the transition into an era defined by algorithmacy, we face an architectural challenge of unprecedented complexity. Algorithms mediate reality through a triadic coordination form, operating as active agents that simultaneously serve and surveil the user. The current push to illuminate the "Black Box Society" through massive data transparency is proving ergonomically flawed. It triggers a Transparency Paradox that overwhelms working memory, replacing the cognitive friction of ignorance with the cognitive overload of excessive data, ultimately stripping users of their perceived autonomy.

To build sophisticated, sustainable algorithmic interfaces, designers and policymakers must look to the lessons of the seventh-century scribes and the Renaissance typographers. True usability does not equal the total exposure of raw data; it requires the intelligent curation of space, structure, and pacing to match human cognitive capacities. Until AI systems are designed with the cognitive ergonomics of an "algorithmic white space," users will continue to rely on folk theories and subversive affordances—such as data pollution and algospeak—to carve out their own agency. Designing for algorithmacy means recognizing that human-AI interaction is not merely an engineering problem of data optimization, but the next great leap in the continuous, sociotechnical evolution of human cognitive architecture.
