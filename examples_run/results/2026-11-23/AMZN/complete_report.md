# Trading Analysis Report: AMZN

- Analysis date: 2026-11-23
- Rating: Hold
- Generated: 2026-11-23 16:11:03
- TradingAgents 0.7.1: anthropic, deep claude-opus-5-5, quick claude-sonnet-5-5
- Analysts: market, sentiment, news, fundamentals; research debate rounds 1, risk debate rounds 1
- Data vendors: core_stock_apis yfinance, technical_indicators yfinance, fundamental_data sec_edgar,yfinance, news_data yfinance, macro_data fred, prediction_markets polymarket

## I. Analyst Team Reports

### Market Analyst
# AMZN (Amazon.com, Inc.): technischer Bericht zum 23.11.2026

## 1. Datengrundlage und Hinweis zur Datenqualität
- Ich habe die Kursdaten von 2026-01-01 bis 2026-11-23 abgerufen (225 Handelstage) und acht Indikatoren geladen. Die exakten Werte stammen aus dem verifizierten Snapshot.
- **Abweichung zwischen den Quellen:** Der Snapshot meldet für den 23.11.2026 einen Schlusskurs von 257,005 und ein Volumen von 20.372.846. Die Kursreihe zeigt 256,97 und 20.360.652. Die Differenz ist klein. Sie deutet darauf hin, dass der Balken vom 23.11. noch nicht abgeschlossen ist, denn das Volumen von rund 20 Mio. liegt weit unter dem üblichen Tagesvolumen von 30–50 Mio. Ich nehme keine Angleichung vor und verwende den Snapshot. Alle Aussagen zum 23.11. sind vorläufig.

## 2. Gewählte Indikatoren und Begründung
Ich habe acht Indikatoren gewählt, die sich ergänzen:
1. **close_200_sma** zeigt den langfristigen Trend.
2. **close_50_sma** zeigt den mittelfristigen Trend und dient als dynamische Referenz.
3. **close_10_ema** zeigt das kurzfristige Momentum.
4. **macd** bzw. **macdh** zeigen Trendwechsel und Momentumstärke. Das Signal (macds) liegt im Snapshot vor.
5. **rsi** zeigt überkaufte oder überverkaufte Zustände.
6. **boll_ub** und **boll_lb** zeigen die Volatilitätsgrenzen und das Kanalverhalten.
7. **atr** dient dem Risikomanagement, also Stop-Abständen und Positionsgröße.

Auf VWMA habe ich verzichtet. Die Tagesvolumina schwanken stark, und einzelne Spitzen würden den Durchschnitt verzerren. Das Volumen betrachte ich stattdessen direkt in den Rohdaten.

## 3. Verifizierte Kennzahlen (Snapshot, 2026-11-23)
| Kennzahl | Wert |
|---|---:|
| Schlusskurs (vorläufig) | 257,005 |
| Tageshoch / Tagestief | 262,48 / 251,25 |
| 10-EMA | 258,475 |
| 50-SMA | 255,101 |
| 200-SMA | 245,384 |
| RSI | 49,45 |
| Bollinger Mitte / oberes / unteres Band | 257,817 / 275,272 / 240,362 |
| MACD / Signal / Histogramm | 0,720 / 1,733 / -1,013 |
| ATR | 10,376 |

## 4. Trendanalyse

### Langfristiger und mittelfristiger Trend: konstruktiv, aber flach
- Der Kurs liegt mit 257,0 über dem 50-SMA (255,10) und über dem 200-SMA (245,38). Der 50-SMA liegt über dem 200-SMA, die Struktur ist also formal bullisch.
- Der Abstand zum 50-SMA beträgt nur etwa 1,9 Punkte. Der 50-SMA hat sich im Beobachtungsfenster kaum bewegt: Er lag zwischen 253,79 (03.11.) und 255,38 (26.10.). Das passt zu einer Seitwärtsphase und nicht zu einem dynamischen Trend.
- Der 200-SMA steigt langsam, von 243,31 am 26.10. auf 245,38. Das ist eine leichte Aufwärtsneigung.
- Der Kurs bewegt sich seit etwa Mitte August in einer breiten Handelsspanne. Die Schlusskurse liegen meist zwischen etwa 240 und 271, die Ausreißer waren der 30.10. (240,35) und der 10.11. (270,87).

### Kurzfristiger Trend und Momentum: nachlassend
- Der Kurs (257,0) liegt knapp unter dem 10-EMA (258,47). Der 10-EMA ist seit dem 13.11. (262,84) gefallen. Das Kurzfristmomentum hat sich also abgekühlt.
- **MACD:** Die Linie lag am 13.11. bei 3,50 und ist auf 0,72 gefallen. Am 20.11. wechselte das Histogramm von 0,003 (19.11.) auf -1,04 und liegt am 23.11. bei -1,01. Das ist ein bärisches Signal-Crossover, die MACD-Linie liegt unter ihrem Signal (1,73). Da sie noch über null liegt, ist es eine Abschwächung und noch kein klarer Abwärtstrend.
- **RSI:** Der RSI liegt bei 49,45, also neutral. Er schwankte im Fenster zwischen 38,3 (30.10.) und 61,6 (10.11.) und war nie überkauft oder überverkauft. Der RSI liefert daher kein Extremsignal. Für eine Richtungsentscheidung fehlt eine Bestätigung.

### Volatilität
- Die Bollinger-Bänder liegen bei 240,36 und 275,27, also ungefähr 34,9 Punkte auseinander. Der Kurs steht fast in der Bandmitte (257,82). Es gibt weder ein Überkauft- noch ein Überverkauft-Signal.
- Das obere Band war zuletzt bei etwa 275 praktisch flach, das untere bei etwa 240. Die Bänder haben sich seit Ende Oktober deutlich geweitet: Das untere Band fiel von 245,29 (28.10.), das obere stieg von 265,06 auf 275,27.
- Der **ATR** stieg von 6,19 (28.10.) auf 10,38. Das ist ein Plus von rund zwei Dritteln. Die Volatilität ist also deutlich höher als noch vor vier Wochen.

## 5. Preisaktion der letzten Wochen
Die Rohdaten zeigen mehrere große Tagesbewegungen mit hohem Volumen:
- **29.–30.10.:** Der Kurs fiel von 254,60 auf 243,79 und dann auf 240,35. Das Volumen lag bei 85,2 Mio. und 104,9 Mio.
- **04.11.:** Der Kurs sprang von 250,69 auf 266,03 (Schluss), das Volumen betrug 93,2 Mio. Die Eröffnung lag bei 264,82, es war also eine Lücke nach oben.
- **16.–20.11.:** Es folgte ein sehr unruhiger Verlauf: 257,75, 257,89, 267,74, 257,37 und 246,82. Am 19.11. eröffnete der Kurs bei 272,56 und schloss bei 257,37. Am 20.11. schloss er bei 246,82 mit 74,1 Mio. Volumen. Am 23.11. liegt der Schlusskurs (vorläufig) wieder bei 257,0, nach einem Tagestief von 251,25.
- Die Daten belegen die Muster, nicht ihre Ursachen. Die Tool-Ausgaben enthalten keine Nachrichten oder Ereignisse. Die Spitzen am 30.10. und 04.11. fallen zeitlich zusammen mit dem Quartalsberichtszeitraum, das ist aber eine Vermutung und kein Beleg.
- Der Verlauf zeigt eine hohe Intraday-Volatilität und mehrfach gescheiterte Ausbrüche über 267–270. Auf der Unterseite wurde der Bereich um 240 zuletzt am 30.10. getestet.

## 6. Handlungsrelevante Beobachtungen
Ich gebe keine Entscheidung vor, sondern ordne ein, was die Daten stützen.

**Szenarien**
- **Bullisch:** Ein Schlusskurs über dem 10-EMA (258,5) und dann über der oberen Handelsspanne bei etwa 267–271 würde ein neues Aufwärtssignal liefern. Dafür sollten das MACD-Histogramm wieder positiv werden und der RSI über etwa 55–60 steigen. Das obere Bollinger-Band (275,3) wäre die nächste Marke.
- **Bärisch:** Ein Schlusskurs unter dem 50-SMA (255,1) mit negativem MACD-Histogramm wäre ein erstes Schwächesignal. Danach wären der 200-SMA (245,4) und das untere Band (240,4) die nächsten Referenzen. Der 20.11. mit einem Schluss bei 246,82 hat die Zone um den 200-SMA bereits berührt.
- **Aktuell neutral bis leicht abwartend:** Die Indikatoren sind gemischt. Der Trend ist positiv, aber das kurzfristige Momentum hat nachgelassen.

**Risikomanagement**
- Bei einem ATR von 10,38 entspricht ein Stop im Abstand von 1,5 × ATR etwa 15,6 Punkten (rund 6 % vom Kurs). Das ist eine rechnerische Orientierung und keine Empfehlung.
- Die Volatilität ist gegenüber Oktober deutlich höher. Wer Positionen steuert, sollte die Größe entsprechend anpassen.
- Da der Balken vom 23.11. noch nicht abgeschlossen ist, sollte man den Schlusskurs abwarten, bevor man Signale daraus ableitet.

**Einschränkungen**
- Ich habe keine Support- oder Widerstands-Bounces historisch geprüft. Die genannten Zonen (240, 255, 267–271) stammen aus den oben genannten Kursen und Indikatoren und sind keine statistisch validierten Marken.
- Es liegen keine Fundamentaldaten oder Nachrichten vor.

## 7. Zusammenfassende Tabelle
| Bereich | Beobachtung | Wert / Datum | Einordnung |
|---|---|---|---|
| Langfristtrend | Kurs über 200-SMA | 257,0 vs. 245,38 | Leicht bullisch |
| Mitteltrend | Kurs über 50-SMA, SMA flach | 257,0 vs. 255,10 | Neutral bis leicht bullisch |
| Kurzfristtrend | Kurs unter 10-EMA | 257,0 vs. 258,47 | Leicht schwächer |
| MACD | Signal-Crossover nach unten (20.11.) | 0,72 vs. 1,73; Hist. -1,01 | Nachlassendes Momentum |
| RSI | Neutral | 49,45 | Kein Extremsignal |
| Bollinger | Kurs nahe Mitte, Bänder weit | 240,36 / 257,82 / 275,27 | Neutral, hohe Spanne |
| ATR | Volatilität gestiegen | 10,38 (28.10.: 6,19) | Größere Stops nötig |
| Volumen | Spitzen an Ereignistagen | 30.10.: 104,9 Mio.; 04.11.: 93,2 Mio. | Starke Marktreaktionen |
| Datenhinweis | Snapshot und Kursreihe weichen minimal ab | 257,005 vs. 256,97 | Balken vom 23.11. vorläufig |
| Gesamtbild | Seitwärts mit leichtem positivem Bias, Momentum schwächer | – | Abwarten, Bestätigung nötig |

FINAL TRANSACTION PROPOSAL: **HOLD**

### Sentiment Analyst
**Overall Sentiment:** **Mildly Bullish** (Score: 5.8/10)
**Confidence:** Low

## Sentimentbericht AMZN (Amazon.com, Inc.) – Zeitraum 16.11.2026 bis 23.11.2026

**Datenlage vorab:** Nachrichten (19 Schlagzeilen) und StockTwits (30 Nachrichten) liegen vor. Reddit (r/wallstreetbets, r/stocks, r/investing) war nicht verfügbar (Abruffehler). Das bedeutet nicht, dass es dort keine Diskussion gab. Über Reddit kann ich keine Aussage treffen. Die Stichprobe bei StockTwits ist klein und überwiegend unmarkiert. Deshalb ist das Vertrauen niedrig.

### 1. Quellenweise Aufschlüsselung

**Nachrichten (Yahoo Finance & Partner):**
- Der einzige direkt AMZN-spezifische Katalysator ist die berichtete Übernahme von Technologie und Team des KI-Startups Decart für rund 7,5 Mrd. USD. Die Meldung geht auf Bloomberg zurück und wurde von Investing.com und InvestorsHub aufgegriffen. Ziel sind Optimierungssoftware und eine bessere kommerzielle Verwertbarkeit der hauseigenen Trainium-Chips. Die Quellen beschreiben das strategisch positiv, als Stärkung der KI-Compute-Position. Es ist ein „reported“-Deal, also nicht von Amazon bestätigt. Auf StockTwits wird erwähnt, dass noch eine behördliche Genehmigung aussteht.
- 24/7 Wall St.: Seth Klarman hält 18 % seines Portfolios von rund 5 Mrd. USD in Amazon. Es ist seine größte Position, und er hat nicht nachgekauft. Der Artikel erwähnt Amazons Investitionsprogramm von rund 220 Mrd. USD. Das ist ein moderat positives Signal (Value-Investor hält die Position), zugleich wird die hohe Kapitalintensität thematisiert.
- Ein Großteil der übrigen Schlagzeilen betrifft Nvidia (Trefis-Serie zu einer gemeldeten SEC-Untersuchung und Kursrisiko bis 92 USD, „Neocloud“-Exposure von 115 Mrd. USD und Rückkehr von Jensen Huang). Außerdem geht es um Anthropic (Kursrutsch) und Alphabet (Kapitalausgaben, verfehlte Gewinne, Kursschwäche). Diese betreffen AMZN indirekt über das KI-Infrastruktur-Thema und über Amazons Anthropic-Beteiligung. Die Beteiligung wird in den Daten nicht ausdrücklich erwähnt, ich nenne sie als Kontext.
- Eine nicht benannte Hyperscaler-Vorauszahlung an Fermi (200 Mio. USD, 600 MW) taucht ebenfalls auf. Der Name Amazon wird nicht genannt, auf StockTwits wird der Titel mit $AMZN getaggt. Es gibt keinen Beleg dafür, dass AMZN der Hyperscaler ist.
- Randthemen: Thanksgiving-Lebensmittelangebote (Walmart, Target, Amazon), FedEx-Artikel mit Verweis auf Amazons Logistik-Vorstoß als Wettbewerbsdruck, ein Verbraucherartikel zu Abos.
- Gesamteindruck der Nachrichten: leicht positiv für AMZN (Decart, Klarman), im Umfeld eines nervösen KI-Sektors (Nvidia-SEC-Meldung, Anthropic-Schwäche, Alphabet-Kritik an Ausgaben).

