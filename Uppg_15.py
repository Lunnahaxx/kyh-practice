"""Ett litet potpurri av småproblem att lösa tillsammans!

15.1 Implementera "wordcount" som jag och Christoffer byggde
15.2 Ta in en godtycklig text (testa att copy-paste från lorumipsum.com) och skriv ut hur många vokaler som finns
 i strängen. Tips: "a" in "abcd" är True!
15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
    runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
    vem = input(“Ange löpare du söker placering för”)"""

"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua."""

vowels = "aeiou"
lorem_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempo"
lowercase = lorem_string.lower()

vowel_counts = {}

for vowel in vowels:
    count = lowercase.count(vowel)

    vowel_counts[vowel] = count

print(vowel_counts)



"""a_string = "orem ipsum dolor sit amet, consectetur adipiscing elit"
lowercase = a_string.lower()

vowel_counts = []

for vowel in a_string:
    count = vowel
    print("It was", (vowel_counts), "i meningen.")


#def wordcount(txt):
#    return len(txt.split())


#text = input("Skriv en mening så räknar vi vokalerna: ")
#count = wordcount(text)


#print(f"Antal ord i inmatad text: {count}")"""