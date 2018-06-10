'''
Написать функцию которая находит факториал числа.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


number_1 = int(input('Введите любое число:'))
calc_factorial = factorial(number_1)
print('Факториал ', number_1, 'равен =', calc_factorial)