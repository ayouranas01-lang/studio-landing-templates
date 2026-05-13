"use client";

import { Container } from "@/components/ui/Container";
import { Badge } from "@/components/ui/Badge";
import { FadeIn } from "@/components/animations/FadeIn";
import { SplitTextReveal } from "@/components/animations/SplitTextReveal";

interface Testimonial {
  quote: string;
  author: string;
  role: string;
  avatar?: string;
}

interface TestimonialsProps {
  badge?: string;
  headline: string;
  testimonials: Testimonial[];
}

export function Testimonials({
  badge,
  headline,
  testimonials,
}: TestimonialsProps) {
  return (
    <section className="py-24 md:py-32 bg-[rgba(255,255,255,0.02)]">
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
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {testimonials.map((testimonial, i) => (
            <FadeIn key={testimonial.author} delay={i * 0.1}>
              <div className="flex flex-col rounded-2xl border border-[rgba(255,255,255,0.06)] bg-[#1c1e1e] p-8">
                <blockquote className="flex-1 text-[#e3e2e2] leading-relaxed">
                  &ldquo;{testimonial.quote}&rdquo;
                </blockquote>
                <div className="mt-6 flex items-center gap-3">
                  {testimonial.avatar ? (
                    <img
                      src={testimonial.avatar}
                      alt={testimonial.author}
                      className="h-10 w-10 rounded-full object-cover"
                    />
                  ) : (
                    <div className="flex h-10 w-10 items-center justify-center rounded-full bg-[rgba(99,102,241,0.15)] text-sm font-medium text-[#6366f1]">
                      {testimonial.author
                        .split(" ")
                        .map((n) => n[0])
                        .join("")}
                    </div>
                  )}
                  <div>
                    <p className="text-sm font-medium text-[#e3e2e2]">
                      {testimonial.author}
                    </p>
                    <p className="text-xs text-[#a1a1aa]">
                      {testimonial.role}
                    </p>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </Container>
    </section>
  );
}
