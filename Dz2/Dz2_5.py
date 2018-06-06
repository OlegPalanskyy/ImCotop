"""Напишите программу, запрашивающую имя, фамилия,
отчество и номер группы студента и выводящую введённые данные в следующем виде:
 ******************************
 *Лабораторная работа № 1   *
 *Выполнил(а): ст. гр. ЗИ-123 *
 *Иванов Андрей Петрович    *
 ******************************
Необходимо, чтобы программа сама определяла нужную длину рамки.
Сама же длина рамки зависит от длины наибольшей строки внутри рамки.
 Используя циклы for легко можно выровнять стороны рамки.
"""
name = input('Введите имя:')
surname = input('Введите фамилию:')
patronymic = input('Введите отчество:')
group_number = input('Введите номер группы')

lines = ['Лабораторная работа № 1', 'Выполнил(а): ст. гр. ' + group_number, surname + ' ' + name + ' ' + patronymic]
max_length = []

for i in range(3):
    max_length.append(len(lines[i]))

if max_length[0] > max_length[1] and max_length[0] > max_length[2]:
    max_length_1 = max_length[0]
elif max_length[1] > max_length[0] and max_length[1] > max_length[2]:
    max_length_1 = max_length[1]
else:
    max_length_1 = max_length[2]

length = max_length_1 + 4

print('*' * length)
for i in range(3):
    last_space = length - max_length[i] - 2
    print('*' + lines[i] + ' ' * last_space + '*')
print('*' * length)


