# Research atlas

A dependency-free browser view of the lab's generated `catalog.json`. It groups questions, probes, studies, foundations work, and open threads. Search and filters use the catalog data; each card links back to the repository.

From the repository root:

```sh
python3 tools/build_catalog.py
python3 -m http.server 8765
```

Open `http://localhost:8765/research-atlas/`. Reload the page after the catalog changes. The browser fetches `../catalog.json` each time, so there is no separate card list to maintain.

The atlas reports catalog metadata and available files. A registered reproduction command is a checkable source, not a grade of evidence or a claim about a real workplace. The catalog does not contain reliable links between every study, so the atlas groups entries instead of drawing inferred connections.
