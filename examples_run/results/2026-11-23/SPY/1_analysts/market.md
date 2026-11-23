# SPY (State Street SPDR S&P 500 ETF Trust, PCX): Technischer Bericht zum 23.11.2026

## 1. Zusammenfassung
SPY ist von einem Hoch im Oktober in eine scharfe Korrekturphase gefallen. Der höchste Schlusskurs im abgefragten Zeitraum (ab 01.11.2025) war 779,09 am 06.10.2026. Am 20.11.2026 gab es einen Kapitulations-ähnlichen Ausverkauf: Tief 686,75, Schlusskurs 689,81 und ein Volumen von rund 151 Mio. Stück. Dieses Volumen gehört zu den höchsten im gesamten Datensatz. Am 23.11.2026 folgte eine kräftige Erholung auf einen verifizierten Schlusskurs von 723,43.

Kurzfristig ist das Bild eine **überverkaufte Gegenbewegung innerhalb eines beschädigten Mittelfristtrends**. Der Kurs liegt unter dem 10er-EMA, dem 50er-SMA und knapp unter dem 200er-SMA. Das Momentum (MACD) ist klar negativ. Die Volatilität hat deutlich zugenommen.

## 2. Datenqualität und Abweichungen
- Der verifizierte Snapshot für den 23.11.2026 nennt Open 724,33, High 727,97, Low 713,54, Close **723,43** und Volumen 32.016.364.
- Der Roh-Datenabruf (`get_stock_data`) nennt für denselben Tag Close **723,75**, High 727,98 und Volumen 32.003.828.
- Das ist eine **Abweichung** zwischen den beiden Quellen. Ich verwende den Snapshot als maßgeblich und rechne keinen Mittelwert.
- Das Volumen von rund 32 Mio. ist für einen ganzen Handelstag niedrig. Es deutet darauf hin, dass die Daten des 23.11. noch nicht den vollständigen Handelstag abbilden. Der Schlusskurs kann sich daher noch ändern.

## 3. Ausgewählte Indikatoren und Begründung
Ich habe 8 Indikatoren gewählt, die sich ergänzen:
1. **close_10_ema** zeigt das kurzfristige Momentum.
2. **close_50_sma** zeigt den mittelfristigen Trend und dynamischen Widerstand.
3. **close_200_sma** ist der langfristige Trendanker.
4. **macd** und **macdh** zeigen Trendrichtung und Momentum-Beschleunigung. Das Signal (macds) steht im Snapshot und ist nicht redundant.
5. **rsi** misst überverkaufte und überkaufte Zustände.
6. **boll** und **boll_lb** zeigen Mittellinie und untere Bandgrenze. Sie dienen als Mean-Reversion-Referenz.
7. **atr** zeigt die Volatilität und dient der Stop- und Positionsgrößenbestimmung.

Ich habe VWMA und das obere Band weggelassen. Der Kurs ist weit vom oberen Band (786,22) entfernt, und das Volumen lässt sich direkt in den Rohdaten beurteilen.

## 4. Detailanalyse

### Trend und gleitende Durchschnitte (Snapshot-Werte)
| Indikator | Wert | Kurs (723,43) relativ dazu |
|---|---:|---|
| 10-EMA | 729,35 | darunter |
| 200-SMA | 730,48 | darunter (knapp) |
| 20-SMA (Boll-Mitte) | 745,71 | darunter |
| 50-SMA | 759,32 | deutlich darunter |

- **Der Kurs liegt unter allen vier Durchschnitten.** Der 10-EMA fiel von 754,52 am 13.11. auf 729,38 am 23.11. (Indikatorabfrage). Das ist ein steiler kurzfristiger Trendbruch.
- Der **50-SMA fällt** (764,09 am 13.11. auf 759,32 am 23.11.), während der **200-SMA** nahezu flach bis leicht steigend ist (729,32 auf 730,48). Der 50er liegt mit rund 29 Punkten noch über dem 200er. Ein Death Cross liegt damit **nicht** vor. Die Lücke schrumpft aber, wenn die Schwäche anhält.
- Der 200-SMA bei rund 730 ist der zentrale Schwellenwert. Eine Rückeroberung per Tagesschluss wäre ein erstes konstruktives Signal. Ein Scheitern daran wäre ein Zeichen für eine bloße Gegenbewegung.

