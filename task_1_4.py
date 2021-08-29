""" Написать программу, которая генерирует в указанных пользователем границах
случайное целое число, случайное вещественное число, случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный
символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random

# Далее все действия идут без проверок вводимых символов!

x = str(input("Для генерации случайного целого числа введите - 'i': " 
                    "для генерации случайного вещественного числа введите - 'v': "
                    "для генерации случайного символа введите - 'c': "))
n = int(input("Введите начальную границу диапазона: "))
m = int(input("Введите конечную границу диапазона: "))

if x == "i":
    print(f'Случайное целое число из выбранного вами диапазона = {random.randint(n, m)}')
elif x == "v":
    print(f'Случайное вещественное число из выбранного вами диапазона = {random.uniform(n, m)}')
else:
    print(f'Случайное символ из выбранного вами диапазона = "#")') #без цикла не могу
