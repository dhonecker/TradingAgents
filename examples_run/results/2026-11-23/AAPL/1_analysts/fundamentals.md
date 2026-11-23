# AAPL (Apple Inc.): Fundamentalanalyse, Stand 23.11.2026

## 0. Datenlage und Einschränkungen
- **Nicht verfügbar:** `get_fundamentals` (Kennzahlen wie KGV, Marktkapitalisierung, Dividendenrendite, Beta, Analystenziele) und `get_insider_transactions` lieferten beide einen Vendor-Fehler (Yahoo Finance, HTTPError). Ich schätze oder erfinde dazu keine Werte. **Bewertungskennzahlen und Insider-Aktivität sind daher in diesem Bericht nicht bewertbar.**
- **Verfügbar:** Quartalsberichte aus SEC EDGAR (Bilanz, Cashflow, GuV) bis zum Quartal zum 26.09.2026 (Bilanz) bzw. 27.06.2026 (GuV und Cashflow).
- **Lücke:** Für das vierte Geschäftsquartal 2026 (Ende 26.09.2026) liegt die Bilanz vor. GuV- und Cashflow-Daten für dieses Quartal fehlen in den Quartalsdaten. Das ist typisch, weil Q4 nur im Jahresabschluss steckt. Alle Ergebnisaussagen gelten deshalb für die ersten drei Quartale des Geschäftsjahres 2026 (9M FY26).
- Alle Beträge sind in Mio. USD, sofern nicht anders angegeben. Alle Wachstumsraten und Margen habe ich selbst aus den gelieferten Rohdaten berechnet.

## 1. Ertragslage (GuV)

| Quartal (Ende) | Umsatz | Bruttogewinn | Operatives Ergebnis | Nettogewinn | EPS (verwässert) |
|---|---|---|---|---|---|
| 28.12.2025 (Q1 FY26) | 143.756 | 69.231 | 50.852 | 42.097 | 2,84 |
| 28.03.2026 (Q2 FY26) | 111.184 | 54.781 | 35.885 | 29.578 | 2,01 |
| 27.06.2026 (Q3 FY26) | 109.417 | 54.770 | 35.695 | 29.789 | 2,02 |
| *Vorjahr: 28.12.2024 / 29.03.2025 / 28.06.2025* | 124.300 / 95.359 / 94.036 | 58.275 / 44.867 / 43.718 | 42.832 / 29.589 / 28.202 | 36.330 / 24.780 / 23.434 | 2,40 / 1,65 / 1,57 |

**Wachstum gegenüber dem Vorjahresquartal:**
- **Q3 FY26:** Umsatz +16,4 %, operatives Ergebnis +26,6 %, Nettogewinn +27,1 %, EPS +28,7 %.
- **Q2 FY26:** Umsatz +16,6 %, Nettogewinn +19,4 %, EPS +21,8 %.
- **Q1 FY26:** Umsatz +15,7 %, Nettogewinn +15,9 %, EPS +18,3 %.
- **9M FY26 gegenüber 9M FY25:**
  - Umsatz 364.357 gegenüber 313.695 (+16,2 %).
  - Nettogewinn 101.464 gegenüber 84.544 (+20,0 %).
  - EPS-Summe 6,87 gegenüber 5,62 (+22 %).
  - Der EPS wächst schneller als der Gewinn, was auf eine sinkende Aktienzahl durch Rückkäufe hindeutet.

**Margen:**
- **Bruttomarge Q3 FY26:** 50,1 % (Vorjahresquartal 46,5 %). Q2 lag bei 49,3 %, Q1 bei 48,2 %. Die Bruttomarge steigt also seit drei Quartalen und erreicht den Höchstwert der gelieferten Historie. Das ist ein klarer Qualitätsbeleg.
- **Operative Marge Q3 FY26:** 32,6 % (Vorjahr 30,0 %).
- **Nettomarge Q3 FY26:** 27,2 % (Vorjahr 24,9 %).
- Das Wachstum von rund 16 % ist für ein Unternehmen dieser Größe überdurchschnittlich. Der Gewinn wächst dank der Margenausweitung deutlich schneller als der Umsatz (positiver operativer Hebel).

## 2. Bilanz (Stand 26.09.2026)

