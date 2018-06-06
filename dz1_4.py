"""
Программа запрашивает у пользователя строку и
выводит ее по центру в таблице 20х3.
Пример 1:
Enter string:
elias
xxxxxxxxxxxxxxxxxx
x      elias      x
xxxxxxxxxxxxxxxxxx
Пример 2
Enter string:
O
xxxxxxxxxxxxxxxxxx
x        O        x
xxxxxxxxxxxxxxxxxx
"""
name = input('name: ')
line_1 = '*' * 20
len_line = len(line_1)
len_name = len(name)
line_2 = ' ' * int((len_line / 2) - (len_name / 2))

print(line_1)
print('*' + line_2 + name + line_2 + '*')
print(line_1)

