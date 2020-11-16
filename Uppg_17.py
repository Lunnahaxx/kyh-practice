from pathlib import Path
import sys
import time
#content_write = p.write_text()
#lines_write = content_write.splitlines()
#todo_lista = []
#answer = splitlines()
file = Path("todo.txt")
content = file.read_text(encoding='utf8')
content_ls = content.splitlines()
new_line = "\n"
new_line_print = print("\n")
#new_line_in_todo = content.append

#def cont_stuff():
#    file = Path("todo.txt")
#    content = file.read_text(encoding='utf8').splitlines()
#    return content

#del list[remove_number - 1]

"""def show_list(content_ls):
    for line in range(len(content_ls)):
        print(f"{line + 1}: {content_ls[line]}")"""

def show_list():
    """Alt 1"""
    uppgifter = "--Uppgifter listan--"
    print(f"\n{uppgifter:>24}")
    num = 0
    for elem in content_ls:
        num += 1
        print(f"Uppgift {num}. {elem}")
    print()


def add_task():
    """Alt 2"""
    ny_uppg = input("Skriv in vad du vill lägga till för en ny uppgift: ").strip()
    content_ls.append(ny_uppg)
    file.write_text(f"{new_line.join(content_ls)}", encoding='utf-8')
    print(f"Du la till: -{ny_uppg} i todolistan.\n")


def remove_task():
    """Alt 3"""
    show_list()
    remove_number = int(input("**Skriv numret på uppgiften du vill ta bort**: "))
    index = remove_number -1
    del content_ls[index]
    file.write_text(f"{new_line.join(content_ls)}", encoding='utf8') #gör listan till en sträng igen, joinar på \n.
    print(f"***Du valde att ta bort -Uppgift nr {remove_number}.- ***\n")


def close_program():
    """Alt 4"""
    print("Stänger programmet. ")
    #file.write_text(save_list(content))
    sys.exit()


def save_list(content_ls):
    return "\n".join(content_ls)


def user_input_meny():
    #file = Path("#t#odo.txt")
    #content = file.read_text(encoding='utf8').splitlines()
    answer = input("Vad vill du göra, ange ditt val mellan 1 -4: \n")
    print(f"--Du valde nummer {answer} --")
    time.sleep(2)
    #todo_list.append(file.read_text())
    return answer


def print_meny():
    meny = "---MENY---"
    print(f"{meny:>15}")
    print("1 - Öppna TODO listan")
    print("2 - Lägg till en ny uppgift")
    print("3 - Ta bort uppgift du är klar med")
    print("4 - Avbryt programmet")


def run():
    print("Detta är en Lunnehaxx todo-lista, välj ett val: ")
    while True:
        print_meny()
        answer = user_input_meny()
        if answer == "1":
            show_list()
        elif answer == "2":
            add_task()
            show_list()
        elif answer == "3":
            remove_task()
        elif answer == "4":
            close_program()
        else:
            print("Välj ett nummer mellan 1 - 4")
        #user_input()


if __name__ == '__main__':
    run()

"""def run():
    print("Detta är en Lunnehaxx todo-lista, välj ett val: ")
    #print("Detta är en Lunnehaxx todo-lista, välj ett val: ")
    #print("1 - Öppna TODO listan")
    #print("2 - Lägg till uppgift")
    #print("3 - Ta bort uppgift")
    #print("4 - Avbryt programmet")
    while True:
        print_meny()
        answer = user_input_meny()
        #meny = "---MENY---"
        if answer == "1":
            show_list()
        elif answer == "2":
            add_task()
            show_list()
            #user_input2 = input("Lägg till uppgift: " )
            #new_list.append(user_input2)
            #print("Du la till", user_input2, "i todo listan.")
            #x = new_list.join()
            #file.write_text(x)
            #CL p.write_text(input("Lägg till uppgift:"))
        elif answer == "3":
            remove_task()
            #print(file.read_text())
            #user_input3 = input("Vad önskas deletas?  ")
            #content_2 = remove_task(content)
            #todo_list.remove(user_input3)
            #file.write_text(f"{todo_list}")
        elif answer == "4":
            close_program()
            #print("Stänger programmet. ")
            #file.write_text(save_list(content))
            #sys.exit()
        else:
            print("Välj ett nummer mellan 1 - 4")
        #user_input()"""