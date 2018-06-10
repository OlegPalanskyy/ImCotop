'''
Написать функцию, которая выводит на экран n первых четных чисел.
'''


def finder(user_number):
    j = 0
    for i in range(1, 3 * user_number):
        if i % 2 == 0:
            print(i)
            j += 1
        if j >= user_number:
            break


n = int(input('Введите кол-во четных чисел:'))
finder(n)
