# В одномерном списке удалить все четные элементы и оставить только нечетные.


import random

LIST_SIZE = 10


def gen_list(n):
    my_list = [random.randint(-100, 100) for i in range(n)]
    print(my_list)
    return my_list


def delite(my_list):
    list_a = []
    for i in range(len(my_list)):
        if i % 2:
            list_a.append(my_list[i])
    return list_a


print(delite(gen_list(LIST_SIZE)))