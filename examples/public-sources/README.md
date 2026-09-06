# Proof lane — real public-domain sources

These folders are **real government-page copy**, redesigned by the engine.
They exist to answer the hardest question a design tool must face: not
"can it make our own examples look good?" but "what does it do with a page
written by someone else, for an audience of millions, under rules it never saw?"

## Why this lane exists

The end-user and community examples are authored fixtures — brands the
maintainer wrote to exercise the engine. Real pages are messier: procedural
voice, no marketing rhythm, dense numbers, and no handy hex palette in the
copy. A redesign engine that only shines on its own showcase is a demo, not
a tool. Every source here is U.S. federal work in the public domain, so the
copy can be committed, regenerated, and audited without permission hurdles.

## Provenance

| Folder | Source | Facts from | Rights |
|---|---|---|---|
| `nps-yellowstone/` | National Park Service visitor bulletin | nps.gov/yell | Public domain (U.S. federal) |
| `nasa-artemis2/` | NASA Artemis II mission overview | nasa.gov/artemis | Public domain (U.S. federal) |
| `noaa-hurricane-outlook/` | NWS hurricane preparedness | weather.gov | Public domain (U.S. federal) |

The sources are paraphrased into compact single-page briefs (the engine is
built for HTML in, HTML out at page scale); every fact in them is real and
checkable at the linked agencies. No hex colors are declared in the copy —
unlike the in-house examples — so the engine must derive a palette from
language alone. That is the point.

## Regeneration

```bash
npx reimagine-it --auto -i examples/public-sources/<slug>/source.html \
  --output examples/public-sources/<slug>/auto.html
```

Auto picks the token; the committed report records it. CI re-runs Auto and
fails if the committed artifacts stop matching the engine.
