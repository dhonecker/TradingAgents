# NVDA – Fundamentalanalyse (Stand: 23.11.2026)

## 0. Datenlage und Einschränkungen
- **Nicht verfügbar:** `get_fundamentals` (Unternehmensprofil, Bewertungskennzahlen wie KGV, Marktkapitalisierung, Dividendenrendite, Analystenziele) und `get_insider_transactions`. Beide Abrufe scheiterten mit einem Yahoo-Finance-HTTP-Fehler. Ich schätze oder erfinde keine Werte. Aussagen zu **Bewertung** und **Insider-Aktivität** sind daher nicht möglich.
- **Verfügbar:** Quartalsberichte (SEC EDGAR) für Bilanz, Cashflow und GuV. Der letzte Berichtsstichtag ist **26.07.2026** (Q2 des Geschäftsjahres 2027).
- **Lücken in den Daten:** Einzelne Quartale fehlen, vor allem die Januar-Quartale (Q4), z. B. der 25.01.2026 in der GuV. Der Cashflow ist teils kumuliert (6 bzw. 9 Monate) ausgewiesen. Quartalswerte, die ich daraus berechne, sind als **abgeleitet** markiert.
- **Aktiensplits:** Die EPS-Werte sind nicht durchgehend splitbereinigt. Der Sprung von 0,82 auf 0,25 im Jahr 2023 ist ein Splitartefakt und kein Gewinnrückgang.

## 1. Ertragslage (GuV, in Mio. USD)

| Quartal | Umsatz | Bruttogewinn | Bruttomarge | Operat. Ergebnis | Op.-Marge | Nettogewinn | EPS (verwässert) |
|---|---|---|---|---|---|---|---|
| 27.07.2025 | 46.743 | 33.853 | 72,4 % | 28.440 | 60,8 % | 26.422 | 1,08 |
| 26.10.2025 | 57.006 | 41.849 | 73,4 % | 36.010 | 63,2 % | 31.910 | 1,30 |
| 26.04.2026 | 81.615 | 61.157 | 74,9 % | 53.536 | 65,6 % | 58.321 | 2,39 |
| **26.07.2026** | **96.221** | **72.142** | **75,0 %** | **63.734** | **66,2 %** | **59.688** | **2,46** |

**Wachstum im letzten Quartal (26.07.2026):**
- Umsatz: **+105,9 % gegenüber dem Vorjahresquartal** und **+17,9 % gegenüber dem Vorquartal** (26.04.2026).
- Operatives Ergebnis: +124 % im Jahresvergleich.
- Nettogewinn: +126 % im Jahresvergleich.
- EPS: +128 % im Jahresvergleich.
- Das operative Ergebnis wächst schneller als der Umsatz, es gibt also positiven operativen Hebel. Die Bruttomarge ist mit rund 75 % stabil auf sehr hohem Niveau. Zum Vergleich: Im Quartal zum 27.04.2025 lag sie bei nur 60,5 %.

**Auffälligkeit:** Im Quartal zum 26.04.2026 liegt der Nettogewinn (58.321) **über** dem operativen Ergebnis (53.536). Die Nettomarge betrug dort 71,5 %. Das deutet auf erhebliche nicht-operative Erträge hin, vermutlich Gewinne aus Beteiligungen oder Zinserträge. Das ist meine Schlussfolgerung und kein Datenpunkt. Die Gewinnqualität dieses Quartals ist daher geringer einzuschätzen als die des Quartals zum 26.07.2026. Dort liegt die Nettomarge bei 62,0 % und der Nettogewinn unter dem operativen Ergebnis.

**Langfristiger Kontext:** Der Umsatz stieg von rund 7,2 Mrd. USD (Quartal zum 30.04.2023) auf 96,2 Mrd. USD. Das ist etwa das 13-Fache in gut drei Jahren, getrieben vom KI-Rechenzentrumsboom.

## 2. Bilanz (in Mio. USD, 26.07.2026)

