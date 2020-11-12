"Task info"
"Uppg_40"

"""
1. Skriv en funktion som "vänder" en textsträng baklänges - utan att använda 
"reverse" (eller [::-1])!
Använd istället strängar eller listor, och en for-loop.
T.ex. "12345" blir "54321".

2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver 
i strängen.

3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.
t.ex.
  inrange(value=1, min=2, max=3) blir False eftersom 1 ligger utanför 2 till 3.
  inrange(value=10, min=0, max=100) blir True eftersom 10 ligger mellan 0 och 100.
"""
"30.1"
print("Uppggift 30.2")
s = input("Låt oss skriva en lista baklänges, mata in dina fr 1 och uppåt med endast komma emellan: ").split(',')
lista = []
for i in s:
    lista.append(s)



ord_strang = "hej på dig"
#for i in range(-10, 6, 3): # sista siffran bestämmer hoppet
#    print(i)

for i in range(len(lista)-1, -1, -1):
    print(f"Lista: {i +1} ")
#for i in range(len(ord_strang) - 1, -1, -1):
#        for word in ord_strang:

#    print(f"Sträng: {i}")


"30.2"
print("\nUppggift 30.2")
print("Låt oss se vlika stora bokstäver det finns i en mening. ")
"""
#input()
#upper = []
def upper_letters(uppe):
    #sho_hoo = text_strang()
        #if upper_letters() in sho_hoo:
    print(f"{uppe}")
    #return sho_hoo
upper_letters("DETta ÄR EN StrÄNG AV stoRa bOkStävER. ")

letters = "DETta ÄR EN StrÄNG AV stoRa bOkstäver. "
upper_letters = [char for char in letters if char.isupper()]
print("Detta är de stora bokstäverna i meningen ovan, kan ser du budskapet?: " + str(upper_letters))
"""
"30.2 m David"

def caps(text):
    lista = []
    for char in text:
        if char.isupper():
            lista.append(char)
    lista_2 = len(lista)
    return lista_2

run = caps(text="Vad vIll Vi SKriva hÄR?")

print("Här antalet stora bokstäver i texten: ", run)


"30.3"
print(f"\nUppggift 30.3")
#inrange(value=1, min=2, max=3) = False #eftersom 1 ligger utan för 2 till 3.
#inrange(value=10, min=0, max=100) = True #eftersom 10 ligger mellan 0 och 100.
"""
Beskrivning:
Program för att komma om integer nummer är inom
 eller utanför ett område. 
"""
print("Låt oss kolla vilka tal som är innanför och utanför andra tal. ")
# Given range
A = int(input("Ange första talet A = "))
B = int(input("Ange andra talet B = "))

def checkRange(num):
   # using comaparision operator
   if A <= num <= B:
       print('Nummer {} är i området ({}, {})'.format(num, A, B))
   else:
      print('Nummer {} är utanför området ({}, {})'.format(num, A, B))

# Test Input List
testInput = [A - 1, A, A + 1, B + 1, B, B - 1]

for eachItem in testInput:
   checkRange(eachItem)