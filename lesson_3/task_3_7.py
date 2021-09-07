# Задание№7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

array = [random.randint(1, 100) for _ in range(10)]
print(f'Созданный массив: {array}')

new_array = sorted(array)
print(new_array[0])
print(new_array[1])
print(f'Два наименьших элемента: {new_array[0]} и {new_array[1]}')
