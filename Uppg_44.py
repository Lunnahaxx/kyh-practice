"Uppg_44 "
"Task info"
"""
Lek med tuppler! (Tuples)

1. Bygg ett program som tar in användarens namn och ålder. 
Lagra resultatet i en tuppel (str, int). Skicka tuppeln till 
en funktion, som skriver ut:

  Namn: <name>
  Ålder: <age>

.. ja ni fattar :)

2. Bygg en funktion som tar en tuppel med två tal som indata, 
och returnerar dessa i omvänd ordning. T.ex.

    t = (5, 6)
    print(swaptuple(t))

.. ska ge följande utskrift:

    (6, 5)

3. Bygg en funktion som tar in en lista ls, och returnerar en 
tuppel som bygger på listan. T.ex.

     print(to_tuple([1, 2, 3]))

... ska ge:

    (1, 2, 3)
 
"""
"-------------------------"
"Koden .Uppg_ "
"Lösningen"
user_tuple=(input("Ange ditt namn: "), int(input("Ange din ålder: ")))
def user_info(user_infooo):
    print(f"namn: {user_infooo[0]}\n"
          f"Ålder: {user_infooo[1]}")

user_info(user_tuple)



"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"

