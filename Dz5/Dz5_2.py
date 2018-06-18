"""
Написать функцию, которая выводит двухмерный список в виде таблицы
Пример
>>print_list([[222, 113], [456, 500]])
—————
| 222 | 113 |
—————
| 456 | 500 |
—————
"""
import random


def gen_list(n):
    my_list = [[random.randint(100, 999) for j in range(n)]for i in range(n)]
    return my_list


def list_decorator(list_1):
    for i in range(len(list_1)):
        print('-' * (4 * len(list_1[i]) + 1))
        for j in range(len(list_1[i])):
            if j == 0:
                print('|' + str(list_1[i][j]) + '|', end='')
            else:
                print(str(list_1[i][j]) + '|', end='')
        print()
    print('-' * (4 * len(list_1[i]) + 1))


if __name__ == '__main__':

    list_decorator(gen_list(random.randint(2, 3)))