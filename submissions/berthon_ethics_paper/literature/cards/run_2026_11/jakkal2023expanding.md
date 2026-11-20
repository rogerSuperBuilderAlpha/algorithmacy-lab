---
citekey: jakkal2023expanding
title: Expanding cloud logging to give customers deeper security visibility
authors: Jakkal, Vasu
year: 2023
doi: null
source_basis: full-text
pages_read: paras 1-11 (whole post; paragraphs counted from the first body paragraph under the byline)
local_path: ~/iit-playground/berthon_ethics_local/run_2026_11/B1/ms_cloudlogging_2023/ms_cloudlogging_2023.txt
sha256: 0205248b7fe32e5c64ab5cd30cdc7876fb9191343767591e9a3ebabef9c8b978
verified: corrected
structure_sections: 4.4-record; 4.1; 7-D04; counter
type: corporate blog post
venue: Microsoft Security Blog, 19 July 2023
source_url: https://www.microsoft.com/en-us/security/blog/?p=131016
record_check: publisher page; saved HTML gives heading "Expanding cloud logging to give customers deeper security visibility", HTML title "How Microsoft is expanding cloud logging to give customers deeper security visibility | Microsoft Security Blog", byline Vasu Jakkal (Corporate Vice President, Microsoft Security), datePublished 2023-07-19T14:00:00Z; HTML sha256 9d3bc80d…
facet: B1
supersedes: none
written: 2026-11-18
---

## Summary

Read in full (saved HTML and its extracted text; the extract carries zero-width characters in the heading only). The
post is Microsoft's statement of 19 July 2023, written in response to nation-state cyberthreats and after coordination
with CISA, that it would widen the cloud security logs available to customers. Customers on the standard audit tier
would receive "detailed logs of email access" and more than 30 other log types that had until then required the
premium subscription, and default retention would rise from 90 to 180 days, at no added cost, rolling out from
September 2023. The post presents the change as a result of its "close partnership with CISA", and quotes CISA's
director welcoming the decision after "over a year" of work. It names no particular intrusion. It
says logs do not prevent attacks but serve forensics and incident response.

## Key facts it relies on

- Occasion: "In response to the increasing frequency and evolution of nation-state cyberthreats". para. 1 [quote]
- The steps followed coordination with customers and CISA "about the types of security log data Microsoft provides to cloud customers for insight and analysis." para. 1 [quote]
- Limit of logs: "These logs themselves do not prevent attacks". para. 2 [quote]
- The change: "we will include access to wider cloud security logs for our worldwide customers at no additional cost." para. 3 [quote]
- Before the change, logs including "detailed logs of email access and more than 30 other types of log data previously only available at the Microsoft Purview Audit (Premium) subscription level" were not in the standard tier; default retention for standard customers rises "from 90 days to 180 days". para. 5 [quote]
- E5/G5 premium customers keep access to all audit events plus "intelligent insights" and longer retention. para. 6 [paraphrase]
- CISA "has called for the industry to take action in order to better protect itself from potential cyberattacks". para. 7 [quote]
- CISA Director Jen Easterly, quoted: "Microsoft’s decision to make necessary log types available to the broader cybersecurity community at no additional cost". para. 9 [quote]
- Rollout: "Microsoft will begin rolling out these logging updates in September 2023 to all government and commercial customers." para. 10 [quote]
- Custody: "Microsoft has historically provided security log data to customers, with options to maintain logs through Microsoft’s storage services or with other security and storage vendors, depending on preferences." para. 10 [quote]

## Critical notes

Microsoft-authored and promotional; it states the change and its reasons as Microsoft frames them. It names no
intrusion and does not say how customers without the premium tier fared before. The scout's lead for an independent
account, the Cyber Safety Review Board's 2024 report, was not reached in this run (scout: CISA PDF 404), so nothing on
this card rests on it. The page shows that which log types a customer could see, and for how long, depended on the
licence tier (para. 5); that Microsoft presents the change as "a result of our close partnership with CISA, which has
called for the industry to take action" (para. 7); and that CISA's director called the log types "necessary" (para. 9).
The record at issue is between provider and deploying organisation; individuals whose mail was accessed are not
mentioned. The post was read on a live page fetched 18 Nov 2026; the saved HTML gives dateModified 2025-06-18, so its
text may have been edited since 2023.
Person acted on gets: record no (the logs go to "customers", i.e. tenant organisations, paras 3-5); brake n/a;
envelope n/a; standing no; loss cover no.

Corrected by the Fable read (V-B-1): "until outside pressure moved it" was an inference and is replaced by the post's own account of why it acted (para. 7); "the intrusion that prompted it" presupposed an intrusion the post never mentions, so the Summary and this note now say only that none is named; the Cyber Safety Review Board report is marked as an unreached lead; "nation-state attacks" changed to the post's "cyberthreats"; the page's dateModified is added.
