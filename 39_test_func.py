def sum_ls(ls): # ls = vad som står inom brackets på rad 7
    summa = 0
    for i in ls:
        summa += i
    return summa
list = [1, 3, 5]
print(sum_ls(list))