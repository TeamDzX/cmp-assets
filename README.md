# cmp-assets

Generated visual assets for the **Business Dashboard** landing page
(invoicing & UK statutory filings app for SMEs and sole traders).

- Images are generated with `gen_images.py` on a self-hosted ComfyUI
  (Flux 2 Klein) server — seeds are fixed so the set is reproducible.
- The landing page hot-links them via
  `https://raw.githubusercontent.com/TeamDzX/cmp-assets/main/images/<name>.jpg`,
  keeping the Wix HTML embed light.
- `hero-mist.jpg` — faint hero backdrop (one soft indigo/violet watercolour wash).
- `pack-*.jpg` — square cover art for the document-template pack cards.

To add a pack cover: add an entry to `COVERS` in `gen_images.py`, run it,
commit, then set `cover: ASSETS + "<name>.jpg"` on the package in the
landing page's `PACKAGES` array.
