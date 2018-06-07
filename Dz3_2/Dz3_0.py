"""
Написать аналог функции len:

"""
def my_len(len):
    counter = 0
    for lens in len:
        counter += 1
    return counter


name = input()
new = my_len(name)
print(new)