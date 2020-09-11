"""Spara följande i "data.json".
Läs in data i Python, spara i en variabel "data = json.loads(content)" i Python.
Med hjälp av debuggern, undersök datatyper ni kan hitta inuti data-variabeln.

[
  12,
  3.5,
  4,
  true,
  false,
  "vi kan ha text också",
  "1234908",
  "99999999",
  {
    "fredrik": {
      "tfn": "12345677",
      "adress": "Banangränd",
      "email": "freddan@proagile.se"
    }
  }
]"""
from pathlib import Path
import json

file = Path("data.json")
content = file.read_text(encoding='utf8')

d2 = json.loads(content)




