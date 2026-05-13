# Master Landing Page Prompt Template

Copy this prompt, adapt for your product, and use with Claude Code.

---

```
I want to build a studio-grade landing page for [PRODUCT NAME].

Reference sites: [URL1], [URL2], [URL3]
Tone: [premium / playful / industrial / editorial]
Audience: [who buys this]

Use:
- Motion + GSAP + Lenis for smooth scroll and animations
- 21st Dev MCP for components
- Nano Banana for the hero image

Follow this order:
1. Scrape the references and extract palette, type, motion vocabulary
2. Lock design tokens before writing any component
3. Plan 5–8 sections with distinct visual treatments
4. For each section, pick a named scroll pattern (pinned-scrub, sticky-stack, etc)
5. Pull components from 21st Dev where possible
6. Generate the hero image via Nano Banana
7. Take screenshots at 1440px after each section, compare to references, iterate

Don't ship until the screenshots feel like the reference sites.
```

## Named Animation Patterns

Use these keywords in your prompts — each maps to a real pattern:

| Keyword | Effect | Reference |
|---|---|---|
| `pinned-scrub` | Page locks while content animates | Apple Vision Pro hero |
| `sticky-stack` | Cards hold while the next slides over | Stripe pricing |
| `image-sequence-scrub` | Frame-by-frame product orbit by scroll | Apple AirPods |
| `horizontal-on-vertical` | Scroll down, content moves sideways | Linear features |
| `splittext-reveal` | Letters animate in one by one | Stripe heroes |

## Design Token Defaults (Anti-Slop)

- Background: `#121414` (NOT pure black `#000`)
- Foreground text: `#e3e2e2` (NOT pure white `#fff`)
- Surface: `#1c1e1e`
- Accent: `#6366f1` (customize per brand)
- Border: `rgba(255, 255, 255, 0.06)`
- Muted text: `#a1a1aa`

## Section Planning Guide

1. **Hero** — First impression. Use `splittext-reveal` + subtle gradient
2. **Problem** — What pain does the user have? Dark, minimal
3. **Features** — Grid of 3-6 cards with icons. Use `FadeIn` stagger
4. **Deep Dive** — One feature at a time. Use `pinned-scrub` or `sticky-stack`
5. **Social Proof** — Testimonials grid. Real photos, real names
6. **Pricing** — 2-3 tiers. Highlight the recommended one
7. **Closing CTA** — Mirror the hero energy. Strong, direct
8. **Footer** — Navigation links, brand info
