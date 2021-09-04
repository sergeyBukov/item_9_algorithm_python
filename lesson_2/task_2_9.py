# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

entered_list = input("Введите список чисел, разделенных пробелом: ").split()

num_list = [int(i) for i in entered_list]
max_number = num_list[0]

for i in num_list:
    if i > max_number:
        max_number = i
max_number_finish = max_number
sum_ = 0
while max_number != 0:
    sum_ = sum_ + max_number % 10
    max_number = max_number // 10
print(f'Наибольшее по сумме цифр число: {max_number_finish}, сумма цифр числа {sum_}')
