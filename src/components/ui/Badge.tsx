interface BadgeProps {
  children: string;
  className?: string;
}

export function Badge({ children, className }: BadgeProps) {
  return (
    <span
      className={`inline-flex items-center rounded-full border border-[rgba(255,255,255,0.1)] bg-[rgba(255,255,255,0.04)] px-3 py-1 text-xs font-medium tracking-wider uppercase text-[#a1a1aa] ${className ?? ""}`}
    >
      {children}
    </span>
  );
}