| Position | 26.09.2026 | 27.09.2025 | Veränderung |
|---|---|---|---|
| Bilanzsumme | 404.548 | 359.241 | +12,6 % |
| Umlaufvermögen | 173.857 | 147.957 | +17,5 % |
| Zahlungsmittel & Äquivalente | 36.305 | 35.934 | +1,0 % |
| Gesamtverbindlichkeiten | 292.455 | 285.508 | +2,4 % |
| Kurzfristige Verbindlichkeiten | 169.915 | 165.631 | +2,6 % |
| Eigenkapital | 112.093 | 73.733 | +52,0 % |

**Kennzahlen:**
- **Current Ratio:** 173.857 / 169.915 = **1,02**. Das ist auskömmlich, aber knapp. Es ist für Apple typisch, weil das Unternehmen sehr effizient mit Working Capital arbeitet.
- **Verbindlichkeiten zu Eigenkapital:** 2,61x (Vorjahr 3,87x). Die Verschuldungsquote sinkt deutlich, weil das Eigenkapital stark wächst.
- **Eigenkapitalquote:** 27,7 % (Vorjahr 20,5 %).
- **Eigenkapitalentwicklung:** 73,7 Mrd. (09/25), 88,2 Mrd. (12/25), 106,5 Mrd. (03/26), 107,5 Mrd. (06/26), 112,1 Mrd. (09/26). Das Eigenkapital steigt, weil Gewinne und Rückkäufe/Dividenden sich nicht mehr so stark ausgleichen wie in früheren Jahren (siehe Cashflow).
- **Q4-Sprung:** Das Umlaufvermögen stieg im Quartal um rund 24 Mrd. (149,8 auf 173,9 Mrd.). Gründe wären etwa saisonaler Vorrats- und Forderungsaufbau vor dem Weihnachtsgeschäft und neue Produktzyklen. Das ist eine Vermutung, die die Daten nicht belegen. Die Zahlungsmittel sanken dagegen von 39,5 auf 36,3 Mrd.
- **Hinweis:** Die gelieferten Daten enthalten weder Finanzschulden noch marktfähige Wertpapiere. Eine Nettoliquiditätsposition lässt sich damit nicht berechnen.

## 3. Cashflow

| Zeitraum | Operativer CF | Capex | Freier CF (OCF − Capex) | Finanzierungs-CF |
|---|---|---|---|---|
| Q1 FY26 | 53.925 | 2.373 | 51.552 | −39.656 |
| Q2 FY26 (abgeleitet) | 28.702 | 1.971 | 26.731 | −22.279 |
| Q3 FY26 (abgeleitet) | 34.369 | 2.455 | 31.914 | −32.640 |
| **9M FY26** | **116.996** | **6.799** | **110.197** | **−94.575** |
| 9M FY25 | 81.754 | 9.473 | 72.281 | −93.210 |

- **Operativer Cashflow:** In den ersten neun Monaten liegt er um 43 % über dem Vorjahr. Das Wachstum ist deutlich stärker als beim Nettogewinn (+20 %). Ein Teil davon dürfte auf Working-Capital-Effekte und Timing zurückgehen. Die Daten erlauben keine genauere Zuordnung.
- **Freier Cashflow:** 110,2 Mrd. gegenüber 72,3 Mrd. im Vorjahr (+52 %). Die Cash-Conversion liegt bei FCF / Nettogewinn = 109 %.
- **Capex:** Er sank sogar um 28 % auf nur 6,8 Mrd. Das sind rund 1,9 % vom Umsatz. Apple investiert damit deutlich weniger kapitalintensiv als andere Großkonzerne im KI-Wettlauf. Ob das ein Vorteil (Kapitaleffizienz) oder ein strategisches Risiko (zu geringe KI-Infrastruktur) ist, lässt sich aus diesen Daten nicht entscheiden.
- **Kapitalrückführung:** Der Finanzierungs-Cashflow von −94,6 Mrd. in 9M FY26 liegt auf Vorjahresniveau (−93,2 Mrd.). Er entspricht etwa 86 % des freien Cashflows. Der Rest stärkt die Bilanz, was die steigende Eigenkapitalquote erklärt. Die Aufteilung auf Aktienrückkäufe, Dividenden und Schuldentilgung liegt nicht vor.

