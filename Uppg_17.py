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

from pathlib import Path
p = Path("todo.txt")

def main():
    print("Detta är en todo-lista, välj ett val: ")
    print("1 - Öppna TODO listan")
    print("2 - Lägg till uppgif")
    print("3 - Ta bort uppgift")
    print("4 - Avbryt programmet")

    answer = input(">> ")
    if answer == "1":

    if answer == "2":

    if answer == "3":

    if answer == "4":


if __name__ == '__main__':
        main()