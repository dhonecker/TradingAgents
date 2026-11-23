# GOOGL: technische Analyse (Stand 23.11.2026)

## 1. Datengrundlage und Hinweise
- Alle exakten Kurs- und Indikatorwerte stammen aus dem **verifizierten Snapshot** vom 23.11.2026. Die Zusatzabfragen zu VWMA und ATR passen dazu. ATR 11,8858 stimmt überein, und ein Widerspruch zwischen den Quellen besteht nicht.
- Die Zeile vom 23.11. zeigt ein Volumen von 16,17 Mio. Stück. Das liegt deutlich unter den üblichen 20–35 Mio. der letzten Wochen. Ob die Handelssitzung vollständig erfasst ist, lässt sich aus den Daten nicht ablesen. Schlusskurs und Tagesindikatoren sollten deshalb mit Vorsicht gelesen werden.
- Über `get_indicators` habe ich nur VWMA und ATR einzeln abgefragt. Die übrigen Werte (EMA, SMA, MACD, RSI, Bollinger) stammen aus dem verifizierten Snapshot.

## 2. Gewählte Indikatoren (8) und Begründung
| Indikator | Rolle im aktuellen Kontext |
|---|---|
| close_200_sma | Langfristiger Trendrahmen. Der Kurs liegt klar darunter. |
| close_50_sma | Mittelfristiger Trend und dynamischer Widerstand. |
| close_10_ema | Kurzfristiges Momentum. Der Kurs liegt praktisch darauf, daher ist er für Einstiege und Ausstiege nützlich. |
| macd (mit macds/macdh als Beleg) | Trendmomentum und Hinweise auf eine Abschwächung des Abwärtsdrucks. |
| rsi | Überverkauft- oder überkauft-Zustand und Divergenzen. |
| boll_lb (mit boll/boll_ub als Kontext) | Volatilitätsrahmen. Er zeigt, wie weit der Ausverkauf in die untere Band-Zone reichte. |
| atr | Volatilität für Stop-Abstände und Positionsgröße. |
| vwma | Volumengewichtete Trendbestätigung. Die Gewichtung ist wegen der Volumenspitzen am 29.10. besonders relevant. |

Die Auswahl vermeidet Redundanz. Die Indikatoren decken Trend, Momentum, Volatilität und Volumen ab.

## 3. Kursverlauf und Kontext
**Übergeordneter Abwärtstrend seit Mai.** Der Schlusskurs lag am 08.05. bei 400,30 und am 23.11. bei 282,25. Der Rückgang verlief in Stufen:
- **Ende Mai bis Juni:** Der Kurs fiel von rund 390 auf 337,17 (Schlusskurs 26.06., bei 114,7 Mio. Volumen). Danach folgte eine Erholung.
- **22.–23.07.:** Der Kurs fiel von 341,87 auf 317,49 (Schlusskurs 23.07.) bei 69,4 Mio. Volumen.
- **Anfang August:** Eine Erholung bis 377,41 (04.08.) scheiterte. Danach folgte eine lange Seitwärtsphase zwischen etwa 330 und 355 (August bis Mitte Oktober).
- **Ab Mitte Oktober:** Der Kurs gab deutlich nach (21.10.: 334,76, 26.10.: 316,80).
- **29.10. – der entscheidende Bruch:** Der Schlusskurs fiel von 324,89 auf 283,82. Das sind rund −12,6 %. Die Eröffnung lag bei 286,88 (Gap nach unten), das Volumen bei 139,7 Mio. Stück. Das ist die höchste Zahl im gesamten Betrachtungszeitraum und deutet auf eine starke, ereignisgetriebene Neubewertung hin. Was der Auslöser war, geht aus den Daten nicht hervor.
- **Nach dem Gap:** Der Kurs konsolidierte zwischen etwa 265 und 299. Auf die Erholung bis 298,70 (12.11.) folgte ein erneuter Rückgang.
- **19.–20.11.:** Der Kurs fiel auf 272,66 und 265,29, bei hohem Volumen (49,7 und 57,3 Mio.). Das Tagestief vom 20.11. lag bei 264,22, dem tiefsten Wert im Datensatz.
- **23.11.:** Der Kurs eröffnete bei 284,265, lag zwischen 275,36 und 284,60 und schloss bei 282,25. Das sind rund +6,4 % gegenüber dem Vortag. Die Bewegung ist ein Gap-up mit Erholung, aber bei auffallend niedrigem Volumen.

