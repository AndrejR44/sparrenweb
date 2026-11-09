// pricing-data.js
// Client-side single source of truth for SparrenWeb pricing & packages

window.SPARRENWEB_PRICING = {
  currency: 'EUR',
  vatNotice: 'Alle Preise verstehen sich netto zzgl. gesetzlicher Mehrwertsteuer.',
  vatBadge: 'zzgl. gesetzl. MwSt.',

  packages: {
    pilot: {
      id: 'pilot',
      name: 'OWL-Referenz-Pilot',
      priceNet: 1500,
      priceDisplay: '1.500 €',
      period: 'einmalig',
      isActive: true,
      maxProjects: 3,
      tagline: 'Zum Start suchen wir drei Referenzbetriebe aus Bielefeld und OWL.',
      monthlyCareNet: 250
    },
    meister_system: {
      id: 'meister_system',
      name: 'SparrenWeb Meister-Auftrags-System',
      shortName: 'Meister-Auftrags-System',
      priceNet: 2800,
      priceDisplay: '2.800 €',
      period: 'einmalig',
      tagline: 'Schlüsselfertige Handwerker-Website mit Vorabfilter, Fachtexten und Google-Grundlagen.',
      paymentSplit: [1400, 1400]
    },
    recruiting: {
      id: 'recruiting',
      name: '60-Sekunden-Recruiting-Modul',
      shortName: 'Recruiting-Modul',
      priceNet: 1200,
      priceDisplay: '1.200 €',
      period: 'einmalig',
      tagline: 'Mobiles Schnellbewerbungs-System ohne Lebenslauf-Pflicht.'
    },
    kombi: {
      id: 'kombi',
      name: 'Meister-System + Recruiting-Kombi',
      shortName: 'Komplett-Kombi',
      priceNet: 3500,
      priceDisplay: '3.500 €',
      period: 'einmalig',
      individualSum: 4000,
      savings: 500,
      tagline: 'Meister-Auftrags-System + 60-Sekunden-Recruiting-Modul gebündelt.'
    }
  },

  care: {
    system: {
      id: 'systembetrieb',
      name: 'Regionaler Sichtbarkeits- & Systembetrieb',
      priceNet: 250,
      priceDisplay: '250 €',
      period: 'monatlich',
      yearlyNet: 2700,
      yearlyDisplay: '2.700 €',
      includedMinutes: 60
    },
    ads: {
      id: 'ads_care',
      name: 'Laufende Social-Media-Anzeigenbetreuung',
      priceNet: 240,
      priceDisplay: '240 €',
      period: 'monatlich'
    },
    combined: {
      priceNet: 490,
      priceDisplay: '490 €',
      period: 'monatlich'
    }
  }
};
