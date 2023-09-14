#Напишите функцию, которая принимает на вход строку —
#абсолютный путь до файла. Функция возвращает кортеж из трёх
#элементов: путь, имя файла, расширение файла.

import  re

def user_string():
    return input('Введите абсолютный путь файла ') #C:\Users\Username\Documents\file.txt

def string_parts(user_string_data):
    return re.split(r'[\\\.]', user_string_data)

def result(string_parts_data):
    print('Путь к файлу ', end='')
    for i in range(len(string_parts_data)-2):
        print(string_parts_data[i], '\\', end='')
    print()
    print('Имя файла ', string_parts_data[len(string_parts_data)-2])
    print('Разрешение файла ', string_parts_data[len(string_parts_data)-1])

result(string_parts(user_string()))