**StockTwits (30 Nachrichten):**
- Markierte Stimmung: 6 bullisch (20 %), 4 bärisch (13 %), 20 ohne Label. Unter den 10 markierten Beiträgen sind das 60/40 bullisch. Das ist eine sehr kleine Basis und nur schwach aussagekräftig.
- Bullische Beiträge: „über 300 USD bis Jahresende“, die Decart-Logik (mehr Leistung aus den eigenen KI-Chips zu geringeren Kosten, ein weiterer Grund für AWS-Kunden, Trainium zu wählen), „Black Friday all time highs“. Zwei bullische Labels stammen von Beiträgen, die kaum AMZN-bezogen sind (Cega zu RZLV, ElmagoMagico steigt aus dem Markt aus).
- Bärische Beiträge: eine kleine Short-Position bei 258 USD, „SLAM THIS JUNK“ (Sammel-Tag auf mehrere Titel) und zwei Beiträge zu Jeff Bezos’ Hecke, die nichts mit dem Kurs zu tun haben. Der bärische Anteil ist also zum Teil Rauschen.
- Optionsfluss (GTA_Terminal): Rund zwei Drittel von 1,4 Mio. USD Prämie entfielen auf Calls, etwa 2.600 Kontrakte (bullisch). Der Kurs lag bei etwa 253 USD (+2,6 %). Das Dark-Pool-Volumen vom Freitag (20.11.) lag beim 1,3-Fachen eines normalen Tages (bärisch). Einzelne Tagesoptionen (260C, 265C mit 0,04–0,70 USD) sind spekulativ und verraten kaum etwas über die Richtung.
- Gemischte Kursbeobachtungen: „Why is this moving so weakly compared to everything else“, „Why is this falling“, „about to go red?“. Das passt nicht zum +2,6 % im Optionsbericht. Intraday gab es offenbar Schwankungen und relative Schwäche.
- Weitere Themen: Sammelklagen zu Ring (Gesichtserkennung) und Fire TV (Datenerfassung) im Frühstadium. Ein Beitrag meldet, dass Amazon einen KI-Agenten sperrt, während Walmart ihn zulässt (Agent Gateway ab Black Friday). Das ist ein kleines Wettbewerbs- und Werbe-Schutz-Thema.
- Auffällig: Mehrere Beiträge verbinden AMZN mit Anthropic („ANT“, der Titel scheint börsennotiert und fällt). Eine Börsenschwäche bei Anthropic wird als Risiko für den KI-Handel insgesamt gesehen.

**Reddit:** nicht verfügbar. Es fehlt jede Aussage zu längerfristig orientierten Anlegern oder zu WSB.

### 2. Divergenzen und Übereinstimmungen
- Übereinstimmung: Nachrichten und Retail sehen Decart als sinnvollen strategischen Schritt (Effizienz, Trainium). Der Optionsfluss ist call-lastig.
- Divergenz: Der KI-Sektorkontext (Nvidia-SEC-Bericht, Anthropic-Abverkauf, Alphabet-Ausgabenkritik) ist eher belastend, während die AMZN-spezifischen Schlagzeilen positiv sind. Einzelne Retail-Nutzer fragen, warum AMZN relativ schwach läuft. Das könnte auf Sorgen über KI-Kapitalausgaben (rund 220 Mrd. USD) hinweisen.
- Die Dark-Pool-Aktivität ist leicht bärisch, der Calls-Fluss bullisch. Das Gesamtbild ist uneinheitlich.

### 3. Dominante Narrative
1. Decart-Deal / Trainium-Strategie: AMZN als Vollstack-KI-Anbieter (Chips + Software).
2. KI-Handel unter Druck: Nvidia (SEC), Anthropic, Alphabet-Ausgaben, Neocloud-Finanzierung. Fokus auf „Wo sitzt das Risiko?“.
3. Hohe Kapitalintensität (220 Mrd. USD), von Value-Investor Klarman aber gehalten.
4. Saisonal: Black Friday / Weihnachtsgeschäft, Thanksgiving-Angebote.
5. Nebenthemen: Datenschutzklagen, Agent-Handel (Walmart vs. Amazon), FedEx-Wettbewerb in der Logistik.

### 4. Katalysatoren und Risiken
- Katalysatoren: Bestätigung und Abschluss des Decart-Deals, Black Friday und Cyber Monday, Trainium-Adoption bei AWS-Kunden, Stabilisierung des KI-Sektors.
- Risiken: Deal nicht bestätigt und genehmigungspflichtig (behördliche Prüfung), KI-Sektor-Abverkauf (Nvidia-SEC, Anthropic), Sorgen über die Investitionshöhe, Rechtsstreitigkeiten (Ring, Fire TV), Wettbewerb bei Agent-Commerce und Logistik, relative Schwäche im Tagesverlauf.
- Fehlend: Keine Kursdaten, Analystenaktionen oder Zahlen im Prompt außer den Kursangaben in Social-Posts (ca. 253 USD, Short bei 258 USD). Reddit fehlt.

### 5. Zusammenfassung

| Signal | Richtung | Quelle | Beleg |
|---|---|---|---|
| Decart-Übernahme (~7,5 Mrd. USD) | Leicht bullisch | News, StockTwits | Bloomberg-Bericht, Trainium-/Effizienzlogik; unbestätigt, Genehmigung nötig |
| Klarman: 18 % Portfolioanteil | Leicht bullisch | News | 24/7 Wall St.; kein Zukauf, aber größte Position |
| StockTwits-Labels | Leicht bullisch (schwache Basis) | StockTwits | 6 bullisch / 4 bärisch / 20 ohne Label; Rauschen in beiden Lagern |
| Call-Optionsfluss | Bullisch | StockTwits (GTA_Terminal) | ~2/3 von 1,4 Mio. USD Prämie in Calls, ~2.600 Kontrakte, +2,6 % |
| Dark Pool 20.11. | Leicht bärisch | StockTwits | 1,3-faches Normalvolumen |
| KI-Sektor-Nervosität | Bärisch (indirekt) | News | Nvidia-SEC-Bericht, Anthropic schwach, Alphabet-Ausgabenkritik |
| Relative Schwäche intraday | Leicht bärisch | StockTwits | „moving so weakly“, „Why is this falling“ |
| Rechtsstreitigkeiten (Ring, Fire TV) | Leicht bärisch | StockTwits | Sammelklagen im Frühstadium |
| Reddit | Keine Aussage | – | Abruf fehlgeschlagen |

**Fazit:** Insgesamt leicht bullisch (5,8/10), getragen von Decart-Nachrichten und call-lastigem Optionsfluss. Der KI-Sektorkontext bremst, und die Datenbasis ist dünn (kleine StockTwits-Stichprobe, Reddit fehlt). Das ist ein Stimmungssignal und keine Kursprognose. Der Händler sollte es zusammen mit Fundamentaldaten und Technik gewichten.

### News Analyst
# AMZN (Amazon.com, Inc.): Nachrichten- und Makrobericht, 16.–23. November 2026

## 1. Kurzfassung
- **Unternehmensnews:** Das wichtigste AMZN-Ereignis der Woche ist die gemeldete Übernahme von Technologie und Team des KI-Startups **Decart** für rund **7,5 Mrd. USD**. Bloomberg berichtet darüber unter Berufung auf eine informierte Person. Eine offizielle Bestätigung habe ich nicht gesehen. Ziel ist, die eigenen **Trainium**-Chips und die Optimierungssoftware zu stärken.
- **Marktumfeld:** Der Gesamtmarkt gilt als „angeschlagen“. Yahoo Finance titelt: „A battered stock market looks for the bottom“. Der KI-Handel steht unter Druck: Nvidia wird mit einer gemeldeten SEC-Untersuchung in Verbindung gebracht, und Anthropic rutscht ab. Alphabet hat laut 24/7 Wall St. die Gewinnerwartungen verfehlt und viel Cash verbrannt.
- **Makro:** Die FRED-Daten (Leitzins, 10-jährige Rendite, CPI, Arbeitslosenquote, VIX) waren nicht abrufbar, weil der API-Schlüssel fehlt. Ich nenne dazu keine Zahlen. Die Prognosemärkte liefern aber ein klares Bild: Die Fed senkt im Dezember so gut wie sicher nicht, und eine US-Rezession bis Jahresende gilt als unwahrscheinlich.

## 2. Amazon-spezifische Nachrichten
**a) Decart-Deal (ca. 7,5 Mrd. USD)**
- Amazon soll Kerntechnologie und das Gründerteam von Decart übernehmen. Das ist ein Technologie- und Talentkauf, keine klassische Komplettübernahme.
- Strategisch zielt der Deal auf die **Vermarktung der Trainium-Chips** und auf eine bessere Inferenz- und Recheneffizienz. Das passt zu Amazons Strategie, die Abhängigkeit von Nvidia zu senken und die AWS-Margen zu stützen.
- Risiken: Der Preis ist hoch, wenn man ihn mit der aktuellen Skepsis gegenüber KI-Ausgaben vergleicht. Außerdem ist der Deal bisher nur über Medienberichte belegt. Mögliche Regulierungsfragen sind offen.

**b) Kapitalintensität und Anlegersicht**
- 24/7 Wall St. nennt einen „220-Mrd.-USD-Ausgabenrausch“ (Capex). Gemeint ist offenbar Amazons KI- und Infrastrukturprogramm.
- Seth Klarman hält 18 % seines Portfolios von rund 5 Mrd. USD in AMZN. Das ist seine größte Position, ohne dass er zugekauft hat. Das ist ein Qualitäts- und Überzeugungssignal, kein Handelssignal.

**c) Weitere Punkte**
- Amazon ist an den Thanksgiving-Lebensmittelrabatten beteiligt (Walmart, Target). Das spricht für intensiven Preiswettbewerb vor dem Weihnachtsgeschäft. Die Rabatte dürften laut MarketWatch nicht von Dauer sein.
- FedEx nennt Amazons Logistikausbau als Wettbewerbsfaktor.
- Ein Hyperscaler (nicht genannt) hat mit Fermi einen 200-Mio.-USD-Vorschuss für 600 MW Strom vereinbart. Das zeigt, dass die Nachfrage nach Rechenzentrumskapazität anhält. Ob Amazon der Käufer ist, bleibt offen.
- Apple, Nvidia und Tesla lehnen die Teilnahme an der tokenisierten Aktienplattform von ICE/OKX ab. Für AMZN ist das nicht direkt relevant.

## 3. Branchen- und Marktumfeld
- **KI-Stimmung:** Nvidia (um 125 USD) steht wegen der gemeldeten SEC-Untersuchung und seiner rund 115 Mrd. USD „Neocloud“-Exposure unter Beobachtung. Die Rückkehr von Jensen Huang löste zwar eine Erholung aus. Analysten warnen aber, dass ausgewaschene Stimmung noch keinen fundamentalen Boden bedeutet.
- **Gegenseite zu Anthropic:** Amazon ist ein großer Anthropic-Investor. Die Bewertungsspanne von 50 bis 250 USD in der Diskussion zeigt, wie unsicher die Werte sind. Die Schwäche bei Anthropic ist daher ein indirektes Bewertungsrisiko für AMZN.
- **Hyperscaler-Vergleich:** Alphabet wurde nach hohen Ausgaben und einem Gewinnverfehlen abgestraft. Der Markt belohnt Capex derzeit nicht automatisch. Er achtet darauf, ob Cloud-Wachstum und Auftragsbestand die Ausgaben rechtfertigen.
- **Konsum:** Der Konsumsektor war vor Handelsbeginn am Montag gemischt. Das Weihnachtsgeschäft (Black Friday, Cyber Monday) steht bevor.
- **Nebenthema:** Die Einführung von GTA VI (3,79 Mrd. USD am ersten Tag) bindet Konsumentenausgaben und Retail-Aufmerksamkeit. Für AMZN ist das nur marginal relevant.

## 4. Makro und Prognosemärkte (Polymarket)
| Ereignis | Wahrscheinlichkeit |
|---|---|
| Fed-Zinssenkung bis Dezember-Sitzung 2026 | 0,8 % |
| Zinssenkung bis Januar 2027 | 3 % |
| Zinssenkung bis März 2027 | 13 % |
| Zinssenkung bis April 2027 | 26 % |
| Zinssenkung bis Juli 2027 | 50 % (sehr geringes Volumen) |
| US-Rezession bis Ende 2026 | 2 % (hohes Volumen, 2,5 Mio. USD) |
| Japan-Rezession 2026 | 16 % (+10 Pp. in einer Woche, geringes Volumen) |

- **Deutung:** Der Markt rechnet mit einer längeren Zinspause. Hohe Zinsen belasten langfristige Wachstumsbewerter und kapitalintensive Geschäftsmodelle wie AMZN. Eine Rezession gilt als nahezu ausgeschlossen. Das stützt die Konsum- und Werbenachfrage.
- Die Märkte für 2027 haben kaum Volumen und sind wenig belastbar.
- **Datenlücke:** Ohne FRED-Daten fehlen mir aktuelle Zahlen zu Inflation, Arbeitsmarkt, Renditen und Volatilität. Das sollte ein anderer Analyst oder Kanal nachholen.

