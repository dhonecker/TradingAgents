# GOOGL (Alphabet Inc., Class A) – Fundamentalanalyse, Stand 23.11.2026

## 0. Datenlage und Einschränkungen
- **`get_fundamentals` war nicht verfügbar** (HTTP-Fehler bei Yahoo Finance). Bewertungskennzahlen wie KGV, Marktkapitalisierung, Dividendenrendite, Beta und Analystenziele fehlen deshalb. Ich schätze sie nicht.
- **`get_insider_transactions` war nicht verfügbar.** Zu Insiderkäufen und -verkäufen kann ich keine Aussage machen.
- **Verfügbar** sind Bilanz, Cashflow und Gewinn- und Verlustrechnung (GuV) auf Quartalsbasis. Sie stammen aus SEC-EDGAR-Einreichungen bis zum 23.11.2026. Der jüngste Datenpunkt ist das Quartal per 30.09.2026 (Q3 2026).
- Aus den Tools geht nicht hervor, was in der letzten Woche neu veröffentlicht wurde. Die Analyse stützt sich auf den neuesten Stand der Einreichungen.
- Alle Zahlen sind in Mio. USD. Abgeleitete Kennzahlen habe ich selbst berechnet und als solche gekennzeichnet.
- Das Tool liefert keine Q4-Einzelwerte, weil Q4 nur im Jahresabschluss steht. Die Cashflow-Werte sind kumuliert (3, 6 und 9 Monate). Die Einzelquartale habe ich durch Differenzbildung berechnet.

## 1. Ertragslage (GuV)

| Quartal | Umsatz | Operatives Ergebnis | Op.-Marge* | Nettogewinn | EPS (verwässert) |
|---|---|---|---|---|---|
| Q3 2025 | 102.346 | 31.228 | 30,5 % | 34.979 | 2,87 |
| Q1 2026 | 109.896 | 39.696 | 36,1 % | 62.578 | 5,11 |
| Q2 2026 | 119.796 | 40.770 | 34,0 % | 112.193 | 9,11 |
| **Q3 2026** | **127.577** | **40.576** | **31,8 %** | **26.468** | **2,12** |

*Eigene Berechnung.

**Beobachtungen**
- **Umsatzwachstum beschleunigt sich leicht und ist hoch.**
  - Q3 2026 liegt bei +24,7 % gegenüber dem Vorjahr (127.577 gegenüber 102.346).
  - Q2 2026 lag bei +24,2 % und Q1 2026 bei +21,8 %.
  - Für ein Unternehmen dieser Größe (rund 500 Mrd. USD Umsatz auf Jahresbasis) ist das außergewöhnlich.
- **Das operative Ergebnis wächst langsamer als zuvor.**
  - Q3 2026 liegt bei +29,9 % gegenüber dem Vorjahr. Gegenüber Q2 2026 (40.770) ist es leicht gesunken (−0,5 %), obwohl der Umsatz um 6,5 % stieg.
  - Die operative Marge fiel von 36,1 % (Q1) auf 34,0 % (Q2) und 31,8 % (Q3). Das sind Margendruck und ein Anzeichen dafür, dass die Kosten schneller steigen als der Umsatz.
- **Die Umsatzkosten steigen.** Ihre Quote lag in Q1 2026 bei 37,6 %, in Q2 bei 38,3 % und in Q3 bei 40,3 %. Das passt zu höheren Abschreibungen und Betriebskosten durch die KI-Infrastruktur. Das ist meine Interpretation. Das Tool liefert keine Kostenaufschlüsselung.
- **Der Nettogewinn ist stark verzerrt.**
  - Q1 (62,6 Mrd.) und Q2 2026 (112,2 Mrd.) liegen weit über dem operativen Ergebnis. Es muss also sehr große nicht-operative Erträge gegeben haben, zum Beispiel Bewertungsgewinne auf Beteiligungen. Die Ursache ist in den Daten nicht angegeben.
  - In Q3 fiel der Nettogewinn auf 26.468 (−24,3 % gegenüber dem Vorjahr), obwohl das operative Ergebnis um 30 % stieg. Der Nettogewinn liegt damit unter dem operativen Ergebnis (40.576). Das deutet auf Verluste oder Belastungen unterhalb der operativen Ebene hin, etwa Bewertungsverluste oder höhere Steuern und Zinsen. Auch hier fehlt die Aufschlüsselung.
  - **Fazit:** Das EPS (9,11 in Q2, 2,12 in Q3) ist als Trendindikator unbrauchbar. Das operative Ergebnis ist die belastbarere Größe.

## 2. Bilanz

