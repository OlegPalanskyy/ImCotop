# Дан список чисел.
# Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

import random

LIST_SIZE = 5


def gen_list(n):
    my_list = [random.randint(-50, 50) for i in range(n)]
    print(my_list)
    return my_list


def analyser(my_list):
    for i in range(len(my_list)):
        if (my_list[i] < 0 and my_list[i + 1] < 0) or (my_list[i] >= 0 and my_list[i + 1] >= 0):
            return [my_list[i], my_list[i + 1]]
    return 'такой пары нет'


lists = gen_list(LIST_SIZE)
print(analyser(lists))
