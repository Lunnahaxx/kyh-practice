"Uppg_34 "
"Task info"
"""
34.1 Lägg till 3 egna nya djur i djur.py från uppgift 33.

Använd wikipedia för att hitta URL:er och för att reda ut eventuella oklarheter 
kring namn och köttätare/vegetarian. :)

34.2 Lägg till följande metod i Djur klassen:

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vetegarian"

Byt ut if-else blocken i programmet mot anrop till denna metod!

34.3 Bygg en metod "get_html_table_row(self)" i klassen Djur, och flytta in f-stringen 
med <tr><td> etc in i Djurklassen. Anropa denna istället för att bygga upp HTML-koden i forloopen. 
Obs! Låt <html><table> d.v.s det som ligger "runtom" tabelldatan vara kvar i 
huvudprogrammet - flytta inte in detta i Djurklassen.
Tips: för att anropa en metod ifrån en annan metod, använd syntaxen self.metod2(arg1, arg2). 
Kan vara användbart för att bygga get_html_table_row ;)
"""
"-------------------------"
"Koden 2.0.Uppg_ "
"Lösningen"
import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')

class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    delfin = Djur('Delfin', True, 'https://sv.wikipedia.org/wiki/Delfiner')
    lunnefogel = Djur('Lunnefågel', False, 'https://sv.wikipedia.org/wiki/Lunnef%C3%A5gel')
    myra = Djur('Myra', False, 'https://sv.wikipedia.org/wiki/Myror')


    djur.append(zebra)
    djur.append(tiger)
    djur.append(delfin)
    djur.append(lunnefogel)
    djur.append(myra)
    html = '<html><table>'
    for d in djur:
        cell_2 = 'Vegetarian'
        if d.carnivore:
            cell_2 = 'Köttätare'
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</td><td>{cell_2}</td></tr>\n'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))

print(f"{zebra}")
"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"


def main():
    pass


if __name__ == '__main__':
    main()
