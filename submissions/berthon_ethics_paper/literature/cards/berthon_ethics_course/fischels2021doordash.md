---
citekey: fischels2021doordash
title: Why DoorDash Drivers Are On Strike
authors: Fischels, Josie
year: 2021
type: web
doi: null
venue: NPR (Business), 31 July 2021
source_basis: full-text
pages_read: all
source_url: https://www.npr.org/2021/07/31/1023265561/why-doordash-drivers-are-on-strike
local_path: /Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C2_law/npr_doordash.txt
sha256: af9e0dcafdef99c8a3420d5654810ca3e30d79696dd70f6d49c0a13855abcd94
manuscript_lines: [225, 327]
ledger_rows: [P6-023]
verified: true
written: 2026-10-14
---

Source note: the key `fischels2021doordash` comes from `review/v3/resolutions/C2_law.bib` (line 147), not
from `literature/references.bib`. The local text is extracted from the NPR page saved by the C2 round
(`npr_doordash.html`, sha256 7ad2aaf9...). The page carries the byline "By Josie Fischels", the date "July
31, 2021 8:03 PM ET" and the section "Business"; it identifies the author as "an intern on NPR's News Desk".

## Summary
The article explains a nationwide one-day strike by DoorDash drivers ("Dashers") on 31 July 2021,
organised on Reddit, TikTok and Facebook and apparently started by a Reddit post of 15 July. Drivers
demanded a minimum base pay of $4.50 and "tip transparency". DoorDash told NPR that base pay depends on
estimated time, distance and desirability and runs from $2 to $10+; drivers said the floor had been $3.
The app shows only a guaranteed minimum and does not reveal the customer's tip until after the driver
accepts; for large tips it shows an estimate, which DoorDash said it does because drivers would otherwise
decline low-tip orders. Some drivers used Para, "a third-party app that used DoorDash's code to let
drivers see the tip amount before accepting an order", until in mid-July it "no longer worked with
DoorDash's app". DoorDash's statement said Para "violated the company's terms of service" and "collects its
information by scraping content without authorization". The article quotes drivers (partly via
Motherboard and Insider) and DoorDash's description of the strikers as "a vocal minority".

## Key facts it relies on
- The strike: drivers "logged off the app for the day as part of a strike organized on social media ... demanding tip transparency and higher pay".
- Demand: a minimum "base pay" of $4.50; DoorDash's stated range "between $2 to $10+".
- The app "does not allow drivers to see how much a customer has tipped until after the driver accepts the order"; large tips are shown as an estimate.
- Para: "a third-party app that used DoorDash's code to let drivers see the tip amount before accepting an order"; "in mid-July, it no longer worked with DoorDash's app".
- DoorDash statement: "Para violated the company's terms of service. 'Para collects its information by scraping content without authorization from the DoorDash platform.'"
- A driver quoted via Motherboard: "Para showed that DoorDash is not as transparent as it could be."
- DoorDash called the strikers "a vocal minority".

## Critical notes from the literature
- The C2 resolution (`review/v3/resolutions/C2_law.md`, P6-023) judged the citation "cite-fixed (narrower)": Para "read order data on the worker's side. It did not keep a long-term record." It names UberCheats as a closer fit, which Uber had removed on a trademark complaint, not on terms of service (Vice, 18 Feb 2021, read through WebFetch in that round; not opened here).
- FIX_CHECK_C (P6-023, `review/v3/FIX_CHECK_C.md`) passed the v3 citation.
- From my reading: the article reports that Para stopped working and that DoorDash said it breached the terms of service. It does not say what DoorDash did to stop it. Much of the driver testimony is second-hand from Motherboard and Insider.

## Key topics covered
DoorDash, gig-work strike, tip transparency, base pay, third-party driver tools, Para, scraping, terms of service, information asymmetry, worker organising on social media

## Where the manuscript uses it
- l. 225: "The operator must permit and not obstruct the user-side record—operators today invoke terms of service against tools that collect it (Fischels, 2021)". Takes: a documented case of a platform invoking its terms of service against a worker-side data tool. Source: the Para paragraph and DoorDash's statement. **narrower**: DoorDash did invoke its terms of service against Para, but Para showed tip amounts before acceptance; it did not keep a record of the worker's jobs, and the article does not say how Para was stopped. "Operators" (plural, as a practice) rests on one instance.
- l. 327 (reference entry): "Fischels, J. (2021, July 31). Why DoorDash drivers are on strike. NPR." with the URL. Byline, date and URL match. The page's headline is "Why DoorDash Drivers Are On Strike"; the HTML title is "DoorDash Drivers Go On Strike".

## Verifier notes
- 2026-10-14. sha256 of `C2_law/npr_doordash.txt` recomputed: matches. Byline "By Josie Fischels", "July 31, 2021", "an intern on NPR's News Desk", headline "Why DoorDash Drivers Are On Strike" and HTML title "DoorDash Drivers Go On Strike : NPR" confirmed.
- Exact-string checks of every fact bullet (strike, $4.50, "$2 to $10+", tip hidden until acceptance, the Para sentences, DoorDash's statement on terms of service and scraping, the Motherboard quotation, "a vocal minority"). All present. The Para passage says only that "in mid-July, it no longer worked with DoorDash's app", so the card is right that the article does not say how Para was stopped.
- Bib: matches v3 l. 327. `references.bib` now holds the entry (the card's source note says it did not); its note points to `D/npr_doordash.html`, which does not exist; the files are in `C2_law/`.
- Use l. 225 (v3 text unchanged): **narrower** confirmed.
