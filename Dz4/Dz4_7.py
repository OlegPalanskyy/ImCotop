"""
Отсортировать список методом пузырьковой сортировки.
"""

def sort_func(input_list):
    n = 1
    while n < len(input_list):
        for i in range(len(input_list) - n):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        n += 1
    return input_list


data = [4, 1, 5, 3, 6]
print('Список до сортировки', data)
print('Список после сортировки', sort_func(data))