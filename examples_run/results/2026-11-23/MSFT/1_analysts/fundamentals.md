# MSFT: Fundamentalanalyse (Stand 23.11.2026)

## 1. Datenlage und Einschränkungen
- **Nicht verfügbar:** `get_fundamentals` (Unternehmensprofil, Bewertungskennzahlen wie KGV, Marktkapitalisierung, Dividendenrendite) und `get_insider_transactions` lieferten wegen eines Vendor-Fehlers (HTTPError) keine Daten. Ich schätze diese Werte nicht und erfinde keine. **Aussagen zu Bewertung und Insider-Aktivität sind daher nicht möglich.**
- **Verfügbar:** Quartalsdaten aus SEC EDGAR zu Bilanz, Cashflow und Gewinn- und Verlustrechnung (GuV). Das jüngste Quartal endet am 30.09.2026.
- **Lücken in der Datenreihe:** In GuV und Cashflow fehlen teils die Quartale zum 30.06. (Geschäftsjahresende) und zum 31.03. Diese Quartale stecken nur im Jahresabschluss. Ich vergleiche deshalb vor allem das Quartal zum 30.09.2026 mit dem zum 30.09.2025.
- **Nicht in den Daten:** Es gibt keine Angaben zu Schulden, kurzfristigen Anlagen, Segmenten oder Aktienrückkäufen und -dividenden. Auch Nachrichten der letzten Woche fehlen. Die jüngste Information ist der Quartalsabschluss zum 30.09.2026.

## 2. Gewinn- und Verlustrechnung (Quartal zum 30.09.2026 gegenüber Vorjahresquartal)

| Kennzahl (Mio. USD) | Q 30.09.2026 | Q 30.09.2025 | Veränderung |
|---|---|---|---|
| Umsatz | 92.279 | 77.673 | +18,8 % |
| Umsatzkosten | 29.720 | 24.043 | +23,6 % |
| Bruttogewinn | 62.559 | 53.630 | +16,6 % |
| Operatives Ergebnis | 45.915 | 37.961 | +20,9 % |
| Nettoergebnis | 36.629 | 27.747 | +32,0 % |
| Verwässertes EPS (USD) | 4,92 | 3,72 | +32,3 % |

**Margen:**
- **Bruttomarge:** ca. 67,8 %, nach ca. 69,0 % im Vorjahr. Die Umsatzkosten wachsen schneller als der Umsatz. Das passt zu steigenden Infrastrukturkosten (Abschreibungen auf das KI-Rechenzentrums-Investitionsprogramm), ist aber eine Vermutung und aus den Daten nicht belegt.
- **Operative Marge:** ca. 49,8 %, nach ca. 48,9 %. Das Unternehmen gleicht den Rückgang der Bruttomarge durch Betriebskosten-Disziplin mehr als aus.
- **Nettomarge:** ca. 39,7 %, nach ca. 35,7 %.
- **Verhältnis Nettoergebnis zu operativem Ergebnis:** ca. 79,8 %, nach ca. 73,1 %. Der Nettogewinn wächst deutlich schneller als das operative Ergebnis. Mögliche Ursachen sind nichtoperative Erträge oder ein geringerer Steuersatz. Die Daten erklären das nicht. Das ist ein Qualitätspunkt, den man in der Gewinnmitteilung prüfen sollte.

**Frühere Quartale:**
- Umsatz: 70.066 (Q 31.03.2025), 81.273 (Q 31.12.2025), 82.886 (Q 31.03.2026), 92.279 (Q 30.09.2026).
- Das Nettoergebnis von 38.458 Mio. USD (EPS 5,16) im Dezember-Quartal 2025 lag über dem operativen Ergebnis von 38.275 Mio. USD. Das deutet auf einen einmaligen oder nichtoperativen Gewinn hin. EPS-Vergleiche sollten diesen Ausreißer berücksichtigen.
- Das operative Ergebnis wächst seit Jahren stetig: von 30.552 Mio. USD (Q 30.09.2024) über 37.961 Mio. USD (Q 30.09.2025) auf 45.915 Mio. USD.

