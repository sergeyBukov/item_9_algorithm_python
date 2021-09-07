# Задача №5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

array = [random.randint(-100, 100) for _ in range(10)]
print(f'Созданный массив: {array}')

negative_list = []
for i in array:
    if i < 0:
        negative_list.append(i)

print(f'В массиве минимальный отрицательный элемент: {max(negative_list)}.\n'
      f'Находится в массиве на позиции {array.index(max(negative_list))}')
