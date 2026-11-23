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