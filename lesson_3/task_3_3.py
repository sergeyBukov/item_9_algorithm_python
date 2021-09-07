# Задание№3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = [random.randint(0, 99) for _ in range(10)]
print(f'Созданный массив: {array}')

max_number = array[0]
min_number = array[0]

for i in array:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i
min_index = array.index(min_number)
max_index = array.index(max_number)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Массив после изменения элементов: {array}')
print(f'максимальное число: {max_number} и минимальное число: {min_number}')
