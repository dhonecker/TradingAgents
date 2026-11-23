# NVDA – Technischer Analysebericht (Stand: 23.11.2026)

## 1. Zusammenfassung

NVDA hat einen außergewöhnlich scharfen Abverkauf hinter sich und danach eine ebenso außergewöhnliche Erholung am letzten Handelstag erlebt. Der Kurs fiel vom Schlusskurs am 06.10.2026 (239,24) bis zum Schlusskurs am 20.11.2026 (125,53). Das sind rund 47,5 % in gut sechs Wochen. Am 23.11.2026 öffnete die Aktie bei 167,04, also mit einer Aufwärtslücke von rund 33 % gegenüber dem Vortagesschluss. Sie schloss laut verifiziertem Snapshot bei 168,505, rund 34 % über dem Schlusskurs vom 20.11.

Der mittel- bis langfristige Trend ist klar gebrochen. Kurzfristig liegt aber eine extreme Überverkauftheit mit einer Reflexbewegung vor. Der Chart zeigt eine Kapitulations- bzw. Stressphase mit sehr hohen Umsätzen und stark steigender Volatilität. Ob der 23.11. eine Trendwende oder nur ein Erholungsimpuls im Abwärtstrend ist, lässt sich aus einem einzelnen Handelstag nicht belegen.

## 2. Gewählte Indikatoren und Begründung

Ich habe acht sich ergänzende Indikatoren gewählt:

| Indikator | Zweck im aktuellen Kontext |
|---|---|
| close_50_sma | Mitteltrend und dynamische Widerstandszone |
| close_200_sma | Langfristiger Trendfilter und Death-Cross-Gefahr |
| close_10_ema | Kurzfristiges Momentum und Reaktion auf die Erholung |
| macd / macdh | Trendmomentum und Abschwächung des Abwärtsimpulses |
| rsi | Überverkauft-Signal und Erholungsmomentum |
| boll_lb | Volatilitätsrahmen und Extrembereiche |
| atr | Risikomanagement und Positionsgröße |
| vwma | Volumengewichtete Trendbestätigung |

## 3. Verifizierte Datenbasis und Diskrepanzen

Der Snapshot ist die maßgebliche Quelle. Für den 23.11.2026 gilt:

- **Open:** 167,04
- **High:** 171,50
- **Low:** 156,93
- **Close:** 168,505
- **Volumen:** 388.684.767

**Hinweis auf Diskrepanzen:** Die Rohdaten von `get_stock_data` weichen für den 23.11. minimal vom Snapshot ab.

| Größe | Rohdaten | Snapshot |
|---|---|---|
| Close | 168,545 | 168,505 |
| Volumen | 388.533.211 | 388.684.767 |

Auch bei den Indikatoren gibt es kleine Abweichungen:

| Indikator | `get_indicators` | Snapshot |
|---|---|---|
| MACD | -17,800 | -17,797 |
| MACD-Histogramm | -2,077 | -2,079 |
| RSI | 44,467 | 44,465 |

Das spricht für eine noch nicht final bereinigte Tageskerze. Ich verwende in diesem Bericht die Snapshot-Werte und habe die Abweichungen nicht abgeglichen. Sie ändern die Aussage nicht.

## 4. Trendanalyse

### Gleitende Durchschnitte (Snapshot-Werte)

- **50-Tage-SMA: 206,15.** Er fällt seit Ende Oktober stetig. Am 26.10. lag er bei 222,22, am 20.11. bei 207,00. Der Kurs liegt rund 18 % darunter (168,505 gegenüber 206,15).
- **200-Tage-SMA: 203,00.** Er ist nahezu flach bis leicht fallend (204,39 am 06.11.). Der Kurs notiert klar darunter.
- **Death-Cross-Konstellation:** Der 50-SMA liegt mit 206,15 nur noch rund 3,15 Punkte über dem 200-SMA (203,00). Der Abstand schrumpft täglich. Fallen die Kurse nicht rasch zurück über diese Marken, droht in den kommenden Handelstagen oder Wochen ein formales Death Cross. Das wäre ein lagging-Signal, das den bereits erfolgten Absturz nachträglich bestätigt.
- **10-EMA: 159,35.** Sie fiel von 217,99 am 26.10. auf 157,32 am 20.11. und dreht jetzt mit dem Kurs leicht nach oben. Der Schlusskurs von 168,505 liegt erstmals im aktuellen Abverkauf deutlich über der 10-EMA. Das ist ein kurzfristig positives Signal.
- **VWMA (20 Tage): 162,57.** Der Kurs liegt auch darüber. Die volumengewichtete Erholung gibt den Kurs damit über das Niveau, auf dem zuletzt das meiste Volumen gehandelt wurde.

