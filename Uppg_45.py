"Uppg_45 "
"Task info"
"""
Vi har gått igenom "".format(..) och % (...) syntaxen. Här är en övning på detta!

1. Leta upp en tidigare lösning på en uppgift som innehåller f-strings. Gör en kopia på filen, 
och byt alla f-strings mot .format. Jämför filerna. Vilken syntax föredrar ni?

2. Gör om samma övning fast byt till % (...) syntaxen.
3. Går det att göra motsvarande {xyz:20}  m.h.a format() eller % syntaxen? D.v.s att kräva ett 
visst antal tecken utrymme vid utskrift. Googla och läs på, experimentera!

4. Samma som (3), fast för vänster, höger, mittenjustering (d.v.s det vi gör med <, > och ^ i f-strings).

Tips: % tuple syntaxen är mycket lik printf i C/C++, så om du kan det så känner du igen dig. 
T.ex. betyder %s sträng, och %d tal.
"""
"-------------------------"
"Koden Uppg_45.1 "
"Lösningen"

"45.1 och 2"
"från Olofs Uppg 18."
def main():
    # Vår telefonkatalog är "hårdkodad" i programmet, och representeras
    # av en dictionary (dict).
    people = {
        "Fredrik": "0702778511",
        "Olof": 123456789,
        "Lisa": "9999999999",
        "Bodil": "555-666-789"
    }

    # Jag lade till en while-true loop så man kan se vad man lägger
    # till i dict:en; det står inte egentligen i uppgiften om ni
    # undrar! :)
    while True:
        # f-string + len() för att skriva ut antal nummer
        #print("Det finns {} nummer i telefonkatalogen.".format(len(people))) #formaterad fr f"string till .format
        #print("Det finns %d nummer i telefonkatalogen."%(len(people))) #formaterad fr f"string till % formatet
        #print("Det finns {:15} nummer i telefonkatalogen.".format(len(people)))  #formaterad fr f"string till % formatet
        print("Det finns :15%d nummer i telefonkatalogen."%(len(people))) #formaterad fr f"string till % formatet
        svar = input("[S]lå upp eller [L]ägg till? ")
        svar = svar[0].upper()  # .upper gör alla tecken stora men här säger vi att index 0, alltså första bokstaven skall blir stor bokstav
        if svar == 'S':
            vem = input("Vem vill du ringa?")
            # Slå upp namnet användaren matar in m.h.a "in" keyword (lätt att läsa!)
            if vem not in people:
                # key fanns inte i dict
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                # key fanns i dict; ta reda på value m.h.a indexering som göra med raka klamrar
                # (precis som med listor fast nycklar måste inte vara heltal!)
                number = people[vem]
                print("Numret till %s är %d "%(vem, number))

        elif svar == 'L':
            namn = input("Ange personens förnamn: ")
            tfn = input("Ange telefonnummer: ")
            people[namn] = tfn

        else:
            print("Förstår inte, avbryter programmet.")
            # Avbryter while True och då tar main slut, d.v.s programmet avslutas
            # eftersom det inte står något mer i Pythonfilen på rad 69!
            break


if __name__ == '__main__':
    main()









"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"

