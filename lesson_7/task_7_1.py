# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
import time
import sys

def bubble_sort(sort):
    counter = 1
    while counter < len(sort):
        flag = True
        for i in range(len(sort) - counter):
            if sort[i] > sort[i + 1]:  # на уроке был знак < ,что приводит к сортировке от большего к меньшему числу
                sort[i], sort[i + 1] = sort[i + 1], sort[i]
                flag = False
        counter += 1
        if flag:
            break


size_array = 100
array = [randint(-100, 100) for _ in range(size_array)]
print(f'Исходный массив: {array}')

start = time.perf_counter()
bubble_sort(array)
stop = time.perf_counter() - start
print(f'Отсортированный массив: {array}')
print(f'Время выполнения функции: {stop}')
print(f'Занимаемая память: {sys.getsizeof(array)} байт')