## 4. Indikatoranalyse (verifizierte Werte)
**Trend (gleitende Durchschnitte)**
- Schlusskurs 282,25, 50-SMA 320,96, 200-SMA 336,51.
- Der Kurs liegt rund 12,1 % unter dem 50-SMA und rund 16,1 % unter dem 200-SMA.
- Der 50-SMA liegt unter dem 200-SMA. Das ist die bärische Konstellation eines „Death Cross". Wann sie entstand, kann ich aus den abgefragten Daten nicht belegen.
- Beide Durchschnitte fallen als Widerstand weit oberhalb des Kurses ab. Der Trend ist mittel- und langfristig klar abwärts gerichtet.
- Der 10-EMA liegt bei 282,05, praktisch auf dem Kurs. Kurzfristig ist der Markt neutral und wartet auf eine Richtung.

**Momentum (MACD, RSI)**
- MACD −12,73 und Signallinie −12,99. Das Histogramm ist mit +0,26 leicht positiv.
- Beide Linien liegen tief im negativen Bereich. Der Trend bleibt also bärisch. Der leicht positive Histogrammwert zeigt aber, dass der Abwärtsdruck nachlässt und der MACD knapp über seiner Signallinie liegt. Bei dieser Größenordnung ist das ein sehr schwaches Signal.
- RSI 41,13. Das ist weder überverkauft (<30) noch überkauft. Die Werte der Tage um den 20.11. habe ich nicht abgefragt. Eine Aussage zu einer RSI-Divergenz ist deshalb nicht belegt.

**Volatilität (Bollinger, ATR)**
- Mittelband 287,72, oberes Band 315,25, unteres Band 260,19. Der Kurs liegt knapp unter dem Mittelband.
- Das Tagestief vom 20.11. (264,22) lag nahe am unteren Band von heute, aber noch darüber. Es handelt sich um eine Annäherung, nicht um einen klaren Bruch. Das untere Band kann sich seither verschoben haben.
- Die Bandbreite von rund 55 Punkten ist hoch.
- ATR 11,89 (rund 4,2 % des Kurses). Er stieg von 9,78 am 18.11. auf 11,31 am 20.11. und 11,89 am 23.11. Die Volatilität nimmt also zu, auch wenn der Kurs erholt.

**Volumengewichtet (VWMA)**
- VWMA 285,84. Er liegt über dem Kurs von 282,25, und seit Anfang November fällt er (296,02 am 09.11. auf 285,84 am 23.11.).
- Der Kurs liegt unter der volumengewichteten Durchschnittslinie. Die Käufer haben die Volumenschwerpunkte noch nicht zurückerobert.
- Beachten Sie, dass die Volumenspitze vom 29.10. den VWMA verzerren kann.

## 5. Szenarien und handelbare Marken
Die Marken basieren ausschließlich auf den im Datensatz sichtbaren Kursen. Ich behaupte keine historisch bestätigten Unterstützungen.

**Obere Marken (Widerstände):**
- 285,84 (VWMA)
- 287,72 (Bollinger-Mittelband)
- um 293–299 (Schlusskurse vom 11.–13.11., Hoch 298,70 am 12.11.)
- 315,25 (oberes Band)
- 320,96 (50-SMA)