## 3. Cashflow (Quartal zum 30.09.2026 gegenüber Vorjahresquartal)

| Kennzahl (Mio. USD) | Q 30.09.2026 | Q 30.09.2025 |
|---|---|---|
| Operativer Cashflow | 58.000 | 45.057 |
| Investitionen (Capex) | 39.367 | 19.394 |
| Freier Cashflow (operativer Cashflow minus Capex, eigene Berechnung) | ca. 18.633 | ca. 25.663 |
| Investitions-Cashflow | -41.965 | -34.559 |
| Finanzierungs-Cashflow | -16.640 | -11.799 |

- Der operative Cashflow stieg um ca. 28,7 %. Das ist stark und höher als das Umsatzwachstum.
- Das **Capex hat sich in einem Jahr mehr als verdoppelt** (+103 %). Es lag bei 16.745 Mio. USD im März-Quartal 2025, 29.876 Mio. USD im Dezember-Quartal 2025, 30.876 Mio. USD im März-Quartal 2026 und nun 39.367 Mio. USD. Das entspricht ca. 43 % des Umsatzes.
- Der **freie Cashflow sank dadurch um ca. 27 %** auf ca. 18,6 Mrd. USD, obwohl der operative Cashflow stark wuchs. Die Kapitalintensität steigt deutlich. Das ist das zentrale Risiko für die Cash-Konversion.
- Die Capex-Zahl könnte Finanzierungsleasing nicht enthalten. Die tatsächliche Investitionslast wäre dann noch höher.
- Der Finanzierungs-Cashflow ist negativ (-16,6 Mrd. USD). Das passt zu Mittelabflüssen für Aktionäre oder Schuldentilgung, die Aufteilung liegt aber nicht vor.

## 4. Bilanz (30.09.2026)

| Position (Mio. USD) | 30.09.2026 | 30.06.2026 | 30.09.2025 |
|---|---|---|---|
| Bilanzsumme | 779.403 | 758.376 | 636.351 |
| Umlaufvermögen | 186.137 | 207.710 | 189.066 |
| Zahlungsmittel | 20.281 | 20.935 | 28.849 |
| Gesamtverbindlichkeiten | 308.894 | 315.989 | 273.275 |
| Kurzfristige Verbindlichkeiten | 151.968 | 168.825 | 134.996 |
| Eigenkapital | 470.509 | 442.387 | 363.076 |

- **Bilanzsumme:** +22,5 % gegenüber dem Vorjahr. Das Wachstum kommt vor allem aus dem Anlagevermögen (Rechenzentren), da das Umlaufvermögen kaum gestiegen ist.
- **Eigenkapital:** +29,6 % auf 470,5 Mrd. USD.
- **Eigenkapitalquote:** ca. 60,4 %. Die Verbindlichkeiten betragen ca. 0,66 des Eigenkapitals (Verbindlichkeiten zu Eigenkapital). Die Bilanz bleibt sehr solide.
- **Liquiditätsgrad 1 (Current Ratio):** ca. 1,22 (186.137 / 151.968). Ein Jahr zuvor waren es ca. 1,40. Die Liquidität ist ausreichend, aber schwächer geworden.
- **Zahlungsmittel:** nur 20,3 Mrd. USD (ohne kurzfristige Anlagen, die in den Daten fehlen). Der Wert liegt unter dem Vorjahr (28,8 Mrd. USD).
- Der Sprung der Verbindlichkeiten im Juni-Quartal 2026 auf 316 Mrd. USD und der Anstieg der kurzfristigen Verbindlichkeiten auf 168,8 Mrd. USD deuten auf zunehmende Finanzierung von Investitionen und Verpflichtungen hin. Genaue Treiber (Schulden, Leasing, abgegrenzte Umsätze) sind nicht ausgewiesen.

