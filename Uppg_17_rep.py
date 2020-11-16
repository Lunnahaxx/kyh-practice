from pathlib import Path

p = Path('Uppg_17_rep_todo.text')
text_ls = p.read_text(encoding='utf8').splitlines()

new_line = "\n"

text_str = "".join(text_ls) #join för att göra om det till en printsnygg sträng
print(f"Test print listan; {text_ls}\n")

def intro_print():
    """First print when program starts."""
    print('Välkommen till din todolista där, "Vad att göra härnäst, är frågan !" ')

def user_input():
    """Action of user input."""
    answer = input("Välj vad du vill göra genom att ange ett nummer: ")
    print(f"--Du valde nummer {answer} --\n")
    return answer

def show_task_list():
    """Alt 1."""
    order_number_print = 0
    uppgift = "--Uppgifter: --"
    print(f"{uppgift:>22}")
    for i in text_ls:
        order_number_print += 1
        print(f"Uppgift: {order_number_print} - {i}")
    print()


def add_task():
    """Alt 2"""
    print("Dessa saker finns på listan nu: ")
    show_task_list()
    new_task = input(f"Skriv en uppgift du vill lägga till: ").strip()
    text_ls.append(new_task)
    p.write_text('\n'.join(text_ls)) #", encoding='utf-8') #bygg en sträng för o kunna överföra
    print(f"Du la till {new_task} till todo-listan. \n")
    show_user_meny()


def remove_task():
    """Alt 3"""
    delete_task = input(f"**Ange numret på den uppgift du vill ta bort**: ")

    print(f"Du valde att ta bort Uppgift {delete_task}. \n")
    return delete_task


def end_program():
    print("Stänger ner programmet. ")

def show_user_meny():
    """Alt 5."""
    meny = "--MENY--"
    print(f"{meny:>12}")
    print("1 - Visa todo listan ")
    print("2 - Lägg till ny uppgift")
    print("3 - Ta bort en klar uppgift")
    print("4 - Avsluta programmet")
    print("5 - Visa denna menyn")

def main():
    intro_print()
    show_user_meny()
    while True:
        answer = user_input()
        if answer == "1":
            show_task_list()
        elif answer == "2":
            add_task()
        if answer == "3":
            show_task_list()
            remove_task()
            show_user_meny()
        if answer == "4":
            end_program()
            break
        elif answer == "5":
            show_user_meny()
        else:
            print("Ange ett nummer mellan 1 - 5. ")
if __name__ == '__main__':
    main()