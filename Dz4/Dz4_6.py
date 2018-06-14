"""
Дан список строк. Посчитать количество символов в первой строке где есть символ ‘а’.
[‘‪fur’, ‘skin’, ‘coat’, ‘pelage’, ‘jack‬’] -> 4 # len(‘coat’)
"""

def find_name(input_list):

    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == 'a':
                return i, len(input_list[i])

data = ['fur', 'skin', 'coat', 'pelage', 'jack‬']
print('Номер индекса строки с символом ‘а’ #', find_name(data)[0], \
        'Количество символов = ', find_name(data)[1])
