# MSFT: Technische Analyse (Stand 23.11.2026)

## 1. Datengrundlage und Hinweis zu Abweichungen
- Alle exakten Werte stammen aus dem **verifizierten Snapshot** vom 23.11.2026. Der letzte Schlusskurs ist **499,27**, die Tageshandelsspanne liegt bei 499,00–509,15.
- **Abweichung:** Die Rohdaten von `get_stock_data` zeigen für den 23.11. einen Schlusskurs von 499,25 und ein Volumen von 8.860.335. Der Snapshot nennt 499,27 und 8.860.546. Die Differenz ist minimal. Der Handelstag ist mit nur rund 8,9 Mio. Stück offenbar noch nicht abgeschlossen. Ich verwende die Snapshot-Werte und stelle keinen "bereinigten" Wert auf.
- Das Tagesvolumen ist unvollständig und deshalb für Volumenschlüsse nicht belastbar.

## 2. Gewählte Indikatoren (8, komplementär)
| Kategorie | Indikator | Begründung |
|---|---|---|
| Trend lang | close_200_sma | Strategische Trendbasis |
| Trend mittel | close_50_sma | Dynamische Unterstützung/Widerstand mittelfristig |
| Trend kurz | close_10_ema | Schnelle Momentumwechsel |
| Momentum | macd (inkl. Signal/Histogramm aus Snapshot) | Trendwechsel, Crossover |
| Momentum | rsi | Überkauft/überverkauft, Divergenzen |
| Volatilität | boll (plus Ober-/Unterband aus Snapshot) | Relative Preislage, Bandbreite |
| Volatilität | atr | Stop-Distanz, Positionsgröße |
| Volumen | vwma | Volumengewichtete Trendbestätigung |

Die Auswahl deckt kurz-, mittel- und langfristigen Trend, Momentum, Volatilität und Volumen ab. Sie ist weitgehend redundanzfrei. Nur MACD, Signal und Histogramm gehören zur selben Familie.

## 3. Kursverlauf im Kontext (aus den OHLCV-Daten)
- **Schwache Phase Nov. 2025 – Juni 2026:** Der Kurs fiel von rund 512 (3.11.2025) auf das Zwischentief bei **351,49** (Schlusskurs 25.06.2026). Der 29.01.2026 war ein Ausverkaufstag mit etwa 128,9 Mio. Stück und einem Schlusskurs von 429,94 nach 477,67 am Vortag.
- **Starke Erholung ab Ende Juli 2026:** Am 30.07.2026 sprang der Kurs von 389,06 auf 449,38, bei etwa 110,2 Mio. Stück. Bis 10.08. folgte ein Anstieg auf 504,14. Die Daten liefern keinen Grund für den Sprung. Ich behaupte keinen.
- **Aufwärtstrend bis Oktober:** Der Kurs stieg von rund 500 (Anfang September) auf einen Schlusskurs von **542,40** (13.10.2026).
- **Jüngster Schlusskurshöchststand:** **554,73** am 04.11.2026 bei rund 50,8 Mio. Stück. Der Kurs gab am Folgetag aber direkt nach (534,90). Tageshoch war 558,07, danach folgte eine Umkehr.
- **Seitdem Korrektur:** Von 554,73 auf 499,27 sind das rund **10 %**. Der 20.11. schloss bei 484,52, bei einem Tagestief von 481,03 und rund 47,1 Mio. Stück. Am 23.11. gibt es bisher eine Erholung (Eröffnung 506,06, Schluss 499,27).

## 4. Indikatorbefunde (Snapshot-Werte)

### Trend
- **200 SMA: 442,43.** Der Kurs liegt rund 12,9 % darüber. Die Reihe der letzten 30 Tage steigt stetig (434,8 am 26.10. auf 442,4). Der langfristige Trend bleibt intakt.
- **50 SMA: 518,77.** Der Kurs liegt rund 3,8 % darunter. Der Durchschnitt steigt weiter leicht (508,1 am 26.10. auf 518,8), flacht aber ab (519,08 am 19.11. gegenüber 518,77 heute). Der Kurs hat ihn zuletzt verloren. Er wird jetzt zu einem Widerstandsbereich, bis ein Rückeroberung gelingt.
- **10 EMA: 507,93.** Der Kurs liegt darunter. Die EMA fällt seit dem 9.11. (532,4) kontinuierlich. Das Kurzfristmomentum ist abwärts gerichtet.
- **VWMA (20): 522,94.** Sie liegt über dem Kurs und über dem Bollinger-Mittelband. Das bedeutet, dass Umsätze der letzten Wochen im Schnitt bei höheren Kursen stattfanden. Der aktuelle Preis liegt unter dem volumengewichteten Durchschnitt, was auf einen Verkaufsdruck mit Volumen hindeutet (Verteilungscharakter in der Korrektur, 20.11. mit 47,1 Mio. Stück).

**Struktur:** Preis (499,27) < 10 EMA (507,93) < 50 SMA (518,77) bei gleichzeitig Preis > 200 SMA (442,43). Das ist ein Rücksetzer innerhalb eines übergeordneten Aufwärtstrends, kein Trendbruch.