### Momentum: MACD und Histogramm
- Der MACD liegt bei **-12,60**, das Signal (macds) bei **-8,36**, das Histogramm bei **-4,24**. Es besteht ein bärisches Momentum mit MACD unter der Signallinie.
- Das Histogramm fiel von -0,06 (13.11.) über -0,78, -1,63, -2,18 und -3,28 auf **-5,40 (20.11.)**. Am 23.11. verengte es sich auf -4,24. Das ist eine **erste Abschwächung des Abwärtsmoments**, aber kein Kaufsignal. Dafür bräuchte es einen MACD-Kreuz über das Signal oder ein Histogramm nahe null.
- Der MACD blieb am 23.11. mit -12,59 praktisch auf dem Niveau vom 20.11. (-12,70). Die Abwärtsdynamik hat sich nicht weiter beschleunigt, aber auch nicht umgekehrt.

### RSI
- Der RSI fiel von 47,1 (13.11.) auf **24,9 am 20.11.**, also klar unter 30 und überverkauft. Am 23.11. liegt er bei **41,98**.
- Das ist ein schneller Rücksprung aus der überverkauften Zone. In Abwärtstrends kann der RSI länger im Bereich 40–55 festhängen. Ein Wert um 42 bestätigt daher eine Erholung, aber noch keine Trendwende.

### Bollinger-Bänder und Volatilität
- Am 20.11. lag der Schlusskurs (689,81) und das Tagestief (686,75) **unter dem unteren Band** (707,79 an diesem Tag). Das ist ein klassischer Extrem-Impuls.
- Am 23.11. liegt das untere Band bei **705,21**, die Mitte bei 745,71 und das obere Band bei 786,22. Der Kurs liegt im unteren Drittel der Bandbreite. Das Band ist sehr breit, was die erhöhte Volatilität widerspiegelt.
- Der **ATR** stieg von 11,03 (13.11.) auf **15,35**. Das entspricht rund 2,1 % des Kurses (eigene Rechnung). Der Anstieg zeigt einen echten Volatilitätsregimewechsel.

### Preis- und Volumenverlauf (Rohdaten)
- Am 05.11. gab es eine Verkaufswelle: Hoch 765,97, Tief 732,71, Close 733,00 bei rund 125,9 Mio. Volumen. Danach folgte eine Erholung auf 759,81 (11.11.).
- Diese Erholung scheiterte. Der Kurs fiel vom 16. bis 20.11. an fünf aufeinanderfolgenden Handelstagen: von 739,95 über 732,44, 730,20 und 715,87 auf 689,81.
- Der 20.11. war mit rund 151 Mio. Volumen und einer Tagesspanne von 686,75 bis 718,29 ein Extremtag. Die Intraday-Spanne beträgt rund 31,5 Punkte.
- Der 23.11. eröffnete bei 724,33 (deutlich über dem Vortagesschluss) und schloss laut Snapshot bei 723,43. Das ergibt eine Erholung von rund +4,9 % gegenüber dem 20.11. (eigene Rechnung aus 689,81 und 723,43).
- Gegenüber dem Schlusshoch vom 06.10. (779,09) liegt der Kurs rund 7,1 % tiefer (eigene Rechnung).

## 5. Relevante Marken (nur aus Tool-Daten abgeleitet)
| Marke | Wert | Herkunft |
|---|---:|---|
| Tief der Kapitulation | 686,75 | Tagestief 20.11. |
| Unteres Bollinger-Band | 705,21 | Snapshot |
| Tagestief 23.11. | 713,54 | Snapshot |
| 10-EMA | 729,35 | Snapshot |
| 200-SMA | 730,48 | Snapshot |
| Tagesschluss 05.11. | 733,00 | Rohdaten |
| Bollinger-Mitte (20-SMA) | 745,71 | Snapshot |
| 50-SMA | 759,32 | Snapshot |

