# Перевернуть список 
# [1, 2, 3, 4] -> [4, 3, 2, 1]


def fun(lst):
    lst_squer = []
    for i in range(len(lst) - 1, -1, -1):
        lst_squer.append(lst[i])
    print(lst_squer)
    return lst_squer


lst = [1, 2, 3, 4, 5, 6]
fun(lst)
