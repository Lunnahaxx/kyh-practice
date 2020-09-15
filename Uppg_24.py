"2.0.Uppg_24 "
"15 Sept 2020""
"Task info"
"""
Nu ska vi använda oss av kunskapen kring JSON och att installera paket från PyPI (cheese shop) på riktigt!

Börja med att utöka "requirements.txt" med paketet "requests":

    pygame
    requests

.. och låt PyCharm installera det nya paketet när frågan dyker upp.

1. Pröva att ladda ned denna URL i browsern:

   https://proagile.se/api/publicEvents
   
2. Läs på hur man gör en GET med requests-API:et (googla!). Gör ett GET-request mot URL ifrån (1) och skriv ut r.text med print, typ:

    r = requests.get( ... )  # fixa rätt parametrar! r.text är råa strängen som är resultatet

3. Använd nu istället pprint för att skriva ut r.json(). pprint finns i inbyggda modulen "pprint".

4. Vi vill veta exakt när alla kurser börjar på ProAgile. Bygg ett program som letar upp alla "startDate" i datan, och skriver ut dem!
"""
"-------------------------"
"Koden 2.0.Uppg_23 "
"Lösningen"
import requests
import json

r = requests.get('https://proagile.se/api/publicEvents')
r.status_code


#r.json()

#content = Path("telefon_22.json").read_text(encoding='utf8')










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