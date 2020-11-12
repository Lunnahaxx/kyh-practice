from uppgift36 import pwstrength
#from pwstrength import compute_strength(pw)

def main ():
    pw = input("Skriv ditt löseord: ")
    pwstrength.compute_strength(pw)


if __name__ == '__main__':
    main()