| Stichtag | Bilanzsumme | Umlaufvermögen | Liquide Mittel | Verbindlichkeiten | Kurzfr. Verbindl. | Eigenkapital |
|---|---|---|---|---|---|---|
| 30.09.2025 | 536.469 | 173.947 | 23.090 | 149.602 | 99.550 | 386.867 |
| 31.12.2025 | 595.281 | 206.038 | 30.708 | 180.016 | 102.745 | 415.265 |
| 31.03.2026 | 703.919 | 213.753 | 38.063 | 225.173 | 111.188 | 478.746 |
| 30.06.2026 | 921.983 | 343.524 | 55.911 | 281.503 | 126.111 | 640.480 |
| **30.09.2026** | **1.003.312** | **374.665** | **56.334** | **325.763** | **134.501** | **677.549** |

**Beobachtungen**
- **Die Bilanzsumme hat sich in einem Jahr fast verdoppelt** (+87 %). Sie überschritt erstmals 1 Billion USD.
- **Die Verbindlichkeiten wuchsen mit +118 % gegenüber dem Vorjahr deutlich schneller als das Eigenkapital (+75 %).**
  - Die Verbindlichkeitenquote (Verbindlichkeiten zu Eigenkapital) stieg von 0,39 auf 0,48.
  - Das ist noch moderat, aber der Trend ist klar. Die Schuldenaufnahme finanziert den Ausbau.
- **Die Liquidität ist solide.** Die Quote aus Umlaufvermögen und kurzfristigen Verbindlichkeiten liegt bei 2,79 (Vorjahr 1,75). Die liquiden Mittel liegen bei 56,3 Mrd. Dazu kommen vermutlich marktfähige Wertpapiere, die das Tool nicht ausweist.
- **Das Eigenkapital sprang in Q2 2026 um rund 162 Mrd.** Der Nettogewinn von 112 Mrd. erklärt nur einen Teil davon. Der Rest könnte aus Eigenkapitalmaßnahmen oder Bewertungseffekten stammen. Das ist aus den Daten nicht ersichtlich und sollte im 10-Q geprüft werden.
- **Die Schulden sind nicht separat ausgewiesen.** Eine genaue Verschuldungsanalyse ist mit diesen Daten nicht möglich.

## 3. Cashflow

Eigene Berechnung der Einzelquartale aus den kumulierten Werten:

| Zeitraum | Operativer CF | Capex | Freier CF (OCF − Capex) |
|---|---|---|---|
| Q3 2025 | 48.414 | 23.953 | 24.461 |
| Q1 2026 | 45.790 | 35.674 | 10.116 |
| Q2 2026 | 39.069 | 44.924 | −5.855 |
| **Q3 2026** | **42.290** | **51.355** | **−9.065** |
| 9M 2025 (kumuliert) | 112.311 | 63.596 | 48.715 |
| **9M 2026 (kumuliert)** | **127.149** | **131.953** | **−4.804** |

**Beobachtungen**
- **Die Investitionen (Capex) haben sich innerhalb von 9 Monaten mehr als verdoppelt** (+107,5 % gegenüber dem Vorjahr). Der operative Cashflow wuchs nur um 13,2 %.
- **Der freie Cashflow ist seit Q2 2026 negativ.** Er lag in Q2 bei −5,9 Mrd. und in Q3 bei −9,1 Mrd. Über 9 Monate beträgt er −4,8 Mrd., gegenüber +48,7 Mrd. im Vorjahr.
- **Der operative Cashflow ist in Q2 und Q3 2026 sogar niedriger als in Q3 2025** (42,3 Mrd. gegenüber 48,4 Mrd.), obwohl der Umsatz um 25 % stieg. Das ist ein Warnsignal für die Cash-Konversion. Mögliche Gründe wie Working Capital oder Steuern sind aus den Daten nicht ableitbar.
- **Die Investitionstätigkeit insgesamt ist enorm.** Der Investitions-Cashflow beträgt −217,2 Mrd. in 9 Monaten (Vorjahr −68,5 Mrd.). Er enthält also neben Capex weitere große Posten wie Wertpapierkäufe oder Übernahmen. Der Capex macht nur rund 61 % davon aus.
- **Die Finanzierung dreht ins Positive: +115,8 Mrd. in 9 Monaten** (Vorjahr −44,4 Mrd.). Alphabet finanziert sich also extern, statt wie früher Kapital zurückzugeben. Das passt zu den gestiegenen Verbindlichkeiten. Ob es Anleihen, Eigenkapital oder anderes ist, zeigt das Tool nicht.

