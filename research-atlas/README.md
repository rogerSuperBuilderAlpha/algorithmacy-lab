# Research atlas

A dependency-free browser view of the lab's generated `catalog.json` and the six research programs' reading cards. It groups lab papers, questions, probes, studies, foundations work, open threads, and outside papers the lab has read. Search and filters use the generated data; each entry links back to the repository.

From the repository root:

```sh
python3 tools/build_catalog.py
python3 research-atlas/build_cards.py
python3 research-atlas/build_snapshot.py
python3 -m http.server 8765
```

Open `http://localhost:8765/research-atlas/`. Reload the page after the source files change. The browser checks `../catalog.json` and `./cards.json` against `snapshot.json` before showing them. Run the snapshot builder after either index changes. The second index is generated from `org_frontier/research/*/literature/cards/*.md`; CI checks that both indexes and the snapshot stay current.

Lab papers are the `paper.md` files attached to full research questions. Reading cards are notes on outside papers, not lab results. The atlas reports catalog metadata and available files. A registered reproduction command is a checkable source, not a grade of evidence or a claim about a real workplace. The catalog does not contain reliable links between every study, so the atlas groups entries instead of drawing inferred connections.
