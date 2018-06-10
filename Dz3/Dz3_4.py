"""
. Написать функцию, которая определяет количество разрядов введенного целого числа.
Пример:
>> func(40)
>> 2
>> func(404)
>> 3

"""


def cel(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i


number = abs(int(input('Введите число:')))
sum_1 = cel(number)
print(sum_1)

