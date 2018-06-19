# Из одномерного списка удалить все повторяющиеся элементы(дубликаты)
#  так, чтобы каждое значение встречалось в списке только один раз.


import random

LIST_SIZE = 10


def gen_list(n):
    my_list = [random.randint(-100, 100) for i in range(n)]
    print(my_list)
    return my_list


def function(my_list):
    n = []
    for i in my_list:
        if i not in n:
            n.append(i)
    return n

print(function(gen_list(LIST_SIZE)))