## 5. Handelsrelevante Schlussfolgerungen
1. **Positiv:** Der Decart-Deal stärkt die Chip-Strategie. Die Nachfrage nach KI-Infrastruktur bleibt hoch. Die Rezessionsgefahr ist gering. Institutionelle Anleger wie Klarman halten an AMZN fest.
2. **Negativ:** Der Markt ist angeschlagen, und der KI-Sektor steht unter Druck. Dazu kommen Nvidia-SEC-Gerüchte, die Anthropic-Schwäche und die Alphabet-Reaktion auf Capex. Es gibt keine Zinssenkungsunterstützung. Capex von etwa 220 Mrd. USD erhöht das Free-Cashflow-Risiko.
3. **Kurzfristige Katalysatoren:** Thanksgiving, Black Friday und Cyber Monday liefern Konsumdaten. Weitere Nachrichten zu Nvidia und Anthropic und eine mögliche Bestätigung des Decart-Deals sind ebenfalls wichtig. Die Dezember-Fed-Sitzung bringt voraussichtlich keine Überraschung.
4. **Einordnung:** Die Nachrichtenlage ist gemischt. Fundamental bleibt die Geschichte intakt, das Sentiment-Risiko im KI-Sektor ist aber hoch. Preis- und technische Daten lagen mir nicht vor. Einstiege sollten gestaffelt erfolgen, mit Blick auf Nvidia- und KI-Sektor-Nachrichten.

## 6. Übersichtstabelle

| Thema | Kernaussage | Wirkung auf AMZN |
|---|---|---|
| Decart-Deal (~7,5 Mrd. USD) | Technologie- und Teamkauf für Trainium (Bloomberg-Bericht, unbestätigt) | Mittelfristig positiv, kurzfristig Kostenfrage |
| Capex (~220 Mrd. USD) | Hohe Investitionen, FCF-Druck | Gemischt |
| Alphabet-Reaktion | Capex plus Gewinnverfehlen führen zu Abverkauf | Negativ für Sektorstimmung |
| Nvidia / SEC-Probe | Gerüchte, Neocloud-Exposure, volatile Erholung | Negativ für KI-Sentiment |
| Anthropic-Schwäche | Bewertungsunsicherheit (50–250 USD Spanne) | Indirektes Risiko (Beteiligung) |
| Gesamtmarkt | „Battered“, Bodensuche | Erhöhte Volatilität |
| Fed (Polymarket) | Dezember-Senkung 0,8 %, Juli 2027 ca. 50 % | Kein Zinsrückenwind |
| Rezession USA 2026 | 2 % | Stützt Konsum und Werbung |
| Konsum / Weihnachtsgeschäft | Rabattwettbewerb, Thanksgiving, Black Friday | Neutral bis positiv, abhängig von Zahlen |
| Klarman-Position | 18 % des Portfolios | Qualitätssignal, kein Timing |
| FRED-Makrodaten | Nicht verfügbar (API-Schlüssel fehlt) | Datenlücke |

FINAL TRANSACTION PROPOSAL: **HOLD**

### Fundamentals Analyst
# AMZN (Amazon.com, Inc.) – Fundamentalanalyse, Stand 23.11.2026

## 1. Zusammenfassung

- **Wachstum:** AMZN wächst weiter zweistellig, aber das Wachstum hat sich zuletzt abgeschwächt. Der Umsatz im Q3 2026 lag bei 201,9 Mrd. USD (+12,1 % ggü. Vorjahr). Im Q2 waren es +19,6 % und im Q1 +16,6 %.
- **Operative Profitabilität:** Sie verbessert sich deutlich. Das operative Ergebnis stieg von 17,4 Mrd. USD (Q3 2025) auf 28,1 Mrd. USD (+61 %). Die operative Marge liegt bei 13,9 %.
- **Gewinnqualität:** Der Nettogewinn wird von nicht-operativen Effekten verzerrt. Der Q2 2026 enthält 62,6 Mrd. USD Nettogewinn bei nur 27,5 Mrd. USD operativem Ergebnis. Die Daten nennen die Ursache nicht. Wahrscheinlich sind es Bewertungsgewinne auf Beteiligungen, das ist aber meine Vermutung. Das TTM-KGV von 20,8 wirkt dadurch zu günstig. Das Forward-EPS (10,93 USD) liegt unter dem TTM-EPS (12,37 USD).
- **Investitionen:** Der Kapex ist explodiert. Er lag im Q3 2026 bei 77,3 Mrd. USD (Vorjahr: 35,1 Mrd. USD, +120 %). Der freie Cashflow ist negativ (TTM ca. –34,7 Mrd. USD), und das Wachstum wird zunehmend über Fremdkapital und Eigenkapitalzuflüsse finanziert.
- **Insider:** Es gibt keine Insiderkäufe am offenen Markt. Verkäufe sind laufend und größtenteils planmäßig. Bezos hat im August 2026 rund 346 Mio. USD verkauft.

## 2. Bewertung und Marktdaten (get_fundamentals)

| Kennzahl | Wert |
|---|---|
| Marktkapitalisierung | ca. 2,78 Bio. USD |
| KGV (TTM) / Forward-KGV | 20,8 / 23,5 |
| PEG | 1,15 |
| Kurs-Buchwert | 4,53 (Buchwert/Aktie 56,76 USD) |
| EPS (TTM) / Forward-EPS | 12,37 / 10,93 USD |
| Umsatz (TTM) | ca. 797,5 Mrd. USD |
| Bruttogewinn / EBITDA | 409,7 Mrd. / 183,7 Mrd. USD |
| Nettogewinn (TTM) | 134,8 Mrd. USD |
| Nettomarge / operative Marge | 16,9 % / 13,1 % |
| ROE / ROA | 27,4 % / 6,6 % |
| Verschuldungsgrad (Debt/Equity) | 49,7 % (0,50x) |
| Current Ratio | 0,99 |
| Freier Cashflow (TTM) | ca. –34,7 Mrd. USD |
| Beta | 1,50 |
| 52-Wochen-Spanne | 196,0 – 287,2 USD |
| 50-/200-Tage-Durchschnitt | 255,0 / 245,2 USD |
| Dividendenrendite | 0 % |

**Einordnung:**
- Der Kurs lag zuletzt laut Insiderdaten bei etwa 259–262 USD. Das ist leicht über dem 50- und 200-Tage-Schnitt und etwa 9 % unter dem 52-Wochen-Hoch.
- Das Forward-KGV von 23,5 ist aussagekräftiger als das TTM-KGV, weil das TTM-EPS durch Einmalgewinne aufgebläht ist.
- Das Beta von 1,5 bedeutet überdurchschnittliche Schwankung.

## 3. Gewinn- und Verlustrechnung (Quartale, Mio. USD)

| Quartal | Umsatz | Bruttogewinn* | Operatives Ergebnis | Nettogewinn | EPS (verwässert) |
|---|---|---|---|---|---|
| Q1 2025 | 155.667 | 78.691 | 18.405 | 17.127 | 1,59 |
| Q2 2025 | 167.702 | 86.893 | 19.171 | 18.164 | 1,68 |
| Q3 2025 | 180.169 | 91.499 | 17.422 | 21.187 | 1,95 |
| Q1 2026 | 181.519 | 94.056 | 23.852 | 30.255 | 2,78 |
| Q2 2026 | 200.606 | 104.828 | 27.461 | 62.647 | 5,75 |
| Q3 2026 | 201.944 | 107.371 | 28.076 | 20.685 | 1,89 |

*Bruttogewinn = Umsatz minus Umsatzkosten, von mir berechnet. Das Q4 2025 fehlt in den gelieferten Daten.

**Beobachtungen:**
- **Wachstum:** Das Umsatzwachstum lag im Q1 2026 bei 16,6 %, im Q2 bei 19,6 % und im Q3 bei 12,1 %.
- **Bruttomarge:** Sie liegt stabil bei etwa 53 %. Die Kostenquote bleibt bei ca. 47 %.
- **Operative Marge:** Sie stieg von 11,2 % (Q3 2025) auf 13,9 % (Q3 2026). Q3 2025 war durch Sonderbelastungen gedrückt, das Vorjahr ist daher eine leichte Vergleichsbasis.
- **Nettogewinn Q3 2026:** Er lag mit 20,7 Mrd. USD leicht unter dem Vorjahr (21,2 Mrd. USD), obwohl das operative Ergebnis um 61 % stieg. Beide Quartale enthalten nicht-operative Positionen.
- **Fazit:** Die Gewinne sind schwer vergleichbar. Das operative Ergebnis ist die verlässlichere Basis.

## 4. Bilanz (Mio. USD)

| Stichtag | Bilanzsumme | Umlaufvermögen | Liquide Mittel | Kurzfr. Verbindlichkeiten | Eigenkapital |
|---|---|---|---|---|---|
| 30.09.2025 | 727.921 | 196.866 | 66.922 | 195.196 | 369.631 |
| 31.03.2026 | 916.630 | 255.155 | 101.816 | 216.756 | 441.914 |
| 30.06.2026 | 1.095.689 | 249.264 | 78.213 | 241.274 | 551.620 |
| 30.09.2026 | 1.243.390 | 255.100 | 55.783 | 257.982 | 613.601 |

**Beobachtungen:**
- **Bilanzsumme:** Sie wuchs binnen eines Jahres um ca. 71 % auf 1,24 Bio. USD. Das spiegelt den Infrastruktur-Ausbau (Rechenzentren, KI) und wohl auch Beteiligungsbewertungen.
- **Liquidität:** Die liquiden Mittel sanken von 101,8 Mrd. USD (Q1) auf 55,8 Mrd. USD. Das ist der niedrigste Stand seit Ende 2024 und ein Minus von 45 % in zwei Quartalen.
- **Current Ratio:** Sie liegt bei 0,99. Das ist für AMZN typisch, aber das Polster sinkt.
- **Eigenkapital:** Es stieg um ca. 62 Mrd. USD im Q3, bei nur 20,7 Mrd. USD Nettogewinn. Im Q2 waren es ca. 110 Mrd. USD bei 62,6 Mrd. USD Gewinn. Der Rest könnte aus Aktienausgabe, aktienbasierter Vergütung oder Bewertungseffekten stammen. Die Daten schlüsseln das nicht auf.
- **Gesamtverbindlichkeiten:** Sie sind nicht getaggt. Bilanzsumme minus Eigenkapital ergibt grob 630 Mrd. USD. Darin stecken auch Leasingverpflichtungen und sonstige Posten.
- **Verschuldung:** Die Kennzahl Debt/Equity von 49,7 % stammt aus den Fundamentaldaten. Sie berücksichtigt möglicherweise nicht den jüngsten Schuldenanstieg.

## 5. Cashflow (Mio. USD)

| Quartal | Operativer CF | Investitions-CF | Finanzierungs-CF | Kapex |
|---|---|---|---|---|
| Q3 2025 | 35.525 | –26.073 | –44 | 35.095 |
| Q1 2026 | 26.032 | –64.212 | +52.767 | 44.203 |
| Q2 2026 | 45.387 | –79.245 | +10.146 | 54.208 |
| Q3 2026 | 42.422 | –113.642 | +48.935 | 77.259 |

**Beobachtungen:**
- **Operativer Cashflow:** Er lag im Q3 2026 bei 42,4 Mrd. USD (+19 % ggü. Vorjahr) und wächst damit viel langsamer als der Kapex (+120 %).
- **Freier Cashflow Q3 2026:** Operativer CF minus Kapex ergibt ca. –34,8 Mrd. USD. Das ist das dritte Quartal in Folge mit hohen Mittelabflüssen: Q1 –18,2 Mrd., Q2 –8,8 Mrd.
- **Investitionen insgesamt:** Der Investitions-CF von –113,6 Mrd. USD im Q3 übersteigt den Kapex deutlich. Es fließt also auch Geld in Beteiligungen oder Wertpapiere.
- **Finanzierung:** Der positive Finanzierungs-CF (+48,9 Mrd. USD im Q3) deutet auf Kapitalaufnahme hin, also Anleihen oder Aktien. Die Daten zeigen die genaue Form nicht.
- **Zentrale Frage:** Wann und in welchem Umfang schlagen sich die Investitionen in höheren Umsätzen und Margen nieder?

## 6. Insider-Transaktionen

**Käufe:** Es gibt keine Käufe am offenen Markt im ausgewiesenen Zeitraum (ab Mai 2025).

**Wichtigste Verkäufe:**
- **Jeff Bezos:**
  - Am 03.08.2026 verkaufte er 1,21 Mio. Aktien zu 286,41 USD (ca. 346 Mio. USD). Das war nahe dem 52-Wochen-Hoch.
  - Von Juni bis Juli 2025 verkaufte er ca. 25 Mio. Aktien (ca. 5,6 Mrd. USD) bei 220–230 USD.
  - Er verschenkt regelmäßig große Aktienpakete, zuletzt 771.492 Stück am 13.11.2026, 415.580 am 26.08.2026 und 1,25 Mio. am 04.05.2026. Das sind Schenkungen ohne Erlös, keine Marktverkäufe.
- **Andy Jassy (CEO):**
  - Er verkauft regelmäßig 20.000 Aktien pro Quartal (zuletzt 21.08.2026 zu ca. 259 USD, ca. 5,2 Mio. USD). Das entspricht einem Muster, wie es bei Verkaufsplänen üblich ist.
  - Hinzu kamen größere Verkäufe am 17.04.2026 (31.000 Stück zu 255 USD) und am 04.05.2026 (31.352 Stück zu 275 USD, ca. 8,6 Mio. USD).
