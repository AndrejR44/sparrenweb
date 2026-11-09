# pricing_data.py
# Single Source of Truth for all SparrenWeb packages, pricing and service descriptions

PRICING_CONFIG = {
    "currency": "EUR",
    "vat_notice": "Alle Preise verstehen sich netto zzgl. gesetzlicher Mehrwertsteuer.",
    "vat_badge": "zzgl. gesetzl. MwSt.",
    
    # ANGEBOT A: OWL-Referenz-Pilot
    "pilot": {
        "id": "pilot",
        "name": "OWL-Referenz-Pilot",
        "price_net": 1500,
        "price_display": "1.500 €",
        "period": "einmalig",
        "scope_description": "Vollständiger Leistungsumfang des Meister-Auftrags-Systems",
        "max_projects": 3,
        "badge": "Einführungs-Angebot · Limitiert auf 3 Referenzbetriebe",
        "tagline": "Zum Start suchen wir drei Referenzbetriebe aus Bielefeld und OWL.",
        "difference_regular": 1300,
        "payment_plan": "50 % bei Beauftragung (750 € netto), 50 % bei Abnahme/Go-live (750 € netto)",
        "payment_split": [750, 750],
        "is_active": True,
        "cooperation": [
            "Bereitschaft zu offenem, ehrlichem Feedback",
            "Möglichkeit einer anonymisierten oder freigegebenen Projektvorstellung nach gesonderter schriftlicher Freigabe",
            "Optional: gemeinsames Vor-Ort-Foto und persönliches Zitat (keine Verpflichtung)",
            "Keine Verpflichtung zu einer positiven Bewertung"
        ]
    },

    # ANGEBOT B: SparrenWeb Meister-Auftrags-System (Reguläres Fundament)
    "meister_system": {
        "id": "meister_system",
        "name": "SparrenWeb Meister-Auftrags-System",
        "short_name": "Meister-Auftrags-System",
        "price_net": 2800,
        "price_display": "2.800 €",
        "period": "einmalig",
        "badge": "Das Fundament für Ihren Betrieb",
        "tagline": "Schlüsselfertige Handwerker-Website mit Vorabfilter, Fachtexten und Google-Grundlagen.",
        "pages_included": "Startseite plus bis zu 5 Leistungs-/Gewerkeseiten (bis zu 6 Inhaltsseiten gesamt; rechtliche Seiten separat)",
        "payment_plan": "1.400 € netto bei Beauftragung, 1.400 € netto bei Abnahme/Go-live",
        "payment_split": [1400, 1400],
        "installment_option": "Optional auf Anfrage: 1.400 € bei Start, 700 € nach 30 Tagen, 700 € nach 60 Tagen",
        "features_included": [
            "Individuell angepasste Website nach Maß (Desktop & mobil optimiert)",
            "Startseite plus bis zu 5 branchenspezifische Leistungsseiten (bis zu 6 Inhaltsseiten gesamt)",
            "Interaktiver mehrstufiger Kunden-Vorabfilter mit Foto-Upload",
            "Branchenspezifische Fachtexte für Ihr Gewerk (Sie müssen nichts vorschreiben)",
            "Strukturierte E-Mail-Weiterleitung aller Anfragedaten & Fotos ins Meisterbüro",
            "Technische & inhaltliche SEO-Grundlagen (Schema.org Strukturdaten, Meta-Setup)",
            "Basis-Einrichtung oder Optimierung des Google-Unternehmensprofils (Zugang vorausgesetzt)",
            "Eine gebündelte Korrekturschleife für Design & Texte",
            "Ein persönlicher Feinschliff-Termin (bis zu 30 Minuten via Video oder Telefon)",
            "Vollständige Übergabe des Website-Codes & Einweisung"
        ],
        "features_excluded": [
            "Keine Logo-Neuentwicklung (Ihr vorhandenes Logo wird sauber integriert)",
            "Keine aufwendigen Vor-Ort-Fotoshootings (Nutzung Ihres Materials oder Fachbilder)",
            "Kein Onlineshop oder ERP-Schnittstellen",
            "Keine unbegrenzten Korrekturschleifen (1 gebündelte Runde + 30 Min. Feinschliff)",
            "Keine laufende Anzeigenbetreuung (optional zubuchbar)",
            "Keine Erfolgs- oder Ranking-Garantien (seriöses Handwerk statt falscher Versprechen)"
        ]
    },

    # ANGEBOT C: Regionaler Sichtbarkeits- & Systembetrieb
    "systembetrieb": {
        "id": "systembetrieb",
        "name": "Regionaler Sichtbarkeits- & Systembetrieb",
        "short_name": "Sichtbarkeits- & Systembetrieb",
        "price_net": 250,
        "price_display": "250 €",
        "period": "monatlich",
        "is_optional": True,
        "cancellation": "Monatlich kündbar (keine Mindestlaufzeit)",
        "badge": "Optional · Monatlich kündbar",
        "tagline": "Technischer Betrieb, Google-Profilpflege und monatliches Änderungskontingent.",
        "yearly_price_net": 2700,
        "yearly_price_display": "2.700 €",
        "yearly_discount_percent": 10,
        "yearly_savings_display": "300 € Ersparnis (10 % Nachlass)",
        "features_included": [
            "Schnelles, DSGVO-konformes Website-Hosting inklusive SSL-Zertifikat",
            "Domainverwaltung & technischer Betrieb aller Formulare und Foto-Uploads",
            "Regelmäßige Backups & proaktives technisches Sicherheits-Monitoring",
            "Pflege des Google-Unternehmensprofils (Öffnungszeiten, Leistungsdaten)",
            "2 Google-Beiträge pro Monat (auf Basis Ihrer bereitgestellten Fotos oder Themen)",
            "Druckfertige QR-Code-Vorlage für Baustellen & Fahrzeuge (Google-Bewertungen)",
            "Änderungsservice mit 60 Minuten monatlichem Kontingent (Texte, Team, Fotos)",
            "Zielbearbeitung innerhalb von 2 Werktagen nach vollständigem Eingang der Inhalte"
        ],
        "important_note": "Das 60-Minuten-Kontingent bezieht sich auf inhaltliche Pflegearbeiten. Größere Relaunches oder neue Unterseiten werden separat angeboten."
    },

    # ANGEBOT D: 60-Sekunden-Recruiting-Modul
    "recruiting": {
        "id": "recruiting",
        "name": "60-Sekunden-Recruiting-Modul",
        "short_name": "Recruiting-Modul",
        "price_net": 1200,
        "price_display": "1.200 €",
        "period": "einmalig",
        "badge": "Erweiterung für Mitarbeitergewinnung",
        "tagline": "Mobiles Schnellbewerbungs-System ohne Lebenslauf-Pflicht inkl. Social-Media-Vorlagen.",
        "features_included": [
            "Eigenständige Karriere-Landingpage im Design Ihres Meisterbetriebs",
            "Darstellung echter Arbeitgebervorteile & authentischer Teameinblicke",
            "Niedrigschwelliges Smartphone-Bewerbungsformular (ohne Lebenslauf-Zwang)",
            "3 maßgeschneiderte Vorlagen für regionale Social-Media-Anzeigen",
            "Grundeinrichtung der Social-Media-Kampagne (Zugang & Budget vorausgesetzt)"
        ],
        "features_excluded": [
            "Kein Werbebudget enthalten (wird direkt vom Kunden an Meta/Google gezahlt)",
            "Keine telefonische Bewerber-Vorqualifizierung",
            "Keine Einstellungs- oder Bewerbergarantien"
        ]
    },

    # ANGEBOT E: Komplett-Kombi
    "kombi": {
        "id": "kombi",
        "name": "Meister-System + Recruiting-Kombi",
        "short_name": "Komplett-Kombi",
        "price_net": 3500,
        "price_display": "3.500 €",
        "period": "einmalig",
        "badge": "Beliebteste Komplettlösung",
        "tagline": "Meister-Auftrags-System + 60-Sekunden-Recruiting-Modul gebündelt.",
        "individual_sum": 4000,
        "package_savings": 500,
        "features_included": [
            "Vollständiges SparrenWeb Meister-Auftrags-System (Wert: 2.800 €)",
            "Vollständiges 60-Sekunden-Recruiting-Modul (Wert: 1.200 €)",
            "500 € Paketvorteil gegenüber Einzelbuchung",
            "Alle Vorabfilter, Fachtexte, SEO-Grundlagen & Karriere-Funktionen aus einer Hand"
        ],
        "monthly_care_option": {
            "system_care_net": 250,
            "ads_care_net": 240,
            "total_monthly_net": 490,
            "total_monthly_display": "490 €",
            "description": "Optional: 250 € Systembetrieb + 240 € laufende Social-Media-Anzeigenbetreuung (gesamt 490 €/Monat zzgl. MwSt.)",
            "ad_budget_guideline": "Empfohlenes monatliches Werbebudget: 500–1.000 € (direkt an Meta/Google zu entrichten)"
        }
    }
}
