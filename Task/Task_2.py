#  Найти сумму положительных элементов списка
import random


def my_func(num):
    a = [random.randint(-999, 999)for i in range(num)]
    print(a)
    return a


def my_sum(num_sum):
    sum = 0
    for i in range(len(num_sum)):
        if num_sum[i] >= 0:
            sum += num_sum[i]
    print(sum)
    return sum


n = int(input('>>>'))
my_sum(my_func(n))