- **Douglas Herrington (Officer):**
  - Er verkauft monatlich 1.000 Aktien und zusätzlich quartalsweise größere Pakete.
  - Am 04.05.2026 verkaufte er 28.500 Stück (ca. 7,8 Mio. USD) und am 14.04.2026 20.500 Stück (ca. 5,0 Mio. USD).
  - Zuletzt verkaufte er am 16.11.2026 3.741 Stück zu ca. 260–262 USD.
- **Weitere Verkäufer:** CFO Olsavsky, Garman, Zapolsky und Reynolds verkauften zuletzt im August 2026 Pakete von 2–15 Tsd. Aktien (jeweils ca. 0,6–4,0 Mio. USD).
- **Direktoren:** Rubinstein verkaufte Ende April 2026 ca. 2,0 Mio. USD, Huttenlocher am 18.11.2026 783 Aktien.

**Bewertung:** Die Verkäufe folgen weitgehend wiederkehrenden Mustern (Vesting-Termine im Februar, Mai, August und November, monatliche Pläne). Sie sind daher nur schwach als Signal zu werten. Auffällig ist das Fehlen jeglicher Insiderkäufe. Die Verkäufe sind außerdem mengenmäßig recht groß.

## 7. Chancen und Risiken

**Chancen:**
- Der operative Hebel ist spürbar (operatives Ergebnis +61 % bei Umsatz +12 %).
- Die Bruttomarge ist stabil bei ca. 53 %, und der ROE ist hoch (27 %).
- Das Forward-KGV von 23,5 ist für einen Konzern dieser Größe und Wachstumsrate nicht extrem.
- Der operative Cashflow wächst weiter zweistellig.

**Risiken:**
- Das Umsatzwachstum hat sich im Q3 auf 12 % verlangsamt, während der Kapex mehr als verdoppelt wurde.
- Der FCF ist negativ, die liquiden Mittel sinken, und die Finanzierung läuft zunehmend extern.
- Die Gewinnqualität ist schwach: Nettogewinn und EPS enthalten große nicht-operative Gewinne, die nicht wiederkehren müssen.
- Das Beta von 1,5 und die Nähe zum 52-Wochen-Hoch erhöhen das Rückschlagrisiko bei enttäuschenden Quartalszahlen.
- Es gibt keine Insiderkäufe und laufende Verkäufe durch das Top-Management.
- Die Lücke zwischen Kapex und operativem Cashflow lässt wenig Spielraum, falls die Nachfrage nach Cloud- und KI-Kapazität nachlässt.

## 8. Handelsrelevante Schlussfolgerungen

- Die Fundamentaldaten sind gemischt: Operativ stark, aber der Kapitalbedarf steigt schnell und der FCF ist negativ.
- Für Trader sind die nächsten Quartalszahlen entscheidend. Zu beobachten sind Umsatzwachstum (hält es über 12 %?), operative Marge, Kapex-Prognose und Finanzierungsmix.
- Als Orientierung dienen der 50-Tage-Schnitt (ca. 255 USD) und der 200-Tage-Schnitt (ca. 245 USD) als Unterstützung sowie das 52-Wochen-Hoch bei 287 USD als Widerstand.
- Die Bewertung ist nicht billig. Das niedrige TTM-KGV sollte nicht als Kaufargument dienen.

FINAL TRANSACTION PROPOSAL: **HOLD**

## 9. Übersichtstabelle

| Bereich | Kernaussage | Einschätzung |
|---|---|---|
| Umsatz | Q3 2026: 201,9 Mrd. USD (+12,1 %); Q2: +19,6 % | Wachstum verlangsamt sich |
| Operatives Ergebnis | 28,1 Mrd. USD (+61 %), Marge 13,9 % | Positiv |
| Nettogewinn / EPS | Q3: 20,7 Mrd. / 1,89 USD; Q2: 62,6 Mrd. (Einmaleffekte) | Gewinnqualität schwach |
| Bewertung | KGV TTM 20,8; Forward-KGV 23,5; PEG 1,15; KBV 4,5 | Fair bis leicht hoch |
| Kapex | Q3: 77,3 Mrd. USD (+120 %) | Hohes Risiko, hohes Potenzial |
| Freier Cashflow | TTM ca. –34,7 Mrd. USD; Q3 ca. –34,8 Mrd. | Negativ |
| Liquidität | Cash 55,8 Mrd. (Q1: 101,8 Mrd.); Current Ratio 0,99 | Sinkend |
| Bilanz | Bilanzsumme 1,24 Bio. USD (+71 %); Eigenkapital 613,6 Mrd. | Starke Expansion, externe Finanzierung |
| Insider | Keine Käufe; Bezos-Verkauf 346 Mio. USD (08/2026); regelmäßige Verkäufe von Jassy u. a. | Neutral bis leicht negativ |
| Kurs/Technik | 52-Wochen-Spanne 196–287 USD; 50-Tage-Schnitt 255; Beta 1,5 | Volatil |
| Empfehlung | Abwarten auf Quartalszahlen und Kapex-Klarheit | HOLD |

## II. Research Team Decision

### Bull Researcher

Bull Analyst: # Bull-Case für AMZN: Warum die Investitionsphase die Chance ist

Da der Bär noch nicht gesprochen hat, nehme ich seine wahrscheinlichsten Argumente gleich vorweg und beantworte sie.

## 1. Das Kerngeschäft wird profitabler

Der Bär wird auf das Umsatzwachstum von 12,1 % im Q3 zeigen. Entscheidend ist aber, was unterhalb der Umsatzlinie passiert:

- **Das operative Ergebnis stieg auf 28,1 Mrd. USD (Q3 2025: 17,4 Mrd.).**
- **Die operative Marge steigt jedes Quartal:** 13,1 % im Q1 2026, 13,7 % im Q2 und 13,9 % im Q3. Das ist ein Trend, kein Basiseffekt. Das Vorjahresquartal war zwar durch Sonderbelastungen gedrückt, das gebe ich zu. Aber die Abfolge Q1 bis Q3 2026 braucht diese Vergleichsbasis nicht.
- **Die Bruttomarge bleibt stabil bei etwa 53 %.** Amazon kauft sich Wachstum also nicht über Preisnachlässe.
- **Der operative Cashflow wuchs im Q3 um 19 % auf 42,4 Mrd. USD.** Die Maschine erzeugt Cash, und zwar in großem Umfang.
- **Der ROE liegt bei 27 %.** Das ist kein Unternehmen, das Kapital vernichtet.

Ein TTM-Umsatz von rund 797,5 Mrd. USD bei zweistelligem Wachstum und steigender Marge ist in dieser Größenordnung außergewöhnlich.

## 2. Die Bewertung ist vernünftig

Wir bewerten AMZN ehrlich auf Forward-Basis. Das TTM-KGV von 20,8 sieht wegen der nicht-operativen Gewinne zu günstig aus, das räume ich ein. Aber auch das Forward-KGV von **23,5** und ein **PEG von 1,15** sind für diese Marktstellung und diesen Margenpfad nicht anspruchsvoll. Der Kurs liegt bei rund 257 USD, etwa 10 % unter dem 52-Wochen-Hoch von 287 USD. Wir zahlen keinen Höchstpreis.

## 3. Der Capex ist ein Hebel, kein Leck

Der Bär wird den freien Cashflow von etwa –34,7 Mrd. USD (TTM) und den Capex von 77,3 Mrd. USD im Q3 (+120 %) ins Zentrum stellen. Dazu drei Punkte:

1. **Die Bilanz trägt das.** Das Eigenkapital liegt bei 613,6 Mrd. USD, das Debt/Equity-Verhältnis bei 0,50. Wer ein Rechenzentrums-Programm dieser Größe finanziert, tut das von einer starken Basis aus. Eine Current Ratio von 0,99 ist bei Amazon seit jeher normal und kein Alarmsignal.
2. **Das Geld fließt in Kapazität, für die Nachfrage besteht.** Der berichtete Fermi-Vorschuss eines Hyperscalers (200 Mio. USD für 600 MW) zeigt, dass Rechenleistung knapp ist. Ob Amazon der Käufer ist, ist offen. Als Branchensignal zählt es trotzdem.
3. **Amazon baut die Wertschöpfungskette selbst.** Die berichtete Decart-Transaktion (rund 7,5 Mrd. USD, Bloomberg, noch unbestätigt) zielt auf Trainium und Optimierungssoftware. Gelingt es, mehr Leistung pro Dollar aus eigenen Chips zu holen, sinkt die Abhängigkeit von Nvidia, und die AWS-Margen werden gestützt. Genau das ist der Grund, warum die steigende operative Marge und der hohe Capex zusammenpassen.

Ich gebe offen zu, dass die Daten keinen Auftragsbestand und keine AWS-Wachstumsraten enthalten. Der Beweis, dass der Capex Rendite bringt, steht also noch aus. Aber die operative Marge zeigt, dass die Investitionen bislang nicht auf die Profitabilität drücken.

## 4. Gegen den Vorwurf der schwachen Gewinnqualität

Ja, die Nettogewinne schwanken. Im Q2 standen 62,6 Mrd. USD Nettogewinn nur 27,5 Mrd. USD operativem Ergebnis gegenüber. Die Daten nennen die Ursache nicht, vermutlich sind es Beteiligungsbewertungen. Deshalb argumentiere ich ausschließlich mit dem operativen Ergebnis und dem operativen Cashflow, und beide zeigen nach oben. Wer das Q2 als Einmaleffekt abzieht, verliert nichts am Investment-Case.

## 5. Insider-Verkäufe sind Routine

Die Verkäufe folgen festen Mustern: Vesting-Termine im Februar, Mai, August und November sowie monatliche Pläne. Jassy verkauft regelmäßig 20.000 Aktien pro Quartal. Bezos' größere Bewegungen sind überwiegend Schenkungen ohne Erlös. Sein Verkauf vom August 2026 (rund 346 Mio. USD) macht etwa 0,01 % der Marktkapitalisierung von 2,78 Bio. USD aus. Wer darin ein Signal sieht, überinterpretiert Rauschen. Dass es keine Insiderkäufe gibt, ist bei einem Management mit aktienbasierter Vergütung ebenfalls normal.

## 6. Der Chart zeigt eine Basis, keinen Bruch

- Der Kurs liegt **über dem 50-SMA (255,1) und über dem steigenden 200-SMA (245,4)**, und der 50-SMA liegt über dem 200-SMA.
- Der **RSI von 49,5** ist neutral. Es gibt keine Überhitzung, die erst abgebaut werden müsste.
- Am **20.11. schloss der Kurs bei 246,82**, also an der Zone des 200-SMA, und am 23.11. liegt er vorläufig wieder bei 257. Das ist eine Erholung von rund 4 % innerhalb eines Handelstages. Dort sind Käufer eingestiegen.
- Am **04.11. sprang der Kurs von 250,69 auf 266,03** bei 93 Mio. Stück Volumen. Der Markt reagiert auf gute Nachrichten kräftig.

Das MACD-Histogramm ist kurzfristig negativ (–1,01). Das ist eine Abkühlung innerhalb einer Seitwärtsspanne, die MACD-Linie liegt weiter über null. Wer eine Spanne von 240 bis 270 mit einem Beta von 1,5 handelt, bekommt zwangsläufig solche Schwankungen. Der Schlusskurs vom 23.11. ist außerdem noch vorläufig.

## 7. Das Umfeld ist besser als die Schlagzeilen

- **Rezessionsrisiko:** Die Prognosemärkte sehen die Wahrscheinlichkeit einer US-Rezession bis Jahresende bei nur 2 % (hohes Volumen). Das stützt Konsum und Werbung, also die Basis des Handelsgeschäfts, gerade vor Black Friday und Cyber Monday.
- **Zinsen:** Eine Senkung im Dezember gilt als praktisch ausgeschlossen. Das ist längst eingepreist, und der Markt wird davon nicht mehr überrascht.
- **Sentiment:** Rund zwei Drittel von 1,4 Mio. USD Optionsprämie entfielen auf Calls. Seth Klarman hält AMZN mit 18 % seines Portfolios als größte Position. Ein Value-Investor, der kein Wachstum um jeden Preis kauft, bleibt investiert. Die Stichprobe der Social-Media-Daten ist dünn, und Reddit fehlt. Ich werte das nur als Begleitindiz.

## 8. Zu den KI-Sorgen

Die Nervosität im Sektor (Nvidia-SEC-Meldung, Anthropic-Schwäche, Alphabet-Gewinnverfehlung) ist real. Aber sie ist ein Sektorthema, kein Amazon-Thema. Alphabet wurde abgestraft, weil die Ausgaben nicht von Gewinnen gedeckt waren. Amazon dagegen liefert steigendes operatives Ergebnis, steigende Marge und wachsenden operativen Cashflow. Die Anthropic-Beteiligung ist ein Bewertungsrisiko, aber gemessen an einer Marktkapitalisierung von 2,78 Bio. USD und einem Kerngeschäft mit 28 Mrd. USD operativem Quartalsgewinn ein Randthema. Und die Chip-Strategie stärkt Amazon unabhängig davon, wie sich einzelne KI-Start-ups bewerten lassen.

## Was ich dem Bären zugestehe