| Position | 26.07.2025 | 26.04.2026 | 26.07.2026 |
|---|---|---|---|
| Bilanzsumme | 140.740 | 259.474 | **320.272** |
| Umlaufvermögen | 102.219 | 150.995 | 197.412 |
| Zahlungsmittel | 11.639 | 13.237 | 22.443 |
| Gesamtverbindlichkeiten | 40.609 | 64.000 | **91.288** |
| Kurzfristige Verbindlichkeiten | 24.257 | 43.884 | 43.019 |
| Eigenkapital | 100.131 | 195.474 | **228.984** |

**Kennzahlen (berechnet):**
- Current Ratio: 197.412 / 43.019 ≈ **4,6**. Die Liquidität ist sehr komfortabel.
- Verbindlichkeiten zu Eigenkapital: ≈ **0,40** (Vorquartal ≈ 0,33, Vorjahr ≈ 0,41).
- Eigenkapitalquote: ≈ 71,5 %.
- Die Bilanzsumme hat sich im Jahresvergleich mehr als verdoppelt (+128 %).

**Auffälligkeiten:**
1. Die Gesamtverbindlichkeiten stiegen in einem Quartal um rund 27,3 Mrd. USD. Die kurzfristigen Verbindlichkeiten blieben dabei nahezu unverändert. Die **langfristigen Verbindlichkeiten sprangen** daher von ca. 20,1 Mrd. auf ca. 48,3 Mrd. USD (abgeleitet). Die Ursache geht aus den Daten nicht hervor. Möglich wären Anleihen, langfristige Lieferverpflichtungen oder Leasing. Das sollte im 10-Q geprüft werden.
2. Der Bilanzposten „Zahlungsmittel" (22,4 Mrd.) enthält keine marktgängigen Wertpapiere. Die gesamte Liquiditätsposition ist mit diesen Daten nicht sichtbar.
3. Das Eigenkapital stieg im letzten Quartal um ca. 33,5 Mrd. USD. Der Nettogewinn betrug 59,7 Mrd. Die Differenz lässt sich mit den vorliegenden Daten nicht abstimmen. Plausibel sind Aktienrückkäufe, Dividenden oder Steuerabführungen auf Aktienvergütung, aber das ist nicht belegt.

## 3. Cashflow (in Mio. USD)

| Zeitraum | Operat. CF | Investitions-CF | Finanzierungs-CF | Capex | FCF (OCF – Capex) |
|---|---|---|---|---|---|
| Q1 FY27 (bis 26.04.2026) | 50.344 | -26.429 | -21.283 | 1.757 | **≈ 48.587** |
| 6 Monate bis 26.07.2026 | 74.421 | -35.124 | -27.459 | 4.434 | **≈ 69.987** |
| *Q2 FY27 (abgeleitet)* | *≈ 24.077* | *≈ -8.695* | *≈ -6.176* | *≈ 2.677* | *≈ 21.400* |
| 6 Monate bis 27.07.2025 | 42.779 | -12.343 | -27.386 | 3.122 | ≈ 39.657 |

**Bewertung:**
- Der FCF der ersten 6 Monate liegt mit ca. 70 Mrd. USD rund **76 % über dem Vorjahreszeitraum** (ca. 39,7 Mrd.).
- **Warnsignal bei der Cash-Konversion:** Der abgeleitete operative Cashflow im Q2 (≈ 24,1 Mrd.) fiel gegenüber Q1 (50,3 Mrd.) um etwa die Hälfte. Der Nettogewinn lag gleichzeitig bei 59,7 Mrd. Das entspricht einer Cash-Konversion von nur ca. 40 %.
- Wahrscheinlich ist ein Aufbau von Working Capital, also Forderungen und Vorräte, bei stark wachsendem Geschäft. Auch das ist eine Schlussfolgerung und kein belegter Fakt. Es muss geprüft werden, ob die Entwicklung temporär ist.
- Die Investitionsausgaben sind im Verhältnis zum Umsatz gering (Q2 ≈ 2,8 % des Umsatzes). Das Geschäftsmodell ist kapitalleicht.
- Der negative Finanzierungs-CF deutet auf Kapitalrückführung an Aktionäre hin (Rückkäufe und Dividenden). Die Details sind nicht im Datensatz.

