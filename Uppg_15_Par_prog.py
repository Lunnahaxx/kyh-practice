#Driver

#Navigator

#Ordräknare

def wordcount(txt):
    return len(txt.split())

text = input("Mata in en kort mening: ")
count = wordcount(text)
print(f"Antal ord i inmatad text: {count}")