Die Rangfolge der Durchschnitte lautet jetzt: Kurs (168,5) > 10-EMA (159,3) > VWMA (162,6) und alles deutlich unter 50-SMA (206,2) und 200-SMA (203,0). Das ist strukturell bärisch, mit einer kurzfristigen Gegenbewegung.

### MACD

- **MACD-Linie:** -17,80 (Snapshot -17,797), Signal: -15,72, Histogramm: -2,08.
- Die MACD-Linie lag am 26.10. noch bei -2,71. Sie ist seitdem kontinuierlich gefallen und markierte am 20.11. mit -19,83 ihr Tief im betrachteten Fenster.
- Das Histogramm verbesserte sich von -4,63 am 20.11. auf -2,08 am 23.11. Der negative Impuls schwächt sich also ab. Es ist aber weiterhin negativ, und die MACD-Linie liegt unter der Signallinie. Ein bullisches Crossover liegt nicht vor.
- Wegen der Trägheit des MACD (der Kurssprung wirkt erst mit Verzögerung) ist ein Crossover in den nächsten Tagen nur bei anhaltend höheren Kursen denkbar.

### RSI

- Der RSI fiel auf 15,05 am 20.11. und lag davor vom 05.11. bis 19.11. durchgehend im Bereich 19,6 bis 30,8. Das ist eine ungewöhnlich lange und tiefe Überverkauftphase.
- Aktuell liegt er bei 44,46. Er ist damit in einem Tag aus dem extremen Überverkauftbereich in eine neutrale Zone gesprungen.
- Der RSI ist ein rückwärtsgerichteter Indikator. Der Sprung zeigt vor allem die Größe der Tagesbewegung. Ein „Überverkauft-Kaufsignal“ ist inzwischen abgelaufen.

### Bollinger-Bänder und Volatilität

- **Mittelband (20-SMA): 179,08**, **oberes Band: 230,05**, **unteres Band: 128,12.**
- Der Schlusskurs am 20.11. (125,53) lag unter dem unteren Band (128,31 am selben Tag). Die Erholung hat den Kurs ins untere Drittel des sehr weiten Bandes zurückgebracht. Das Mittelband bei 179,08 ist die nächste Referenzmarke nach oben.
- **ATR: 13,22.** Der ATR stieg von rund 5,7 (29.10.) auf 13,22. Das ist mehr als eine Verdopplung der durchschnittlichen Tagesschwankung.

## 5. Volumen und Kursverlauf

- Die Umsätze waren im November außergewöhnlich hoch. Am 12.11. wurden 747,7 Mio. Aktien gehandelt, am 20.11. 626,4 Mio. und am 09.11. 462,7 Mio. Im Vergleich dazu lagen die Umsätze im Oktober meist bei rund 70 bis 135 Mio.
- Der 12.11. mit dem Intraday-Tief von 148,80 bei einem Schluss von 166,19 zeigt bereits eine große Handelsspanne. Es folgten dennoch weitere Verluste bis zum 20.11.
- Am 20.11. bildete sich bei 124,50 (Tagestief) ein vorläufiger Boden. Der Schlusskurs von 125,53 lag nur knapp darüber. Am 23.11. gab es dann den Aufwärtsgap mit knapp 389 Mio. Aktien Umsatz.
- Hohe Umsätze bei einem Rebound können auf Kapitulation und Short-Covering hindeuten. Das ist aber eine Interpretation. Ob der Kurs hält, zeigen erst die Folgetage.

Hinweis zu Kursmarken: Ich nenne unten nur Referenzpunkte aus den Daten. Dass diese Niveaus als Support oder Resistance funktionieren, ist nicht belegt.

