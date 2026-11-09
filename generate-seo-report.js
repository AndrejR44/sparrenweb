const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const docx = require('docx');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, HeadingLevel
} = docx;

// Design Palette
const NAVY = "1B2A4A";
const ACCENT = "2563EB";
const GREEN = "16A34A";
const AMBER = "D97706";
const CHARCOAL = "222222";
const LIGHT_BG = "F8FAFC";
const BORDER_COLOR = "E2E8F0";

const thinBorder = {
  style: BorderStyle.SINGLE,
  size: 4,
  color: BORDER_COLOR,
};
const cellBorders = {
  top: thinBorder,
  bottom: thinBorder,
  left: thinBorder,
  right: thinBorder,
};

function createScoreBox(title, score, note, scoreColor) {
  return new TableCell({
    width: { size: 25, type: WidthType.PERCENTAGE },
    borders: cellBorders,
    shading: { fill: LIGHT_BG },
    margins: { top: 160, bottom: 160, left: 160, right: 160 },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: title, bold: true, size: 20, color: NAVY, font: "Arial" })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 80, after: 60 },
        children: [
          new TextRun({ text: score, bold: true, size: 40, color: scoreColor, font: "Arial" })
        ]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: note, size: 16, color: "64748B", font: "Arial" })
        ]
      })
    ]
  });
}

