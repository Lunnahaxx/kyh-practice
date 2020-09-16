"2.0.Uppg_25 "
"15 Sept 2020"
"Task info"
"""
Fortsättning på uppgift 24 - mer om JSON och requests (webapi-anrop).

Nu ska vi bearbeta datan något med hjälp av Python och f-string tricken jag visade er!

25.1 Skriv ett Pythonprogram som använder requests mot URLen ni fick i uppgift 24, och skriver ut kurstillfällen som sker under oktober 2020, på denna form:

   Kursnamn: Professional Scrum Product Owner (EN), 15-16 september, Stockholm
 Startdatum: 2020-10-15
   Slutdatum: 2020-10-17

   Kursnamn: Professional Scrum Master, 15-16 september, Stockholm
 Startdatum: 2020-10-15
   Slutdatum: 2020-10-16

Den första kolumnen, fram till och med ":" är 12 tecken bred, och högerställd. 
Den andra kolumen är 100 tecken bred, och vänsterställd.

25.2 Istället för att hårdkoda oktober 2020 just, låt användaren mata in ett år och en månad, 
som ni sedan använder för att filtrera ut kurserna som skrivs ut! T.ex.

   Year: 2020
   Month (1-12): 12
   Searching for courses in date range 2020-12-01 to 2020-12-31

Tips: det går bra att använda -01 och -31 för att inkludera hela månaden, 
även om vissa månader inte har så många dagar!
"-------------------------"
"""
"Koden 2.0.Uppg_25 "
"Lösningen 16 Sept"
""""""
import requests
import json
import datetime
from pprint import pprint

r = requests.get('https://proagile.se/api/publicEvents')

indata = json.loads(r.text)

#hintar
#today datytime type som, year.month.day  som int
#jämnför vår datum tid i strängar < > går att skriva

for i in indata:
    if '2020' or '10' or '01' in i:
        print("startDatum")
        #print(i["2020-10-15"])

#2020 10 == date


#for i in indata:
    #if i in (datetime.month)

#datetime.month datetime.datetime.10()

#in range
#datetime.month
#pprint(indata)

#d = datetime.fromtimestamp(time.time())
















"-------------------------"
"Koden 2.0.Uppg_25 "
"Lösningen 15 Sept"
"""
Kursnamn:      Professional Scrum Product Owner (EN), 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-17

Kursnamn:      Professional Scrum Master, 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-16
"""
#dagens_datum
"""
k1 = "Kursnamn:"
s1 = "Startdatum:"
a1 = "Slutdatum:"

Kursnamn_1 = "Professional Scrum Product Owner (EN)"
Startdatum_1 = "2020-09-15"
Slutdatum_1 = "2020-09-17"

Kursnamn_2 = "Professional Scrum Master, 15-16 september, Stockholm"
Startdatum_2 ="2020-09-15"
Slutdatum_2 = "2020-09-16"


print(f"{k1:15} {Kursnamn_1} \n{s1:15} {Startdatum_1} \n{a1:15} {Slutdatum_1}\n")

print(f"{k1:15} {Kursnamn_2} \n{s1:15} {Startdatum_2:} \n{a1:15} {Slutdatum_2:}")

#print(f"")

#print(f"Jag vill se talet med nollor! {tal:>05}")


#print(f"Kursnamn: {Kursnamn_1:<10} } är {tal:<10} och datum {datum:^100}. Värder är {value}")
"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"


def main():
    pass


if __name__ == '__main__':
    main()"""


