"""
Запрограммировать следующее выражение:
 (a + b - f / a) + f * a * a - (a + b) Числа а, b, f вводятся с клавиатуры.
Организовать пользовательский интерфейс, таким образом, чтобы было понятно,
в каком порядке должны вводиться числа.
Пример:
1.Введите A: 1
2.Введите В: 1
3.Введите F: 1
4.Результат: 0

"""

first_number = float(input('Введите а: '))
second_number = float(input('Введите b: '))
third_number = float(input('Введите f: '))
result = ((first_number + second_number - third_number / first_number)
          + third_number * first_number ** - (first_number + second_number))
print('Результат =', result)
