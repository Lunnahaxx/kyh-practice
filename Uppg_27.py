"2.0.Uppg_ "
"Task info"
"""
27.1 Det här är lite Python-kod. Spara den i data.json fil och översätt till JSON-format!
Obs! Ingen kod i JSON!

contents = [
    {
        'what': 'Energi',
        'value': 385,
        'unit': 'kcal',
        'rightalign': False
    },
    {
        'what': 'Fett',
        'value': 2.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav mättat fett',
        'value': 1.7,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Kolhydrat',
        'value': 82,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav sockerarter',
        'value': 79.5,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Fiber',
        'value': 6.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Protein',
        'value': 4.6,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Salt',
        'value': .48,
        'unit': 'g',
        'rightalign': False
    }
]

27.2 Som ni kanske sett är det en lista på ingredienser i någon produkt - 
här är förlagan som ni kan titta på i en browser:

      https://www.oboy.se/~/media/oboy/se/images/products/original-mobile.png

Det är alltså data från kolumn 1 och 2. Bygg ett Pythonscript som skriver ut 
en liknande "tabell" på konsollen!

Tips: Tabellens första kolumn ska vara 25 tecken bred, och andra 12.
Tips 2: Notera att det finns ett attribut "rightalign" i datan, som 
beskriver om "what" ska justeras till 
vänster eller höger!
"""
"-------------------------"
"Koden 2.0.Uppg_ "
"Lösningen"
from pathlib import Path
import json
from pprint import pprint


content = Path("data_U27.json").read_text(encoding='utf8')
data = json.loads(content)

for key in data:
    #if "what" in key:
    print(key["what"])

#pprint(data)






"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"
"""
def main():
    pass


if __name__ == '__main__':
    main()
"""