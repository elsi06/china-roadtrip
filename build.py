#!/usr/bin/env python3
"""
Baut index.html aus template.html + content.html.

Der Inhalt wird unverschluesselt in die Seite eingesetzt. Suchmaschinen
halten sich per <meta name="robots" content="noindex, nofollow"> fern.

Benutzung:
    python3 build.py

Danach index.html (und den images-Ordner) committen und pushen.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def build() -> None:
    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
        template = f.read()
    with open(os.path.join(HERE, "content.html"), encoding="utf-8") as f:
        content = f.read()

    out = template.replace("__CONTENT__", content)
    out_path = os.path.join(HERE, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)

    kb = len(out.encode("utf-8")) / 1024
    print(f"index.html geschrieben ({kb:.0f} KB).")


if __name__ == "__main__":
    build()
