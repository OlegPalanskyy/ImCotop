"""
Дописать конвертер!
Дoлжен перехватывать все возможные ошибки, работать в цикле.
"""

converts = {'usd': 26.6,
            'eur': 30.8,
            }


def con_ver(convert):
    uah = int(input("введите сумму в гривнах ="))
    val = input("""Выберите валюту: \n usd \n eur \n""")
    sum_1 = uah / convert.get(val)
    print(uah, "грн", '=', sum_1 // 1)


def main():
        try:
            con_ver(converts)
        except TypeError:
            print('wrong volutes')
        except ValueError:
            print('is not a number')
        exit_1()


def exit_1():
    print('Продолжать?: \n y/n')
    inquiry = input('>>>')
    if inquiry == 'y':
        return main()
    elif inquiry == 'n':
        exit('Bye Bye')
    else:
        print('wrong')
        return exit_1()


main()
