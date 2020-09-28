"Task info"
"Uppg_39"
"""
Repetition och träning på funktioner!


1. Skriv en funktion som beräknar maximum av tre tal!
2. Skriv en funktion som summerar alla tal i en lista. 
Inbyggda funktionen sum() ska ej användas.
3. Skriv en funktion som räknar ut produkten (=multiplikation av alla tal) 
av en lista av heltal.
"""

""
#tal = input("Ange 3 tal med komma emellan: Ex. 1,3,4: ").split(',')


"39.1"
def add_sum_max(a, b, c):
    result = a + b + c
    return result

def add_sum_max_2(a, b):
    result = a + b
    return result

def sum_ls(ls):
    summa = 0
    for i in ls:
        summa += int(i)
    return summa

def multiply_all_in_ls(ls):
    ls = [1, 2, 3, 4, 5, 6, 7, 8]
    for numb in ls:
        result = numb * numb
    return result

#list = [1, 2, 3]

def run():
    print("Välj nedan vad du vill göra: ")
    print("1 - Beräknar maximum av tre tal.")
    print("11 - Beräknar maximum av två tal")
    print("2 - Summera alla tal i en lista.")
    print("3 - Räknar ut produkten (multiplikation av alla tal) av en lista av heltal.")

    answer = input(">> ")
    if answer == "1":
        a = int(input("A= "))
        b = int(input("B= "))
        c = int(input("C= "))
        result = add_sum_max(a, b, c)
    if answer == "11":
        a = int(input("A= "))
        b = int(input("B= "))
        result = add_sum_max_2(a, b)
    if answer == "2":

        lista = input("Ange värden till listan du vill summera med komma emellan: ").split(',')
        print(type(lista))
        print("Nu får du värden ifrån din lista: ")
        result = sum_ls(lista)

        #a = int(input("Ange listan du vill kalla på: 1=ls_1, 2=ls_2"))
        #if a == "1":
        #    result =
        #if a == "2":

    #if answer == "3":
    #    result = multiply_all_in_ls(a, b)

    print("Result = " + str(result))

if __name__ == '__main__':
    run()
    #ls = [1, 2, 3, 4, 5, 6,]
    #run = sum_ls(ls)
    #print(run)
"""
"39.2"

def sum_all_ls(a, b, c):
    num_ls = [1, 2 ,3, 4]
    for i in range(len(num_ls):
        print(a[i])
        a = num_ls[i]
    return
ls_2 =
print(length)
"""

#num_ls = [1, 2 ,3, 4]
#for i in range(len(num_ls)):
#    print(num_ls[i])
