# Задание№1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')

print()
