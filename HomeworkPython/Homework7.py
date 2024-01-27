import random
def q():
    a = input("Пожалуйста, введите число для генерации уникальных цифр от 1 до 9: ")
    try:
        s = int(a)
        if s > 0:
            return s
        else:
            print("Число должно быть больше 0.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число больше 0.")
    return q()
def w(s):
    numbers = random.sample(range(1, s + 1), s)
    print(numbers)

s = q()
w(s)