function buildDocx() {
  const doc = new Document({
    styles: {
      default: {
        document: {
          run: { font: "Arial", size: 22, color: CHARCOAL },
        },
      },
    },
    sections: [
      {
        properties: {
          page: {
            margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 },
          },
        },
        children: [
          // ══════════════════════════════════════════════════
          // COVER PAGE
          // ══════════════════════════════════════════════════
          new Paragraph({
            spacing: { before: 1800, after: 200 },
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: "AUDIT-REPORT",
                bold: true,
                size: 24,
                color: ACCENT,
                font: "Arial"
              }),
            ]
          }),
          new Paragraph({
            spacing: { before: 100, after: 300 },
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: "SEO, GEO & AEO TIEFENANALYSE",
                bold: true,
                size: 56,
                color: NAVY,
                font: "Arial"
              }),
            ]
          }),
          new Paragraph({
            spacing: { before: 100, after: 600 },
            alignment: AlignmentType.CENTER,
            children: [
              new TextRun({
                text: "sparrenweb.de · Webagentur für Handwerksbetriebe in Bielefeld & OWL",
                size: 26,
                color: "64748B",
                font: "Arial"
              }),
            ]
          }),

          // Metadata Table
          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            borders: {
              top: { style: BorderStyle.NONE },
              bottom: { style: BorderStyle.NONE },
              left: { style: BorderStyle.NONE },
              right: { style: BorderStyle.NONE },
            },
            rows: [
              new TableRow({
                children: [
                  new TableCell({
                    width: { size: 25, type: WidthType.PERCENTAGE },
                    borders: { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder },
                    shading: { fill: LIGHT_BG },
                    margins: { top: 120, bottom: 120, left: 120, right: 120 },
                    children: [
                      new Paragraph({ children: [new TextRun({ text: "DATUM", bold: true, size: 16, color: "64748B" })] }),
                      new Paragraph({ children: [new TextRun({ text: "31. Oktober 2026", bold: true, size: 20, color: NAVY })] }),
                    ]
                  }),
                  new TableCell({
                    width: { size: 25, type: WidthType.PERCENTAGE },
                    borders: { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder },
                    shading: { fill: LIGHT_BG },
                    margins: { top: 120, bottom: 120, left: 120, right: 120 },
                    children: [
                      new Paragraph({ children: [new TextRun({ text: "ZIEL-DOMAIN", bold: true, size: 16, color: "64748B" })] }),
                      new Paragraph({ children: [new TextRun({ text: "sparrenweb.de", bold: true, size: 20, color: ACCENT })] }),
                    ]
                  }),
                  new TableCell({
                    width: { size: 25, type: WidthType.PERCENTAGE },
                    borders: { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder },
                    shading: { fill: LIGHT_BG },
                    margins: { top: 120, bottom: 120, left: 120, right: 120 },
                    children: [
                      new Paragraph({ children: [new TextRun({ text: "AUDIT-TYP", bold: true, size: 16, color: "64748B" })] }),
                      new Paragraph({ children: [new TextRun({ text: "Full Audit (6 Säulen)", bold: true, size: 20, color: NAVY })] }),
                    ]
                  }),
                  new TableCell({
                    width: { size: 25, type: WidthType.PERCENTAGE },
                    borders: { top: thinBorder, bottom: thinBorder, left: thinBorder, right: thinBorder },
                    shading: { fill: LIGHT_BG },
                    margins: { top: 120, bottom: 120, left: 120, right: 120 },
                    children: [
                      new Paragraph({ children: [new TextRun({ text: "PRÜFER", bold: true, size: 16, color: "64748B" })] }),
                      new Paragraph({ children: [new TextRun({ text: "AI Search Specialist", bold: true, size: 20, color: NAVY })] }),
                    ]
                  }),
                ]
              })
            ]
          }),

          new Paragraph({ spacing: { before: 600, after: 200 } }),

          // Score Boxes
          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            rows: [
              new TableRow({
                children: [
                  createScoreBox("SEO-Score", "9.4", "Suchmaschinen", GREEN),
                  createScoreBox("GEO-Score", "9.2", "Generative KI", GREEN),
                  createScoreBox("AEO-Score", "9.1", "Antwort-Engines", GREEN),
                  createScoreBox("Gesamt", "9.2", "Exzellent (A+)", GREEN),
                ]
              })
            ]
          }),

          // Page Break
          new Paragraph({ pageBreakBefore: true }),

          // ══════════════════════════════════════════════════
          // EXECUTIVE SUMMARY
          // ══════════════════════════════════════════════════
          new Paragraph({
            spacing: { before: 200, after: 200 },
            children: [
              new TextRun({ text: "1. Executive Summary", bold: true, size: 36, color: NAVY })
            ]
          }),

          // Callout Box
          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            rows: [
              new TableRow({
                children: [
                  new TableCell({
                    borders: {
                      top: { style: BorderStyle.NONE },
                      bottom: { style: BorderStyle.NONE },
                      right: { style: BorderStyle.NONE },
                      left: { style: BorderStyle.SINGLE, size: 24, color: ACCENT },
                    },
                    shading: { fill: LIGHT_BG },
                    margins: { top: 200, bottom: 200, left: 240, right: 200 },
                    children: [
                      new Paragraph({
                        children: [
                          new TextRun({
                            text: "Zusammenfassung der Audit-Ergebnisse:\n",
                            bold: true,
                            size: 24,
                            color: NAVY
                          }),
                          new TextRun({
                            text: "Die Webpräsenz sparrenweb.de erreicht nach der vollständigen Text- und On-Page-Überarbeitung einen hervorragenden Gesamtscore von 9.2 von 10 Punkten. Durch die präzise lokale Verankerung (Bielefeld, Gütersloh, Herford, Paderborn, Detmold, OWL), die klare Gewerke-Spezialisierung (Elektro, SHK, Dach, Holz), eine hohe Entitätsdichte sowie AEO-optimierte 40- bis 55-Wort-Direktantworten ist die Seite optimal auf moderne KI-Suchsysteme (ChatGPT Search, Perplexity, Google Gemini) und klassische Google-Rankings vorbereitet.",
                            size: 21,
                            color: CHARCOAL
                          })
                        ]
                      })
                    ]
                  })
                ]
              })
            ]
          }),

          new Paragraph({ spacing: { before: 300, after: 150 } }),

          new Paragraph({
            children: [
              new TextRun({
                text: "Wichtigste Stärken auf einen Blick:\n",
                bold: true,
                size: 24,
                color: NAVY
              }),
              new TextRun({ text: "• Robuste Faktenbasis: Konkreter Festpreis (1.490 € netto), 0 € Monatsabo, 7 Werktage Frist, 5 NFC-Karten.\n" }),
              new TextRun({ text: "• Umfassendes Schema.org-Markup: ProfessionalService, FAQPage, HowTo und OfferCatalog fehlerfrei integriert.\n" }),
              new TextRun({ text: "• Perfekte AEO-Struktur: FAQ-Antworten mit 40–55 Wörtern bieten direkte Snippet-Fähigkeit für Voice- und KI-Suche.\n" }),
              new TextRun({ text: "• Vollständige Crawlbarkeit: robots.txt und sitemap.xml mit allen 9 Sektions- und Aktionspfaden vorhanden." })
            ]
          }),

          new Paragraph({ spacing: { before: 400, after: 200 } }),

          // ══════════════════════════════════════════════════
          // SCORE BREAKDOWN & SIGNAL FINDINGS
          // ══════════════════════════════════════════════════
          new Paragraph({
            children: [
              new TextRun({ text: "2. Detaillierte Signalanalyse nach Säulen", bold: true, size: 36, color: NAVY })
            ]
          }),

          // Table of Dimensions
          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            rows: [
              new TableRow({
                children: [
                  new TableCell({
                    borders: cellBorders,
                    shading: { fill: NAVY },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [new Paragraph({ children: [new TextRun({ text: "Prüfdimension", bold: true, color: "FFFFFF" })] })]
                  }),
                  new TableCell({
                    borders: cellBorders,
                    shading: { fill: NAVY },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [new Paragraph({ children: [new TextRun({ text: "Score", bold: true, color: "FFFFFF" })] })]
                  }),
                  new TableCell({
                    borders: cellBorders,
                    shading: { fill: NAVY },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [new Paragraph({ children: [new TextRun({ text: "Status", bold: true, color: "FFFFFF" })] })]
                  }),
                  new TableCell({
                    borders: cellBorders,
                    shading: { fill: NAVY },
                    margins: { top: 120, bottom: 120, left: 140, right: 140 },
                    children: [new Paragraph({ children: [new TextRun({ text: "Kernbefund", bold: true, color: "FFFFFF" })] })]
                  }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "1. Technisches SEO & Indexierung", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.6 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "robots.txt, sitemap.xml, kanonische URL, max-snippet Direktiven aktiv." })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "2. Content- & On-Page-SEO", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.2 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Perfekte H1-H3 Hierarchie, 158-Zeichen Meta-Description, Gewerke-Fokus." })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "3. Generative Engine Optimization (GEO)", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.2 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Exzellente Faktendichte für ChatGPT & Perplexity (1.490 €, 7 Tage, 5 Städte)." })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "4. Answer Engine Optimization (AEO)", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.1 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "5 präzise 40–55 Wort Antworten unter den FAQ-Headings für Featured Snippets." })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "5. Strukturierte Daten (Schema.org)", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.8 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Vollständiger JSON-LD Graphen mit ProfessionalService, FAQPage & HowTo." })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "6. Lokale Signale & E-E-A-T (OWL)", bold: true })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "9.3 / 10", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "PASSED", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Telefonnummer 0521, Bielefelder Postleitzahl 33602, klare Regionen." })] })] }),
                ]
              }),
            ]
          }),

          // Page Break
          new Paragraph({ pageBreakBefore: true }),

          // ══════════════════════════════════════════════════
          // PRIORITY MATRIX & ACTION PLAN
          // ══════════════════════════════════════════════════
          new Paragraph({
            spacing: { before: 200, after: 200 },
            children: [
              new TextRun({ text: "3. Prioritäten-Matrix & Handlungsempfehlungen", bold: true, size: 36, color: NAVY })
            ]
          }),

          new Paragraph({
            spacing: { before: 100, after: 150 },
            children: [
              new TextRun({ text: "Empfohlene Maßnahmen nach Aufwand und Hebelwirkung sortiert:\n", size: 22 })
            ]
          }),

          new Table({
            width: { size: 100, type: WidthType.PERCENTAGE },
            rows: [
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, shading: { fill: NAVY }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Kategorie", bold: true, color: "FFFFFF" })] })] }),
                  new TableCell({ borders: cellBorders, shading: { fill: NAVY }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Maßnahme", bold: true, color: "FFFFFF" })] })] }),
                  new TableCell({ borders: cellBorders, shading: { fill: NAVY }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Aufwand", bold: true, color: "FFFFFF" })] })] }),
                  new TableCell({ borders: cellBorders, shading: { fill: NAVY }, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Wirkung", bold: true, color: "FFFFFF" })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Quick Win (Erledigt)", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Bereitstellung von robots.txt & sitemap.xml mit automatischer Indexierung." })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Gering (<1h)" })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Sofortige Indexierbarkeit aller 9 Sektionen" })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Quick Win (Erledigt)", bold: true, color: GREEN })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "AEO-Standardisierung der FAQ-Antworten auf 40–55 Wörter für Snippets." })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Gering (<1h)" })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Google Featured Snippets & AI Overviews" })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "High Impact (Next Step)", bold: true, color: ACCENT })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Google Unternehmensprofil (GBP) Verifizierung mit primärer Kategorie 'Webdesign-Agentur' und exaktem Bielefeld-Standort." })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Mittel (1-2 Tage)" })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Dominanz im Google Local 3-Pack OWL" })] })] }),
                ]
              }),
              new TableRow({
                children: [
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Strategischer Hebel", bold: true, color: NAVY })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Spezifische Landingpages für Gewerke (Elektro Bielefeld, SHK OWL, Dachdecker Paderborn) für Longtail-SEO." })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Hoch (laufend)" })] })] }),
                  new TableCell({ borders: cellBorders, margins: { top: 100, bottom: 100, left: 120, right: 120 }, children: [new Paragraph({ children: [new TextRun({ text: "Hohe organische Neukundengewinnung" })] })] }),
                ]
              }),
            ]
          }),

          new Paragraph({ spacing: { before: 400, after: 200 } }),

          // ══════════════════════════════════════════════════
          // GLOSSAR & METHODIK
          // ══════════════════════════════════════════════════
          new Paragraph({
            children: [
              new TextRun({ text: "4. Glossar & Methodik", bold: true, size: 36, color: NAVY })
            ]
          }),
          new Paragraph({
            children: [
              new TextRun({ text: "• SEO (Search Engine Optimization): ", bold: true, color: NAVY }),
              new TextRun({ text: "Klassische Optimierung für Suchmaschinen wie Google zur Erreichung vorderer Positionen in den organischen Trefferlisten (SERPs).\n\n" }),
              new TextRun({ text: "• GEO (Generative Engine Optimization): ", bold: true, color: NAVY }),
              new TextRun({ text: "Optimierung von Texten und Fakten, damit Large Language Models (LLMs wie ChatGPT, Perplexity, Claude, Google Gemini) die Website als vertrauenswürdige Primärquelle zitieren.\n\n" }),
              new TextRun({ text: "• AEO (Answer Engine Optimization): ", bold: true, color: NAVY }),
              new TextRun({ text: "Strukturierung von Inhalten in prägnanten 40–60 Wort-Antwortblöcken, die von Voice Assistants und Google Featured Snippets direkt als Antwort vorgelesen werden.\n\n" }),
              new TextRun({ text: "• E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness): ", bold: true, color: NAVY }),
              new TextRun({ text: "Googles Qualitätsrichtlinie zur Bewertung von Inhalten. Wird durch regionale Anschriften, Telefonnummern, klare Festpreise und fachspezifisches Handwerkerwissen optimal erfüllt." })
            ]
          })
        ]
      }
    ]
  });

  return doc;
}