## 4. Insider-Transaktionen
Nicht verfügbar (Datenabruf fehlgeschlagen). Es lässt sich keine Aussage zu Insider-Käufen oder -Verkäufen treffen. Das sollte über eine andere Quelle, z. B. SEC Form 4, nachgeholt werden.

## 5. Handlungsrelevante Erkenntnisse für Trader
**Positiv:**
- Das Umsatzwachstum von rund 106 % im Jahresvergleich bei zugleich steigenden Margen (Bruttomarge ca. 75 %, operative Marge ca. 66 %) ist außergewöhnlich.
- Die Bilanz ist solide (Current Ratio 4,6, Eigenkapitalquote ca. 71 %).
- Der Free Cashflow ist in absoluten Zahlen enorm (ca. 70 Mrd. USD in 6 Monaten).

**Risiken und Beobachtungspunkte:**
- Die Cash-Konversion im letzten Quartal war schwach (ca. 40 % des Nettogewinns). Ein Anstieg der Forderungen und Vorräte kann ein Frühindikator für Nachfrageschwäche oder Zahlungsziele sein.
- Die langfristigen Verbindlichkeiten stiegen sprunghaft. Die Ursache ist zu klären.
- Die Gewinnqualität im Quartal zum 26.04.2026 ist durch mutmaßliche nicht-operative Erträge verzerrt.
- Das Wachstum von Q1 auf Q2 verlangsamte sich auf +17,9 %. Das ist weiterhin stark, aber eine Verlangsamung gegenüber dem vorherigen Sprung. Das Q4 (Januar 2026) fehlt in den Daten.
- **Bewertung unbekannt:** Ohne KGV, Kurs und Konsensschätzungen kann kein Einstiegspunkt aus den Fundamentaldaten abgeleitet werden. Bei hohen Erwartungen reagieren Kurse oft empfindlich auf Marginabweichungen oder Guidance-Änderungen.

## 6. Übersichtstabelle

| Bereich | Kernaussage | Einschätzung |
|---|---|---|
| Datenlage | Fundamentals und Insider-Daten nicht verfügbar | Lücke, Bewertung nicht beurteilbar |
| Umsatz (Q 26.07.2026) | 96,2 Mrd. USD, +106 % YoY, +18 % QoQ | Sehr stark |
| Bruttomarge | ≈ 75,0 % (Vorjahr 72,4 %) | Stabil hoch |
| Operative Marge | ≈ 66,2 % | Starker operativer Hebel |
| Nettogewinn / EPS | 59,7 Mrd. USD / 2,46 USD (+126 % / +128 % YoY) | Sehr stark |
| Gewinnqualität | Q 26.04.2026: Nettogewinn > operatives Ergebnis | Vorsicht, nicht-operative Effekte |
| Bilanzsumme | 320,3 Mrd. USD (+128 % YoY) | Rasches Wachstum |
| Liquidität | Current Ratio ≈ 4,6 | Sehr solide |
| Verschuldung | Verbindlichkeiten/Eigenkapital ≈ 0,40; langfristige Verbindlichkeiten +ca. 28 Mrd. QoQ | Ursache klären |
| Free Cashflow | ≈ 70 Mrd. USD in 6 Monaten (+76 % YoY) | Sehr stark |
| Cash-Konversion Q2 | OCF ≈ 24,1 Mrd. vs. Nettogewinn 59,7 Mrd. (≈ 40 %) | Warnsignal |
| Capex | ≈ 2,8 % vom Umsatz in Q2 | Kapitalleicht |
| Insider-Transaktionen | Keine Daten | Extern prüfen |

**Rating**: Hold

FINAL TRANSACTION PROPOSAL: **HOLD**

Die Fundamentaldaten sind außergewöhnlich stark. Die fehlenden Bewertungsdaten, die schwache Cash-Konversion im letzten Quartal und der Anstieg der langfristigen Verbindlichkeiten sprechen aber gegen eine Positionsausweitung, solange diese Punkte ungeklärt sind.