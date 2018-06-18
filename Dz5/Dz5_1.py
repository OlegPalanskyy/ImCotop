# Написать функцию, которая генерирует список списков (двух мерный массив) размерности NxN заполненный
# случайными числами от 100 до 999 (использовать функцию random.randint(100, 999)
# >>gen_list(2)
# [[222, 113], [456, 500]]

import random


def gen_list(n):
    my_list = [[random.randint(100, 999) for j in range(n)]for i in range(n)]
    return my_list


my_list = int(input('размер списка: '))
print(gen_list(my_list))