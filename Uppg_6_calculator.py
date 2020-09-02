import Uppg_7_calc


def run():
    print("This program will help with simple calculations. What do you want to do?")
    print("1 - add numbers")
    print("2 - subtract numbers")
    print("3 - multiply numbers")
    print("4 - divide numbers")
    answer = input(">> ")
    a = int(input("A="))
    b = int(input("B="))
    if answer == "1":
        result = Uppg_7_calc.add(a, b)
        print("Result = " + str(result))
    if answer == "2":
        result = Uppg_7_calc.subtract(a, b)
        print("Result = " + str(result))
    if answer == "3":
        result = Uppg_7_calc.multiply(a, b)
        print("Result = " + str(result))
    if answer == "4":
        result = Uppg_7_calc.divide(a, b)
        print("Result = " + str(result))


if __name__ == '__main__':
    run()
