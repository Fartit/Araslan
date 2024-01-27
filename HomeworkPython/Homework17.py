


print("Введите два целых числа в диапазоне от 97 до 122 включительно")

while True:
    try:
        a = int(input("Введите первое случайное число: "))
        b = int(input("Введите второе случайное число: "))
        if 97 <= a <= 122 and 97 <= b <= 122:
            break
        else:
            raise ValueError
    except ValueError:
        print("Некорректный ввод. Числа должны быть целыми и в диапазоне от 97 до 123.")

a, b = min(a, b), max(a, b)

print("Символы в возрастающем порядке:")
for i in range(a, b + 1):
    print(chr(i), end=" ")
