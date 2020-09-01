def mainloop():


    import random

    n = random.randint(1, 3)
    print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilket.")

    antal_gissningar = 1

    while True:
        text = input("Din gissning: ")
        as_number = int(text)

        if as_number == n:
            print("Det var rätt du satte det på", antal_gissningar, "gissningar. ")
            break

        if as_number < n:
            print("Tyvärr fel, mitt nummer är högre. Försök igen!")
            antal_gissningar = antal_gissningar + 1

        if as_number > n:
            print("Tyvärr fel, mitt nummer är lägre. Försök igen!")
            antal_gissningar = antal_gissningar + 1

mainloop()