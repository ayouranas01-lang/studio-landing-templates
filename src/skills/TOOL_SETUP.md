# Tool Setup Guide

## 1. Claude Code
Already running. This is your orchestrator.

## 2. Nano Banana (Image Generation)

Nano Banana is a Gemini CLI extension for generating real product photography.

### Setup:
```bash
# Install Gemini CLI first (if not installed)
npm install -g @anthropic-ai/gemini-cli

# Install Nano Banana extension
gemini extensions install https://github.com/gemini-cli-extensions/nanobanana

# Set your API key (get one from https://aistudio.google.com/apikey)
export NANOBANANA_API_KEY="your-api-key-here"
```

### Usage:
```bash
/generate "professional product photo of [your product] on minimal background"
/icon "app logo" --sizes="64,128,256" --type="app-icon"
/edit hero.png "adjust lighting, add depth of field"
```

## 3. Motion (Framer Motion)

Already installed in this project:
```bash
npm install framer-motion
```

Pre-built components available in `src/components/animations/`:
- `FadeIn` — Directional fade with viewport trigger
- `SplitTextReveal` — Word-by-word text reveal
- `ScrollReveal` — GSAP-powered scroll animation

## 4. GSAP + GreenSock Skills

Already installed:
```bash
npm install gsap @gsap/react
```

GreenSock Skills repo: https://github.com/greensock/gsap-skills

Pre-built components available in `src/components/animations/`:
- `PinnedSection` — Pin content while scrolling (pinned-scrub pattern)
- `StickyStack` — Cards stack on scroll (sticky-stack pattern)
- `HorizontalScroll` — Horizontal movement on vertical scroll

## 5. 21st Dev MCP

Connect to 21st Dev for premium React components:
- URL: https://21st.dev/mcp
- Provides a catalog of production-ready components
- Once connected, Claude can pull components by name instead of building from scratch

### Setup:
Add to your MCP configuration:
```json
{
  "mcpServers": {
    "21st-dev": {
      "url": "https://21st.dev/mcp"
    }
  }
}
```

## 6. Lenis (Smooth Scroll)

Already installed and configured in the layout:
```bash
npm install lenis
```

The `SmoothScroll` component wraps the entire app for buttery-smooth scrolling.