## 5. Langfristiger Verlauf
- **Umsatz:** von ca. 15,1 Mrd. USD im Quartal (Sep. 2008) auf 92,3 Mrd. USD. Seit 2023 wächst er im Quartal im niedrigen bis mittleren Zehnerprozentbereich.
- **Operatives Ergebnis:** von ca. 6,0 Mrd. USD (Sep. 2008) auf 45,9 Mrd. USD.
- **Eigenkapital:** von ca. 36 Mrd. USD (2008) auf 470,5 Mrd. USD.
- **Capex:** von unter 1 Mrd. USD im Quartal (2008) auf 39,4 Mrd. USD. Der Zyklus der KI-Infrastrukturinvestitionen beschleunigt sich seit 2023 (Capex Q 30.09.2023: 9,9 Mrd. USD).

## 6. Einschätzung für Trader

**Positiv:**
- Starkes Umsatzwachstum (+18,8 %) bei sehr hoher operativer Marge (ca. 50 %) und EPS-Wachstum von ca. 32 %.
- Der operative Cashflow wächst überproportional (+28,7 %).
- Die Bilanz ist robust, mit einer Eigenkapitalquote von ca. 60 %.

**Risiken und Beobachtungspunkte:**
- Das Capex hat sich verdoppelt, der freie Cashflow ist um ca. 27 % gesunken. Die Rendite auf die Investitionen muss sich in beschleunigtem Umsatzwachstum zeigen.
- Die Bruttomarge sinkt (ca. -1,2 Prozentpunkte). Das ist ein Zeichen für steigende Infrastrukturkosten.
- Die Gewinnqualität ist unklar: Das Nettoergebnis wächst viel schneller als das operative Ergebnis, und im Dezember-Quartal 2025 gab es einen Ausreißer.
- Der Liquiditätsgrad sinkt, und die Zahlungsmittel sind rückläufig.
- **Ohne Bewertungsdaten und Insider-Informationen** lässt sich nicht beurteilen, ob die operative Stärke bereits im Kurs eingepreist ist. Diese Daten sollten ergänzt werden (KGV, Free-Cashflow-Rendite, Insider-Käufe und -Verkäufe).

**Fazit:** Die operativen Fundamentaldaten sind exzellent. Der stark steigende Kapitalbedarf bremst den freien Cashflow. Mangels Bewertungs- und Insiderdaten ist eine Halteempfehlung vorsichtig und vertretbar. Bei Rücksetzern oder bestätigter Capex-Rendite wäre ein Aufstocken zu prüfen.

## 7. Zusammenfassende Tabelle

| Bereich | Kernaussage | Wert / Beleg | Bewertung |
|---|---|---|---|
| Umsatz (Q 30.09.2026) | Starkes Wachstum | 92,3 Mrd. USD, +18,8 % im Jahresvergleich | Positiv |
| Operatives Ergebnis | Wächst schneller als der Umsatz | 45,9 Mrd. USD, +20,9 %, Marge ca. 49,8 % | Positiv |
| Nettoergebnis / EPS | Starker Anstieg, Qualität prüfen | 36,6 Mrd. USD, EPS 4,92 (+32 %) | Positiv, mit Vorsicht |
| Bruttomarge | Leicht rückläufig | ca. 67,8 % nach ca. 69,0 % | Leicht negativ |
| Operativer Cashflow | Sehr stark | 58,0 Mrd. USD, +28,7 % | Positiv |
| Capex | Mehr als verdoppelt | 39,4 Mrd. USD, +103 % | Risiko |
| Freier Cashflow | Rückläufig | ca. 18,6 Mrd. USD, ca. -27 % | Negativ |
| Bilanzsumme / Eigenkapital | Starkes Wachstum | 779,4 Mrd. USD / 470,5 Mrd. USD | Positiv |
| Verschuldung (Verbindlichkeiten) | Moderat, steigend | 308,9 Mrd. USD, Eigenkapitalquote ca. 60 % | Neutral bis positiv |
| Liquidität | Schwächer geworden | Current Ratio ca. 1,22 (Vorjahr ca. 1,40), Zahlungsmittel 20,3 Mrd. USD | Leicht negativ |
| Bewertungskennzahlen / Profil | Nicht verfügbar | Vendor-Fehler (HTTPError) | Datenlücke |
| Insider-Transaktionen | Nicht verfügbar | Vendor-Fehler (HTTPError) | Datenlücke |

FINAL TRANSACTION PROPOSAL: **HOLD**