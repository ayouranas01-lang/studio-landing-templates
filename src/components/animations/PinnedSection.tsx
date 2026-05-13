"use client";

import { useRef, useEffect, type ReactNode } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

interface PinnedSectionProps {
  children: ReactNode;
  className?: string;
  pinDuration?: string;
}

export function PinnedSection({
  children,
  className,
  pinDuration = "200%",
}: PinnedSectionProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = containerRef.current;
    const content = contentRef.current;
    if (!container || !content) return;

    const ctx = gsap.context(() => {
      ScrollTrigger.create({
        trigger: container,
        pin: content,
        start: "top top",
        end: `+=${pinDuration}`,
        scrub: 1,
      });
    }, container);

    return () => ctx.revert();
  }, [pinDuration]);

  return (
    <div ref={containerRef} className={className}>
      <div ref={contentRef}>{children}</div>
    </div>
  );
}
