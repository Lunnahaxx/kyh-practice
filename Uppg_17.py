"""Bygg ett program där användaren ser denna meny:

1. Lista TODO
2. Lägg till uppgift
3. Ta bort uppgift
4. Avbryt programmet

Programmet ska spara en fil "TODO.txt" som läses in i början, och innehåller en
 lista med saker att göra.
Listan kan manipuleras med alternativ 2 och 3.

När programmet avslutas sparas listan till TODO.txt (skrivs över).

Detta är ett miniprojekt! Jag rekommenderar att ni fortsätter jobba
tillsammans utanför lektionstid för att bli klara.
Diskutera hur ni ska lösa uppgiften först tillsammans."""


#content_write = p.write_text()
#lines_write = content_write.splitlines()


#todo_lista = []
#answer = splitlines()



from pathlib import Path

#file = Path("todo.txt")
#content = file.read_text(encoding='utf8').splitlines()
#lines = content.splitlines()


print("Detta är en Lunnehaxx todo-lista, välj ett val: ")
print("1 - Öppna TODO listan")
print("2 - Lägg till uppgift")
print("3 - Ta bort uppgift")
print("4 - Avbryt programmet")

todo_list = []
#todo_list.append(file.read_text())



def user_input():
    file = Path("todo.txt")
    content = file.read_text(encoding='utf8').splitlines()
    answer = input("Gör ditt val: ")

    while True:

        if answer == "1":
            print(content)
        elif answer == "2":
            user_input2 = input("Lägg till uppgift: ")
            todo_list.append(user_input2)
            file.write_text(f"{todo_list}")


            #CL p.write_text(input("Lägg till uppgift:"))
        elif answer == "3":
            print(file.read_text())
            user_input3 = input("Vad önskas deletas?: ")
            todo_list.remove(user_input3)
            file.write_text(f"{todo_list}")

        elif answer == "4":
            quit()
        else:
            print("Välj ett nummer mellan 1 - 4")
        user_input ()


if __name__ == '__main__':
        user_input()