Ich behaupte hier keine historisch bestätigten Unterstützungen oder Widerstände. Die Marken sind Referenzpunkte aus den Indikatoren und den genannten Kursen.

## 6. Handlungsrelevante Einschätzung
**Szenario A: Erholung hält an (bullisch bedingt)**
- Bestätigung bräuchte einen Tagesschluss über dem 10-EMA und dem 200-SMA (rund 729–730). Danach wären die Bollinger-Mitte (745,71) und der 50-SMA (759,32) die nächsten Ziele.
- Das MACD-Histogramm müsste sich weiter Richtung null bewegen.
- Das Tief vom 20.11. (686,75) sollte nicht erneut unterschritten werden.

**Szenario B: Gegenbewegung scheitert (bärisch bedingt)**
- Ein Abprallen an 729–731 mit neuem Schluss unter dem 23.11.-Tief (713,54) würde die Abwärtsstruktur bestätigen.
- Ein erneuter Test des unteren Bandes (705,21) und des Tiefs von 686,75 wäre dann wahrscheinlich.
- Ein Bruch von 686,75 würde den Kapitulationstag entwerten.

**Risikomanagement**
- Bei einem ATR von 15,35 wären Stops von 1,5 bis 2 ATR rund 23 bis 31 Punkte vom Einstieg entfernt. Das ist deutlich weiter als noch vor einer Woche (ATR 11,03). Die Positionsgröße sollte entsprechend kleiner sein.
- Starke Tagesschwankungen sind wahrscheinlich. Die letzten Tage zeigten Spannen von 20 bis über 30 Punkten.
- Nach einem Extremtag mit Volumenspitze sind scharfe Gegenbewegungen normal. Ein einzelner Erholungstag ist noch keine Trendwende.

**Gesamtbild:** Die Datenlage ist gemischt. Die Überverkauft-Erholung (RSI-Rücksprung, Schluss nach Kapitulationsvolumen) spricht für eine Stabilisierung. Der Bruch aller Durchschnitte, das negative MACD-Momentum und der steigende ATR sprechen dagegen. Ein klares Signal in eine Richtung gibt es noch nicht. Der Schlusskurs vom 23.11. ist zudem möglicherweise nicht final.

## 7. Übersichtstabelle
| Kategorie | Indikator | Wert (23.11.2026) | Aussage |
|---|---|---:|---|
| Kurs | Close (Snapshot) | 723,43 | Erholung nach 689,81 am 20.11. (Rohdaten: 723,75, Abweichung) |
| Kurzfristtrend | 10-EMA | 729,35 | Kurs darunter, fallend seit 13.11. (754,52) |
| Mitteltrend | 50-SMA | 759,32 | Kurs deutlich darunter, fallend |
| Langtrend | 200-SMA | 730,48 | Kurs knapp darunter, zentrale Schwelle |
| Trendstruktur | 50-SMA vs. 200-SMA | 759,32 vs. 730,48 | Kein Death Cross, Abstand schrumpft |
| Momentum | MACD / Signal | -12,60 / -8,36 | Bärisch |
| Momentum | MACD-Histogramm | -4,24 | Verengt sich nach -5,40 (20.11.) |
| Momentum | RSI | 41,98 | Rücksprung von 24,9 (20.11.), neutral bis schwach |
| Volatilität | Bollinger Mitte / unten / oben | 745,71 / 705,21 / 786,22 | Kurs im unteren Drittel, Bänder weit |
| Volatilität | ATR | 15,35 | Stark gestiegen (11,03 am 13.11.), Stops weiter setzen |
| Volumen | Volumen 20.11. | ca. 151 Mio. | Extremtag, kapitulationsartig |
| Datenqualität | Volumen 23.11. | ca. 32 Mio. | Vermutlich unvollständiger Handelstag |

FINAL TRANSACTION PROPOSAL: **HOLD**