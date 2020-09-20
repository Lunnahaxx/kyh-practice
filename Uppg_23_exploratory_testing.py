"2.0.Uppg_ "
"Task info"
"""
Den här uppgift går ut på att träna "exploratory testing", d.v.s att man prövar hur något system/API/program fungerar
genom att helt enkelt experimentera på ett systematiskt och kreativt sätt!

Vanligast är att testa ett användargränssnitt (UI/webbsida/system) som en användare, men i denna kurs lär vi oss 
programmering, så vi testa att försöka ta isär en inbyggd funktion! :)

Vi har alla sett funktionen som delar upp strängar i listor av strängar: split(), t.ex:

   "abc,def,ghi".split(",") ---> ["abc", "def", "ghi"]
   
Nu är er uppgift att hitta alla sätt som får split att "krasha" eller på annat sätt bete sig underligt. 
Pröva helt enkelt att skicka in "fel sorts argument", och samla ihop så många Exceptions 
(och annat udda beteende) som ni kan hitta!

Tips: Använd Python Console för att pröva snabbt. Dokumentera vad du hittar i split-observations.txt i ditt
kyh-practice repo.
"""
"-------------------------"
"Koden 2.0.Uppg_ "
"Lösningen"

test = "abc,def,ghi".split(",")
print(test)
"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"

"""
def main():
    pass


if __name__ == '__main__':
    main()"""