### Momentum
- **MACD: -6,48; Signal: -1,88; Histogramm: -4,60.** Der MACD ist zwischen dem 16.11. (+1,01) und dem 17.11. (-0,73) unter die Nulllinie gefallen und hat sich seither weiter nach unten bewegt (-5,89 am 20.11.). Das Histogramm ist negativ und wird größer. Das Momentum ist klar bärisch. Ein Bullish Crossover ist noch nicht in Sicht.
- **RSI: 42,59.** Am 20.11. lag er bei 35,02, dem tiefsten Wert der betrachteten 30 Tage. Das ist knapp über der Überverkauft-Marke von 30, aber nicht darunter. Der aktuelle Anstieg auf 42,6 ist eine Entspannung, noch keine Trendwende. Der RSI-Höchstwert in der Periode war 64,33 (4.11.), bei einem Kurshoch. Eine Divergenz lässt sich daraus nicht ableiten.

### Volatilität
- **Bollinger:** Mittelband 520,43, Oberband 552,94, Unterband 487,91. Der Kurs liegt im unteren Drittel der Bänder, aber über dem Unterband (rund 11 Punkte Abstand). Das Mittelband fällt (530,6 am 5.11. auf 520,4). Es fungiert zusammen mit der 50 SMA als Widerstandszone um 518–523.
- **ATR: 16,97.** Er ist von 10,78 (28.10.) deutlich gestiegen. Die Volatilität hat sich seit Anfang November um rund 57 % erhöht. Das entspricht den großen Tagesbewegungen (4.11., 5.11., 19.–20.11.).

## 5. Einordnung und Szenarien
**Basisszenario (leicht bärisch kurzfristig / neutral mittelfristig):** Alle kurzfristigen Signale (10 EMA, MACD, Histogramm, VWMA, Kurs unter 50 SMA) zeigen nach unten. Der Langfristtrend (200 SMA) ist intakt. Die Korrektur von rund 10 % passt zu einem Rücksetzer nach starker Rallye (von 351 im Juni auf 554 im November), aber die Dynamik ist noch nicht gedreht.

**Beobachtungsmarken (nur aus den Daten abgeleitet):**
- **Unterstützung:** Der Schlusskurs-Tiefpunkt vom 20.11. bei 484,52 und das Tagestief bei 481,03. Das aktuelle Bollinger-Unterband liegt bei 487,91. Ein Schluss unter ca. 481 würde das Korrekturszenario ausweiten. Die 200 SMA bei 442,43 ist die nächste strukturelle Marke. Ich behaupte dabei keine historischen Reaktionen auf diese Marken, da die Daten keine belegen.
- **Widerstand:** 10 EMA bei 507,93, dann der Bereich 518–523 (50 SMA 518,77, Bollinger-Mitte 520,43, VWMA 522,94). Erst ein Schluss über diesen Zone würde das Bild verbessern.
- **Bullisches Signal:** MACD-Histogramm dreht nach oben und RSI steigt über 50, zusammen mit einem Schluss über der 50 SMA.
- **Bärisches Signal:** Neues Schlusstief unter 484,52 mit hohem Volumen, RSI unter 30.

**Risikomanagement:** Bei einem ATR von 16,97 entspricht ein Stop von 1,5 × ATR rund 25,5 Punkten und 2 × ATR rund 33,9 Punkten. Die Positionsgröße sollte wegen der gestiegenen Volatilität kleiner gewählt werden. Tagesbewegungen von 10–20 Punkten sind derzeit normal.

## 6. Grenzen
- Das heutige Volumen ist unvollständig.
- Die Indikatoren sind rückwärtsgerichtet. Es gibt keine Informationen zu Fundamentaldaten oder Nachrichten (die Kurssprünge am 29.01., 30.07. und 04.11. sind in den Daten nicht erklärt).
- Es gibt keine belegten historischen Bounces an den genannten Marken. Sie sind reine Orientierungspunkte.

## 7. Zusammenfassung
| Punkt | Wert / Befund | Bewertung |
|---|---|---|
| Schlusskurs 23.11.2026 | 499,27 (Rohdaten: 499,25, Volumen unvollständig) | Tag noch nicht abgeschlossen |
| 200 SMA | 442,43 (steigend) | Langfristtrend bullisch |
| 50 SMA | 518,77 (leicht steigend, flacht ab) | Kurs ca. 3,8 % darunter, Widerstand |
| 10 EMA | 507,93 (fallend) | Kurzfristig bärisch |
| MACD / Signal / Hist. | -6,48 / -1,88 / -4,60 | Bärisches Momentum, unter Null seit 17.11. |
| RSI | 42,59 (Tief 35,02 am 20.11.) | Schwach, nicht überverkauft |
| Bollinger (Mitte/Ober/Unter) | 520,43 / 552,94 / 487,91 | Kurs im unteren Bandbereich |
| ATR | 16,97 (von 10,78 am 28.10.) | Volatilität deutlich erhöht |
| VWMA | 522,94 | Kurs unter volumengewichtetem Schnitt |
| Schlusskurshoch / Korrektur | 554,73 (04.11.) / rund -10 % | Rücksetzer im Aufwärtstrend |
| Wichtige Unterstützung | 484,52 (Schluss 20.11.), 481,03 (Tief), 487,91 (Unterband), 442,43 (200 SMA) | Beobachten |
| Wichtiger Widerstand | 507,93, dann 518–523 | Erholung muss diese Zone überwinden |
| Stop-Orientierung | 1,5–2 × ATR = ca. 25–34 Punkte | Kleinere Positionsgröße |

Gesamtbild: Kurzfristig schwach, mittel- bis langfristig intakt. Ein neuer Einstieg ist aus technischer Sicht erst bei einer Stabilisierung (Histogramm dreht, Kurs über der 10 EMA und später der 50 SMA) sinnvoll. Bestehende Positionen sind mit ATR-basierten Stops zu halten.

FINAL TRANSACTION PROPOSAL: **HOLD**