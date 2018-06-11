# Заменить элементы с нечетными номерами на 0
# [1, 1, 1, 1, 1] -> [1, 0, 1, 0, 1]


def fun(lst_squer):

    for j in range(1, len(lst_squer), 2):
        lst_squer[j] = 0
    print(lst_squer)
    return lst_squer


lst_squer = [1, 1, 1, 1, 1]
fun(lst_squer)