## 4. Langfristige Einordnung
- Der Umsatz stieg von 16,5 Mrd. (Q3 2014) auf 127,6 Mrd. (Q3 2026), also rund das 7,7-Fache.
- Die operative Marge lag historisch bei 22–32 %. Sie stieg 2024–2026 auf über 30 % und erreichte in Q1 2026 mit 36 % ihren Höhepunkt.
- Die Bilanz war bis 2025 sehr konservativ (Verbindlichkeiten unter 30 % der Bilanzsumme). Per 30.09.2026 liegt die Quote bei etwa 32,5 %. Das ist noch niedrig, aber der Trend zeigt nach oben.
- Das Unternehmen befindet sich in einem Investitionszyklus von beispielloser Größe. Die Frage ist, ob die Erträge daraus die Kapitalkosten und Abschreibungen verdienen.

## 5. Handlungsrelevante Erkenntnisse für Trader

**Positiv**
1. Das Umsatzwachstum von knapp 25 % und das operative Ergebniswachstum von knapp 30 % gegenüber dem Vorjahr zeigen starke Nachfrage.
2. Die Liquidität ist gut, die Verschuldung moderat, und die Bilanz bietet Spielraum.
3. Die operative Marge liegt mit rund 32 % weiter über dem langfristigen Durchschnitt.

**Negativ / Risiken**
1. Die operative Marge sinkt seit drei Quartalen, von 36,1 % auf 31,8 %. Das operative Ergebnis stagniert sequenziell.
2. Der freie Cashflow ist negativ, der Capex hat sich verdoppelt, und der operative Cashflow wächst nur unterproportional.
3. Die externe Finanzierung (+115,8 Mrd.) und die Verbindlichkeiten (+118 % gegenüber dem Vorjahr) steigen schnell.
4. Die Ergebnisqualität ist schwach. Der Nettogewinn schwankt stark wegen nicht-operativer Posten, und in Q3 lag er deutlich unter dem operativen Ergebnis.
5. Es fehlen Bewertungskennzahlen und Insiderdaten. Ohne sie ist eine Einschätzung, ob das Wachstum eingepreist ist, nicht möglich.

**Was beobachtet werden sollte**
- Den 10-Q für Q3 2026 auf die Zusammensetzung der nicht-operativen Posten, der Schulden und der Finanzierung prüfen.
- Den Ausblick des Managements zu Capex und zum Zeitpunkt, ab dem der freie Cashflow wieder positiv wird.
- Die Margenentwicklung in Q4 2026.
- Die Bewertung und die Insidertransaktionen mit einer anderen Datenquelle nachholen.

## 6. Zusammenfassende Tabelle

| Bereich | Kennzahl / Befund | Wert | Einschätzung |
|---|---|---|---|
| Umsatz Q3 2026 | Gegenüber Vorjahr | 127.577 Mio. (+24,7 %) | Positiv |
| Operatives Ergebnis Q3 2026 | Gegenüber Vorjahr | 40.576 Mio. (+29,9 %) | Positiv |
| Operative Marge | Q1 → Q3 2026 | 36,1 % → 31,8 % | Negativ (Trend) |
| Umsatzkostenquote | Q1 → Q3 2026 | 37,6 % → 40,3 % | Negativ |
| Nettogewinn Q3 2026 | Gegenüber Vorjahr | 26.468 Mio. (−24,3 %) | Negativ, verzerrt |
| EPS Q3 2026 | Verwässert | 2,12 USD (Vorjahr 2,87) | Wenig aussagekräftig |
| Nettogewinn Q2 2026 | Ausreißer | 112.193 Mio. | Vermutlich nicht-operativ |
| Bilanzsumme | 30.09.2026 | 1.003.312 Mio. (+87 %) | Starkes Wachstum |
| Verbindlichkeiten | 30.09.2026 | 325.763 Mio. (+118 %) | Steigendes Risiko |
| Eigenkapital | 30.09.2026 | 677.549 Mio. | Stark gewachsen |
| Liquide Mittel | 30.09.2026 | 56.334 Mio. | Solide |
| Current Ratio | Eigene Berechnung | 2,79 | Sehr gut |
| Operativer Cashflow | 9M 2026 | 127.149 Mio. (+13,2 %) | Unterproportional |
| Capex | 9M 2026 | 131.953 Mio. (+107,5 %) | Sehr hoch |
| Freier Cashflow | 9M 2026 | −4.804 Mio. (Vorjahr +48.715) | Negativ |
| Finanzierungs-Cashflow | 9M 2026 | +115.757 Mio. | Externe Finanzierung |
| Bewertungskennzahlen | – | Nicht verfügbar | Datenlücke |
| Insidertransaktionen | – | Nicht verfügbar | Datenlücke |

FINAL TRANSACTION PROPOSAL: **HOLD**