n = int(input('Введите n: '))
figur = int(input("""
Выбеоите фигуру:
1:Квадрат  
2:Триугольник
3:Ромб
4:Елочка
5:Лесенка
"""))
# Квадрат
if figur == 1:
    print('Квадрат')
    for i in range(n):
        print('*' * n)


# Триугольник
if figur == 2:
    print('Триугольник')
    start_point = 2
    triangl = n // 2
    if n % 2 != 0:
        triangl = (n + 1) // 2
        start_point = 1
    for i in range(triangl):
        print(' ' * ((n - start_point) // 2) + '*' * start_point)
        start_point += 2

# Ромб
if figur == 3:
    print('Ромб')
    start_point = 2
    triangle_height = n // 2
    if n % 2 != 0:
        triangle_height = (n + 1) // 2
        start_point = 1
    for i in range(triangle_height):
        print(' ' * ((n - start_point) // 2) + '*' * start_point)
        if i < triangle_height - 1:
            start_point += 2
    for i in range(triangle_height - 1, 0, -1):
        start_point -= 2
        print(' ' * ((n - start_point) // 2) + '*' * start_point)

# fir
if figur == 4:
    print('Елочка')
    start_point = 2
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

# stairs
if figur == 5:
    print('Лесинка')
    for i in range(n):
        print(' ' * i * 2 + '*' * i * 2)
        print(' ' * i * 2 + '*' * i * 2)


