# Studio Landing Templates

Professional landing page templates built with the **5-Tool Stack** for studio-grade results — no AI slop.

## The 5-Tool Stack

| Tool | Purpose |
|------|---------|
| **Claude Code** | The brain — orchestrates everything |
| **Nano Banana** | Google's image model for real product photography |
| **Motion** (Framer Motion) | Animation runtime |
| **GSAP + ScrollTrigger** | Named scroll patterns (pinned-scrub, sticky-stack, etc.) |
| **21st Dev MCP** | Premium pre-built React components |
| **Lenis** | Buttery-smooth scroll foundation |

## Quick Start

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## Project Structure

```
src/
├── app/
│   ├── layout.tsx          # Root layout with Lenis smooth scroll
│   ├── page.tsx            # Demo landing page showcasing all templates
│   └── globals.css         # Design tokens (anti-slop defaults)
├── components/
│   ├── animations/
│   │   ├── FadeIn.tsx          # Directional fade with viewport trigger
│   │   ├── SplitTextReveal.tsx # Word-by-word text animation
│   │   ├── ScrollReveal.tsx    # GSAP scroll-triggered reveal
│   │   ├── PinnedSection.tsx   # pinned-scrub pattern
│   │   ├── StickyStack.tsx     # sticky-stack pattern
│   │   └── HorizontalScroll.tsx# horizontal-on-vertical pattern
│   ├── sections/
│   │   ├── Hero.tsx            # Hero with split text + gradient
│   │   ├── Features.tsx        # Feature grid (2/3/4 columns)
│   │   ├── Pricing.tsx         # Pricing tiers with highlighting
│   │   ├── Testimonials.tsx    # Testimonial cards grid
│   │   ├── CTA.tsx             # Call-to-action section
│   │   └── Footer.tsx          # Multi-column footer
│   ├── ui/
│   │   ├── Button.tsx          # Animated button (primary/secondary/ghost)
│   │   ├── Card.tsx            # Hover card with border
│   │   ├── Badge.tsx           # Section label badge
│   │   └── Container.tsx       # Responsive container
│   └── SmoothScroll.tsx        # Lenis wrapper
├── lib/
│   ├── design-tokens.ts        # Design system values
│   └── animations.ts           # Motion variants library
└── skills/
    ├── LANDING_PAGE_PROMPT.md   # Master prompt template
    └── TOOL_SETUP.md            # Setup guide for all 5 tools
```

## Design Token Defaults (Anti-Slop)

```
Background: #121414  (NOT pure black)
Text:       #e3e2e2  (NOT pure white)
Surface:    #1c1e1e
Accent:     #6366f1
Border:     rgba(255,255,255, 0.06)
Muted:      #a1a1aa
```

## Named Animation Patterns

Use these keywords in prompts — each maps to a GSAP pattern:

- `pinned-scrub` — Page locks while content animates (Apple Vision Pro)
- `sticky-stack` — Cards hold while next slides over (Stripe pricing)
- `image-sequence-scrub` — Frame-by-frame orbit by scroll (Apple AirPods)
- `horizontal-on-vertical` — Scroll down, content moves sideways (Linear)
- `splittext-reveal` — Letters animate in one by one (Stripe heroes)

## The 7-Step Framework

1. Show it what good looks like (send reference URLs)
2. Lock the look before any code (design tokens)
3. Plan sections like a magazine
4. Pick named scroll patterns
5. Pull in real components (21st Dev)
6. Generate imagery (Nano Banana)
7. Test, fix, repeat

## Tool Setup

See `src/skills/TOOL_SETUP.md` for detailed setup instructions for each tool.

## Deploy

```bash
npm run build
```

Output is in the `out/` directory, ready for static hosting.
