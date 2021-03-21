# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


my_file = open('test1.txt', 'w')
string = input('Введите текст \n')
while string:
    my_file.writelines(string)
    string = input('Введите текст \n')
    if not string:
        break

my_file.close()
my_file = open('test1.txt', 'r')
content = my_file.readlines()
print(content)
my_file.close()