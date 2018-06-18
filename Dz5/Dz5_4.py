"""
Написать функцию сортировки списка (любым алгоритмом)
"""


import random


def gen_list(n):
    my_list = [[random.randint(100, 999) for j in range(n)]for i in range(n)]
    return my_list


def sorted_list(a):
    a = sorted(a)
    print(a)


my_list = int(input('размер списка: '))
my_l = gen_list(my_list)
print(my_l)
sorted_list(my_l)