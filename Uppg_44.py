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
"Koden .Uppg_44.1 "
"Lösningen"
print("Uppgift 44.1. En namn och nummer övning för tuples.")

user_tuple=(input("Ange ditt namn: "), int(input("Ange din ålder: ")))
def user_info(user_infooo):
    print(f"Namn: {user_infooo[0]}\n"
          f"Ålder: {user_infooo[1]}")

user_info(user_tuple)

"Koden. Uppg_44.2"
print("\nUppgift 44.2 En funktionk med två tal som indata, som returnerar dessa i omvänd ordning")
num_tupp = (1, 2)
def switch(old_number):
    new_number = (old_number[1], old_number[0])
    return new_number

print(f"Detta är omvända siffror ifrån num_tup inputen {switch(num_tupp)}")


"Koden. Uppg_44.3"
print("\nUppgift 44.3")

ls = [1, 2, 3]
def list_to_Tuple(ls):
    t = (ls[0], ls[1], ls[2])
    return t
print(list_to_Tuple(ls))

"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"