- Der freie Cashflow ist negativ, die liquiden Mittel sind auf 55,8 Mrd. USD gesunken, und die Finanzierung läuft zunehmend extern.
- Das Umsatzwachstum hat sich im Q3 verlangsamt, und der Umsatz stieg gegenüber dem Q2 kaum (200,6 auf 201,9 Mrd. USD). Das müssen die nächsten Zahlen widerlegen.
- Der Decart-Deal ist unbestätigt und könnte regulatorisch geprüft werden.

Das sind aber Fragen der Ausführung, keine Schwächen der Substanz. Mein Fazit lautet: Amazon verbindet eine steigende operative Marge, einen wachsenden operativen Cashflow und eine moderate Forward-Bewertung (KGV 23,5) mit einem klar erkennbaren strategischen Plan, nämlich eigene Chips, Software und Kapazität. Der Kurs steht nach der jüngsten Korrektur auf einer intakten Trendstruktur. Für Anleger mit Geduld liegt das Chance-Risiko-Verhältnis klar auf der Seite der Käufer. Einstiege lassen sich gestaffelt vornehmen, etwa mit Blick auf den 50-SMA und die Zone um 245 bis 255 USD, mit einem Stop nach ATR (rund 1,5 × 10,4 Punkte).

Bär, ich bin gespannt: Was ist dein stärkstes Argument dafür, dass die operative Marge den Capex nicht tragen kann?

### Bear Researcher

Bear Analyst: # Bear-Case für AMZN: Die Frage ist nicht, ob Amazon gut ist, sondern was der aktuelle Preis schon verlangt

Bull, du hast mir eine direkte Frage gestellt, also bekommst du eine direkte Antwort. Danach gehe ich deine Punkte der Reihe nach durch.

## 1. Deine Frage: Warum die operative Marge den Capex nicht trägt

Die Zahlen aus dem Q3 2026:

- **Operatives Ergebnis:** 28,1 Mrd. USD
- **Operativer Cashflow:** 42,4 Mrd. USD
- **Capex:** 77,3 Mrd. USD

In einem einzigen Quartal investiert Amazon fast das Dreifache des operativen Ergebnisses und fast das Doppelte des operativen Cashflows. Über die ersten drei Quartale 2026 summiert sich der Capex auf rund 175,7 Mrd. USD (44,2 + 54,2 + 77,3). Der freie Cashflow lag bei –18,2, –8,8 und –34,8 Mrd. USD, zusammen also rund –62 Mrd. USD in neun Monaten. Der Trend verschlechtert sich, er stabilisiert sich nicht. Der TTM-Wert von –34,7 Mrd. USD wirkt nur deshalb milder, weil das nicht gelieferte Q4 2025 offenbar noch deutlich positiv war.

Der entscheidende Punkt ist die Abschreibung. Die Marge von 13,9 % spiegelt nur einen kleinen Teil dieser Investitionen. Ein Rechenbeispiel mit einer Annahme, die ich nicht aus den Daten habe: Bei einer durchschnittlichen Nutzungsdauer von etwa fünf Jahren erzeugen 100 Mrd. USD Capex rund 5 Mrd. USD zusätzliche Abschreibung pro Quartal. Das sind knapp 18 % des aktuellen Quartals-EBIT. Bei 175,7 Mrd. USD wären es rund 9 Mrd. USD pro Quartal, also etwa ein Drittel. Nicht alles davon ist schon in Betrieb, und nicht alles sind Server. Aber die Größenordnung zeigt: Die Kosten dieses Programms kommen erst noch in die Gewinn- und Verlustrechnung. Dass die Bruttomarge bei 53 % stabil bleibt, ist deshalb kein Beweis für Disziplin. Es ist ein Zeitverzug.

## 2. Der Margentrend ist schon flach geworden

Du nennst 13,1 %, 13,7 % und 13,9 % als Trend. Schau dir die Steigung an: Von Q2 auf Q3 stieg die Marge um 0,2 Prozentpunkte. Das operative Ergebnis wuchs sequenziell um nur etwa 2 % (27,5 auf 28,1 Mrd. USD). Der Umsatz legte gegenüber dem Q2 nur um 0,7 % zu (200,6 auf 201,9 Mrd. USD). Im Vorjahr lag das sequenzielle Plus von Q2 auf Q3 bei etwa 7 % (167,7 auf 180,2 Mrd. USD). Das hast du selbst als offenen Punkt eingeräumt, aber unterschätzt: Das Wachstum von +19,6 % im Q2 auf +12,1 % im Q3 ist ein Einbruch der Dynamik, und das ausgerechnet in dem Quartal, in dem der Capex um 120 % explodiert. Mehr Kapital, weniger Wachstum, das ist die falsche Richtung.

Auch der „Gewinn" von +61 % im operativen Ergebnis ist zum Teil Basiseffekt. Du gibst zu, dass Q3 2025 durch Sonderbelastungen gedrückt war. Gegenüber Q1 2025 (18,4 Mrd. USD) und Q2 2025 (19,2 Mrd. USD) lag das Plus bei etwa 30 % beziehungsweise 43 %. Das ist gut, aber weniger spektakulär als die Schlagzeile.

Beim operativen Cashflow sagst du „wächst um 19 %". Sequenziell fiel er aber von 45,4 auf 42,4 Mrd. USD. Der Cash-Motor beschleunigt nicht, er stottert, während der Capex nach oben schießt.

## 3. Du widersprichst dir bei der Gewinnqualität

Du sagst, du argumentierst ausschließlich mit operativen Größen. Zwei Absätze später zitierst du aber den **ROE von 27 %** als Beleg, dass Amazon kein Kapital vernichtet. Dieser ROE basiert auf einem TTM-Nettogewinn von 134,8 Mrd. USD, der klar über dem operativen Ergebnis liegt (Nettomarge 16,9 % gegenüber operativer Marge 13,1 %). Ein Konzern, dessen Nettomarge die operative Marge übertrifft, verdient nicht-operativ. Das ist keine Qualität, das ist Bewertungsrauschen. Dasselbe gilt für das TTM-KGV von 20,8, und das Forward-EPS von 10,93 liegt rund 12 % unter dem TTM-EPS von 12,37 USD.

Die Ursache der Q2-Zahl nennen die Daten nicht. Ich gehe wie du von Beteiligungsbewertungen aus, das ist aber eine Vermutung. Wenn es so ist, hängt ein Teil des Gewinns und des Eigenkapitals an Marktwerten wie dem von Anthropic. Die Nachrichtenlage nennt dort eine Bewertungsspanne von 50 bis 250 USD und einen Kursrutsch. Solche Gewinne können sich umkehren. Du nennst das ein „Randthema". Bei einem Eigenkapitalzuwachs von rund 62 Mrd. USD im Q3 bei nur 20,7 Mrd. USD Nettogewinn und rund 110 Mrd. USD im Q2 bei 62,6 Mrd. USD Gewinn ist es das nicht.

## 4. Die Bilanz ist weniger solide, als das Debt/Equity von 0,50 suggeriert

Du verweist auf Eigenkapital von 613,6 Mrd. USD und Debt/Equity von 0,50. Die Fundamentaldaten selbst sagen, dass diese Kennzahl den jüngsten Schuldenanstieg möglicherweise nicht abbildet. Rechnen wir selbst: Bilanzsumme minus Eigenkapital ergibt rund 630 Mrd. USD Gesamtverbindlichkeiten, also etwa das 1,0-Fache des Eigenkapitals. Vor einem Jahr waren es rund 358 Mrd. USD (727,9 minus 369,6). Die Verbindlichkeiten sind in zwölf Monaten um etwa 75 % gewachsen. Darin stecken auch Leasing und Sonstiges, aber die Richtung ist eindeutig. Gleichzeitig ist das Eigenkapital durch Posten aufgebläht, die die Daten nicht aufschlüsseln: Aktienausgabe, Vergütung oder Bewertungseffekte.

Das Finanzierungsbild passt dazu:

- **Finanzierungs-Cashflow:** +52,8, +10,1 und +48,9 Mrd. USD in drei Quartalen, zusammen rund 112 Mrd. USD frisches Kapital.
- **Liquide Mittel:** minus 45 % seit dem Q1, von 101,8 auf 55,8 Mrd. USD, und das trotz dieser Kapitalaufnahme.
- **Kurzfristige Verbindlichkeiten:** von 195,2 auf 258,0 Mrd. USD (+32 %) in einem Jahr. Die Current Ratio von 0,99 bei Amazon ist historisch „normal". Aber vor einem Jahr stand dahinter mehr Cash (66,9 Mrd. USD), und die absoluten Beträge sind jetzt deutlich größer.
- **Investitions-Cashflow im Q3:** –113,6 Mrd. USD, etwa 36 Mrd. USD mehr als der Capex. Wohin dieses Geld fließt, zeigen die Daten nicht, vermutlich in Beteiligungen oder Wertpapiere. Das ist zusätzliches Bewertungsrisiko.

Ein Unternehmen, das 112 Mrd. USD Kapital aufnimmt, dabei Cash verbrennt und im Hochzinsumfeld finanziert, ist nicht mehr der Selbstfinanzierer, den die Bullen-These voraussetzt.

## 5. Die Bewertung: „vernünftig" nur, wenn man die Lücken ignoriert

Forward-KGV 23,5 auf ein Forward-EPS, das **unter** dem TTM-EPS liegt. Das ist kein Wachstumspreis, sondern ein Preis für Gewinne, die laut Konsens schrumpfen. Das Kurs-Buchwert-Verhältnis von 4,5 steht auf einem Buchwert, der durch die oben genannten Posten aufgebläht sein könnte. Der PEG von 1,15 braucht ein Wachstum, das gerade von 19,6 % auf 12,1 % gefallen ist. Und auf Free-Cashflow-Basis ist das Papier gar nicht bewertbar, weil der FCF negativ ist. Du sagst, wir zahlen „keinen Höchstpreis". Ohne FCF und mit Beta 1,5 ist „10 % unter dem Hoch" keine Sicherheitsmarge.

Dein eigener Einstiegsvorschlag verrät dich übrigens: gestaffelt kaufen in der Zone **245 bis 255 USD**. Der Kurs steht bei rund 257 USD. Du räumst damit selbst ein, dass der aktuelle Preis nicht der attraktive ist.

## 6. Der Chart: Aus „Käufer sind eingestiegen" wird ein Muster gescheiterter Ausbrüche

- **Seitwärtsspanne seit August:** Der 50-SMA hat sich im Beobachtungsfenster nur zwischen 253,8 und 255,4 bewegt. Das ist kein Trend, das ist Stillstand. Kurs und 50-SMA liegen praktisch aufeinander (257,0 gegenüber 255,1).
- **19.11.:** Eröffnung bei 272,56, Schluss bei 257,37. Das ist ein Ausbruchsversuch über 267–270, der innerhalb eines Tages komplett abverkauft wurde, ein klassisches Umkehrmuster. Der Ausbruch scheiterte nicht zum ersten Mal.
- **20.11.:** Schluss bei 246,82 bei 74,1 Mio. Stück Volumen. Das ist hohes Verkaufsvolumen genau an der 200-SMA-Zone.
- **Deine „4 %-Erholung" am 23.11.:** Der Balken ist unvollständig (rund 20 Mio. Stück statt der üblichen 30–50 Mio.). Außerdem war die Spanne an dem Tag 251,25 bis 262,48. Bei einem ATR von 10,4 ist das normales Rauschen, kein Käufersignal. Der Schlusskurs liegt zudem unter dem 10-EMA (258,5).
- **MACD:** Signal-Crossover nach unten am 20.11., Histogramm bei –1,01, MACD-Linie von 3,50 auf 0,72 gefallen. Das ist kein „Abkühlen", das ist ein verlorenes Momentum, das sich mit nur etwas mehr Schwäche ins Negative dreht.
- **Volatilität:** Der ATR stieg von 6,19 auf 10,38 (+68 %). Die Bänder (240,4 bis 275,3) weiten sich. Bei steigender Volatilität und fallendem Momentum ist das typische Verhalten die Verteilung, nicht die Akkumulation.

Zum Chance-Risiko-Verhältnis: Fällt der Kurs unter 240, gibt es auf den gelieferten Daten keine nahe Unterstützung mehr. Die nächste Referenz wäre das 52-Wochen-Tief bei 196 USD, also rund 24 % unter dem aktuellen Kurs. Nach oben liegen 287 USD (52-Wochen-Hoch) rund 12 % entfernt, und dazwischen warten die gescheiterten Ausbruchszonen. Das ist kein asymmetrisches Verhältnis zugunsten der Käufer.

## 7. Das Umfeld ist schlechter, als du es darstellst

