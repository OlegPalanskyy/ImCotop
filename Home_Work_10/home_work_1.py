# Переписать информацию с одного файла в другой

save_some_text = open('old_file.txt', 'w')
test_text = input('Some text here...>>>')
save_some_text.write(test_text)
save_some_text.close()

if __name__ == '__main__':
    with open('old_file.txt') as file:
        copy = file.read()
    with open('new_file.txt', 'w') as new_file:
        new_file.write(copy)