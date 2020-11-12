"2.0.Uppg_24 "
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

Den första kolumnen, fram till och med ":" är 12 tecken bred, och högerställd. Den andra kolumen är 100 tecken bred, och vänsterställd.

25.2 Istället för att hårdkoda oktober 2020 just, låt användaren mata in ett år och en månad, som ni sedan använder för att filtrera ut kurserna som skrivs ut! T.ex.

   Year: 2020
   Month (1-12): 12
   Searching for courses in date range 2020-12-01 to 2020-12-31

Tips: det går bra att använda -01 och -31 för att inkludera hela månaden, även om vissa månader inte har så många dagar!
"""
"-------------------------"
"Koden 2.0.Uppg_24 "
"Lösningen"
import requests
import json
#from pprint import pprint


# 24.2 print(r.text)

def main(startdate, enddate):
    r = requests.get('https://proagile.se/api/publicEvents')
    course_list = r.json()

for course in course_list:

    startdate ="2020-10-01"
    enddate = "20-10-31"
    coursedate = course['startDate']
    if startdate < coursedate and coursedate < enddate:
        print()
        print(f"Kursnamn: {course['name']}")
        print(f"Startdatum: {coursedate}")
        print(f"Slutdatum: {course['endDate']}")




"""
for i in list:
    if 'startDate' in i:
        #print(i)
        print(i["startDate"])


# key === startdate
# value === innhållet efter; :
#










"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"
"""
"""
def main():
    pass


if __name__ == '__main__':
    main()
"""