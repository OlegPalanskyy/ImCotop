# Написать программу запрашивающую у пользователя его имя при первом запуске.
# При последующих запуска программа должна обращаться по имени. Хранить имя последнего юзера в файле.
# Пример
# - Первый запуск:
# Привет! Введи свое имя!
# >>Алексей
# Привет, Алексей!
# 1. Закрыть программу
# 2. Сменить имя.
#
# - Последующие запуски:
# Привет, Алексей!
# 1. Закрыть программу
# 2. Сменить имя.

USER_FILE = 'user.txt'


def user_name(filename):
    with open(filename, 'w') as user:
        name = input('Привет! Как тебя зовут?:\n >>>')
        user.write(name)


def main(file):
    with open(file) as file:
        string = f'Привет, {file.read()}!\n1. Закрыть программу\n2. Сменить имя'
        print(string)
        user_options = 0
        while user_options not in ['1', '2']:
            user_options = input('>>>')
            if user_options == '2':
                user_name(USER_FILE)
                return main(USER_FILE)


user = USER_FILE
main(user)
