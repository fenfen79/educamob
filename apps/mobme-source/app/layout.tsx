import type { Metadata, Viewport } from "next";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
  interactiveWidget: "resizes-content"
};

export const metadata: Metadata = {
  title: "Mob.me - Seu Tutor Inteligente",
  description: "Tire suas dúvidas escolares com o Mob.me, seu tutor de aprendizagem com inteligência artificial.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR" suppressHydrationWarning>
      <head>
        {/* Camada 1: Imunização do HTML de Entrada contra Cache do Navegador */}
        <meta httpEquiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
        <meta httpEquiv="Pragma" content="no-cache" />
        <meta httpEquiv="Expires" content="0" />

        {/* Camada 3: Mecanismo de Auto-Cura Global para Chunks Desatualizados */}
        <script
          dangerouslySetInnerHTML={{
            __html: `
              window.addEventListener('error', function(e) {
                if (e && e.message && (
                  e.message.indexOf('Loading chunk') !== -1 ||
                  e.message.indexOf('dynamically imported module') !== -1 ||
                  e.message.indexOf('Failed to fetch dynamically imported module') !== -1
                )) {
                  console.warn('⚠️ Chunk desatualizado detectado. Auto-recuperando para a nova versao...');
                  window.location.reload();
                }
              });
            `,
          }}
        />

        <script
          dangerouslySetInnerHTML={{
            __html: `
              (function() {
                try {
                  var storedTheme = localStorage.getItem('educamob_theme');
                  if (storedTheme === 'dark') {
                    document.documentElement.setAttribute('data-theme', 'dark');
                  } else {
                    document.documentElement.removeAttribute('data-theme');
                  }
                } catch (e) {}
              })();
            `,
          }}
        />
        <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
        <script src="../../shared/js/supabase-client.js?v=3"></script>
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
