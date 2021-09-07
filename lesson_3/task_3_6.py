# Задание №6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

array = [random.randint(1, 100) for _ in range(10)]
print(f'Созданный массив: {array}')
# Находим макс и мин элемент
max_array = max(array)
min_array = min(array)
# удаляем макс и мин элементы из массива
for i in array:
    if i == max_array or i == min_array:
        array.remove(i)

        print(i)

sum_array = sum(array)
print(f'Сумма элементов массива между мин и макс элементами: {sum_array}')
