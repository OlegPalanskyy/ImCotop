
# Дан список чисел, заменить каждый отрицательный элемент на следующий
# [1, 2, -3, 5, -6, 7, -9] -> [1, 2, 5, 5, 7, 7, -9]


def fun(numbers):
    n = len(numbers)
    for i in range(n):
        if i == n - 1:
            break
        if numbers[i] <= 0:
            numbers[i] = numbers[i + 1]
    return numbers


numbers = [1, 2, -3, 5, -6, 7, -9]
print(fun(numbers))