"use client";

import { motion } from "framer-motion";
import type { ReactNode } from "react";

interface CardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
}

export function Card({ children, className, hover = true }: CardProps) {
  return (
    <motion.div
      whileHover={hover ? { y: -4, transition: { duration: 0.3 } } : undefined}
      className={`rounded-2xl border border-[rgba(255,255,255,0.06)] bg-[#1c1e1e] p-6 md:p-8 ${className ?? ""}`}
    >
      {children}
    </motion.div>
  );
}
