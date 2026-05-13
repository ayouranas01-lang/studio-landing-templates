"use client";

import { Container } from "@/components/ui/Container";
import { Button } from "@/components/ui/Button";
import { FadeIn } from "@/components/animations/FadeIn";
import { SplitTextReveal } from "@/components/animations/SplitTextReveal";

interface CTAProps {
  headline: string;
  subheadline?: string;
  ctaPrimary: { text: string; href: string };
  ctaSecondary?: { text: string; href: string };
}

export function CTA({
  headline,
  subheadline,
  ctaPrimary,
  ctaSecondary,
}: CTAProps) {
  return (
    <section className="py-24 md:py-32 relative overflow-hidden">
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom,rgba(99,102,241,0.1),transparent_60%)]" />

      <Container className="relative z-10">
        <div className="mx-auto max-w-3xl text-center">
          <SplitTextReveal
            text={headline}
            as="h2"
            className="text-3xl font-bold tracking-tight text-[#e3e2e2] sm:text-4xl md:text-5xl"
          />

          {subheadline && (
            <FadeIn delay={0.3}>
              <p className="mt-6 text-lg text-[#a1a1aa]">{subheadline}</p>
            </FadeIn>
          )}

          <FadeIn delay={0.5}>
            <div className="mt-10 flex flex-wrap items-center justify-center gap-4">
              <Button href={ctaPrimary.href} size="lg">
                {ctaPrimary.text}
              </Button>
              {ctaSecondary && (
                <Button href={ctaSecondary.href} variant="secondary" size="lg">
                  {ctaSecondary.text}
                </Button>
              )}
            </div>
          </FadeIn>
        </div>
      </Container>
    </section>
  );
}
