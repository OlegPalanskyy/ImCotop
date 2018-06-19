# Дан список, содержащий положительные и отрицательные числа. Заменить все элементы списка на противоположные по знаку.
# Например, задан список [1, -5, 0, 3, -4].
# После преобразования должно получиться [-1, 5, 0, -3, 4].

import random


def gen_list(n):
    my_list = [random.randint(-999, 999) for j in range(n)]
    print('До: ', my_list)
    return my_list


def inver(rev):
    for i in range(len(rev)):
        if rev[i] < 0:
            rev[i] *= -1
        elif rev[i] > 0:
            rev[i] *= -1
    print('После: ', rev)
    return rev


inver(gen_list(10))