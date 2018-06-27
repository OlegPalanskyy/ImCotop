"""
Напишите программу калькулятор, реализующую операции (+ - * /).
Программа выдает сообщение в случай некорректных данных и продолжает работу.
"""
def calculate():
        sumbl = input("Операция +  -  *  /: ")
        x = int(input("x = "))
        y = int(input("y = "))
        if sumbl == "+":
            result = x + y
        elif sumbl == "-":
            result = x - y
        elif sumbl == "*":
            result = x * y
        elif sumbl == "/":
            result = x / y
        print(result)


def main():
    try:
        calculate()
    except ZeroDivisionError:
        print("Деление на 0 невозможно!")
    except ValueError:
        print("Введеное значение не является числом!")
    except UnboundLocalError:
        print("Вы указали несуществующую операцию")
    calculate()


main()