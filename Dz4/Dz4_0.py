'''
Дан список чисел, заменить каждое число на квадрат этого числа.
[1, 2, 3, 4] -> [1, 4, 9, 16]
'''


def namber(lst):
    lst_squer = []
    for i in lst:
        lst_squer.append(i * i)
    print(lst_squer)


lst = [1, 2, 3, 4]
namber(lst)