## 6. Referenzniveaus aus den Daten

**Nach oben:**
- 179,08 (Bollinger-Mittelband)
- 178,67 (Schlusskurs 09.11.) und 186,64 (Schlusskurs 06.11.)
- 203,00 bis 206,15 (200-SMA und 50-SMA, eng beieinander)

**Nach unten:**
- 156,93 (Tagestief 23.11.)
- 159,35 (10-EMA) und 162,57 (VWMA)
- 124,50 (Tagestief 20.11.) bzw. 125,53 (Schlusskurs 20.11.)

## 7. Handlungsrelevante Einschätzung

1. **Trend:** Mittel- und langfristig bärisch. Der Kurs liegt unter 50- und 200-SMA, beide Durchschnitte konvergieren, und der 50-SMA fällt.
2. **Kurzfristig:** Der Kurs liegt über 10-EMA und VWMA, und der RSI sowie das MACD-Histogramm erholen sich. Das spricht für eine Reflexbewegung. Eine bestätigte Trendumkehr zeigen die Indikatoren nicht.
3. **Risiko:** Mit einem ATR von 13,22 sind Tagesschwankungen von mehreren Prozent normal. Ein Stopp von 1,5 × ATR entspräche rund 19,8 Punkten, also etwa 11,8 % des Kurses. Die Positionsgröße sollte entsprechend reduziert werden.
4. **Gap-Risiko:** Ein Aufwärtsgap dieser Größe kann teilweise wieder geschlossen werden. Ein Rückfall unter 156,93 (Tagestief) würde das Erholungsbild abschwächen. Ein erneuter Test des Tiefs bei 124,50 bis 125,53 ist nicht auszuschließen.
5. **Bestätigungssignale, auf die zu achten ist:**
   - Mehrere Schlusskurse über dem Mittelband (179,08)
   - Ein bullisches MACD-Crossover (Linie über Signal)
   - Sinkende Umsätze bei steigenden Kursen oder ein Schlusskurs über dem 50-SMA
   - Dagegen: Schlusskurse unter 10-EMA und VWMA sowie ein formales Death Cross

**Fazit:** Das Bild ist gemischt. Die Erholung ist deutlich, die Trendstruktur bleibt aber gebrochen. Neue Positionen sind wegen der extremen Volatilität und der fehlenden Bestätigung riskant. Bestehende Positionen sollten eng überwacht werden.

## 8. Übersichtstabelle

| Thema | Beobachtung (Snapshot, 23.11.2026) | Einschätzung |
|---|---|---|
| Schlusskurs | 168,505 (Open 167,04, High 171,50, Low 156,93) | Starke Erholung nach Schlusskurs 125,53 am 20.11. |
| Volumen | 388.684.767 | Sehr hoch, Oktober meist ca. 70–135 Mio. |
| 10-EMA | 159,35 | Kurs darüber, kurzfristig positiv |
| VWMA | 162,57 | Kurs darüber, volumengewichtet positiv |
| 50-SMA | 206,15 (fallend) | Kurs deutlich darunter, bärisch |
| 200-SMA | 203,00 | Kurs darunter, Abstand zum 50-SMA nur ca. 3,15 |
| Death Cross | Noch nicht eingetreten, Abstand schrumpft | Risiko in den kommenden Wochen |
| MACD / Signal | -17,80 / -15,72 | Unter Signallinie, bärisch |
| MACD-Histogramm | -2,08 (Vortag -4,63) | Abwärtsimpuls schwächt sich ab |
| RSI | 44,46 (Tief 15,05 am 20.11.) | Aus Überverkauft zurück in Neutralzone |
| Bollinger | Mitte 179,08, oben 230,05, unten 128,12 | Sehr weite Bänder, Kurs im unteren Drittel |
| ATR | 13,22 (Ende Oktober ca. 5,7–6,1) | Volatilität mehr als verdoppelt |
| Datenabweichung | Rohdaten Close 168,545 / Volumen 388.533.211 vs. Snapshot | Geringfügig, Snapshot maßgeblich |
| Gesamtbild | Bärischer Trend, kurzfristige Reflexerholung | Abwarten, Bestätigung nötig |

FINAL TRANSACTION PROPOSAL: **HOLD**