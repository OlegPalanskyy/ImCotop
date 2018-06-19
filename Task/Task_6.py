# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.


def sort(t_list):
    a = []
    for i in range(1, len(t_list)):
        if t_list[i] > t_list[i - 1]:
            a.append(t_list[i])
    print(a)
    return a


n = [1, 5, 7, 5, 10, 45, 10]
sort(n)