"use client";

import { motion } from "framer-motion";
import { Container } from "@/components/ui/Container";
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";
import { SplitTextReveal } from "@/components/animations/SplitTextReveal";

interface HeroProps {
  badge?: string;
  headline: string;
  subheadline: string;
  ctaPrimary: { text: string; href: string };
  ctaSecondary?: { text: string; href: string };
  image?: string;
}

export function Hero({
  badge,
  headline,
  subheadline,
  ctaPrimary,
  ctaSecondary,
  image,
}: HeroProps) {
  return (
    <section className="relative min-h-screen flex items-center overflow-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(99,102,241,0.08),transparent_60%)]" />

      <Container className="relative z-10 py-32">
        <div className="mx-auto max-w-4xl text-center">
          {badge && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5 }}
            >
              <Badge>{badge}</Badge>
            </motion.div>
          )}

          <SplitTextReveal
            text={headline}
            as="h1"
            delay={0.2}
            className="mt-6 text-4xl font-bold leading-[1.1] tracking-tight text-[#e3e2e2] sm:text-5xl md:text-6xl lg:text-7xl"
          />

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.6 }}
            className="mt-6 text-lg leading-relaxed text-[#a1a1aa] md:text-xl max-w-2xl mx-auto"
          >
            {subheadline}
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.8 }}
            className="mt-10 flex flex-wrap items-center justify-center gap-4"
          >
            <Button href={ctaPrimary.href} size="lg">
              {ctaPrimary.text}
            </Button>
            {ctaSecondary && (
              <Button href={ctaSecondary.href} variant="secondary" size="lg">
                {ctaSecondary.text}
              </Button>
            )}
          </motion.div>
        </div>

        {image && (
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1 }}
            className="mt-20"
          >
            <div className="relative mx-auto max-w-5xl overflow-hidden rounded-2xl border border-[rgba(255,255,255,0.06)] shadow-2xl">
              <img
                src={image}
                alt="Product preview"
                className="w-full"
              />
            </div>
          </motion.div>
        )}
      </Container>
    </section>
  );
}
