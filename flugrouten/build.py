#!/usr/bin/env python3
"""Erzeugt die eigenständige index.html (offline nutzbar) aus src/.

Eingebettet werden: Kartendaten (world-atlas countries-110m), d3 v7.9.0, topojson-client v3.1.0.
"""
import json
from pathlib import Path

src = Path(__file__).parent / "src"
world = json.dumps(json.loads((src / "countries-110m.json").read_text()), separators=(",", ":"))
html = (src / "template.html").read_text()
for key, val in {
    "__WORLD__": world,
    "__D3__": (src / "vendor" / "d3.min.js").read_text(),
    "__TOPOJSON__": (src / "vendor" / "topojson-client.min.js").read_text(),
}.items():
    assert key in html, key
    html = html.replace(key, val.replace("</script", "<\\/script"))
(Path(__file__).parent / "index.html").write_text(html)
print(f"index.html geschrieben ({len(html) // 1024} KB)")
