# Задание №8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
matrix = []

for i in range(4):  # столбцы матрицы
    matrix.append([])
    sum_line = 0
    for n in range(4):  # строки матрицы
        user_number = int(input(f'Введите элемент {i+1}-ой строки и {n+1} столбца: '))
        sum_line += user_number
        matrix[i].append(user_number)
    matrix[i].append(sum_line)

for i in matrix:
    print(i)
