"""Uppgift 5 - mer ändringar av gissa.
Task assignment:
Vi har gått igenom funktioner i teorin, nu blir det praktik!

1. Ändra så att hela while-loopen ligger i en funktion som heter
"mainloop", och testa så att programmet fungerar fortfarande.
2. Bygg en funktion "ask_number" som returnerar ett heltal som
användaren matar in.
3. Ändra på mainloop så att den returnerar antal gissningar
användaren använt sig av, och skriv ut antalet utanför mainloop,
inte  inuti.

def ask_number():
    text = input("Vad är din gissning?")
    tal = int(text)
    return tal"""


import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Du skall nu gissa vilket.")

antal_gissningar = 1

while True:
    text = input("Vad är din gissning: ")
    as_number = int(text)

    if as_number == n:
        print("Det var rätt du satte det på", antal_gissningar, "gissningar. ")
        break
    antal_gissningar = antal_gissningar + 1

    if as_number < n:
        print("Tyvärr fel, mitt nummer är högre. Försök igen!")

    if as_number > n:
        print("Tyvärr fel, mitt nummer är lägre. Försök igen!")
