def is_it_too_long(name):
    return len(name) > 5

def main():
    students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    for name in students:
        if is_it_too_long(name):
            print(f"{name} är för långt!")


if __name__ == '__main__':
    main()

"""
12.1 Indentera koden så att programmet fungerar hos er!
12.2 Ändra så att användaren matar in studenternas namn separerade med ",".
12.3 Ändra så att de namn skrivs ut med Stor Bokstav i början.
12.4 Ändra så att användaren matar in maxlängden på ett namn, och om det blir en ValueError exception så antas värdet "5" gälla

Tips: Googla eller kör help(..) i Python Console på följande:
  strip, title, split"""
