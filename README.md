# Roadtrip Shenzhen → Xi'an

Einseitige Website, zweisprachig (Deutsch / 中文). Kein Passwort mehr: Der Inhalt
steht direkt in `index.html`. Suchmaschinen werden per
`<meta name="robots" content="noindex, nofollow">` ausgeschlossen — wer die URL
kennt, kann die Seite aber öffnen.

## Dateien

| Datei | Zweck |
|---|---|
| `index.html` | fertige Seite — das ist das Einzige, was online muss |
| `content.html` | der Inhalt, hier bearbeiten (jeder Text auf Deutsch und Chinesisch) |
| `template.html` | Layout, Styles, Skripte |
| `build.py` | setzt `content.html` in `template.html` ein → `index.html` |
| `images/` | eigene Fotos, Dateinamen siehe unten |

## Inhalt bearbeiten

```bash
python3 build.py
```

Danach `index.html` committen und pushen; GitHub Pages braucht ein bis zwei
Minuten.

## Warum keine robots.txt?

Eine `robots.txt` wirkt nur im Wurzelverzeichnis der Domain
(`<name>.github.io/robots.txt`), nicht unter `/china-roadtrip/`. Ausserdem würde
ein `Disallow` Suchmaschinen daran hindern, das `noindex` in der Seite überhaupt
zu lesen — verlinkte URLs könnten dann trotzdem in der Suche auftauchen.

## Fotos

Sieben Bilder sind eingebaut, alle von Wikimedia Commons unter CC-BY- oder
CC-BY-SA-Lizenz. Urheber und Quelle stehen in `images/CREDITS.md` und in der
Bildunterschrift auf der Seite — beides muss so bleiben, das ist die Bedingung
dieser Lizenzen.

Eigene Fotos ersetzen sie einfach durch Überschreiben derselben Dateinamen:

```
01-danxia.jpg      04-tianmen.jpg     07-xian.jpg
02-yangshuo.jpg    05-wulingyuan.jpg
03-fenghuang.jpg   06-wudang.jpg
```

Querformat, etwa 1800 px breit. Wenn du ein Bild ersetzt, lösche die zugehörige
Zeile in `CREDITS.md` und passe die Bildunterschrift in `content.html` an.
