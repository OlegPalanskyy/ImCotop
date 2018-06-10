'''
Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран.
'''


SYMBOL = '*'


def graph_builder(request):
    if request == 'квадрат':
        square_side = 10
        for i in range(1, square_side + 1):
            print(SYMBOL * square_side)
    elif request == 'треугольник':
        triangle_side = 10
        for i in range(1, triangle_side + 1):
            if i % 2 != 0:
                space_length = (triangle_side - i) // 2
                print(' ' * space_length + SYMBOL * i + ' ' * space_length)
    elif request == 'ромб':
        romb_length = 7
        for i in range(1, romb_length + 1):
            if i % 2 != 0:
                space_length = (romb_length - i) // 2
                print(' ' * space_length + SYMBOL * i)
        for i in range(romb_length - 1, 0, -1):
            if i % 2 != 0:
                space_length = (romb_length - i) // 2
                print(' ' * space_length + SYMBOL * i)
    elif request == 'елочка':
        start_point = 2
        n = 10
        triangle_height = n // 2
        if n % 2 != 0:
            triangle_height = (n + 1) // 2
            start_point = 1
        next_point = start_point
        for j in range(3):
            start_point = next_point
            if j == 0:
                for i in range(triangle_height):
                    print(' ' * ((n - start_point) // 2) + '*' * start_point)
                    if i < triangle_height - 1:
                        start_point += 2
            else:
                start_point += 2
                for i in range(1, triangle_height):
                    print(' ' * ((n - start_point) // 2) + '*' * start_point)
                    if i < triangle_height - 1:
                        start_point += 2

    elif request == 'лесинка':
        for i in range(10):
            print(' ' * i * 2 + '*' * i * 2)
            print(' ' * i * 2 + '*' * i * 2)

    else:
        print('ошибочный ввод')


# начало основной программы
user_input = input('Введите имя фигуры для отрисовки (квадрат, треугольник, ромб, лесинка, елочка): ').lower()
graph_builder(user_input)