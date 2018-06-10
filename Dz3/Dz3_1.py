"""
Написать функцию is_prime(a), Которая принимает число и возвращает
True или False в зависимости от того, простое это число или нет
"""

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

number = int(input('Введите число для провверки:'))
isprime = IsPrime(number)
print(isprime)