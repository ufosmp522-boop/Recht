# Flugrouten-Rechner

Eigenständiges Web-Tool (eine HTML-Datei, läuft offline im Browser), das die **ideale Flugroute**
zwischen zwei Punkten als **Großkreis (Orthodrome)** berechnet – die kürzeste Verbindung über die
Erdoberfläche. Luftraumsperrungen, Überflugverbote und politische Spannungen werden bewusst
**nicht** berücksichtigt.

## Nutzung

`index.html` im Browser öffnen. Start und Ziel als IATA-/ICAO-Code (`FRA`, `EDDF`), Stadtname
(`Tokio`) oder Koordinaten (`52.52, 13.40`) eingeben.

## Funktionen

- Großkreisdistanz (km / NM / mi), Anfangs- und Endkurs
- Vergleich mit der Loxodrome (konstanter Kurs) inkl. Ersparnis
- Nördlichster/südlichster Punkt und Streckenmitte, Hinweis bei Polarkreis-Überflug
- Flugzeit- und Treibstoffschätzung je Flugzeugtyp (oder eigene Werte) inkl. Windkomponente
- Reichweitenprüfung: bei zu langer Strecke Vorschlag der Route mit den wenigsten Tankstopps
  (danach kürzester Gesamtstrecke) über ~170 Flughäfen
- Wegpunktliste in frei wählbarem Abstand, Export als CSV / GPX oder in die Zwischenablage
- Drehbarer Globus und Weltkarte, Hell-/Dunkelmodus, mobiltauglich

## Bauen

`index.html` wird aus `src/` erzeugt (bettet Kartendaten, d3 und topojson-client ein):

```
python3 build.py
```

Quellen: Kartendaten `world-atlas@2.0.2` (Natural Earth, Public Domain), `d3@7.9.0` (ISC),
`topojson-client@3.1.0` (ISC).

Berechnungen auf der Kugel (mittlerer Erdradius 6371,0 km); Näherungswerte für Planung und
Vergleich, keine Navigationsgrundlage.
