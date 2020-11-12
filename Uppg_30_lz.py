num = []

tal = input("Ange tal med komma emellan: 11,2,3,4,5,6,7100: ").split(",")
back = ', '.join(list(reversed(tal)))
for i in tal:
    num.append(int(i))

print(f"Första talet:{tal[0]}\nSista talet:{tal[-1]}\nSumman av talen:{sum(num)}\nTalen baklänges: {back}")

print(f"Udda tal: {tal[0:len(tal):2]}")
print(f"Jämna tal: {tal[1:len(tal):2]}")