- **Zinsen:** Du sagst, die Dezember-Pause sei eingepreist. Das Problem ist nicht der Dezember, sondern der Horizont: 13 % für eine Senkung bis März 2027, 26 % bis April und erst bei Juli 2027 etwa 50 %, bei sehr dünnem Volumen. Ein Konzern, der rund 112 Mrd. USD in drei Quartalen extern aufnimmt, finanziert bei anhaltend hohen Zinsen, und das mit einem Beta von 1,5.
- **Rezession 2 %:** Das ist der Konsens, und was alle für fast sicher halten, ist als Positiv nur eingepreist. Es schützt vor dem Absturz, liefert aber keinen Auftrieb.
- **KI-Sektor:** Du nennst es ein „Sektorthema". Aber Alphabet wurde für hohen Capex plus Gewinnverfehlung abgestraft, und die Nachrichtenlage sagt, der Markt belohne Capex nicht mehr automatisch, sondern verlange Belege durch Cloud-Wachstum und Auftragsbestand. Du selbst räumst ein, dass die Daten **weder Auftragsbestand noch AWS-Wachstumsraten** enthalten. Damit ruht deine ganze These auf dem Beweis, der fehlt. Die Beweislast liegt bei dir, nicht bei mir.
- **Fermi-Vorschuss:** Du nutzt ihn als Nachfragesignal, räumst aber ein, dass unklar ist, ob Amazon der Käufer ist. Das ist keine Evidenz, das ist ein Stimmungsbild.
- **Decart:** 7,5 Mrd. USD für Technologie und Team, unbestätigt (Bloomberg, anonyme Quelle), mit offener behördlicher Prüfung. Selbst im Erfolgsfall ist es ein weiterer Mittelabfluss in einer Phase, in der der Markt Ausgabendisziplin sehen will. Dass Trainium bei AWS-Kunden die Margen stützt, ist eine Hoffnung, kein Datenpunkt.
- **Wettbewerb am Rand:** Walmart lässt KI-Agenten zu (Agent Gateway ab Black Friday), Amazon sperrt sie aus. Wenn Agent-Commerce der nächste Einkaufskanal wird, kann das Aussperren zum Risiko werden. Dazu kommen Preiskampf bei Lebensmitteln (die Rabatte sind laut MarketWatch nicht von Dauer), FedEx, das Amazons Logistik als Wettbewerber nennt, und Sammelklagen zu Ring und Fire TV im Frühstadium. Jedes davon ist klein, zusammen kosten sie Marge und Aufmerksamkeit.

## 8. Insider und Sentiment: kein Alarm, aber auch keine Rückendeckung

Ich bin hier fair. Die Verkäufe folgen großteils Plänen, und Bezos' Verkauf von 346 Mio. USD ist gemessen an 2,78 Bio. USD Marktkapitalisierung winzig. Aber das Argument war nie die Größe. Es geht um **Überzeugung**: Es gibt im gesamten Zeitraum seit Mai 2025 **keinen einzigen Kauf am offenen Markt**, während Bezos nahe dem 52-Wochen-Hoch bei 286,41 USD verkaufte und das Management gerade ein 220-Mrd.-USD-Programm vom Markt finanzieren lässt. Wer so viel Kapital einsetzt und glaubt, es sei zu diesen Preisen unterbewertet, könnte auch selbst kaufen.

Auch Klarman trägt die Last nicht, die du ihm gibst. Er hat bei 18 % Portfolioanteil **nicht zugekauft**. Das ist ein Halten, kein Votum. Und der Optionsfluss von 1,4 Mio. USD Prämie, davon zwei Drittel Calls, ist bei einem Handelsvolumen dieser Größenordnung Rauschen. Dem steht ein Dark-Pool-Volumen von 1,3-fachem Normalwert am 20.11. gegenüber. Die StockTwits-Basis (10 markierte Beiträge, Reddit fehlt) taugt weder für die eine noch die andere Seite.

## Was ich dir zugestehe

- Das operative Ergebnis wächst, und die Bruttomarge von etwa 53 % hält. Das Kerngeschäft ist profitabel und stark.
- Der operative Cashflow von 42,4 Mrd. USD pro Quartal ist riesig, und das Rezessionsrisiko ist gering.
- Amazon kann den Capex-Zyklus wegen seiner Größe vermutlich finanzieren. Die Frage ist, **zu welchem Preis für den Aktionär**.

## Fazit

Mein Argument ist nicht, dass Amazon ein schlechtes Unternehmen ist. Mein Argument ist, dass der Kurs von rund 257 USD eine Erfolgsgeschichte einpreist, die die Daten noch nicht belegen:

1. **Capex +120 % bei Umsatzwachstum von 19,6 % auf 12,1 %**: Die Kapitalrendite des Programms ist unbewiesen, und die Abschreibungswelle kommt noch.
2. **Negativer und sich verschlechternder FCF**, sinkende Liquidität (–45 % in zwei Quartalen), rund 112 Mrd. USD externes Kapital in drei Quartalen und Verbindlichkeiten, die in einem Jahr um rund 75 % gewachsen sind.
3. **Gewinnqualität**: Nettogewinn und ROE hängen an nicht-operativen Posten und möglicherweise an KI-Beteiligungen, deren Bewertung gerade wackelt.
4. **Bewertung** von 23,5 auf ein schrumpfendes Forward-EPS, ohne FCF-Unterstützung, bei Beta 1,5 und ohne Zinsrückenwind bis mindestens Mitte 2027.
5. **Technik**: Mehrfach gescheiterte Ausbrüche bei 267–272, bearisches MACD-Signal, Kurs unter dem 10-EMA, steigende Volatilität, und der nächste harte Boden liegt weit unten.
6. **Management und große Investoren**: Es gibt keine Insiderkäufe und keine neue Zukäufe von Klarman. Es fehlt jede Rückendeckung durch Menschen mit Insiderwissen.

Wer jetzt kauft, wettet darauf, dass die nächsten Quartalszahlen ein Umsatzwachstum über 12 %, eine weiter steigende Marge, einen plausiblen Capex-Pfad und Belege für Auftragsbestand und Trainium-Adoption liefern. Das ist möglich. Aber dann gibt es keine Eile, vor diesen Zahlen zu kaufen. Eine Enttäuschung trifft einen Titel mit Beta 1,5, dessen Abwärtsrisiko (bis 240 und darunter) größer und weniger abgesichert ist als sein Aufwärtspotenzial. Meine Haltung: nicht kaufen, bevor Capex-Rendite, FCF-Trend und Gewinnqualität belegt sind.

Bull, meine Gegenfrage: Welche Zahl in den nächsten Quartalsergebnissen müsste dich überzeugen, dass du falsch liegst, und wenn es keine gibt, ist das dann noch eine Analyse oder schon eine Überzeugung?

### Research Manager
**Recommendation**: Hold

**Rationale**: Unterm Strich hat der Bär die Debatte knapp gewonnen. Für Underweight oder Sell reicht sein Vorsprung aber nicht, weil seine Kernthese lautet: „noch nicht bewiesen“. Er sagt nicht „falsch“.

Für den Bären spricht: Im Q3 investierte Amazon 77,3 Mrd. USD Capex, dem standen 42,4 Mrd. USD operativer Cashflow und 28,1 Mrd. USD operatives Ergebnis gegenüber. Der freie Cashflow verschlechtert sich (–18,2, –8,8 und –34,8 Mrd. USD, zusammen rund –62 Mrd. USD in neun Monaten). Das Umsatzwachstum fiel von 19,6 % auf 12,1 %, sequenziell nur +0,7 %, und das im Quartal mit +120 % Capex. In drei Quartalen kamen rund 112 Mrd. USD externe Finanzierung, trotzdem sanken die liquiden Mittel um 45 %. Die Abschreibungswelle wird die stabile Marge später belasten. Der Bulle widerspricht sich, wenn er nur mit operativen Größen argumentieren will und dann ROE und TTM-KGV nennt, die an nicht-operativen Gewinnen hängen. Die Daten enthalten weder AWS-Wachstum noch Auftragsbestand, und der Markt verlangt diesen Beweis gerade (siehe Alphabet). Im Chart scheiterte am 19.11. ein Ausbruch, der MACD zeigt einen bärischen Crossover und der ATR ist um 68 % gestiegen.

Gegen Underweight spricht: Die operative Marge steigt (13,1 %, 13,7 %, 13,9 %), die Bruttomarge hält sich bei etwa 53 %, der operative Cashflow wuchs im Jahresvergleich um 19 %. Das Forward-KGV von 23,5 und der PEG von 1,15 sind moderat. Der Kurs liegt über dem 50-SMA und dem steigenden 200-SMA. Das Rezessionsrisiko liegt bei 2 %, und das Weihnachtsgeschäft steht bevor. Dass das Forward-EPS unter dem TTM-EPS liegt, ist zum Teil verzerrt, weil das TTM-EPS nicht-operative Gewinne enthält, ein echter Gewinnrückgang ist das also nicht. Insider und Sentiment sind Rauschen.

Ergebnis: Das Geschäft ist stark, aber der Preis für Neukäufe ist nicht zwingend, und das kurzfristige Chance-Risiko-Verhältnis ist neutral. Entscheidend ist der fehlende Beleg, dass sich der Capex auszahlt. Deshalb halten, aber oberhalb von 255 USD nicht aufstocken.

**Strategic Actions**: 1) Bestehende Positionen auf Standardgewicht (100 %) halten. Oberhalb von etwa 255 USD nicht aktiv aufstocken.
2) Wer untergewichtet ist, kauft höchstens bis zu 25 % einer Standardposition nach. Voraussetzung: Der Kurs hält in der Zone 245 bis 250 USD (Bereich des 200-SMA) und schließt danach wieder über dem 10-EMA (etwa 258,5 USD).
3) Risikogrenze: Bei zwei Schlusskursen unter 240 USD auf etwa 70 % des Standardgewichts reduzieren. Darunter liefern die Daten keine nahe Unterstützung, das nächste Bezugsniveau ist das 52-Wochen-Tief bei 196 USD. Stops bei Neueinstiegen bei etwa 1,5 × ATR (≈15,6 USD).
4) Upgrade auf Overweight bei mindestens zwei der folgenden Punkte in den nächsten Zahlen: Umsatzwachstum über 12 % mit sequenzieller Wiederbeschleunigung; operative Marge über 14 % trotz steigender Abschreibungen; offengelegtes beschleunigtes AWS-Wachstum oder wachsender Auftragsbestand; flacherer Capex-Ausblick bei sich verbessernder FCF-Tendenz. Alternativ ein bestätigter Tagesschluss über 272 USD bei hohem Volumen.
5) Downgrade auf Underweight bei: Umsatzwachstum unter 10 %, sinkender operativer Marge, weiter steigendem Capex bei einem FCF schlechter als –35 Mrd. USD pro Quartal oder deutlichen Abwertungen von KI-Beteiligungen (z. B. Anthropic).
6) Beobachten: Bestätigung des Decart-Deals und regulatorische Prüfung, Black Friday und Cyber Monday, Walmart-Agent-Gateway, Zinspfad bis Mitte 2027, Entwicklung von Liquidität und Schulden. Ohne AWS- und Auftragsbestandsdaten bleibt die Überzeugung bewusst neutral.

## III. Trading Team Plan

### Trader
**Action**: Hold

**Reasoning**: Der Research-Plan empfiehlt Hold. Die Fundamentaldaten sind gemischt: Die operative Marge steigt, aber Capex von 77,3 Mrd. USD, ein negativer freier Cashflow und ein langsameres Umsatzwachstum belasten. Der Chart bestätigt das neutrale Bild. Der Kurs liegt bei 257,0 zwischen 50-SMA (255,1) und 10-EMA (258,5). Der MACD hat nach unten gekreuzt, der RSI liegt bei 49,45, und Ausbrüche über 267–272 sind mehrfach gescheitert. Der 200-SMA (245,4) und das untere Bollinger-Band (240,4) bilden Unterstützung. Es gibt kein klares Chance-Risiko-Verhältnis für einen Neukauf oder Verkauf, und der Balken vom 23.11. ist noch vorläufig. Bestehende Positionen werden gehalten. Neukäufe kommen nur in Frage, wenn der Kurs an der Zone 245–250 hält und danach wieder über 258,5 schließt. Der Stop-Loss bezieht sich auf solche Neueinstiege und liegt bei 1,5 × ATR (ca. 15,6 USD) unter dem Einstieg.

**Entry Price**: 248.0

**Stop Loss**: 238.5

**Position Sizing**: Bestehende Positionen auf Standardgewicht (100 %) halten und über ca. 255 USD nicht aufstocken. Untergewichtete Anleger kaufen höchstens 25 % einer Standardposition nach, und nur bei Halt der Zone 245–250 USD plus Schluss über dem 10-EMA (ca. 258,5). Bei zwei Schlusskursen unter 240 USD auf ca. 70 % des Standardgewichts reduzieren. Wegen des ATR von 10,38 (28.10.: 6,19) die Positionsgröße eher klein wählen.

FINAL TRANSACTION PROPOSAL: **HOLD**

## IV. Risk Management Team Decision

### Aggressive Analyst

Aggressive Analyst: Ich eröffne die Runde, weil ich vermute, dass die Vorsichtigen gleich "Verkaufen" oder "lieber ganz klein bleiben" rufen werden. Mein Standpunkt: Hold ist bei AMZN keine müde Verlegenheitslösung. Es ist die aggressivste Position, die die Daten derzeit hergeben, weil sie das Kapital für den Moment aufspart, in dem das Chance-Risiko-Verhältnis wirklich kippt.

Zuerst zum Kurs. Bei 257 ist das Verhältnis tatsächlich schlecht. Mit dem Stopp bei 238,5 riskiere ich rund 18,5 Punkte, nach oben liegt der Deckel bei 267–272, wo mehrere Ausbrüche gescheitert sind, also etwa 10 bis 15 Punkte. Das ist kein Trade, den ein Aggressiver nimmt. Bei 248 sieht es anders aus. Das Risiko bis 238,5 beträgt 9,5 Punkte, der Weg bis 271 gut 23 Punkte, also etwa 2,4 zu 1. Bis zum 52-Wochen-Hoch von 287 sind es fast 39 Punkte, also über 4 zu 1. Aggressiv heißt nicht, dauernd zu kaufen. Es heißt, schlechte Preise auszulassen und bei guten Preisen groß zu sein. Dass die Zone 245–250 mit dem 200-SMA bei 245,4 zusammenfällt und das untere Bollinger-Band bei 240,4 knapp darunter liegt, ist genau die Konfluenz, auf die man warten will. Der 20.11. hat diese Zone mit einem Schluss bei 246,82 schon berührt, und zwei Handelstage später steht der Kurs wieder bei 257. Der Markt zeigt also, dass dort Käufer sitzen.

