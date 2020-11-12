"Uppg_30"
"Task info"
"""
Träna slicing av strängar och listor!

Reg.nr på bilar i Sverge skrivs traditionellt* med tre bokstäver och tre siffror.

1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
var för sig; använd slicing-syntax för att dela upp inputsträngen.

Ex.

Ange regnr: ABC663
Bokstävsgrupp: ABC
Siffergrupp: 663

2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, 
och skriver ut följande:
    Ange tal med komma emellan: 1,2,3,5,100
    Första talet: 1
    Sista talet: 100
    Summan av talen: 111
    Talen baklänges: 100, 5, 3, 2, 1

Tips: Använd slicing och inbyggda funktionen sum().
Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
   är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
   Pröva båda :)

*numera kan det vara bokstäver i sifferdelen också. Det gör ont att se men 
det är moderna tider!
"""
"-------------------------"
"Koden Uppg_30 "
"Lösningen"
heltal = input("Ange tal med komma emellan: 1,2,3,5,100 ").split(',')
num = []

for i in heltal:
    num.append(int(i))
#print(f"Första talet {heltal[0]} \nSista talet: {heltal[-1]} \nSumman av talen: {sum(num)} \nTalen baklänges: {heltal[::-1]}")
print(heltal.reversed())



#tal = input("Ange tal med komma emellan: ").split(',')
#print(sum(num))

#print(int()"Summan av talen:" + sum(heltal))
#print(heltal.reverse())
#heltal_2 = inte
#print()

#summan = gör en int och loopa uppräkningen

#Summan av talen: {sum(heltal)}
#\nTalen baklänges: {heltal[]}
"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"
"""30.1 reg_nr_1 = input("Skriv in reg nr: ")
print(f"Bokstävsgrupp: {reg_nr_1[0:3]} \nSiffergrupp: {reg_nr_1[3:6]}")
"""

"-------------------------"
"-------------------------"


