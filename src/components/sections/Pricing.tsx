"use client";

import { motion } from "framer-motion";
import { Container } from "@/components/ui/Container";
import { Button } from "@/components/ui/Button";
import { Badge } from "@/components/ui/Badge";
import { FadeIn } from "@/components/animations/FadeIn";
import { SplitTextReveal } from "@/components/animations/SplitTextReveal";

interface PricingTier {
  name: string;
  price: string;
  period?: string;
  description: string;
  features: string[];
  cta: { text: string; href: string };
  highlighted?: boolean;
}

interface PricingProps {
  badge?: string;
  headline: string;
  subheadline?: string;
  tiers: PricingTier[];
}

export function Pricing({ badge, headline, subheadline, tiers }: PricingProps) {
  return (
    <section className="py-24 md:py-32">
      <Container>
        <div className="mx-auto max-w-3xl text-center mb-16">
          {badge && (
            <FadeIn>
              <Badge>{badge}</Badge>
            </FadeIn>
          )}
          <SplitTextReveal
            text={headline}
            as="h2"
            className="mt-4 text-3xl font-bold tracking-tight text-[#e3e2e2] sm:text-4xl md:text-5xl"
          />
          {subheadline && (
            <FadeIn delay={0.3}>
              <p className="mt-4 text-lg text-[#a1a1aa]">{subheadline}</p>
            </FadeIn>
          )}
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3 max-w-5xl mx-auto">
          {tiers.map((tier, i) => (
            <FadeIn key={tier.name} delay={i * 0.15}>
              <motion.div
                whileHover={{ y: -6 }}
                transition={{ duration: 0.3 }}
                className={`flex flex-col rounded-2xl border p-8 ${
                  tier.highlighted
                    ? "border-[rgba(99,102,241,0.4)] bg-[rgba(99,102,241,0.06)]"
                    : "border-[rgba(255,255,255,0.06)] bg-[#1c1e1e]"
                }`}
              >
                <p className="text-sm font-medium tracking-wider uppercase text-[#a1a1aa]">
                  {tier.name}
                </p>
                <div className="mt-4 flex items-baseline gap-1">
                  <span className="text-4xl font-bold text-[#e3e2e2]">
                    {tier.price}
                  </span>
                  {tier.period && (
                    <span className="text-[#a1a1aa]">/{tier.period}</span>
                  )}
                </div>
                <p className="mt-2 text-sm text-[#a1a1aa]">{tier.description}</p>

                <ul className="mt-8 flex-1 space-y-3">
                  {tier.features.map((feature) => (
                    <li
                      key={feature}
                      className="flex items-start gap-3 text-sm text-[#e3e2e2]"
                    >
                      <svg
                        className="mt-0.5 h-4 w-4 shrink-0 text-[#6366f1]"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                      >
                        <path
                          fillRule="evenodd"
                          d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                          clipRule="evenodd"
                        />
                      </svg>
                      {feature}
                    </li>
                  ))}
                </ul>

                <div className="mt-8">
                  <Button
                    href={tier.cta.href}
                    variant={tier.highlighted ? "primary" : "secondary"}
                    className="w-full"
                  >
                    {tier.cta.text}
                  </Button>
                </div>
              </motion.div>
            </FadeIn>
          ))}
        </div>
      </Container>
    </section>
  );
}
