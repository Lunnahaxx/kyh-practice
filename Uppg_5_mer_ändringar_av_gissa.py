"""Uppg_8.1 - titta igenom alla program hittills ni byggt i kyh-practice,
och byt ut till f-strings där det behövs.
-
Uppgift 5 - mer ändringar av gissa.
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

max_number = 100
n = random.randint(1, max_number)


print(f"Jag tänker på ett nummer mellan 1 och {max_number}. Du skall nu gissa vilket.")
antal_gissningar = 1
antal_gissningar = antal_gissningar + 1

def mainloop():

    def ask_number():
        text = input("Vad är din gissning? ")
        tal = int(text)
        return tal


    while True:

        as_number = ask_number()

        if as_number == n:
            break



        if as_number < n:
            print("Tyvärr fel, mitt nummer är högre. Försök igen!")

        if as_number > n:
            print("Tyvärr fel, mitt nummer är lägre. Försök igen!")

mainloop()
print("Det var rätt du satte det på", antal_gissningar, "gissningar. ")