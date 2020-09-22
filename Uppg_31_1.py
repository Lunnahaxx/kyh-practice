#num = []


tal = input("Ange tal med komma emellan: Ex. 1,3,4,5,6,100: ").split(',')
summa = [int(elem)for elem in tal]
baklanges = ', '.join(list(reversed(tal)))
print_talen = ' ,'.join(tal)

od_even = ' ,'.join(tal)

even = [num for num in tal if int(num) % 2 == 0] #Dett är ett exempel på list comprehension
odd = [num for num in tal if int(num) % 2 == 1]

print(f"Första talet: {summa[0]}\nSista talet: {summa[-1]}\nSumman av talen: {sum(summa)}\nTalen baklänges: {baklanges}\n")
print(f"Antal tal: {len(tal)}")
print("Talen:", print_talen)

print(f"Varannat udda index: {od_even[0:len(od_even):2]}")
print(f"Varannat jämna index: {od_even[1:len(od_even):2]}")

print("\nNya jämna tal: " + ', '.join(even))
print("Nya udda tal: " + ', '.join(odd))



"""
"Från nätet"
for i in tal():
    if i % 2 == 0:
        print("Jämnt")
    else:
        print("Ojämn")
"""

'''
"Från nätet"
numlist = []

number = int(input("Enter total number of elements: "))
for i in range(1, number + 1):
    value = int(input("Enter Value of %d Element: "))
    numlist.append(value)

print("\nOdd numbers in this list are: ")
for j in range(number):
    if(numlist[j] % 2 != 0):
        print(numlist[j], end='')
'''


'''
"Från nätet"
n = int(input("Enter a number:"))
if n % 2 == 0:
    print("Jämnt")
else:
    print("Ojämn")
'''


'''
"Från nätet"
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
'''


'''
"Från nätet"
 #Python program to print odd Numbers in a List

# list of numbers
list1 = input("Nummer: ")
list = list1.split(',')
# iterating each number in list
for num in list:

    # checking condition
    if num % 2 != 0:
       print(num, end = " ")
'''