**Untere Marken:**
- 275,36 (Tagestief 23.11.)
- 272,36 (Tagestief 19.11.)
- 264,22 (Tief 20.11., tiefster Wert im Datensatz)
- 260,19 (unteres Band)

**Bullisches Szenario:** Der Kurs hält sich über dem 10-EMA und gewinnt VWMA und Mittelband zurück. Das Hoch vom 20.11. bleibt dabei unangetastet. Dann ist eine Erholung in Richtung 293–299 möglich. Eine Bestätigung wäre ein Anstieg des Volumens auf Erholungstagen und ein MACD, der weiter über die Signallinie steigt.

**Bärisches Szenario:** Die Erholung scheitert am VWMA oder Mittelband. Das niedrige Volumen am 23.11. spräche dann für einen schwachen Rebound. Ein Schlusskurs unter 264,22 würde ein neues Tief setzen. Die nächste Referenz wäre das untere Band bei etwa 260.

**Risikomanagement:** Bei einem ATR von rund 11,9 sind Tagesschwankungen von ±4 % normal. Enge Stops innerhalb eines ATR laufen Gefahr, durch Rauschen ausgelöst zu werden. Als Faustregel wäre ein Stop-Abstand von etwa 1,5–2 ATR (rund 18–24 Punkte) denkbar, mit entsprechend kleinerer Positionsgröße.

## 6. Fazit
Die Lage ist **mittel- und langfristig bärisch** (Kurs weit unter 50- und 200-SMA, 50-SMA unter 200-SMA, MACD deutlich negativ). Der Kurs bewegt sich seit dem Gap vom 29.10. in einer volatilen Bodenbildungs- oder Konsolidierungszone. Kurzfristig gibt es erste Entspannungszeichen (MACD-Histogramm knapp positiv, Kurs am 10-EMA, Erholung am 23.11.). Gegen eine belastbare Wende sprechen der Kurs unter dem VWMA, der steigende ATR und das niedrige Volumen am 23.11. Ein Einstieg auf der Long-Seite ist erst nach einer Bestätigung sinnvoll. Für bestehende Positionen sprechen die Daten eher für Abwarten und Risikokontrolle als für Zukäufe.

## 7. Übersichtstabelle
| Bereich | Indikator / Beobachtung | Wert (verifiziert) | Einschätzung |
|---|---|---|---|
| Kurs | Schlusskurs 23.11. | 282,25 | Erholung von 265,29 (20.11.) |
| Kurs | Tagesspanne 23.11. | 275,36 – 284,60 | Gap-up, Volumen nur 16,17 Mio. (evtl. unvollständig) |
| Ereignis | 29.10. Gap | 324,89 → 283,82, Volumen 139,7 Mio. | Starke Neubewertung, Auslöser nicht in den Daten |
| Trend lang | 200-SMA | 336,51 | Kurs rund 16 % darunter, bärisch |
| Trend mittel | 50-SMA | 320,96 | Kurs rund 12 % darunter, bärisch |
| Trend kurz | 10-EMA | 282,05 | Neutral, Kurs liegt darauf |
| Momentum | MACD / Signal / Hist. | −12,73 / −12,99 / +0,26 | Trend bärisch, Abwärtsdruck lässt leicht nach |
| Momentum | RSI | 41,13 | Neutral, leicht schwach |
| Volatilität | Bollinger unten / Mitte / oben | 260,19 / 287,72 / 315,25 | Kurs unter dem Mittelband |
| Volatilität | ATR | 11,89 | Steigend (9,78 am 18.11.), Stops weit setzen |
| Volumen | VWMA | 285,84 | Kurs darunter, fallend, kein Kaufbeleg |
| Marken oben | VWMA, Mittelband, 293–299 | 285,84; 287,72; 293–299 | Erholungsziele und Widerstände |
| Marken unten | Tiefs 19./20.11., unteres Band | 272,36; 264,22; 260,19 | Risikoreferenzen |

FINAL TRANSACTION PROPOSAL: **HOLD**