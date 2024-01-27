import math


def calculate_area(choice, base, height):
    if choice == 1:
        area = base * height
    elif choice == 2:
        area = 0.5 * base * height
    elif choice == 3:
        area = math.pi * (base ** 2)
    else:
        area = 0

    return round(area, 2)


choice = int(input("Выберите фигуру (1 - прямоугольник, 2 - треугольник, 3 - круг): "))
if choice == 1:
    base = float(input("Введите длину прямоугольника: "))
    height = float(input("Введите высоту прямоугольника: "))
elif choice == 2:
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
elif choice == 3:
    base = float(input("Введите радиус круга: "))
    height = None
else:
    base = height = None

area = calculate_area(choice, base, height)
print(f"Площадь фигуры: {area}")










