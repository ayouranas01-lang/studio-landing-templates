"use client";

import { useRef, useEffect, type ReactNode } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

interface StickyStackProps {
  children: ReactNode[];
  className?: string;
}

export function StickyStack({ children, className }: StickyStackProps) {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const cards = container.querySelectorAll<HTMLElement>(".sticky-card");

    const ctx = gsap.context(() => {
      cards.forEach((card, i) => {
        ScrollTrigger.create({
          trigger: card,
          start: `top-=${i * 30} top+=80`,
          endTrigger: container,
          end: "bottom bottom",
          pin: true,
          pinSpacing: false,
        });

        if (i < cards.length - 1) {
          gsap.to(card, {
            scale: 0.95 - i * 0.02,
            opacity: 0.6,
            scrollTrigger: {
              trigger: cards[i + 1],
              start: "top bottom",
              end: "top top+=80",
              scrub: 1,
            },
          });
        }
      });
    }, container);

    return () => ctx.revert();
  }, [children]);

  return (
    <div ref={containerRef} className={className}>
      {children.map((child, i) => (
        <div key={i} className="sticky-card">
          {child}
        </div>
      ))}
    </div>
  );
}