Jetzt zu dem, was die Konservativen gleich vortragen werden: negativer freier Cashflow, Capex von 77,3 Mrd. USD, sinkende Liquidität. Das stimmt, und ich bestreite es nicht. Aber schauen wir auf die andere Seite derselben Medaille. Das operative Ergebnis ist um 61 % auf 28,1 Mrd. USD gestiegen, die operative Marge liegt bei 13,9 %, die Bruttomarge ist stabil bei rund 53 %, und der operative Cashflow wächst mit 19 % weiter zweistellig. Ein Unternehmen, das seine Margen ausweitet, während es Kapazität für KI und Cloud aufbaut, verbrennt kein Geld aus Not. Es kauft sich Marktanteil in der wichtigsten Infrastrukturwelle des Jahrzehnts. Das Forward-KGV von 23,5 und ein PEG von 1,15 sind für diese Größenordnung keine Blasenbewertung. Alphabet wurde laut Nachrichtenlage für verfehlte Gewinne bestraft. Bei Amazon steigt das operative Ergebnis kräftig. Das sind zwei verschiedene Geschichten, und wer sie in einen Topf wirft, verwechselt Sektorstimmung mit Unternehmensqualität.

Das Argument, das Umsatzwachstum sei auf 12,1 % gefallen, nehme ich ernst, aber ich würde es einordnen. Q2 mit 19,6 % war ein Ausreißer nach oben, und 12 % auf einer Basis von fast 800 Mrd. USD TTM sind absolut gesehen enorm. Der entscheidende Test ist, ob das Wachstum bei den nächsten Zahlen über 12 % hält. Dort entscheidet sich die These, nicht bei einem Wochenchart.

Zu den Insidern: Keine Käufe sind kein Beweis für Pessimismus. Die Verkäufe von Jassy, Herrington und anderen folgen Vesting-Terminen und festen Plänen, und die Bezos-Schenkungen bringen gar keinen Erlös. Das ist Rauschen. Die Information steckt woanders. Klarman hält 18 % seines Portfolios in AMZN, seine größte Position, und das in einem Umfeld, in dem alle über die 220-Mrd.-Capex streiten.

Beim Sentiment sollte man ehrlich bleiben. Die Datenbasis ist dünn, Reddit fehlt, nur 10 StockTwits-Beiträge sind markiert. Der Optionsfluss ist aber auffällig. Etwa zwei Drittel von 1,4 Mio. USD Prämie gingen in Calls, während der Markt als "angeschlagen" beschrieben wird. Dazu kommt der Decart-Deal. Er ist unbestätigt, und 7,5 Mrd. USD sind viel Geld, aber er passt zur Strategie, die Abhängigkeit von Nvidia zu senken und die AWS-Margen über Trainium zu stützen. Die Makrolage ist ebenfalls nicht schlecht. Polymarket sieht die US-Rezession bis Jahresende bei 2 %, und mit Black Friday und Cyber Monday stehen die stärksten Konsumtage des Jahres vor der Tür. Ein Zinsrückenwind fehlt, aber er ist auch längst eingepreist, denn eine Dezember-Senkung liegt bei 0,8 %. Das ist keine Überraschungsquelle mehr.

Der Neutrale wird sagen, man müsse erst den Schluss über dem 10-EMA bei 258,5 sehen. Dazu zwei Punkte. Erstens lege ich den Plan so aus, dass die Bestätigung die Größe der Position bestimmt, nicht das Ob. Wer bei 248 eine erste Tranche kauft und bei einem Schluss über 258,5 aufstockt, nutzt beide Signale. Zweitens würde ich die Obergrenze von 25 % einer Standardposition für Untergewichtete eher als Untergrenze betrachten. Wenn die Zone hält und das Volumen mitspielt, wäre ich bereit, in zwei Schritten auf bis zu 50 % zu gehen, vorausgesetzt, die Gesamtrisikobudgets des Anlegers erlauben das. Mit einem Beta von 1,5 und einem ATR, der sich in vier Wochen von 6,19 auf 10,38 gesteigert hat, ist die Volatilität da. Wer von Volatilität leben will, muss sie auch mal halten können.

Ein Punkt, bei dem ich selbst kritisch bin: Der Stopp bei 238,5 liegt nur 9,5 Punkte unter dem Einstieg, also eher bei knapp einem ATR als bei den genannten 1,5 ATR. Das ist enger, als die Rechnung hergibt. Ich halte das für vertretbar, weil 238,5 knapp unter dem unteren Bollinger-Band und unter dem Tief vom 30.10. (240,35) liegt. Fällt der Kurs dort durch, ist die Spanne seit August gebrochen. Aber man sollte wissen, dass bei diesem ATR ein Stopp-Out durch normales Rauschen möglich ist. Die Antwort darauf ist, die Tranche klein zu halten und nicht den Stopp zu weiten.

Wer schon investiert ist, hält weiter, und zwar mit Überzeugung. Der Kurs steht über dem 50-SMA und dem 200-SMA, die Struktur ist formal bullisch, und gegen ein Verkaufssignal spricht, dass der RSI bei 49,45 neutral ist und nichts überverkauft oder überkauft ist. Wer hier verkauft, verkauft mitten in der Spanne, ohne Not und ohne Nachweis, dass die These bricht. Die Regel, bei zwei Schlusskursen unter 240 auf 70 % zu reduzieren, ist dafür die richtige Notbremse. Die Konservativen werden sie früher ziehen wollen, ich würde sie genau so lassen, weil früheres Aussteigen in einer Spanne mit ATR über 10 vor allem Gebühren und Whipsaws produziert.

Meine Bilanz: Die Konservativen sehen den negativen Cashflow und blenden das Margenwachstum aus. Die Neutralen verlangen Bestätigung und bezahlen dafür mit schlechteren Preisen. Hold mit klar definierten Kaufpunkten bei 245–250 und Aufstockung über 258,5 ist die Position, die Optionalität nach oben behält, ohne dass man im Mittelfeld Kapital bindet.

FINAL TRANSACTION PROPOSAL: **HOLD**

### Conservative Analyst

Conservative Analyst: Ich fange bei dem Punkt an, den der Aggressive selbst als Schwachstelle benennt und dann wegwischt: dem Stopp. Der Plan nennt 1,5 × ATR, also rund 15,6 Punkte. Der tatsächliche Stopp bei 238,5 liegt aber nur 9,5 Punkte unter dem Einstieg bei 248, das sind knapp ein ATR. Die Antwort "Tranche klein halten" ist im Kern richtig, nur zieht der Aggressive daraus den falschen Schluss. Wenn ein Stopp im normalen Rauschen liegt, ist das Chance-Risiko-Verhältnis von 2,4 zu 1 kein belastbarer Wert. Es ist ein Rechenergebnis, das erst mal eine Serie von Stopp-Outs überstehen muss. Dazu kommen die Lücken: Am 04.11. sprang der Kurs von 250,69 auf 266,03, und am 29./30.10. fiel er mit über 100 Mio. Stück Volumen auf 240,35. Bei so einem Verlauf ist ein Stopp bei 238,5 keine Garantie, sondern ein Wunsch.

Das Kursziel in seiner Rechnung ist ebenfalls fragil. Die 271 sind genau die Zone, an der Ausbrüche mehrfach gescheitert sind. Wer mit 2,4 zu 1 rechnet, setzt voraus, dass das Ziel erreicht wird, obwohl es sich als Deckel erwiesen hat. Ehrlich gewichtet sinkt das Verhältnis deutlich. Auch die Erzählung vom 20.11. gefällt mir nicht. Der Schlusskurs von 246,82 soll zeigen, dass dort Käufer sitzen. Ich lese denselben Verlauf anders: Am 19.11. eröffnete der Kurs bei 272,56 und schloss bei 257,37, eine Umkehr von 15 Punkten innerhalb eines Tages. Am 20.11. folgten 10,5 Punkte Verlust bei 74 Mio. Stück Volumen. Das ist Verkaufsdruck. Die Erholung auf 257 am 23.11. stammt aus einem noch unfertigen Balken mit nur 20 Mio. Volumen. Darauf eine These aufzubauen, nenne ich nicht Konfluenz, sondern Wunschdenken.

Bei den Fundamentaldaten zeigt der Aggressive nur die gute Hälfte. Die operative Ergebnissteigerung von 61 % ist zu einem Teil eine leichte Vergleichsbasis, denn Q3 2025 war durch Sonderbelastungen gedrückt. Die Marge von 13,9 % ist gut, aber der Umsatz wuchs nur noch um 12,1 %, nach 19,6 % im Vorquartal. Gleichzeitig wuchs der operative Cashflow um 19 %, der Capex aber um 120 %. Der freie Cashflow ist das dritte Quartal in Folge negativ und lag zuletzt bei rund minus 34,8 Mrd. USD. Die liquiden Mittel sind in zwei Quartalen von 101,8 auf 55,8 Mrd. USD gefallen, die Current Ratio liegt bei 0,99, und der Finanzierungs-Cashflow von knapp 49 Mrd. USD zeigt, dass externes Kapital die Lücke schließt. Das ist keine Not, aber es ist Abhängigkeit von offenen Kapitalmärkten, in einem Umfeld, in dem ohnehin kein Zinsrückenwind zu erwarten ist. Das nehme ich dem Aggressiven nicht ab, wenn er sagt, das sei "eingepreist". Eingepreist heißt nicht ungefährlich. Es bedeutet nur, dass keine positive Überraschung mehr kommt, während die Kosten der Refinanzierung hoch bleiben.

Zur Bewertung: Das Forward-KGV von 23,5 stützt sich auf ein Forward-EPS von 10,93 USD, und das liegt unter dem TTM-EPS von 12,37 USD. Der Markt erwartet also sinkende Gewinne je Aktie. Das PEG von 1,15 hängt an einem Wachstum, das sich gerade verlangsamt. Die Gewinnqualität habe ich noch gar nicht erwähnt: 62,6 Mrd. USD Nettogewinn im Q2 bei nur 27,5 Mrd. USD operativem Ergebnis, und das Eigenkapital stieg im Q3 um rund 62 Mrd. USD bei 20,7 Mrd. USD Gewinn. Die Daten erklären das nicht. Wahrscheinlich spielen Bewertungsgewinne auf Beteiligungen mit, das ist meine Vermutung und kein Beleg. Wenn das stimmt und die Anthropic-Bewertung, laut Nachrichtenlage mit einer Spanne von 50 bis 250 USD, weiter unter Druck gerät, kann der Effekt in die andere Richtung laufen. Das ist ein indirektes Risiko, das im Chart nicht auftaucht.

Die Insider-Argumente wischt er als Rauschen weg. Die Verkäufe sind größtenteils planmäßig, das stimmt. Trotzdem gibt es seit Mai 2025 keinen einzigen Kauf am offenen Markt, während das Management bei einem Kurs über 280 verkauft hat. Als Verkaufssignal taugt das nicht, als Bestätigung für Optimismus auch nicht. Dasselbe gilt für Klarman: Er hat die Position nicht aufgestockt, und 13F-Daten sind rückwärtsgewandt. Ein Halten ist kein Kaufsignal für uns.

Beim Optionsfluss muss man die Größenordnung sehen. 1,4 Mio. USD Prämie bei einer Marktkapitalisierung von 2,78 Billionen sind statistisches Rauschen, und der Dark-Pool-Anteil von 1,3-fachem Normalvolumen am 20.11. zeigt in die andere Richtung. Der Decart-Deal ist unbestätigt, mit 7,5 Mrd. USD teuer und genehmigungspflichtig. Alphabet wurde für hohe Ausgaben abgestraft, und der Markt belohnt Capex gerade nicht automatisch. Dass Amazons operatives Ergebnis steigt, ist ein Unterschied, aber Amazons Capex ist mit 77 Mrd. USD pro Quartal deutlich größer als die Lücke bei Alphabet. Hinzu kommen Datenlücken: Reddit fehlt, die FRED-Daten fehlen, wir kennen weder VIX noch Renditen, und der Balken vom 23.11. ist vorläufig. Auf so dünner Basis eine Aufstockung auf 50 % zu erwägen, widerspricht dem Plan, der 25 % als Obergrenze nennt. Eine Obergrenze zur Untergrenze umzudeuten, ist keine Interpretation, sondern das Umgehen der Risikodisziplin.

Mein Vorschlag, in Begriffen, die jeder auf die eigene Position anwenden kann: Halten ist vertretbar, aber nicht in unveränderter Form.

Erstens sollte, wer mehr als Standardgewicht hält, auf 100 % zurückführen und nicht aufstocken. Die Spanne gibt keinen Vorteil für Übergewichte her, bei Beta 1,5 und einem Quartalsbericht in einigen Wochen mit Lückenrisiko in beide Richtungen.

Zweitens sollte die Reduktionsregel früher greifen. Ein Schlusskurs unter dem 200-SMA bei etwa 245 sollte schon die erste Stufe sein, also Reduktion auf rund 80 %. Zwei Schlusskurse unter 240 sollten auf etwa 50 bis 60 % führen statt auf 70 %. Bei einem ATR von über 10 und mit möglichen Lücken liegt zwischen 245 und 238 bereits ein Verlust von fast 8 % vom aktuellen Kurs. Wer erst bei 240 handelt, handelt vielleicht erst bei 232.

