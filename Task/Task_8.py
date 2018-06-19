# Дан список чисел.
# Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

import random

LIST_SIZE = 5


def gen_list(n):
    my_list = [random.randint(-20, 20) for i in range(n)]
    print(my_list)
    return my_list


def analyser(my_list):
    counter = 0
    for i in range(1, len(my_list) - 1):
        if my_list[i - 1] < my_list[i] and my_list[i] > my_list[i + 1]:
            counter += 1
    return counter


lists = gen_list(LIST_SIZE)
print(analyser(lists))
