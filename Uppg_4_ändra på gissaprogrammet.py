"""Uppgift 4 - ändra på gissaprogrammet
Task assignment:
Genomför följande ändringar.

1. Fråga efter tal mellan 1 och 100 istället.
2. Översätt programmet till svenska!
3. Lägg till en ny variabel "antal_gissningar", som håller
reda på hur många gissningar användaren behövde för att hitta talet.
Skriv ut hur många gissningar efteråt."""

import random

n = random.randint(1, 20)
print("I'm thinking of a value between 1 and 30. Guess which?")

while True:
    text = input("Your guess: ")
    as_number = int(text)

    if as_number == n:
        print("Correct!")
        break

    if as_number < n:
        print("Wrong, my number is higher.. Try again!")

    if as_number > n:
        print("Wrong, my number is lower... Try again!")
