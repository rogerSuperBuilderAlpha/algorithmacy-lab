---
citekey: dieter2019multisituated
title: Multi-Situated App Studies: Methods and Propositions
authors: Dieter, Michael and Gerlitz, Carolin and Helmond, Anne and Tkacz, Nathaniel and van der Vlist, Fernando N. and Weltevrede, Esther
year: 2019
doi: 10.1177/2056305119846486
arxiv: null
journal: Social Media + Society
programs: [field]
pdf_status: ACQUIRED
source_basis: full-text
oa_source: landing:repository
source_url: https://pure.uva.nl/ws/files/46421717/2056305119846486.pdf
sha256: 062e4b45942e3a1a1930740983ded58f6625e0232608664bbfb9790d9630d077
pdf_path: literature/pdfs/dieter2019multisituated.pdf
verified: true
generated_run: 2026-06-25
---

## Summary
This methodological article asks how media researchers can empirically study mobile apps given that apps tend to recede into the background while remaining entangled with data-intensive infrastructures and platform economics. The authors argue apps are not self-contained objects but are "multivalent" software packages that enter into different groupings and relations depending on the infrastructural "situation" they are placed in, so the researcher's task is less to "follow the thing" across sites (Marcus, 1995) than to actively situate and re-situate apps using their affordances. They propose a "multi-situated" approach organized around four methodological entry points—app stores, app interfaces, app packages, and app connections—each of which deploys and makes visible different infrastructural settings and stakeholders. App stores are treated as indices and gatekeepers (obligatory passage points) whose set-making and ranking can be queried and reconfigured; app interfaces are studied through repurposed "walkthrough" methods using user/research personas; app packages (.apk/.ipa files) are decompiled and scanned (e.g., for trackers via Exodus Privacy) outside their normal consumption context; and app connections are captured via network sniffing/packet inspection to trace dynamic ties to third parties, CDNs, cloud services, and ad networks. The article concludes with nine propositions (e.g., move beyond ready-made social data, navigate infrastructural resistance, (un)do the user, resist presentism, contest Silicon Valley imperialism, don't leave ethics behind) as prompts for further situated app research. The work emerges from Digital Methods Initiative summer/winter school projects (2015–2018) and is oriented toward the political economy and infrastructural embeddedness of apps rather than interpretive studies of single apps.

## Key facts it relies on
- The article presents exactly four methodological entry points (app stores, app interfaces, app packages, app connections) and nine propositions for situated app studies.
- 10 July 2018 marked the 10-year anniversary of Apple's App Store; Google launched Android Market (later Google Play) shortly after, on 22 October 2008.
- As of May 2018 the paper cites over 3.8 million Android apps and 2 million iOS apps generating over USD 86 billion in revenue, with the average user spending almost 1.5 months per year using apps (App Annie, 2018).
- The two main mobile app formats are .apk (Android package) and .ipa (iOS application archive); APK files are always also valid .zip archives that can be unzipped, and the AndroidManifest.xml file describes metadata (name, version, contents) and app permissions.
- The walkthrough method is adapted from Light, Burgess, and Duguay (2016), who define it as "step-by-step observation and documentation of an app's screens, features and flows of activity" contextualized within an app's "environment of expected use" (pp. 881–886); the authors extend it to comparative, multi-sided, and historical walkthroughs using personas.
- Named tools/repositories include the DMI Google Play Similar Apps and iTunes Store tools, Exodus Privacy and the DMI App Tracker Tracker (built on Exodus) for tracker detection, Appcestry (Chao, 2018), Raccoon for downloading APKs from Google Play, Cydia/Cydia Impactor (iOS), and Android repositories Aptoide, APKPure, APKMirror, and F-Droid.
- Network connection analysis uses tools such as Wireshark and tcpdump to inspect HTTP query parameters; Figure 3 shows an encoded MoPub ad-request URL exposing device name, bundle ID, gender, age, lat/long, screen dimensions, language, carrier, and permissions over unencrypted HTTP.
- App stores are framed as "obligatory passage points" (Callon, 1984; Fagerjord, 2015) operating on a multi-sided marketplace model (Rochet & Tirole, 2003), and most stores do not offer systematic data access via standard APIs, with Apple's App Store cited as one exception.
- The article distinguishes "static" methods (extracted from a native situation, e.g., APK research) from "dynamic" methods (deployed within a native situation, requiring personas, VPNs, or research phones); examples illustrate include mindfulness apps (Figure 1) and dating apps Tinder, Grindr, OkCupid, Christian Mingle, Badoo, BeeTalk (Figures 2 and 4).

## Critical notes from the literature
- The authors explicitly acknowledge "infrastructural resistance" (Proposition 2): obfuscation, certificate pinning, encrypted channels, and DRM (e.g., iOS appearing "off-limits") frustrate decompiling and packet sniffing, so analyses yield only partial perspectives.
- They flag a "presentism" problem (Proposition 7): app stores display only latest versions and app repositories are incomplete and may contain illegal or spammy software; emulating old versions can mix current dynamically loaded assets with old frameworks, complicating historical research.
- The paper notes a Silicon Valley bias (Proposition 8): methods are built around Google Play and Apple's App Store, while country/manufacturer-specific stores (e.g., Yandex.Store with no web interface, China's banned Google Play, Tencent's store) require different language skills and registration and may require reworking the proposed methods.
- The authors stress ethical hazards (Proposition 9): handling large-scale network connection data, providing personal data for registration, using personas that may violate apps' terms and conditions and affect other users; there is "no straightforward ethical checklist," and they warn against replicating apps' "ethical deficit."
- Scope is largely limited to mobile apps; the authors note the framework might be extended to other software ecosystems (sensor media, smart cities, IoT) and to developer-side entry points (IDEs) and "geo-situating," but these remain proposals rather than demonstrated methods.

## Key topics covered
app studies; mobile apps; situatedness / multi-situatedness; multi-sidedness; software studies; platform studies; infrastructure studies; app stores (Google Play, Apple App Store, third-party repositories); obligatory passage points; multi-sided markets; app interfaces; walkthrough method; user and research personas; behavioral/dark-pattern design; app packages (.apk/.ipa); decompilation; AndroidManifest.xml; SDKs; trackers; Exodus Privacy / App Tracker Tracker; network connections; packet inspection (Wireshark, tcpdump); CDNs, cloud services, ad networks; static vs dynamic methods; digital methods; political economy of apps; research ethics; obfuscation / infrastructural resistance; presentism; Silicon Valley imperialism
