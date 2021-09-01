# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.
# разностороний а != b !=c; равнобедеренный a = b; равносторонний a = b = c
a = int(input("Введите длину первого отрезка = "))
b = int(input("Введите длину второго отрезка = "))
c = int(input("Введите длину третьего отрезка = "))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print(f'Треугольник со сторонами {a} {b} {c} - равносторонний')
    elif a == b or b == c or c == a:
        print(f'Треугольник со сторонами {a} {b} {c} - равнобедренный')
    else:
        print(f'Треугольник со сторонами {a} {b} {c} - разносторонний')
else:
    print(f'Треугольника со сторонами {a} {b} {c} не существует')
