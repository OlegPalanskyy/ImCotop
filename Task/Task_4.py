# В списке найти минимальный и максимальный элементы, поменять их местами
import random

LIST_SIZE = 5


def gen_list(n):
    my_list = [random.randint(-50, 50)for i in range(n)]
    print(my_list)
    return my_list


def sort(t_list):
    max_number = 0
    min_number = 0
    for i in range(len(t_list)):
        if t_list[i] > max_number:
            max_number = t_list[i]
            index_max = i
        elif t_list[i] < min_number:
            min_number = t_list[i]
            index_min = i

    t_list[index_max] = min_number
    t_list[index_min] = max_number

    return t_list


list_random = gen_list(LIST_SIZE)
print(sort(list_random))

