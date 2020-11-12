from uppgift36.pwstrength import compute_strength

def test_password_with_length_11_gives_1_point2():
    pw = '1' * 11
    assert compute_strength(pw) == 1

def test_password_with_length_5_gives_5_gives_0_points2():
    pw = "1" * 5
    assert compute_strength(pw) == 0

def test_password_with_length_11_gives_1_point():
    pw = '1' * 11
    assert compute_strength(pw) == 1

def test_password_with_length_5_gives_5_gives_0_points():
    pw = "1" * 5
    assert compute_strength(pw) == 0

def test_password_is_isalpha_and_isdigita_gives_1_point():
    pw = 'abc1234'
    assert compute_strength(pw) == 1

def test_password_is_not_isalpha_and_isdigita_gives_0_point():
    pw = 'abc'
    assert compute_strength(pw) == 0

def test_password_is_not_isalpha_and_isdigita_gives_0_point():
    pw = '123'
    assert compute_strength(pw) == 0

def test_password_is_a_special_gives_1_point():
    pw = '#%&+_-'
    assert compute_strength(pw) == 1

def test_if_none_as_char_gives_0_point():
    pw = '123'
    assert compute_strength(pw) == 0


#att vid #%&+_- +1 poäng
#att vid ej #%&+_- +0 p





