#!/usr/bin/env python3
"""Generate Business Dashboard landing imagery -> images/*.jpg (web-sized).

Covers are square (cropped by CSS either as a left column or top banner);
the hero backdrop is wide. Style is shared so the set reads as one family.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/.claude/scripts/imagegen"))
from comfy_gen import generate

STYLE = (", abstract conceptual digital art, soft glowing translucent glass shapes, "
         "deep indigo and royal violet palette with warm white highlights, "
         "dark navy background, premium minimal fintech aesthetic, generous negative space, "
         "no text, no letters, no numbers, no people, no watermark")

COVERS = {
 "pack-agreements":       "two overlapping translucent glass sheets of paper with one elegant glowing pen-stroke signature curve sweeping across them",
 "pack-general":          "a neat ascending fan of completely blank translucent glass sheets like floating cards, soft light rising from between them, pure smooth surfaces",
 "pack-engagement":       "an opening glass folder radiating warm welcoming light, a small glowing sphere arriving into it",
 "pack-credit-control":   "a flowing luminous ribbon threading through floating translucent glass coins, settling into balance",
 "pack-working-together": "two interlocking translucent glass rings merging where they overlap into a brighter glow",
 "pack-project-lifecycle":"a circular orbit of small glowing milestone spheres around a bright central core, one arc segment highlighted",
}

HERO = ("a vast soft abstract gradient field, gentle indigo and violet aurora ribbons flowing "
        "horizontally across a pale off-white background, faint translucent ledger grid lines "
        "dissolving into light, premium minimal fintech art, very light and airy, lots of negative space, "
        "no text, no letters, no numbers, no people, no watermark")

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    img = lambda n: os.path.join(here, "images", n + ".jpg")
    generate(img("hero-aurora"), HERO, seed=101, width=1216, height=832)
    for i, (name, prompt) in enumerate(COVERS.items()):
        generate(img(name), prompt + STYLE, seed=201 + i, width=1024, height=1024, max_px=640)

if __name__ == "__main__":
    main()
