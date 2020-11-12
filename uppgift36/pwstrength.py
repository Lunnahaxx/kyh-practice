def compute_strength(pw):
    user_points = 0
    special = set("#%&+_-")
    if len(pw) > 10:
        user_points += 1
    if any(c.isalpha() for c in pw) and any(c.isdigit() for c in pw):
        user_points += 1
    #if not any(pw.isalnum() for c in pw):
    #    user_points += 1
    if any((c in special) for c in pw):
        user_points += 1
    if not any(c.isalpha() for c in pw) and not any(c.isdigit() for c in pw) and not any((c in special) for c in pw):
        user_points = 0
    print(f'Du fick {user_points} av 3 poäng')
    return user_points

if __name__ == '__main__':
    compute_strength()
