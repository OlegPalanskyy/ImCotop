# Найти номер (индекс) и значение первого положительного элемента списка.
import random


def gen_list(n):
    my_list = [random.randint(-999, 999) for j in range(n)]
    print(my_list)
    return my_list


def numbers(num):
    n = len(num)
    for i in range(n):
        if i == n:
            break
        if num[i] >= 0:
            print('index:' + str(i), 'number:' + str(num[i]))
            break
    return num


n = int(input('>>>'))
gen_list(n)
numbers(gen_list(n))