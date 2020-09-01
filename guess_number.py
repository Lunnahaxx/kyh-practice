def mainloop():

    def ask_number():
        text = input("Vad är din gissning?")
        tal = int(text)
        return tal

    import random

    n = random.randint(1, 3)
    print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket.")

    antal_gissningar = 1

    while True:

        answer = ask_number()

        if answer == n:
            print("Det var rätt du satte det på", antal_gissningar, "gissningar. ")
            break
        antal_gissningar = antal_gissningar + 1

        if answer < n:
            print("Tyvärr fel, mitt nummer är högre. Försök igen!")

        if answer > n:
            print("Tyvärr fel, mitt nummer är lägre. Försök igen!")

mainloop()