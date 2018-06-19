# Найти сумму и произведение элементов одномерного числового списка.
import random

LIST_SIZE = 2


def gen_list(n):
    my_list = [random.randint(-50, 50)for i in range(n)]
    print(my_list)
    return my_list


def sum_list(t_list):
    summ = 0
    mult = 1
    for i in range(len(t_list)):
        summ += t_list[i]
        mult *= t_list[i]
    print('Сумма', summ)
    print('Произведение', mult)
    return summ, mult


some_list = gen_list(LIST_SIZE)
sum_list(some_list)

