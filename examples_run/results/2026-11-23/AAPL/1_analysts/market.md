# AAPL – Technische Analyse (Stand: 23.11.2026)

## 1. Datenbasis und Hinweise
- Alle exakten Kurs- und Indikatorwerte stammen aus dem verifizierten Snapshot vom 23.11.2026. Die Werte für VWMA, RSI, MACD-Histogramm und ATR habe ich zusätzlich über `get_indicators` abgerufen. Sie stimmen mit dem Snapshot überein.
- **Kleine Abweichung:** Die Kursreihe nennt für den 23.11. einen Schlusskurs von 350,91, der Snapshot 350,895. Das Volumen liegt bei etwa 14,98 Mio. (14.983.576 gegenüber 14.984.524). Ich verwende die Snapshot-Werte.
- **Die Tageskerze vom 23.11. ist sehr wahrscheinlich noch nicht abgeschlossen.** Das Volumen von rund 15 Mio. ist deutlich niedriger als an den Vortagen, an denen es meist 30–50 Mio. waren. Der Schlusskurs ist daher eher ein aktueller Stand, und die Indikatorwerte können sich bis zum Handelsschluss noch ändern.

## 2. Gewählte Indikatoren und Begründung
Ich habe acht Indikatoren gewählt, die sich möglichst wenig überschneiden:

| Kategorie | Indikator | Zweck |
|---|---|---|
| Trend (lang) | close_200_sma | Strategische Trendbasis |
| Trend (mittel) | close_50_sma | Mittelfristiger Trend, dynamische Unterstützung |
| Trend (kurz) | close_10_ema | Kurzfristiges Momentum und Timing |
| Momentum | macd / macds / macdh | Trendwechsel und Momentumstärke |
| Momentum | rsi | Überkauft/überverkauft, Divergenzen |
| Volatilität | boll, boll_ub, boll_lb | Preisband und Ausbruchszonen |
| Volatilität | atr | Stop-Abstände und Positionsgröße |
| Volumen | vwma | Bestätigung des Trends durch Volumen |

Ich habe nicht jeden Indikator einzeln abgerufen. Moving Averages, MACD-Linie, Signal und Bollinger-Bänder stammen aus dem verifizierten Snapshot.

## 3. Trendstruktur
**Langfristig: klar bullisch.**
- Der Schlusskurs von 350,895 liegt deutlich über dem 200-Tage-SMA (303,154), also rund 15–16 % darüber.
- Er liegt auch über dem 50-Tage-SMA (341,946).
- Die Reihenfolge Kurs > 10-EMA (349,464) > 50-SMA > 200-SMA bestätigt eine intakte, geordnete Aufwärtsstruktur.
- Im Datensatz stieg AAPL von etwa 279 (Schlusskurs 01.05.2026) auf etwa 351. Der höchste Schlusskurs im abgerufenen Zeitraum war 356,27 am 13.11.2026. Das Intraday-Hoch an diesem Tag lag bei 360,83.

**Mittelfristig: Aufwärtstrend mit Rücksetzern.**
- Es gab zwei deutliche Einbrüche mit hohem Volumen:
  - Am 25./26.06. fiel der Kurs auf 274,704, bei 107 Mio. und 262 Mio. Stück Volumen. Er erholte sich danach schnell.
  - Am 31.07. fiel der Kurs von 332,89 auf 308,409, bei 132 Mio. Stück Volumen.
- Beide Rücksetzer wurden im weiteren Verlauf wieder aufgeholt. Der Kurs notiert inzwischen über den damaligen Hochs. Das spricht für Nachfrage auf tieferen Niveaus. Es ist aber keine Garantie für künftige Rücksetzer.
- Seit Mitte Oktober bewegt sich der Kurs überwiegend zwischen etwa 331 und 356 (Schlusskurse). Das ist eine Konsolidierung auf hohem Niveau, mit leicht steigenden Hochs.

## 4. Momentum
- **RSI: 54,22.** Das ist neutral. Der RSI war zuletzt bei 60,9 (13.11.) und fiel am 20.11. auf 46,59, nachdem der Kurs auf 342,56 gefallen war. Er hat sich mit der Erholung wieder über 50 gebracht. Es gibt keine Überkauft- oder Überverkauft-Signale. Es gibt auch keine bärische Divergenz, denn der RSI erreichte beim Kurshoch im November nur etwa 61 und lag Ende Oktober ähnlich hoch (61,4).
- **MACD:** Die MACD-Linie liegt bei 2,696 und die Signallinie bei 3,322. Das Histogramm ist mit −0,626 negativ.
  - Das Histogramm drehte am 19.11. ins Negative (−0,05) und erreichte am 20.11. −0,736. Heute ist es mit −0,626 leicht weniger negativ.
  - Das ist ein kurzfristiges Abkühlen des Momentums innerhalb eines positiven MACD-Niveaus (MACD-Linie über null). Es ist noch kein klares Verkaufssignal.
  - Ein erneuter Aufwärtskreuz von MACD über die Signallinie wäre ein erstes Zeichen für neues Aufwärtsmomentum.

