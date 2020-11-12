"2.0.Uppg_ "
"Task info"
"""

"""
"-------------------------"
"Koden 2.0.Uppg_ "
"Lösningen"

"-------------------------"
"-------------------------"
"Förklaring till Lösningen på Koden"

"-------------------------"
"-------------------------"
from Uppg_39 import maximum, sum_ls, multiply_all_in_ls

# 39.1 test av funktion för att skriva ut högsta numret
def test_1_maximum_highest_numb_a():
    a = 60
    b = 34
    c = 4
    assert maximum(a, b, c) == 60

def test_2_maximum_highest_numb_b():
    assert maximum(3, 60, 34) == 60
    #man kan skriva värdena för a, b, c direkt i
    # paranteserna istället

def test_3_maximum_highest_numb_c():
    #a = 34
    #b = 3
    #c = 60
    assert maximum(3, 34, 60) == 60

def test_4_maximum_highest_numb_c():
    #a = 34
    #b = 3
    #c = 60
    assert maximum(1, 1, 1) == 1

def test_1_not_maximum_numb_a():
    #a = 34
    #b = 60
    #c = 3
    assert maximum(3, 60, 3) != 59

def test_2_not_maximum_numb_b():
    #a = 34
    #b = 60
    #c = 3
    assert maximum(3, 60, 34) != 59

def test_3_not_maximum_numb_c():
    #a = 34
    #b = 60
    #c = 3
    assert maximum(3, 60, 34) != 59

# 39.2 test av funktion för summan av en lista
def test_1_sum_ls():
    a = [1, 1, 2]
    assert sum_ls(a) == 4

def test_2_sum_ls():
    a = [3, 3, 3]
    assert sum_ls(a) == 9

def test_3_not_sum_ls():
    a = [3, 4, 3]
    assert sum_ls(a) != 9

# 39.3 test av funktion för produkten av en lista
def test_1_mulitply_all_in_ls():
    m = [3, 3]
    assert multiply_all_in_ls(m) == 9

def test_2_mulitply_all_in_ls():
    m = [3, 3, 3]
    assert multiply_all_in_ls(m) == 27

def test_2_mulitply_all_in_ls():
    m = [3, 3, 3]
    assert multiply_all_in_ls(m) != 22

def main():
    pass


if __name__ == '__main__':
    main()