Drittens sollten Neukäufe kleiner und später erfolgen. Ich würde nicht 25 % einer Standardposition erlauben, sondern höchstens 10 bis 15 %, und nur nach Doppelbestätigung: Halt der Zone 245–250 und danach ein Schlusskurs über 258,5, nicht eines von beiden. Der Stopp muss zum ATR passen. Entweder gilt 1,5 × ATR, dann liegt er bei etwa 232 und die Position wird entsprechend kleiner, oder der Stopp bleibt bei 238,5 und die Position wird noch kleiner. Das Dollarrisiko je Trade bleibt dasselbe, nur die Stückzahl ändert sich.

Viertens würde ich vor den Zahlen und Feiertagsdaten eine Absicherung prüfen, etwa Puts oder einen Collar, sofern die Kosten bei dieser Volatilität tragbar sind.

Der Aggressive sagt, früheres Aussteigen produziere nur Gebühren und Whipsaws. Das stimmt in einer ruhigen Spanne. Hier ist die Spanne aber nicht ruhig: Der ATR ist um zwei Drittel gestiegen, die Bänder haben sich geweitet, und das Momentum kippt nach unten. Gebühren sind kalkulierbar, ein Drawdown von 15 % mit Lücke ist es nicht. Wer Kapital schützen soll, zahlt lieber den kleinen, sicheren Preis.

FINAL TRANSACTION PROPOSAL: **HOLD**

### Neutral Analyst

Neutral Analyst: Ich fange mit dem Punkt an, bei dem beide Seiten stillschweigend am selben Problem vorbeigehen: Der Plan ist in sich nicht konsistent. Der Entry steht bei 248, aber freigegeben werden Neukäufe erst nach einem Schluss über 258,5. Wer wirklich auf beide Signale wartet, kauft nicht bei 248, sondern bei etwa 259. Dann gilt die Rechnung des Aggressiven nicht mehr. Mit einem 1,5-ATR-Stopp bei etwa 243 und einem Ziel bei 271 stehen rund 16 Punkte Risiko gegen 12 Punkte Ertrag, also deutlich unter 1 zu 1. Der Aggressive will den günstigen Preis und die Bestätigung gleichzeitig, der Konservative bekommt durch seine Doppelbestätigung ein schlechtes Verhältnis. Beides geht nicht.

Dem Aggressiven halte ich seine 2,4 zu 1 entgegen. Sie setzen den Stopp bei knapp einem ATR an und das Ziel genau dort, wo Ausbrüche mehrfach gescheitert sind. Rechnet man den Stopp ehrlich mit 1,5 ATR, also bei etwa 232, und nimmt ein realistisches Ziel bei 265 statt 271, bleiben etwa 1,1 zu 1. Das ist kein Trade, für den man Größe aufbaut. Auch die Geschichte vom 20.11. als Beweis für Käufer trägt nur halb. Ein Schluss bei 246,82 mit 74 Mio. Stück Volumen ist ebenso Verkaufsdruck, und die Erholung stammt aus einem noch unfertigen Balken. Die Aufstockung von 25 auf 50 % lehne ich ab. Der Plan nennt 25 % ausdrücklich als Obergrenze, und bei Beta 1,5, ATR über 10 und fehlenden Makrodaten gibt die Datenlage keinen Grund, sie zu verdoppeln. Seine Abgrenzung zu Alphabet ist ebenfalls zu bequem. Amazon hat zwar steigende operative Gewinne, aber auch einen TTM-Free-Cashflow von rund minus 35 Mrd. USD. Ob der Markt das bestraft, entscheidet sich an der Cloud-Rendite des Capex, nicht an der Marge allein. Die Call-Prämie von 1,4 Mio. USD ist bei 2,8 Billionen Marktkapitalisierung kaum ein Signal.

Der Konservative überzieht an anderer Stelle. Er schließt aus dem Forward-EPS unter dem TTM-EPS, der Markt erwarte sinkende Gewinne, und erklärt zwei Absätze später selbst, das TTM-EPS sei durch Beteiligungsgewinne aufgebläht. Beides zusammen geht nicht. Der Rückgang ist größtenteils ein Basiseffekt und kein Gewinnrückgang. Die operative Linie ist ordentlich: 23,9, 27,5 und 28,1 Mrd. USD in den letzten drei Quartalen. Allerdings hat sich der sequenzielle Zuwachs auf etwa 2 % verlangsamt, und der Umsatz stieg gegenüber Q2 nur um rund 0,7 %. Das ist die berechtigte Sorge, aber sie ist kein Alarm. Der operative Cashflow von 42 Mrd. USD pro Quartal und eine Verschuldung von 0,5x Eigenkapital sind keine Notlage. Der Finanzierungsbedarf ist ein Risiko, aber keines, das in den nächsten Wochen zuschlägt. Zur Zeitachse: Er spricht von einem Quartalsbericht in einigen Wochen. Der letzte Bericht fiel nach dem Muster der Kursspitzen auf Ende Oktober und Anfang November. Der nächste liegt damit nach üblichem Rhythmus eher Ende Januar oder Anfang Februar. Das nahe Ereignisrisiko sind Black Friday, Cyber Monday, die Decart-Bestätigung und die Nachrichten zu Nvidia und Anthropic, und das ist weniger dramatisch als ein Gap-Risiko durch Zahlen. Eine Reduktion auf 80 % schon beim ersten Schluss unter 245 halte ich für zu eng. Der 200-SMA liegt bei 245,4 und der Kurs schloss am 20.11. bei 246,82, also gerade mal 1,4 Punkte darüber. Bei einem ATR von 10 löst normales Rauschen diese Regel aus, und man verkauft dann genau in der Spanne, vor der der Konservative warnt. Eine Reduktion auf 50 bis 60 % bei zwei Schlüssen unter 240 würde in einem möglichen Fehlausbruch den Großteil der Position kosten. Neukäufe von höchstens 10 bis 15 % sind bei diesem Risiko ein Rundungsfehler. Und Puts oder Collars kenne ich nur als Idee, denn zur impliziten Volatilität liegen keine Daten vor. Das ist eher etwas für stark konzentrierte Positionen als eine allgemeine Regel.

Mein Vorschlag, den jeder auf die eigene Position übertragen kann: Bestehende Positionen werden gehalten. Wer deutlich über Standardgewicht liegt, führt sie schrittweise auf 100 % zurück. Wer darüber liegt, weil das so geplant war, muss nicht zwingend verkaufen. Bei Beta 1,5 und fehlender Spanne nach oben gibt es aber keinen Grund, noch mehr zu wollen.

Für Neukäufe sollte man sich entscheiden, statt beide Bedingungen zu stapeln. Variante eins ist ein kleiner Einstieg in der Zone 245 bis 250 mit etwa 15 bis 20 % einer Standardposition. Wichtig ist, die Stückzahl am Dollarrisiko auszurichten und nicht am Stopp. Mit einem Stopp bei etwa 232, also 1,5 ATR, sind das rund 40 % weniger Stück als mit einem Stopp bei 238,5. Wer 238,5 behält, nimmt dafür eine höhere Chance auf einen Stopp durch Rauschen in Kauf und sollte die Tranche noch kleiner wählen. Eine zweite Tranche von höchstens 10 % kommt erst nach einem Schluss über 267 bis 272 mit positivem MACD-Histogramm. Der Schluss über 258,5 allein ist mitten in der Spanne zu wenig, denn er bestätigt nur, dass der Kurs wieder über dem 10-EMA liegt.

Bei den Reduktionen würde ich eine gestaffelte Leiter nehmen. Zwei Schlusskurse unter 245 bringen etwa 90 %. Zwei Schlusskurse unter 240 bringen etwa 70 %, also die Regel des Plans. Ein Schluss unter etwa 232 bringt etwa 50 %. Damit hat man die frühere Vorsicht der Konservativen, ohne bei jedem Ausschlag um den 200-SMA zu handeln.

Zwei Datenpunkte sollte man vorher prüfen, bevor man sich auf Zahlen verlässt. Der Balken vom 23.11. ist vorläufig, daher gelten alle Signale erst nach dem Schlusskurs. Und die genannten 220 Mrd. USD Capex passen nicht gut zu den knapp 176 Mrd. USD in neun Monaten bei steigendem Trend. Entweder ist die Zahl veraltet oder anders abgegrenzt. Beides ändert das Bild beim Free Cashflow.

Hold ist also richtig, aber mit einem konsistenten Kaufplan, einer weniger hektischen Verkaufsleiter und einem Stopp, der zur Volatilität passt.

FINAL TRANSACTION PROPOSAL: **HOLD**

## V. Portfolio Manager Decision

### Portfolio Manager
**Rating**: Hold

**Executive Summary**: AMZN halten: Bestehende Positionen bleiben auf Standardgewicht (100 %). Wer übergewichtet ist, führt schrittweise auf 100 % zurück, oberhalb von etwa 255 USD wird nicht aufgestockt. Untergewichtete kaufen höchstens 15–20 % einer Standardposition in der Zone 245–250 USD. Die Stückzahl richtet sich nach dem Dollarrisiko bei einem Stopp nach 1,5 × ATR (≈232 USD). Eine zweite Tranche von höchstens 10 % gibt es erst nach einem Schluss über 267–272 USD. Absicherung nach Stufen: zwei Schlüsse unter 245 USD → ca. 90 %, zwei Schlüsse unter 240 USD → ca. 70 %, ein Schluss unter 232 USD → ca. 50 %. Horizont bis zu den Q4-Zahlen (voraussichtlich Ende Januar/Anfang Februar).

**Investment Thesis**: Alle drei Analysten kommen auf Hold. Das allein ist kein Grund, sondern das Ergebnis der Abwägung, denn die Belege für beide Seiten wiegen etwa gleich schwer. Für AMZN spricht: Die operative Marge steigt (13,1 %, 13,7 %, 13,9 %), die Bruttomarge liegt stabil bei ~53 %, der operative Cashflow wächst um 19 % zum Vorjahr, das Forward-KGV ist mit 23,5 moderat (PEG 1,15), und der Kurs liegt über dem 50-SMA und dem steigenden 200-SMA. Dagegen spricht: Der Capex stieg im Q3 um 120 % auf 77,3 Mrd. USD, der FCF war drei Quartale negativ (zuletzt ~–34,8 Mrd. USD), die liquiden Mittel fielen von 101,8 auf 55,8 Mrd. USD, und das Umsatzwachstum verlangsamte sich auf 12,1 % bei nur +0,7 % zum Vorquartal. Belege, dass sich die Investitionen auszahlen (AWS-Wachstum, Auftragsbestand), fehlen in den Daten. Charttechnisch: Am 19.11. scheiterte ein Ausbruch (Eröffnung 272,56, Schluss 257,37), der MACD hat nach unten gekreuzt, und der ATR stieg von 6,19 auf 10,38. Der Bulle hat ein gutes Geschäftsmodell auf seiner Seite, der Bär einen unbewiesenen Capex-Return. Für Under- oder Overweight reicht das in keine Richtung.

Zur Umsetzung liefert der Neutrale die stärksten Argumente. Er zeigt, dass der Trader-Plan in sich nicht stimmig ist: Einstieg bei 248, aber Freigabe erst über 258,5. Bei Doppelbestätigung fällt das Chance-Risiko-Verhältnis unter 1:1. Die 2,4:1 des Aggressiven beruhen auf einem Stopp von knapp 1 ATR (238,5) und einem Ziel genau am mehrfach bestätigten Deckel bei 271. Rechnet man mit 1,5 ATR (~232) und realistisch 265, bleiben ~1,1:1. Deshalb wird die Ausweitung auf 50 % abgelehnt, die 25-%-Grenze ist eine Obergrenze. Den Konservativen widerlegt der Neutrale an zwei Stellen. Erstens ist das Forward-EPS unter dem TTM-EPS weitgehend ein Basiseffekt aus nicht-operativen Gewinnen. Zweitens würde eine Reduktion schon beim ersten Schluss unter 245 bei einem ATR über 10 durch bloßes Rauschen ausgelöst (Schluss am 20.11.: 246,82). Berechtigt bleibt seine Mahnung zur Größenbestimmung über das Dollarrisiko, ebenso der Hinweis auf Gap-Risiken (04.11.: 250,69→266,03) und auf die Abhängigkeit vom Kapitalmarkt (Current Ratio 0,99, ~49 Mrd. USD Finanzierungs-Cashflow). Deshalb wird die Reduktion gestaffelt, mit einer dritten Stufe bei 232.

Datenlücken: Es fehlen AWS- und Auftragsbestandsdaten, VIX, Renditen (FRED), Reddit-Sentiment und Daten zur impliziten Volatilität für Absicherungen. Der Balken vom 23.11. ist vorläufig, und die genannten 220 Mrd. USD Capex passen nicht sauber zu den ~176 Mrd. USD aus neun Monaten. Signale gelten deshalb nur auf Schlusskursbasis.

Upgrade auf Overweight, wenn mindestens zwei Bedingungen erfüllt sind: Umsatzwachstum über 12 % mit sequenzieller Beschleunigung; operative Marge über 14 % trotz steigender Abschreibungen; offengelegte AWS-Beschleunigung oder wachsender Auftragsbestand; flacherer Capex bei besserem FCF. Alternativ ein bestätigter Schluss über 272 USD bei hohem Volumen. Downgrade auf Underweight bei: Umsatzwachstum unter 10 %, sinkender operativer Marge, FCF schlechter als –35 Mrd. USD pro Quartal bei weiter steigendem Capex, deutlichen Abwertungen von KI-Beteiligungen (Anthropic) oder einem nachhaltigen Bruch unter 232 USD.

**Price Target**: 271.0

**Time Horizon**: 2-3 Monate (bis zu den Q4-Zahlen Ende Januar/Anfang Februar)