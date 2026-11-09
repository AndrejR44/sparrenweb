#!/usr/bin/env python3
"""
SparrenWeb - Internes Finanzmodell & Wirtschaftlichkeitsberechnung (12 und 36 Monate)
Zweck: Detaillierte Prognose von Umsatz, Liquidität, Kosten, Kapazitäten und Zielerreichung (15.000 € / Monat Netto-Überschuss vor Steuern).
Exportiert die Ergebnisse in '02_finanzmodell_12_und_36_monate.csv'.
"""

import csv
import os
import sys

def calculate_financials():
    # Preisdefinitionen (netto in Euro)
    P_PILOT = 1500.0          # Angebot A (max 3x insgesamt)
    P_MEISTER = 2800.0        # Angebot B
    P_BETREUUNG = 250.0       # Angebot C monatlich
    P_RECRUITING = 1200.0     # Angebot D einmalig
    P_KOMBI = 3500.0          # Angebot E einmalig
    P_KOMBI_BETREUUNG = 490.0 # Angebot E monatlich (250 Betreuung + 240 Ad-Betreuung)
    
    # Fixkosten & variable Betriebskosten monatlich (netto in Euro)
    # Hosting/Server, Software/Tools (Figma, GitHub, Form-Dienste, Buchhaltung), Verwaltung, Versicherung
    BASE_FIXED_COSTS_MONTHLY = 350.0  # Hosting, SaaS, Buchhaltung, Telefon/Internet anteilig
    AD_BUDGET_OWN_MONTHLY = 300.0     # Eigenes Marketing / Akquise
    
    # Kapazitätsannahmen
    HOURS_PER_WEEK_CAPACITY = 25.0
    WEEKS_PER_MONTH = 4.33
    HOURS_PER_MONTH_AVAILABLE = HOURS_PER_WEEK_CAPACITY * WEEKS_PER_MONTH # ca. 108 Stunden/Monat
    
    # Arbeitsaufwand in Stunden
    HOURS_PILOT = 20.0
    HOURS_MEISTER = 24.0
    HOURS_RECRUITING = 10.0
    HOURS_KOMBI = 30.0
    HOURS_BETREUUNG_PER_CLIENT = 2.0  # Inkl. 60 Min. Änderungsservice + Check
    HOURS_KOMBI_BETREUUNG_PER_CLIENT = 3.5 # Inkl. Ads & Reporting
    
    scenarios = ["Konservativ", "Standard", "Wachstum"]
    
    # Monatspläne für 36 Monate
    # Monat 1-36
    results_rows = []
    
    for scen in scenarios:
        cum_revenue = 0.0
        cum_costs = 0.0
        cum_profit = 0.0
        active_retainers = 0
        active_kombi_retainers = 0
        
        for m in range(1, 37):
            pilots = 0
            meisters = 0
            recruitings = 0
            kombis = 0
            new_retainers = 0
            new_kombi_retainers = 0
            
            if scen == "Konservativ":
                # Langsames Wachstum: Monate 1-3 je 1 Pilot, danach 1 Meister alle 1-2 Monate
                if m <= 3:
                    pilots = 1
                    new_retainers = 0 if m < 2 else 1
                elif m <= 12:
                    meisters = 1 if m % 2 == 1 else 0
                    if meisters > 0 and m % 3 == 0:
                        recruitings = 1
                    new_retainers = 1 if m % 3 == 0 else 0
                else: # Monate 13-36
                    meisters = 1
                    recruitings = 1 if m % 4 == 0 else 0
                    kombis = 1 if m % 6 == 0 else 0
                    new_retainers = 1 if m % 4 == 0 else 0
                    new_kombi_retainers = 1 if m % 8 == 0 else 0
            
            elif scen == "Standard":
                # Realistischer Zielpfad
                if m == 1:
                    pilots = 1
                elif m == 2:
                    pilots = 2
                    new_retainers = 1
                elif m <= 6:
                    meisters = 1
                    recruitings = 1 if m % 2 == 0 else 0
                    kombis = 1 if m % 3 == 0 else 0
                    new_retainers = 1
                    if kombis > 0:
                        new_kombi_retainers = 1
                elif m <= 12:
                    meisters = 2
                    recruitings = 1
                    kombis = 1 if m % 2 == 0 else 0
                    new_retainers = 1
                    new_kombi_retainers = 1 if kombis > 0 else 0
                elif m <= 24:
                    meisters = 2
                    recruitings = 1
                    kombis = 1
                    new_retainers = 1
                    new_kombi_retainers = 1
                else: # Monate 25-36
                    meisters = 2
                    recruitings = 1
                    kombis = 2
                    new_retainers = 1
                    new_kombi_retainers = 1
                    
            elif scen == "Wachstum":
                # Schneller Ausbau, Partner-Unterstützung ab Monat 12
                if m <= 2:
                    pilots = 2 if m == 2 else 1
                elif m <= 6:
                    meisters = 2
                    kombis = 1
                    new_retainers = 2
                    new_kombi_retainers = 1
                elif m <= 12:
                    meisters = 2
                    recruitings = 1
                    kombis = 2
                    new_retainers = 2
                    new_kombi_retainers = 1
                else: # Monate 13-36
                    meisters = 3
                    recruitings = 2
                    kombis = 2
                    new_retainers = 2
                    new_kombi_retainers = 2
            
            # Churn-Rate bei Retainern (ca. 5% Abgang ab Monat 6)
            if m > 6:
                if active_retainers > 10 and m % 4 == 0:
                    active_retainers -= 1
                if active_kombi_retainers > 8 and m % 6 == 0:
                    active_kombi_retainers -= 1
                    
            active_retainers += new_retainers
            active_kombi_retainers += new_kombi_retainers
            
            # Projektumsatz
            setup_rev = (pilots * P_PILOT + 
                         meisters * P_MEISTER + 
                         recruitings * P_RECRUITING + 
                         kombis * P_KOMBI)
            
            # Wiederkehrender Umsatz
            mrr = (active_retainers * P_BETREUUNG + 
                   active_kombi_retainers * P_KOMBI_BETREUUNG)
            
            total_rev = setup_rev + mrr
            
            # Kosten
            # Bei hohem Projektvolumen (ab Monat 13 im Wachstumsszenario) evtl. Freelance-Unterstützung
            partner_costs = 0.0
            if scen == "Wachstum" and m > 12:
                # Auslagerung von Fachtext/Asset-Zuarbeit: 400 € pro Meister, 500 € pro Kombi
                partner_costs = (meisters * 400.0) + (kombis * 500.0)
            elif scen == "Standard" and m > 24:
                partner_costs = (meisters * 300.0) + (kombis * 400.0)
                
            monthly_costs = BASE_FIXED_COSTS_MONTHLY + AD_BUDGET_OWN_MONTHLY + partner_costs
            
            net_profit_before_tax = total_rev - monthly_costs
            
            # USt (19%) - wird vereinnahmt und an Finanzamt abgeführt (durchlaufender Posten)
            vat_collected = total_rev * 0.19
            vat_input_deduction = monthly_costs * 0.19
            vat_payable = vat_collected - vat_input_deduction
            gross_cash_inflow = total_rev + vat_collected
            gross_cash_outflow = monthly_costs + vat_input_deduction + vat_payable
            
            # Arbeitszeit-Bedarf
            hours_needed = (pilots * HOURS_PILOT + 
                            meisters * HOURS_MEISTER + 
                            recruitings * HOURS_RECRUITING + 
                            kombis * HOURS_KOMBI + 
                            active_retainers * HOURS_BETREUUNG_PER_CLIENT + 
                            active_kombi_retainers * HOURS_KOMBI_BETREUUNG_PER_CLIENT)
            
            capacity_pct = (hours_needed / HOURS_PER_MONTH_AVAILABLE) * 100.0
            
            cum_revenue += total_rev
            cum_costs += monthly_costs
            cum_profit += net_profit_before_tax
            
            results_rows.append({
                "Szenario": scen,
                "Monat": m,
                "Projekte_Pilot": pilots,
                "Projekte_Meister": meisters,
                "Projekte_Recruiting": recruitings,
                "Projekte_Kombi": kombis,
                "Aktive_Retainer_250": active_retainers,
                "Aktive_Kombi_Retainer_490": active_kombi_retainers,
                "Umsatz_Setup_Netto": round(setup_rev, 2),
                "Umsatz_MRR_Netto": round(mrr, 2),
                "Umsatz_Gesamt_Netto": round(total_rev, 2),
                "Fix_und_Betriebskosten_Netto": round(monthly_costs, 2),
                "Gewinn_vor_Steuern_Netto": round(net_profit_before_tax, 2),
                "USt_Zahllast_19pct": round(vat_payable, 2),
                "Kumulierter_Gewinn_Netto": round(cum_profit, 2),
                "Arbeitsaufwand_Stunden": round(hours_needed, 1),
                "Kapazitaetsauslastung_25h_pct": round(capacity_pct, 1),
                "Ziel_15k_erreicht": "JA" if net_profit_before_tax >= 15000.0 else "NEIN"
            })
            
    # Schreibe CSV
    out_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(out_dir, "02_finanzmodell_12_und_36_monate.csv")
    
    fieldnames = [
        "Szenario", "Monat", "Projekte_Pilot", "Projekte_Meister", "Projekte_Recruiting", "Projekte_Kombi",
        "Aktive_Retainer_250", "Aktive_Kombi_Retainer_490", "Umsatz_Setup_Netto", "Umsatz_MRR_Netto",
        "Umsatz_Gesamt_Netto", "Fix_und_Betriebskosten_Netto", "Gewinn_vor_Steuern_Netto",
        "USt_Zahllast_19pct", "Kumulierter_Gewinn_Netto", "Arbeitsaufwand_Stunden",
        "Kapazitaetsauslastung_25h_pct", "Ziel_15k_erreicht"
    ]
    
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for r in results_rows:
            writer.writerow(r)
            
    print(f"Finanzmodell erfolgreich berechnet. CSV generiert unter: {csv_path}")
    
    # Zusammenfassung ausgeben
    print("\n--- ZUSAMMENFASSUNG ZIELERREICHUNG (15.000 € Monatsüberschuss vor Steuern) ---")
    for scen in scenarios:
        scen_rows = [r for r in results_rows if r["Szenario"] == scen]
        hit_months = [r["Monat"] for r in scen_rows if r["Ziel_15k_erreicht"] == "JA"]
        m12 = scen_rows[11]
        m36 = scen_rows[35]
        print(f"\nSzenario: {scen}")
        print(f"  Monat 12: Umsatz {m12['Umsatz_Gesamt_Netto']} €, Gewinn {m12['Gewinn_vor_Steuern_Netto']} €, MRR {m12['Umsatz_MRR_Netto']} €, Auslastung {m12['Kapazitaetsauslastung_25h_pct']} %")
        print(f"  Monat 36: Umsatz {m36['Umsatz_Gesamt_Netto']} €, Gewinn {m36['Gewinn_vor_Steuern_Netto']} €, MRR {m36['Umsatz_MRR_Netto']} €, Auslastung {m36['Kapazitaetsauslastung_25h_pct']} %")
        if hit_months:
            print(f"  -> 15.000 € Monatsgewinn erstmals erreicht in Monat {hit_months[0]}")
        else:
            print(f"  -> 15.000 € Monatsgewinn im 36-Monats-Fenster noch nicht nachhaltig erreicht (benötigt Skalierung)")

if __name__ == "__main__":
    calculate_financials()
