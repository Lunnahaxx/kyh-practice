"2.0.Uppg_25 "
"15 Sept 2020"
"Task info"
"""
Fortsättning på uppgift 24 - mer om JSON och requests (webapi-anrop).

Nu ska vi bearbeta datan något med hjälp av Python och f-string tricken jag visade er!

25.1 Skriv ett Pythonprogram som skriver ut framtida kurstillfällen, på denna form:

Kursnamn:      Professional Scrum Product Owner (EN), 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-17

Kursnamn:      Professional Scrum Master, 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-16

Osv.

Det går bra att "hårdkoda" dagens datum: 2020-09-15, och använda som filter på startDate (det går att använda mindre
 än och större än tecken för att jämföra datumsträngar som är formatterade enligt YYYY-MM-DD, 
 mycket bra egenskap med det formatet!!)


25.2 Istället för att hårdkoda dagens datum, använd denna funktion:

    today = datetime.datetime.today()

"today" blir ett objekt med attribut som .year, .month och .day. Bygg ihop dagens datum dynamiskt (d.v.s när programmet
kör)!
"""
"-------------------------"
"Koden 2.0.Uppg_25 "
"Lösningen"
"""
Kursnamn:      Professional Scrum Product Owner (EN), 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-17

Kursnamn:      Professional Scrum Master, 15-16 september, Stockholm
Startdatum:    2020-09-15
Slutdatum:     2020-09-16
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
#Plats_1 =

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
    main()
