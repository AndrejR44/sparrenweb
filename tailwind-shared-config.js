tailwind.config = {
      theme: {
        extend: {
          colors: {
            // Strict 5-Color User Palette:
            // Soft White (#F8FAFC) - Hintergrund
            // Light Slate (#E2E8F0) - Flächen / Karten
            // Slate Gray (#64748B) - Sekundärtext / Struktur
            // Dark Navy (#0F172A) - Primärtext
            // Cobalt Blue (#2563EB) - Akzent / Buttons / Links
            palette: {
              canvas: '#F8FAFC',
              card: '#E2E8F0',
              secondary: '#64748B',
              primary: '#0F172A',
              accent: '#2563EB',
              accentHover: '#1D4ED8',
            },
            brand: {
              ash: '#E2E8F0',
              mutedTeal: '#64748B',
              deepTeal: '#64748B',
              darkSlate: '#0F172A',
              charcoalBlue: '#0F172A',
              indigo: '#2563EB',
              indigoDark: '#1D4ED8',
              indigoHover: '#1D4ED8',
              watermelon: '#2563EB',
              golden: '#2563EB',
              goldenLight: '#E2E8F0',
              honeydew: '#F8FAFC',
              honeydewSoft: '#E2E8F0',
              charcoal: '#0F172A',
            },
            pastel: {
              sage: '#E2E8F0',        // Light Slate structure / border
              lightSage: '#E2E8F0',   // Light Slate
              cream: '#F8FAFC',       // Soft White canvas
              sand: '#E2E8F0',        // Light Slate surface
              caramel: '#2563EB',      // Cobalt Blue Accent
              caramelLight: '#2563EB', // Cobalt Blue Accent
              caramelDark: '#0F172A',  // Dark Navy
              caramelHover: '#1D4ED8', // Cobalt Blue Hover
            },
            ink: {
              950: '#0F172A',         // Dark Navy (15.5:1 on canvas - AAA pass!)
              900: '#0F172A',         // Dark Navy
              800: '#0F172A',         // Dark Navy
              700: '#64748B',         // Slate Gray
              600: '#64748B',         // Slate Gray (4.6:1 on canvas - AA pass!)
              500: '#64748B',         // Slate Gray
              400: '#64748B',         // Slate Gray
              300: '#64748B',         // Slate Gray
              200: '#E2E8F0',         // Light Slate
            },
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          },
        },
      },
    }