## 5. Volatilität und Bänder
- **Bollinger:** Das Mittelband liegt bei 347,669, das obere Band bei 359,708 und das untere bei 335,63. Der Kurs liegt knapp über dem Mittelband, also in der oberen Bandhälfte, aber nicht am Rand. Das Hoch vom 13.11. (360,83 intraday) lag leicht über dem damaligen oberen Band-Bereich. Der anschließende Rückgang passt zu einer Mean-Reversion zur Mitte.
- **ATR: 8,31.** Das sind etwa 2,4 % des Kurses. Die Volatilität ist seit Ende Oktober gestiegen (ATR 6,16 am 28.10., Spitze 8,86 am 05.11.). Sie ist auf hohem Niveau stabil. Die Ausschläge um die Quartalszahlen-Phase (03./04.11.: 331,648 → 349,245 bei knapp 90 Mio. Stück) sind darin enthalten.
- Der Handelsbereich ist also breiter als im Oktober. Enge Stops werden schneller ausgelöst.

## 6. Volumen
- Der VWMA liegt bei 349,767 und damit leicht unter dem Kurs (350,895). Er ist seit Ende Oktober stetig gestiegen (342,25 am 26.10.). Das bestätigt, dass der Anstieg durch Volumen getragen wurde.
- Am 20.11. fiel der Kurs auf 342,56 bei rund 80 Mio. Stück Volumen, mit einem Tagestief von 340,56. Das war erhöhter Verkaufsdruck, der aber heute (bei bisher geringem Volumen) teilweise ausgeglichen wird. Eine Bewertung der heutigen Erholung ist erst nach dem Handelsschluss belastbar.

## 7. Szenarien und konkrete Marken
Diese Marken leiten sich aus den Indikatorwerten und den Kursdaten oben ab. Ich behaupte nicht, dass sie in der Vergangenheit als Unterstützung oder Widerstand gehalten haben.

- **Bullisch:** Ein Schlusskurs über 356,27 (Schlusshoch vom 13.11.) und später über dem oberen Bollinger-Band (ca. 359,7) würde den Aufwärtstrend bestätigen. Zusätzlich sollte das MACD-Histogramm wieder positiv werden.
- **Neutral/Seitwärts:** Der Bereich zwischen dem Mittelband (ca. 347,7)/10-EMA (ca. 349,5) und dem oberen Band ist die wahrscheinlichste Spanne, solange das Histogramm um null pendelt.
- **Bärisch:** Ein Schlusskurs unter dem unteren Band (ca. 335,6) oder dem 50-SMA (ca. 341,9) würde die Konsolidierung in eine Korrektur verwandeln. Das Tagestief vom 20.11. liegt bei 340,56 und das Tief vom 03.11. bei 325,083 (Intraday). Das Schlussniveau vom 03.11. (331,648) wäre ein nächster Prüfstein.
- **Risikomanagement:** Bei einem ATR von 8,31 entspricht ein Stop von etwa 1,5–2 ATR einem Abstand von rund 12–17 Punkten. Ein Stop unter dem 50-SMA liegt in dieser Größenordnung, etwa 9 Punkte unter dem aktuellen Kurs.

## 8. Fazit
Der übergeordnete Trend ist klar bullisch: Der Kurs liegt über allen wichtigen Durchschnitten und der VWMA bestätigt ihn. Kurzfristig fehlt ein frischer Impuls. Der RSI ist neutral, das MACD-Histogramm ist leicht negativ, und die Volatilität ist erhöht. Der Kurs liegt knapp unter dem Hoch vom 13.11. Die heutige Kerze ist noch nicht abgeschlossen.

Für Trendfolger spricht das für Halten bestehender Positionen. Neue Käufe sind erst bei einem Ausbruch über rund 356–360 oder bei einem Rücksetzer in Richtung 50-SMA/unteres Band mit Stabilisierung attraktiver. Das ist keine Anlageberatung. Die Entscheidung trifft der nachgelagerte Agent.

## 9. Übersicht

| Punkt | Wert / Befund | Einschätzung |
|---|---|---|
| Schlusskurs (Snapshot, 23.11.) | 350,895 (Tageskerze noch unvollständig) | Vorläufig |
| 10-EMA | 349,464 | Kurs leicht darüber, kurzfristig positiv |
| 50-SMA | 341,946 | Kurs darüber, mittelfristig bullisch |
| 200-SMA | 303,154 | Kurs deutlich darüber, langfristig bullisch |
| RSI | 54,22 | Neutral, keine Extreme |
| MACD / Signal | 2,696 / 3,322 | Positives Niveau, MACD unter Signal |
| MACD-Histogramm | −0,626 | Momentum kühlt kurzfristig ab |
| Bollinger (unten/Mitte/oben) | 335,63 / 347,669 / 359,708 | Kurs in der oberen Bandhälfte |
| ATR | 8,31 (ca. 2,4 % des Kurses) | Erhöhte Volatilität, Stops großzügig setzen |
| VWMA | 349,767 | Volumen bestätigt den Aufwärtstrend |
| Wichtige Kursmarken | Schlusshoch 356,27 (13.11.), Tagestief 340,56 (20.11.) | Ausbruchs- bzw. Warnmarken |
| Datenabweichung | Schlusskurs 350,91 (Kursreihe) gegenüber 350,895 (Snapshot) | Snapshot gilt |
| Gesamtbild | Langfristiger Aufwärtstrend, kurzfristig Konsolidierung | Abwarten / Halten |

FINAL TRANSACTION PROPOSAL: **HOLD**