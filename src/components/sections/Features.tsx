"use client";

import { Container } from "@/components/ui/Container";
import { Card } from "@/components/ui/Card";
import { Badge } from "@/components/ui/Badge";
import { FadeIn } from "@/components/animations/FadeIn";
import { SplitTextReveal } from "@/components/animations/SplitTextReveal";

interface Feature {
  icon: string;
  title: string;
  description: string;
}

interface FeaturesProps {
  badge?: string;
  headline: string;
  subheadline?: string;
  features: Feature[];
  columns?: 2 | 3 | 4;
}

const gridCols = {
  2: "grid-cols-1 md:grid-cols-2",
  3: "grid-cols-1 md:grid-cols-2 lg:grid-cols-3",
  4: "grid-cols-1 md:grid-cols-2 lg:grid-cols-4",
};

export function Features({
  badge,
  headline,
  subheadline,
  features,
  columns = 3,
}: FeaturesProps) {
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

        <div className={`grid gap-6 ${gridCols[columns]}`}>
          {features.map((feature, i) => (
            <FadeIn key={feature.title} delay={i * 0.1}>
              <Card className="h-full">
                <div className="text-3xl mb-4">{feature.icon}</div>
                <h3 className="text-lg font-semibold text-[#e3e2e2] mb-2">
                  {feature.title}
                </h3>
                <p className="text-[#a1a1aa] leading-relaxed">
                  {feature.description}
                </p>
              </Card>
            </FadeIn>
          ))}
        </div>
      </Container>
    </section>
  );
}
