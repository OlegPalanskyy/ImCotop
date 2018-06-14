"""
Посчитать сумму первых двух четных чисел в списке
[5, 7, 8, 3, 4, 6, 8] -> 12
"""


def coun (input_list):
    summa = 0
    counter = 0
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            counter += 1
            summa += input_list[i]
        elif counter >= 2:
            break
    return summa



my_list = [5, 7, 4, 3, 4, 5,10]
print('Сумма 2х четных = ',coun(my_list))
