"use client";

import { Hero } from "@/components/sections/Hero";
import { Features } from "@/components/sections/Features";
import { Pricing } from "@/components/sections/Pricing";
import { Testimonials } from "@/components/sections/Testimonials";
import { CTA } from "@/components/sections/CTA";
import { Footer } from "@/components/sections/Footer";
import { ScrollReveal } from "@/components/animations/ScrollReveal";
import { HorizontalScroll } from "@/components/animations/HorizontalScroll";
import { StickyStack } from "@/components/animations/StickyStack";
import { Card } from "@/components/ui/Card";
import { Container } from "@/components/ui/Container";
import { Badge } from "@/components/ui/Badge";
import { FadeIn } from "@/components/animations/FadeIn";

export default function Home() {
  return (
    <main>
      {/* ─── Hero Section ─── */}
      <Hero
        badge="Studio-Grade Templates"
        headline="Build landing pages that look like a designer made them"
        subheadline="A complete toolkit of premium templates, animation patterns, and design tokens. Powered by Motion, GSAP, and Lenis for buttery-smooth scroll experiences."
        ctaPrimary={{ text: "Get Started", href: "#features" }}
        ctaSecondary={{ text: "View Components", href: "#showcase" }}
      />

      {/* ─── Features Section ─── */}
      <Features
        badge="The Stack"
        headline="Five tools, zero AI slop"
        subheadline="Each tool solves a specific problem. Together they produce studio-grade results."
        features={[
          {
            icon: "🧠",
            title: "Claude Code",
            description:
              "The brain. Wires everything else and writes the site with precision and intent.",
          },
          {
            icon: "🍌",
            title: "Nano Banana",
            description:
              "Google's image model for real product photography. No more AI art or stock photos.",
          },
          {
            icon: "🎬",
            title: "Motion",
            description:
              "Formerly Framer Motion. The animation runtime that makes every interaction feel alive.",
          },
          {
            icon: "📜",
            title: "GSAP + ScrollTrigger",
            description:
              "The scroll vocabulary. Pinned scrub, sticky stack, horizontal scroll — all by name.",
          },
          {
            icon: "🧩",
            title: "21st Dev MCP",
            description:
              "Premium pre-built React components. Pull real ones instead of writing from scratch.",
          },
          {
            icon: "🌊",
            title: "Lenis Smooth Scroll",
            description:
              "Buttery smooth scrolling that feels native. The foundation for every scroll animation.",
          },
        ]}
        columns={3}
      />

      {/* ─── Horizontal Scroll Showcase ─── */}
      <section id="showcase" className="py-24">
        <Container className="mb-12">
          <FadeIn>
            <Badge>Animation Patterns</Badge>
          </FadeIn>
          <FadeIn delay={0.1}>
            <h2 className="mt-4 text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
              Scroll patterns that ship
            </h2>
          </FadeIn>
          <FadeIn delay={0.2}>
            <p className="mt-4 text-lg text-[#a1a1aa] max-w-2xl">
              Named patterns Claude already knows. Use them by name for consistent, premium results.
            </p>
          </FadeIn>
        </Container>
        <HorizontalScroll>
          {[
            {
              name: "pinned-scrub",
              desc: "Page locks while content animates",
              ref: "Apple Vision Pro hero",
            },
            {
              name: "sticky-stack",
              desc: "Cards hold while the next slides over",
              ref: "Stripe pricing",
            },
            {
              name: "image-sequence-scrub",
              desc: "Frame-by-frame product orbit driven by scroll",
              ref: "Apple AirPods",
            },
            {
              name: "horizontal-on-vertical",
              desc: "Scroll down, content moves sideways",
              ref: "Linear features",
            },
            {
              name: "splittext-reveal",
              desc: "Letters animate in one by one",
              ref: "Stripe heroes",
            },
          ].map((pattern) => (
            <div
              key={pattern.name}
              className="min-w-[340px] md:min-w-[400px] flex-shrink-0 rounded-2xl border border-[rgba(255,255,255,0.06)] bg-[#1c1e1e] p-8"
            >
              <code className="text-sm font-mono text-[#6366f1]">
                {pattern.name}
              </code>
              <h3 className="mt-3 text-xl font-semibold text-[#e3e2e2]">
                {pattern.desc}
              </h3>
              <p className="mt-2 text-sm text-[#a1a1aa]">
                Reference: {pattern.ref}
              </p>
            </div>
          ))}
        </HorizontalScroll>
      </section>

      {/* ─── Sticky Stack Demo ─── */}
      <section className="py-24">
        <Container className="mb-12">
          <ScrollReveal>
            <Badge>Sticky Stack</Badge>
            <h2 className="mt-4 text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
              The 7-step framework
            </h2>
            <p className="mt-4 text-lg text-[#a1a1aa] max-w-2xl">
              Don&apos;t ask Claude to &ldquo;build me a landing page.&rdquo;
              Walk it through these steps, in order.
            </p>
          </ScrollReveal>
        </Container>
        <Container>
          <StickyStack>
            {[
              {
                step: "01",
                title: "Show it what good looks like",
                desc: "Send 3-5 reference URLs. Tell Claude to study them before writing a single line.",
              },
              {
                step: "02",
                title: "Lock the look before any code",
                desc: "Colors, fonts, vibe. Write them down once. Every section obeys this.",
              },
              {
                step: "03",
                title: "Plan sections like a magazine",
                desc: "Hero, problem, feature deep-dive, comparison, pricing, closing CTA. Different visual treatments.",
              },
              {
                step: "04",
                title: "Pick how things move",
                desc: "Use named patterns: pinned-scrub, sticky-stack, splittext-reveal. Naming them activates training data.",
              },
              {
                step: "05",
                title: "Pull in real parts",
                desc: "Use 21st Dev components and GreenSock patterns. Don't let it write custom ones unless needed.",
              },
              {
                step: "06",
                title: "Generate the imagery",
                desc: "Nano Banana for the hero. Real product photography beats AI illustrations.",
              },
              {
                step: "07",
                title: "Test, fix, repeat",
                desc: "Screenshot after every section. Compare to references. Iterate until Awwwards-worthy.",
              },
            ].map((item) => (
              <Card key={item.step} className="mb-6">
                <div className="flex items-start gap-6">
                  <span className="text-4xl font-bold text-[rgba(99,102,241,0.3)] font-mono">
                    {item.step}
                  </span>
                  <div>
                    <h3 className="text-xl font-semibold text-[#e3e2e2]">
                      {item.title}
                    </h3>
                    <p className="mt-2 text-[#a1a1aa] leading-relaxed">
                      {item.desc}
                    </p>
                  </div>
                </div>
              </Card>
            ))}
          </StickyStack>
        </Container>
      </section>

      {/* ─── Testimonials Section ─── */}
      <Testimonials
        badge="What People Say"
        headline="Real results, not templates"
        testimonials={[
          {
            quote:
              "Switched from generic AI output to this stack. Our conversion rate went up 40% in the first week.",
            author: "Sarah Chen",
            role: "Growth Lead, Startup X",
          },
          {
            quote:
              "The animation patterns alone saved us 20 hours of custom development per landing page.",
            author: "Marcus Rivera",
            role: "Frontend Engineer",
          },
          {
            quote:
              "Finally, a way to use AI for design without everything looking the same. The scroll patterns are chef's kiss.",
            author: "Amira Okafor",
            role: "Creative Director",
          },
        ]}
      />

      {/* ─── Pricing Section ─── */}
      <Pricing
        badge="Pricing"
        headline="Start building today"
        subheadline="Everything you need, nothing you don't."
        tiers={[
          {
            name: "Starter",
            price: "Free",
            description: "For personal projects and experiments.",
            features: [
              "All section templates",
              "Animation components",
              "Design tokens",
              "Community support",
            ],
            cta: { text: "Get Started", href: "#" },
          },
          {
            name: "Pro",
            price: "$49",
            period: "mo",
            description: "For teams shipping landing pages at scale.",
            features: [
              "Everything in Starter",
              "21st Dev MCP access",
              "Nano Banana integration",
              "Priority support",
              "Custom design tokens",
            ],
            cta: { text: "Start Free Trial", href: "#" },
            highlighted: true,
          },
          {
            name: "Enterprise",
            price: "Custom",
            description: "For organizations with specific needs.",
            features: [
              "Everything in Pro",
              "Custom component library",
              "Dedicated support",
              "SLA guarantee",
              "White-label option",
            ],
            cta: { text: "Contact Sales", href: "#" },
          },
        ]}
      />

      {/* ─── CTA Section ─── */}
      <CTA
        headline="Stop building AI slop. Start building studio-grade."
        subheadline="Five tools. Seven steps. One prompt. The gap between AI template and studio-grade is just these working together."
        ctaPrimary={{ text: "Get the Template", href: "#" }}
        ctaSecondary={{ text: "Read the Guide", href: "#" }}
      />

      {/* ─── Footer ─── */}
      <Footer
        logo="Studio Templates"
        description="Professional landing page templates built with the 5-tool stack for studio-grade results."
        columns={[
          {
            title: "Product",
            links: [
              { label: "Templates", href: "#" },
              { label: "Components", href: "#" },
              { label: "Animations", href: "#" },
              { label: "Documentation", href: "#" },
            ],
          },
          {
            title: "Stack",
            links: [
              { label: "Motion", href: "https://www.npmjs.com/package/framer-motion" },
              { label: "GSAP", href: "https://gsap.com" },
              { label: "Nano Banana", href: "https://github.com/gemini-cli-extensions/nanobanana" },
              { label: "21st Dev", href: "https://21st.dev/mcp" },
            ],
          },
          {
            title: "Resources",
            links: [
              { label: "Guide", href: "#" },
              { label: "Examples", href: "#" },
              { label: "GitHub", href: "#" },
              { label: "Support", href: "#" },
            ],
          },
        ]}
      />
    </main>
  );
}
