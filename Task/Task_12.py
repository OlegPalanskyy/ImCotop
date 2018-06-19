# Дан список значений. Превратить список в словарь поочередно превращая елементы в ключи и значения.
# [1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}


import random

LIST_SIZE = 10


def gen_list(n):
    my_list = [random.randint(-10, 10) for i in range(n)]
    print(my_list)
    return my_list


def dictionary(my_list):
    my_diction = {}
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_diction[my_list[i]] = my_list[i + 1]
    return my_diction


print(dictionary(gen_list(LIST_SIZE)))