---
citekey: taylor2026laion
title: The Algorithmic Gaze of Image Quality Assessment: An Audit and Trace Ethnography of the LAION-Aesthetics Predictor
authors: Taylor, Jordan and Agnew, William and Sap, Maarten and Fox, Sarah E. and Zhu, Haiyi
year: 2026
doi: null
arxiv: 2601.09896
journal: arXiv preprint
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: arxiv
source_url: https://arxiv.org/pdf/2601.09896
sha256: 67711f0aaba706d7ce8ee79bfba01de7f260b324bb809e51137a88064d0b0ced
pdf_path: literature/pdfs/taylor2026laion.pdf
verified: writer-grounded
generated_run: 2026-06-25
---

## Summary
The paper investigates the LAION-Aesthetics Predictor (LAP), an aesthetic quality assessment (AQA) model widely used to curate training data for visual generative AI (e.g., the earliest Stable Diffusion) and to evaluate AI-generated image quality. Asking "whose taste" LAP encodes, the authors (RQ1) audit what LAP rates as high-quality across three datasets and (RQ2) conduct a trace ethnography of public materials to explain where its biases originate. The audit finds that LAP disproportionately filters *in* images whose captions mention women (and Hindu/Buddhist/Christian communities) while filtering *out* those mentioning men, LGBTQ+ people, Jews, or Muslims; on art datasets it most highly rates realistic two-dimensional landscapes, cityscapes, and portraits by western and Japanese artists. The authors interpret these patterns as reproducing the imperial, realist, and male gazes of western art history. The trace ethnography shows LAP was a single-layer perceptron over CLIP embeddings, built largely to the individual taste of LAION's founder Christoph Schuhmann, trained by conflating three inconsistently documented datasets (AVA, SAC, LAION-Logos) whose annotators were primarily English-speaking photographers and western AI-enthusiasts. The authors argue aesthetic evaluation perpetuates representational harms, caution that greater "inclusion" can itself exacerbate harm, and call for a shift from prescriptive universalist "aesthetics" toward descriptive, pluralistic evaluation. Methodologically they advocate combining audits and trace ethnographies for FAccT research.

## Key facts it relies on
- LAP was used to curate the LAION-Aesthetics Dataset (LAD) from LAION-5B (5.86 billion image-text pairs); LAD 4.5+ contains ~1.2B images and LAD 6.5+ ~625k images; the 6.5 threshold is commonly used in computer vision to mark "high-quality" images.
- Audit used three datasets: LAD; 249,351 public-domain Metropolitan Museum of Art (MET) images (only 865 modern/contemporary); and the WikiArt dataset of 81,444 images by 128–129 primarily modern (mid-1800s–mid-1900s) artists, with 27 styles across 10 genres.
- Domain analysis: in LAD 4.5+ the top 25 domains account for ~36% of images; in LAD 6.5+ the top 25 account for ~52%, shifting toward sites used by independent artists/photographers (Redbubble, DeviantArt, SmugMug, Flickr, 500px), suggesting LAP favors photographic images.
- PMI (pointwise mutual information) of caption regexes: 'wom[ae]n' has the highest PMI and the most appearances in LAD 6.5+ (15,706); LGBTQ+ regexes are rare — 'gays?' (102), 'lesbians?' (20), 'transgenders?' (9), 'bi-?sexuals?' (2), 'non[ -]?binary' (0); 'whites?' and 'latin[oaxe]s?' both have PMI -0.95 but with 9,617 vs 26 images respectively.
- MET (Table 1): not a single African, Native American, Oceanian, Egyptian, Islamic, Ancient West Asian, or Greek & Roman piece scored ≥6.5; ~97% of MET images scored 6+ (3,180 of 3,284) come from just five departments (Asian Art, Photographs, European Paintings, The American Wing, Drawings & Prints).
- MET top medium/artist detail: of 249,351 images only 177 (across 35 mediums, 99 artists) scored ≥6.5; the ≥6.5 set came from 5 mediums (72 oil paintings, 60 Japanese woodblock prints, 26 watercolors, 15 photographs, etc.); top artists by ≥6.5 count were Katsushika Hokusai (32) and Utagawa Hiroshige (23), 19th-century ukiyo-e woodblock printmakers.
- WikiArt: Cityscape, Portrait, Landscape are 39% of WikiArt images but 73% of images rated 6.5+; realistic French cityscape painters Édouard Cortès (208/214 rated 6.5+) and Antoine Blanchard (168/170) scored very high, while Picasso, Warhol, and Dalí scored lower.
- Trace ethnography (Table 4): LAP is a single-layer perceptron over CLIP embeddings predicting a 1–10 score; trained by weighting three datasets equally — AVA (2012, 255,530 images, ~60%, from dpchallenge.com, *relative* ratings), SAC (2022, 146,372, ~34%, T2I-generated, 294 AI enthusiasts, *absolute*), and LAION-Logos (2022, 26,730, ~6%, from LAION-5B, only 18 annotators, *absolute*); 428,632 total training images.

## Critical notes from the literature
- The authors caution that greater "inclusion" of women in training data is not a fix: they note LAP's over-inclusion of women parallels the non-consensual circulation of (disproportionately) women's images and could exacerbate harms such as deepfakes, NCII, and sexual-abuse imagery; they advocate descriptive/pluralistic evaluation rather than a "better" universal aesthetic model.
- The authors flag that PMI is a *relative* measure and absolute caption counts must also be considered; they also offer an alternative reading (e.g., whiteness as an "unmarked racial category") for why European/Caucasian captions appear less, acknowledging interpretive ambiguity.
- They acknowledge (citing Seaver) that audits show the *existence* of bias but cannot explain *how* disparate impact arises, motivating the trace ethnography; they also caution that trace ethnographies are no substitute for traditional participant observation and leave open *why* the founder chose those datasets and how LAION made sense of LAP's circulation.
- The authors note ethical tension in their own method: documenting LAP required an *unlisted* YouTube video found in an old Discord message, and they acknowledge "public-ness" of data does not automatically make scavenging ethical.
- Scope: the analysis inherits the colonial category of "primitive art" via the MET's department structure (authors flag this self-critically), and the extent of contemporary models' reliance on LAION is hard to assess because developers (e.g., Stability AI's SD 3.5-Large model card) have grown opaque about training data.

## Key topics covered
Aesthetic quality assessment (AQA); image quality assessment; LAION-Aesthetics Predictor (LAP); LAION-5B / LAION-Aesthetics Dataset; Stable Diffusion training data curation; algorithmic auditing; trace ethnography; pointwise mutual information (PMI); CLIP embeddings; AI evaluation and alignment; pluralistic alignment; representational harms; the imperial/male/realist "gaze"; western art history (Berger, male gaze); AVA / SAC / LAION-Logos training datasets; data consent and annotation; FAccT methodology; photorealism bias.
