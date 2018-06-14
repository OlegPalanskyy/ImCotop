# Заменить каждый элемент на следующий, последний на первый
# [1, 2, 3, 4] -> [4, 1, 2, 3]


def sort(t_list):
    n = list(t_list)
    t_list[0] = t_list[-1]
    for i in range(len(t_list) - 1):
        t_list[i + 1] = n[i]
    return t_list


n = [1, 2, 3, 4]
print(sort(n))