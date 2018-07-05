# Скопировать файл в выбранную директорию
# Пример:
# Введите путь к файлу:
# >>files/avatar.jpg
# Куда скопировать?
# >>files2/
# Готово!
import shutil

old_file = input('Введите путь к файлу:>>> ')
directory = input('Куда скопировать?:>>> ')


shutil.copy(old_file, directory)
print('Готово!')