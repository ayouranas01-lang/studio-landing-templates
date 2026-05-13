"use client";

import { useRef, useEffect, type ReactNode } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

interface ScrollRevealProps {
  children: ReactNode;
  className?: string;
  scrub?: boolean;
  start?: string;
  end?: string;
}

export function ScrollReveal({
  children,
  className,
  scrub = false,
  start = "top 85%",
  end = "top 20%",
}: ScrollRevealProps) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    const ctx = gsap.context(() => {
      gsap.from(el, {
        y: 60,
        opacity: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
          trigger: el,
          start,
          end,
          scrub: scrub ? 1 : false,
          toggleActions: scrub ? undefined : "play none none none",
        },
      });
    }, el);

    return () => ctx.revert();
  }, [scrub, start, end]);

  return (
    <div ref={ref} className={className}>
      {children}
    </div>
  );
}
