export const tokens = {
  colors: {
    background: {
      dark: "#121414",
      light: "#fafafa",
    },
    foreground: {
      dark: "#e3e2e2",
      light: "#1a1a1a",
    },
    accent: {
      primary: "#6366f1",
      secondary: "#8b5cf6",
      muted: "#a1a1aa",
    },
    surface: {
      dark: "#1c1e1e",
      light: "#ffffff",
    },
    border: {
      dark: "rgba(255,255,255,0.08)",
      light: "rgba(0,0,0,0.08)",
    },
  },
  fonts: {
    heading: "var(--font-geist-sans)",
    body: "var(--font-geist-sans)",
    mono: "var(--font-geist-mono)",
  },
  spacing: {
    section: "clamp(80px, 12vw, 160px)",
    container: "clamp(16px, 5vw, 64px)",
  },
  breakpoints: {
    sm: "640px",
    md: "768px",
    lg: "1024px",
    xl: "1280px",
    "2xl": "1440px",
  },
  animation: {
    duration: {
      fast: 0.3,
      normal: 0.6,
      slow: 1.0,
    },
    ease: {
      smooth: [0.25, 0.1, 0.25, 1.0] as const,
      spring: [0.43, 0.13, 0.23, 0.96] as const,
      snappy: [0.6, 0.01, 0.05, 0.95] as const,
    },
  },
} as const;