## 4. Langfristiger Kontext
- **Umsatz:** Q3 FY26 liegt bei 109,4 Mrd. Zum Vergleich: Q3 FY19 lag bei 53,8 Mrd., Q3 FY21 bei 81,4 Mrd. und Q3 FY24 bei 85,8 Mrd. Der Umsatz hat sich in sieben Jahren etwa verdoppelt.
- **Bruttomarge:** Sie lag 2019 bei rund 37–38 % (z. B. Q3 FY19: 20.227 / 53.809 = 37,6 %), 2021 bei rund 43 % und liegt jetzt bei 50 %. Das ist die Folge des wachsenden margenstarken Services-Mixes. Diese Begründung ist eine gängige Annahme. Die gelieferten Daten enthalten keine Segmentaufteilung.
- **Eigenkapital:** Der Tiefpunkt lag bei 50,7 Mrd. (09/2022). Jetzt sind es 112,1 Mrd. Jahrelang schrumpfte das Eigenkapital durch Rückkäufe von 134 Mrd. (2017) auf 51 Mrd. (2022). Der aktuelle Aufbau ist eine Trendwende.

## 5. Insider-Transaktionen
Daten nicht verfügbar (Vendor-Fehler). Es ist keine Aussage über Käufe oder Verkäufe von Insidern möglich. Händler sollten die Form-4-Meldungen separat prüfen.

## 6. Handlungsrelevante Schlussfolgerungen
**Positiv:**
1. Zweistelliges Umsatzwachstum (rund 16 % in drei aufeinanderfolgenden Quartalen) bei rasch steigenden Margen.
2. Der Gewinn je Aktie wächst mit 20–29 % deutlich schneller als der Umsatz.
3. Sehr starker freier Cashflow (110 Mrd. in 9M) bei niedrigem Capex.
4. Die Bilanz verbessert sich (Eigenkapital +52 %, Verschuldungsquote sinkt).

**Risiken und offene Punkte:**
1. **Bewertung unbekannt.** Ohne Kurs, KGV und Kennzahlen lässt sich nicht beurteilen, ob das Wachstum bereits eingepreist ist. Das ist der wichtigste Punkt für eine Handelsentscheidung.
2. Die Current Ratio von 1,02 und die hohen kurzfristigen Verbindlichkeiten (169,9 Mrd.) lassen wenig Puffer. Bei Apples Liquidität ist das aber kein akutes Problem.
3. Q4 FY26 (Ergebnis, Cashflow, Ausblick) fehlt in den Daten. Der Bilanzanstieg im Umlaufvermögen sollte mit dem Quartalsbericht abgeglichen werden.
4. Der OCF-Anstieg (+43 %) übertrifft das Gewinnwachstum deutlich. Das kann teilweise ein einmaliger Working-Capital-Effekt sein. Nachhaltigkeit prüfen.
5. Der niedrige Capex kann bei einem KI-getriebenen Branchenumfeld zum strategischen Risiko werden. Das ist eine Einschätzung, die die Daten nicht belegen.

**Gesamteinschätzung:** Die operative und finanzielle Qualität ist ausgezeichnet. Ohne Bewertungsdaten und Insider-Informationen gibt es aber keinen belegbaren Vorteil für eine Positionsveränderung. Ich empfehle, die vorhandene Position zu halten und die Bewertung (KGV, FCF-Rendite) sowie den Q4-Bericht vor einer Aufstockung zu prüfen.

## 7. Zusammenfassende Tabelle

| Bereich | Kernpunkt | Bewertung |
|---|---|---|
| Umsatzwachstum | Q3 FY26 109,4 Mrd. (+16,4 % im Jahresvergleich); 9M +16,2 % | Positiv |
| Profitabilität | Bruttomarge 50,1 %, operative Marge 32,6 %, Nettomarge 27,2 % | Sehr positiv |
| EPS | Q3 2,02 (+28,7 %); 9M 6,87 (+22 %) | Positiv |
| Freier Cashflow | 9M 110,2 Mrd. (+52 %), Cash-Conversion 109 % | Sehr positiv |
| Capex | 9M 6,8 Mrd. (−28 %), rund 1,9 % vom Umsatz | Neutral (Effizienz oder KI-Risiko) |
| Kapitalrückführung | Finanzierungs-CF −94,6 Mrd. (rund 86 % des FCF) | Positiv |
| Bilanz | Eigenkapital 112,1 Mrd. (+52 %); Verbindlichkeiten/Eigenkapital 2,61x | Positiv |
| Liquidität | Current Ratio 1,02; Zahlungsmittel 36,3 Mrd. | Neutral |
| Q4 FY26 GuV/Cashflow | In den Quartalsdaten nicht enthalten | Datenlücke |
| Bewertungskennzahlen | `get_fundamentals` nicht verfügbar | Datenlücke |
| Insider-Transaktionen | Nicht verfügbar | Datenlücke |

FINAL TRANSACTION PROPOSAL: **HOLD**