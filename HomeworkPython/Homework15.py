
circle_area = lambda r: 3.14159 * r ** 2
print("площадь окружности, где радиус = 2 то, будет:", circle_area(2))

rectangle_area = lambda length, width: length * width
print("площадь прямоугольника, где ширина = 10, длина = 13 то, будет:", rectangle_area(10, 13))

trapezoid_area = lambda a, b, h: (a + b) * h / 2
print("площадь трапеции, где длина нижнего основания = 7, верхнего основания = 5, высота = 3 то, будет:", trapezoid_area(7, 5, 3))
