# Задание№4. Определить, какое число в массиве встречается чаще всего
import random

array = [random.randint(1, 10) for _ in range(20)]
print(f'Созданный массив: {array}')

max_index = 0
list_number = []
# находим максимальное кол-во повторений
for i in array:
    if array.count(i) > array.count(max_index):
        max_index = array.count(i)
# находим все числа с макимальным повторением
for i in array:
    if array.count(i) == max_index:
        list_number.append(i)
set_number = set(list_number)
print(f'Максимальное число повторений равно: {max_index} для чисел: {set_number}')