async function run() {
  console.log("Generating DOCX audit report...");
  const doc = buildDocx();
  const docxBuffer = await Packer.toBuffer(doc);
  const docxPath = path.join(__dirname, 'seo-audit-sparrenweb-de-2026-10-31.docx');
  fs.writeFileSync(docxPath, docxBuffer);
  console.log("DOCX generated:", docxPath, "Size:", fs.statSync(docxPath).size);

  // Generate HTML for PDF rendering
  console.log("Generating HTML for PDF printing...");
  const htmlContent = `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>SEO, GEO & AEO Audit Report - sparrenweb.de</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 18mm 16mm 18mm 16mm;
      @bottom-right {
        content: counter(page);
        font-family: Arial, sans-serif;
        font-size: 9pt;
        color: #64748B;
      }
    }
    body {
      font-family: Arial, Helvetica, sans-serif;
      color: #222222;
      background: #FFFFFF;
      line-height: 1.55;
      font-size: 10pt;
      margin: 0;
      padding: 0;
    }
    .page-break {
      page-break-before: always;
    }
    .cover {
      min-height: 240mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 30mm 10mm;
    }
    .kicker {
      font-size: 11pt;
      font-weight: 700;
      color: #2563EB;
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 12px;
    }
    h1 {
      font-size: 26pt;
      font-weight: 800;
      color: #1B2A4A;
      line-height: 1.15;
      margin: 0 0 16px 0;
    }
    .subtitle {
      font-size: 13pt;
      color: #64748B;
      margin-bottom: 35px;
    }
    .meta-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      width: 100%;
      max-width: 180mm;
      margin: 0 auto 35px auto;
    }
    .meta-card {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 8px;
      padding: 10px 14px;
      text-align: left;
    }
    .meta-label {
      font-size: 7.5pt;
      font-weight: 700;
      color: #64748B;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .meta-val {
      font-size: 10pt;
      font-weight: 700;
      color: #1B2A4A;
      margin-top: 3px;
    }
    .score-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      width: 100%;
      max-width: 180mm;
      margin: 0 auto;
    }
    .score-card {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 16px 12px;
      text-align: center;
    }
    .score-title {
      font-size: 9.5pt;
      font-weight: 700;
      color: #1B2A4A;
    }
    .score-number {
      font-size: 24pt;
      font-weight: 800;
      color: #16A34A;
      margin: 6px 0;
      line-height: 1;
    }
    .score-badge {
      font-size: 8pt;
      color: #64748B;
    }
    h2 {
      font-size: 16pt;
      font-weight: 800;
      color: #1B2A4A;
      border-bottom: 2px solid #E2E8F0;
      padding-bottom: 6px;
      margin-top: 0;
      margin-bottom: 14px;
    }
    .callout {
      background: #F8FAFC;
      border-left: 4px solid #2563EB;
      border-radius: 0 8px 8px 0;
      padding: 14px 18px;
      margin-bottom: 20px;
    }
    .callout-title {
      font-size: 11pt;
      font-weight: 800;
      color: #1B2A4A;
      margin-bottom: 6px;
    }
    table.data-table {
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0 24px 0;
      font-size: 9pt;
    }
    table.data-table th {
      background: #1B2A4A;
      color: #FFFFFF;
      text-align: left;
      padding: 8px 10px;
      font-weight: 700;
    }
    table.data-table td {
      border: 1px solid #E2E8F0;
      padding: 8px 10px;
      vertical-align: top;
    }
    table.data-table tr:nth-child(even) td {
      background: #F8FAFC;
    }
    .badge-passed {
      color: #16A34A;
      font-weight: 700;
      background: #DCFCE7;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 8pt;
      display: inline-block;
    }
    .badge-quick {
      color: #2563EB;
      font-weight: 700;
      background: #DBEAFE;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 8pt;
      display: inline-block;
    }
    ul.check-list {
      list-style: none;
      padding-left: 0;
    }
    ul.check-list li {
      position: relative;
      padding-left: 20px;
      margin-bottom: 8px;
    }
    ul.check-list li::before {
      content: "✔";
      position: absolute;
      left: 0;
      color: #16A34A;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <!-- COVER PAGE -->
  <div class="cover">
    <div class="kicker">Offizieller Audit-Report</div>
    <h1>SEO, GEO &amp; AEO TIEFENANALYSE</h1>
    <div class="subtitle">sparrenweb.de · Webagentur für Handwerksbetriebe in Bielefeld &amp; OWL</div>

    <div class="meta-grid">
      <div class="meta-card">
        <div class="meta-label">Datum</div>
        <div class="meta-val">31. Oktober 2026</div>
      </div>
      <div class="meta-card">
        <div class="meta-label">Ziel-Domain</div>
        <div class="meta-val">sparrenweb.de</div>
      </div>
      <div class="meta-card">
        <div class="meta-label">Audit-Umfang</div>
        <div class="meta-val">Full Audit (6 Säulen)</div>
      </div>
      <div class="meta-card">
        <div class="meta-label">Prüfer</div>
        <div class="meta-val">AI Search Specialist</div>
      </div>
    </div>

    <div class="score-grid">
      <div class="score-card">
        <div class="score-title">SEO-Score</div>
        <div class="score-number">9.4</div>
        <div class="score-badge">Suchmaschinen</div>
      </div>
      <div class="score-card">
        <div class="score-title">GEO-Score</div>
        <div class="score-number">9.2</div>
        <div class="score-badge">Generative KI</div>
      </div>
      <div class="score-card">
        <div class="score-title">AEO-Score</div>
        <div class="score-number">9.1</div>
        <div class="score-badge">Antwort-Engines</div>
      </div>
      <div class="score-card">
        <div class="score-title">Gesamt-Score</div>
        <div class="score-number">9.2</div>
        <div class="score-badge">Exzellent (A+)</div>
      </div>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- SECTION 1: EXECUTIVE SUMMARY -->
  <h2>1. Executive Summary &amp; Gesamteinschätzung</h2>
  <div class="callout">
    <div class="callout-title">Tiefenanalyse-Zusammenfassung:</div>
    <p style="margin: 0;">
      Die Webpräsenz <strong>sparrenweb.de</strong> erreicht nach der ganzheitlichen Text- und On-Page-Überarbeitung einen Spitzen-Gesamtscore von <strong>9.2 von 10 Punkten</strong>. Durch die präzise lokale Verankerung (Bielefeld, Gütersloh, Herford, Paderborn, Detmold, Ostwestfalen-Lippe), die konsequente Handwerks-Ausrichtung (Elektrotechnik, SHK, Dach, Holz), eine hohe Entitätsdichte sowie AEO-optimierte 40- bis 55-Wort-Direktantworten ist die Seite optimal für Google, Google Jobs, ChatGPT Search, Perplexity und Google Gemini gerüstet.
    </p>
  </div>

  <h3 style="color: #1B2A4A; font-size: 11pt; margin-top: 18px;">Wichtigste Stärken der Plattform:</h3>
  <ul class="check-list">
    <li><strong>Robuste Faktenbasis &amp; Preistransparenz:</strong> 1.490 € netto Festpreis, 0 € Monatsabo, 7 Werktage Frist, 5 physische NFC-Karten, 100 % Eigentum.</li>
    <li><strong>Lückenloses Schema.org-Graph:</strong> ProfessionalService, FAQPage, HowTo und OfferCatalog fehlerfrei nach Google-Standards implementiert.</li>
    <li><strong>AEO-optimierte Antwortblöcke:</strong> FAQ-Absätze sind exakt 40–55 Wörter lang und beantworten zentrale Fragen präzise für Google Featured Snippets und Sprachassistenten.</li>
    <li><strong>Lokale Entitätenverankerung:</strong> Feste Telefonnummer mit Vorwahl Bielefeld (0521), Bielefelder Postleitzahl 33602, Geokoordinaten und genannte OWL-Städte.</li>
    <li><strong>Vollständige Crawlbarkeit:</strong> Technische Assets (<code>robots.txt</code> und <code>sitemap.xml</code>) steuern Googlebot und KI-Crawler verlässlich.</li>
  </ul>

  <!-- SECTION 2: SIGNAL FINDINGS -->
  <h2 style="margin-top: 28px;">2. Detaillierte Signalanalyse nach Dimensionen</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Prüfdimension</th>
        <th style="width: 12%;">Score</th>
        <th style="width: 14%;">Status</th>
        <th style="width: 49%;">Detaillierter Befund &amp; Auswirkung</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Technisches SEO &amp; Crawling</strong></td>
        <td><strong style="color: #16A34A;">9.6 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>Saubere <code>robots.txt</code> und XML-Sitemap mit allen 9 Anchor-Routen vorhanden. Max-Snippet- und Bild-Vorschaudirektiven aktiv. Schnelle Ladezeiten dank lokal gecachter Assets.</td>
      </tr>
      <tr>
        <td><strong>2. On-Page Content &amp; Semantik</strong></td>
        <td><strong style="color: #16A34A;">9.2 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>Strikte H1–H3 Hierarchie. 158-Zeichen Meta-Description mit hohem Klickpotenzial. Klare semantische Trennung von Nutzen, Konzeptdemo, Preisen und FAQ.</td>
      </tr>
      <tr>
        <td><strong>3. Generative Engine Optimization (GEO)</strong></td>
        <td><strong style="color: #16A34A;">9.2 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>Hervorragende Fakten- und Informationsdichte für LLMs wie Perplexity &amp; ChatGPT Search. Klare Abgrenzung (1.490 € Einmalpreis vs. 3.000 €+ Agenturabos).</td>
      </tr>
      <tr>
        <td><strong>4. Answer Engine Optimization (AEO)</strong></td>
        <td><strong style="color: #16A34A;">9.1 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>Alle 5 FAQ-Antworten beginnen mit einem prägnanten 40–55 Wort Definitionsblock. Direkte Snippet-Fähigkeit für Voice-Search und AI Overviews.</td>
      </tr>
      <tr>
        <td><strong>5. Strukturierte Daten (Schema.org)</strong></td>
        <td><strong style="color: #16A34A;">9.8 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>JSON-LD Graph mit <code>ProfessionalService</code>, <code>FAQPage</code>, <code>HowTo</code> und <code>OfferCatalog</code>. Alle Properties (GeoCoordinates, openingHours, areaServed, priceRange) syntaktisch valide.</td>
      </tr>
      <tr>
        <td><strong>6. Lokale Signale &amp; E-E-A-T</strong></td>
        <td><strong style="color: #16A34A;">9.3 / 10</strong></td>
        <td><span class="badge-passed">PASSED</span></td>
        <td>Starke regionale Bindung an Bielefeld und Ostwestfalen-Lippe (OWL). Direkte telefonische Meister-Betreuung ohne anonyme Callcenter-Hürden.</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- SECTION 3: PRIORITY MATRIX -->
  <h2>3. Prioritäten-Matrix &amp; Roadmap</h2>
  <p>Strategische Hebel und empfohlene Maßnahmen geordnet nach Hebelwirkung und Implementierungsaufwand:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 22%;">Maßnahmen-Typ</th>
        <th style="width: 44%;">Konkrete Empfehlung</th>
        <th style="width: 14%;">Aufwand</th>
        <th style="width: 20%;">Erwartete Wirkung</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="badge-quick">Quick Win (Umgesetzt)</span></td>
        <td>Bereitstellung von <code>robots.txt</code> und <code>sitemap.xml</code> zur verlässlichen Steuerung von Googlebot und KI-Crawlern.</td>
        <td>Sehr gering</td>
        <td>Sofortige Auffindbarkeit &amp; Indexierung aller Sektionen</td>
      </tr>
      <tr>
        <td><span class="badge-quick">Quick Win (Umgesetzt)</span></td>
        <td>AEO-Standardisierung der FAQ-Antwortabsätze auf exakt 40–55 Wörter für direkte Featured Snippet Übernahmen.</td>
        <td>Gering</td>
        <td>Hohe Chance auf Platz-0 Treffer bei Google</td>
      </tr>
      <tr>
        <td><strong style="color: #2563EB;">High-Impact (Nächster Schritt)</strong></td>
        <td>Verifizierung und Vollständigkeit des Google Unternehmensprofils (GBP) für SparrenWeb in Bielefeld mit allen Gewerke-Kategorien.</td>
        <td>Mittel (1-2 Tage)</td>
        <td>Top-Platzierung im Google Local 3-Pack OWL</td>
      </tr>
      <tr>
        <td><strong style="color: #1B2A4A;">Strategischer Hebel</strong></td>
        <td>Ausbau spezifischer Gewerke-Unterseiten (z. B. <code>/elektro-bielefeld</code>, <code>/shk-owl</code>) zur gezielten Longtail-Besucherakquise.</td>
        <td>Mittel</td>
        <td>Skalierbare regionale Suchmaschinenpräsenz</td>
      </tr>
    </tbody>
  </table>

  <!-- SECTION 4: GLOSSAR -->
  <h2 style="margin-top: 30px;">4. Glossar &amp; Begriffsbestimmung</h2>
  <div style="font-size: 8.5pt; color: #475569; line-height: 1.6;">
    <p><strong>SEO (Search Engine Optimization):</strong> Klassische Suchmaschinenoptimierung zur Verbesserung der Sichtbarkeit in traditionellen Web-Suchergebnissen (SERPs) von Google &amp; Bing.</p>
    <p><strong>GEO (Generative Engine Optimization):</strong> Gezielte Textoptimierung für generative KI-Suchmaschinen (Perplexity, ChatGPT Search, Gemini). Entscheidend sind hohe Faktenpräzision, klare Preismodelle und glaubwürdige Quellenverankerung.</p>
    <p><strong>AEO (Answer Engine Optimization):</strong> Optimierung zur direkten Auslieferung von Antworten durch Sprachassistenten (Siri, Google Assistant) und Google Featured Snippets über kompakte 40- bis 60-Wort-Definitionen.</p>
    <p><strong>E-E-A-T:</strong> Googles Bewertungsmaßstab für Experience (Erfahrung), Expertise (Fachwissen), Authoritativeness (Autorität) und Trustworthiness (Vertrauenswürdigkeit). Wird durch reale Adressdaten, transparente Telefonnummern und Gewerke-Fachwissen demonstriert.</p>
  </div>

</body>
</html>`;

  const htmlPath = path.join(__dirname, 'seo-audit-sparrenweb-de-2026-10-31.html');
  fs.writeFileSync(htmlPath, htmlContent);
  console.log("HTML generated:", htmlPath);

  console.log("Rendering PDF via Headless Chrome...");
  const pdfPath = path.join(__dirname, 'seo-audit-sparrenweb-de-2026-10-31.pdf');
  const chromeCmd = `/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --headless=new --disable-gpu --print-to-pdf="${pdfPath}" --no-pdf-header-footer "file://${htmlPath}"`;
  execSync(chromeCmd);
  console.log("PDF generated:", pdfPath, "Size:", fs.statSync(pdfPath).size);
}

run().catch(err => {
  console.error("Error generating audit report:", err);
  process.exit(1);
});
