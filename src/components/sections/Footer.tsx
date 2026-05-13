import { Container } from "@/components/ui/Container";

interface FooterLink {
  label: string;
  href: string;
}

interface FooterColumn {
  title: string;
  links: FooterLink[];
}

interface FooterProps {
  logo?: string;
  description?: string;
  columns: FooterColumn[];
  copyright?: string;
}

export function Footer({ logo, description, columns, copyright }: FooterProps) {
  return (
    <footer className="border-t border-[rgba(255,255,255,0.06)] py-16">
      <Container>
        <div className="grid grid-cols-1 gap-12 md:grid-cols-12">
          <div className="md:col-span-4">
            {logo && (
              <span className="text-xl font-bold text-[#e3e2e2]">{logo}</span>
            )}
            {description && (
              <p className="mt-4 max-w-xs text-sm text-[#a1a1aa] leading-relaxed">
                {description}
              </p>
            )}
          </div>

          {columns.map((col) => (
            <div key={col.title} className="md:col-span-2">
              <p className="text-sm font-medium tracking-wider uppercase text-[#a1a1aa]">
                {col.title}
              </p>
              <ul className="mt-4 space-y-3">
                {col.links.map((link) => (
                  <li key={link.label}>
                    <a
                      href={link.href}
                      className="text-sm text-[#e3e2e2] opacity-70 transition-opacity hover:opacity-100"
                    >
                      {link.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-16 border-t border-[rgba(255,255,255,0.06)] pt-8">
          <p className="text-xs text-[#a1a1aa]">
            {copyright ?? `© ${new Date().getFullYear()} All rights reserved.`}
          </p>
        </div>
      </Container>
    </footer>
  );
}
