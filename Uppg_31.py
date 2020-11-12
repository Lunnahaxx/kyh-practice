num = []

tal = input("Ange tal med komma emellan: 1,2,3,5,100: ").split(",")
back = ', '.join(list(reversed(tal)))
for i in tal:
    num.append(int(i))

print(f"Första talet:{tal[0]}\nSista talet:{tal[-1]}\nSumman av talen:{sum(num)}\nTalen baklänges: {back}")

