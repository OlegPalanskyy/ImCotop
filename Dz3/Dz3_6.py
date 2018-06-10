"""
Решить рекурсивно задачу нахождения n-го числа фиббоначи
"""


def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(input('n = '))
print(fib(n))
