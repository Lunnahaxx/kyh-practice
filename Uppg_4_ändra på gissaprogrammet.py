"""Uppg_8.1 - titta igenom alla program hittills ni byggt i kyh-practice,
och byt ut till f-strings där det behövs.
-
Uppgift 4 - ändra på gissaprogrammet
Task assignment:
Genomför följande ändringar.

1. Fråga efter tal mellan 1 och 100 istället.
2. Översätt programmet till svenska!
3. Lägg till en ny variabel "antal_gissningar", som håller
reda på hur många gissningar användaren behövde för att hitta talet.
Skriv ut hur många gissningar efteråt."""


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
