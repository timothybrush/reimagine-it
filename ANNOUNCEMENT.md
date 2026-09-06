# v2.11.0 announcement — paste-ready

*Paste-ready for X/LinkedIn/dev.to. Cover: `docs/og.png`. Tags: `ai`, `webdev`, `css`, `opensource`.*

---

**reimagine-it v2.11.0 — distinct directions, proven on real pages**

We just cut v2.11.0. Two questions every design tool must answer honestly: *are your seventeen "directions" actually different?* and *does it work on pages you didn't write?* This release answers both with artifacts, not adjectives.

**1. Every direction now has its own layout grammar.** We measured structural (class-set) difference between all 17 tokens on the same sources and found the clusters that converged: cinematic looked like a webpage with chapters, photography carried the same glyph chips as lookbook, dashboard and infographic shared the same donut chart. Now cinematic ships a **filmstrip + timecode chapter grid** with per-scene frames, photography is **monospace-captioned plates with no overlays**, motion draws **labeled orbit rings** carrying the source anchors, and the data faces split into charts vs ranked bars vs data tables. Mean structural difference: **96.5%**, and the one remaining floor (webpage+landing, 76%) is tracked publicly as issue #38 — because two genuinely different products can share a skeleton.

**2. A proof lane of real public-domain pages.** `examples/public-sources/` rebuilds three U.S. government pages — the **Yellowstone visitor bulletin** (NPS), the **Artemis II mission overview** (NASA), and a **hurricane outlook** (NOAA/NWS) — none of which declare a palette in their copy. The engine had to derive color from language alone. Auto routed Artemis II to an interactive `3js` orbit view (100% fidelity), the hurricane outlook to a `landing` brief (100%), and Yellowstone to an `editorial` feature (84%, above the 80% floor we publish). Every artifact regenerates byte-identically in CI, and the sources are U.S. federal public domain — checkable at the linked agencies, committable without permission.

**3. The claims got audited too.** Six "runners-up" rows in the README's example table had drifted from the actual Auto reports after the routing changes; they're corrected against regenerated ground truth. New intake labels (`public-source`, `auto-routing`, `token-distinctness`) route future issues, and the docs site carries the public-proof section with stills.

Try it on your own page:

```bash
npx reimagine-it --auto -i page.html -o redesign.html
```

Offline, deterministic, no API key. The source is the brief.
