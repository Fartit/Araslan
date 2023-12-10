# # name = "Bob"  # инициализация переменной
# # print("Hello,", name)
# age = 20.4
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))
# print(type(age))  # int - 20, float - 20.4
# print(type(text))  # str - "Hello"
# a = False  # True
# print(a)
# print(type(a))  # bool - True, False
import random
import time


# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))


# a = b = c = 1
# print(a)
# print(b)
# print(c)


# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)


# name_new = "Bob"
# print(name_new)


# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 10
# b = 20
# print("a:", a)
# print("b:", b)
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# a, b = b, a
# print("a:", a)
# print("b:", b)


# print("Строка символов")
# print('Строка \nсимволов \rfile.text')
# print('Строка \nсимволов D:\\folder\\file.text')


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# # print(s1, ",", s2, "!")
# print(s3 * 5)


# print(46545456545456454)
# print(4.665565656566545456545456454)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.5
# print(6 // 2)  # 3
# print(6 // 4)  # 1
# print(6 ** 2)  # 36
# print(6 % 4)  # 2

# a = 5
# b = 7
# c = 3
#
# sum1 = a + b + c
# proiz1 = a * b * c
# arifmet1 = sum1 / 3
#
# print("Сумма:", sum1)
# print("Произведение:", proiz1)
# print("Среднее арифметическое:", arifmet1)


# урок 2

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 320
#
# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12

# num = 4321
# print("Исходное число:", num)
# a = num % 10  # 4
# print(a)
# num //= 10
# print(num)  # 432
# b = num % 10
# print(b)  # 2
# num //= 10
# print(num)  # 43
# c = num % 10
# print(num)  # 4


# num = 4325  # => 432
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# 3

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)  # 23
# res = float(num1) + num2  # 5
# print(res)

# print(int(3.8))
# print(round(3.89, 2))
# print(type(round(3.89, 2)))

# name = "Вова"
# age = 20
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="___", end=" ")
# print("Я учу Python.")

# name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# res = num ** power
# print("Число", num, "В степени", power, "Равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)  # 1+5
# print(b2 + 5)  # 0+5

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# test = None
# print(test)

#  print(7 == 7)
# # print(2 + 5 == 7)
# # print(7 != 10 - 7)
# # print(8 > 5)
# # print(8 < 5)
# # print(9 <= 9)
# # print(9 >= 9)
# # print("привет" > "ПРИВЕТ")

# print(2 < 4 < 9)  # 2 < 4 < 9  => True && True => True
# print(2*5>7>=4+3)  # True && True
# print(3*3<=7>=2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False:False)
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False:False)

# print(9 - 7)
# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 25
# b = 15
# if a > b:
#     print("a>b")
# elif a < b:
#     print("a<b")
# else:
#     print("a == b")


# a = int(input('vvedite a = '))
# b = int(input('vvedite b = '))
# c = int(input('vvedite c = '))
# if a == b == c:
#     print('treugolnik ravnostoronniy.')
# elif a == b or a == c or b == c:
#     print('treugolnik ravnobedrennuy.')
# else:
#     print('treugolnik raznostoronniy.')


# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <=5:  # (day >= 1) and (day <= 5):
#     print('Рабочий день - ', end="")
#     if day == 1:
#         print('пон')
#     if day == 2:
#         print('вт')
#     if day == 3:
#         print('ср')
#     if day == 4:
#         print('чт')
#     if day == 5:
#         print('пт')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end="")
#     if day == 6:
#         print('суб')
#     if day == 7:
#         print('вс')
# else:
#     print('Такого дня недели не существует')


# урок 3


# n = int(input('Введите количество ворон: '))
# if 0 <= n <= 9:
#     print('На ветке', n, end=' ')
#     if n == 1:
#         print('ворона')
#     elif 2 <= n <= 4:  # n == 2 or n == 3 or n == 4
#         print('вороны')
#     else:
#         print('ворон')
# else:
#     print('Ошибка ввода данных')


# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case _:
#         print('Логин не найден')


# day = 'вторник'
# time = 14
#
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 13 or 15<= time <= 16:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('такого дня недели не существует или не рабочее время')


# a, b = 30, 20
#
# print(a if a < b else b)
# if a< b:
#     print(a)
# else:
#     print(b)


# a, b = 30, 20
#
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# ии придумал
# a = int(input("Введите числитель: "))
# b = int(input("Введите знаменатель: "))
#
# result = a / b if b != 0 else "На ноль делить нельзя"
#
# print("Результат:", result)


# a = 5
# b = 1
# print("на ноль делить нельзя " if b == 0 else a / b)
# print(a/b)


# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')
#
# print('Следующая строка')


# try:
#     n = int(input('введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')


# try:
#     n = int(input('введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки или Нельзя делить на ноль')
# else:  # когда в блоке try не возникло исключения
#     print('всё нормально. вы ввели числа', n, 'и', m)
# finally:  # выполнится в любом случае
#     print('Конец программы')


# n = input('введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
#
# try:
#     result = int(num1) + int(num2)
# except ValueError:
#     result = str(num1) + str(num2)
#
# print("Результат:", result)


# Циклы
# while


# i = 0
# while i < 9:
#     print('i =', i)
#     i += 1


# num = 2
# # while num <= 20:
# #     print(num)
# #     num += 2


# n = int(input('кол-во символов:'))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1


# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print(res)


# Урок 4

# n = input('Введите целое число: ')
# while type(n) != int and type(n) != float:
#     try:
#         n = int(n)
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print('Число не целое!')
#             n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершён')


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break


# result = 1
#
# while True:
#     number = int(input("Введите число: "))
#
#     if number == 0:
#         break
#
#     result *= number
#
# print("Результат:", result)


# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=' ')
#     i += 1
# else:
#     print('\nЦикл окончен, i =', i)


# j = 1
# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j +=1
#     i += 1


# таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('*', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(' ', end='')
#         j += 1
#     print('*')
#     i += 1


# for element in collection:
#     print(element)


# for i in "Hello", "World", "!":
#     print(i)


# for element in range(n):
#     print(element)


# print(list(range(5)))

# range(start, stop, step)


# for i in range(9, 0, -2):
#     print(i, end=' ')
#
#
# print()
# i = 9
# while i > 0:
#     print(i, end=' ')
#     i -= 2


# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')


# a = int(input("Ведите целое число: "))
# for i in range(11, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

#
# def guess_number():
#     min_number = 1
#     max_number = 100
#     secret_number = 13
#     attempts = 0
#
#     print("Добро пожаловать в игру 'Угадай число'!")
#     print("Я загадал число от 1 до 100. Попробуйте угадать.")
#
#     while True:
#         attempts += 1
#         user_input = input("Введите число от 1 до 100 (или 0 для выхода): ")
#
#         if user_input == '0':
#             print("Вы вышли из игры.")
#             break
#
#         try:
#             guess = int(user_input)
#         except ValueError:
#             print("Ошибка! Введите целое число.")
#             continue
#
#         if guess < min_number or guess > max_number:
#             print("Число должно быть в диапазоне от 1 до 100.")
#             continue
#
#         if guess < secret_number:
#             print("Загаданное число больше.")
#         elif guess > secret_number:
#             print("Загаданное число меньше.")
#         else:
#             print("Вы угадали загаданное число с", attempts, "попытки.")
#             break
#
#
# guess_number()

# урок 5


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')


# for i in range(3):  # 0 1 2
#     print('+++ i=', i)
#     for j in range(2):  # 0 1
#         print('_____ j =', j)


# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         print('$', end='')
#     print()


# w = int(input('введите ширину прямоугольника: '))
# h = int(input('введите высоту прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('$', end='')
#         else:
#             print(' ', end='')
#     print()


# nums = [letter for letter in 'banana']
# nums = [i for i in range(18) if i % 2 == 0]
# print(nums)


# Список (list)
# nums = [8, 3, 9, 4, 1, 'one']
# print(nums)
# print(type(nums))
#
# print(nums[0])
# print(nums[2])
# # print(nums[6])  # IndexError
# print(nums[-1])
# print(nums[-2])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)


# nums = [8, 3, 9, 4, 1,]
# print(nums)
# # print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] ** 2)


# s = []
# print(s)
#
# b = list('hello')
# print(b)


# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10)))
# print(list(range(2, 10 + 1, 2)))


# [выражение For переменная in последовательность]
# a = [0 for i in range(5)]
# print(a)
#
# b = [i for i in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)


# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)


# a = [0] * int(input('vvedite  kolichestvo elementov cpicka: '))
# print(a)
# for i in range(len(a)):
#     a[i] = input('->')
# print(a)


# a = [input('-> ') for i in range(int(input('n = ')))]
# print(a)


# n = int(input('Введите количество элементов списка: '))
# a = [int(input('-> ')) for _ in range(n)]
#
# sum_negative = sum([num for num in a if num < 0])
# print('Сумма отрицательных элементов:', sum_negative)


# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# j = 0
# for i in a:
#     if i < 0:
#         j += i
# print(j)


# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
#
# for i in a:
#     print(i, end=' ')


# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n))
# #     if n[i] % 22 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print('sum нечетных элементов: ', s)
# print('count четных элементов: ', k)


# n = list(range(21, 41))
# print(n)
# a = 2
# print(n[a])
# print(n[a-1])
# print(n[a+1])


# a = [int(input('-> ')) for _ in range(int(input('n = ')))]
# print(a)
# # for i in range(len(a)):
# #     # print(a[i], '-> ', end='')
# #     # print(a[i - 1])
# #     if a[i] > a[i - 1]:
# #         print(a[i], end='')
#
# for i in a:
#     if i > i - 1:
#         print(i, end='')


# урок 6


# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a[1:4])
# # print(a[1:])
# # print(a[:1])
# # print(a[:3])
# print(a[5:2:-1])
# b = a[10:20]
# print(b)


# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1:8:2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:-6:-1])
# print(a[2:5])


# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# # s[2:5] = []
# # del s[1]
# del s[:]
# print(s)


# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет элемент(второй параметр), в заданный индекс(первый параметр)
# print(s)
# s.insert(-1, 200)
# print(s)


# s = []
# n = int(input('кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
#
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:  # 2
#     for j in b:  # 4
#         if i in c:  # если i находится в с
#             continue
#         if i == j:  # 3 == 3
#             c.append(i)
#             break
#
# print(c)  # [2,1,4,3]


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5, 9, 6]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])  # Добавляем i-й элемент из списка a в список c
#     c.append(b[i])  # Добавляем i-й элемент из списка b в список c
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])  # Добавляем i-й элемент из списка a в список c
# #         c.append(b[i])  # Добавляем i-й элемент из списка b в список c
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])  # Добавляем i-й элемент из списка a в список c
# #         c.append(b[i])  # Добавляем i-й элемент из списка b в список c
# #     for i in range(len(b), len(a)):
# #         c.append(a[i])
# print(c)


# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# s.remove(9)  # удаляет элемент по заданному значению
# print(s)
# s.pop()  # без параметров - удаляет последний элемент из списка
# a = s.pop(-1)  # передаём индекс ля удаления элемента
# print(a)
# print(s)
# s.clear()
# print(s)


# # numbers = [int(input('-> ')) for _ in range(int(input('n =')))]
# numbers = [6, 4, 7, 8, 9]
# index = int(input('Введите индекс удаляемого элемента: '))
# numbers.pop(index)
# print(numbers)


# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(-9)  # считает кол-во заданных значений в списке
# # print(num)
#
# ind = s.index(-9)  # возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(9, 5)
# print(ind)


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# result = []
#
# for a in s:
#     if s.count(a) == 1:
#         result.append(a)
#
# for a in result:
#     print(a, end=' ')


# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# result = []
#
# for i in range(len(s)):
#     a = False
#     for j in range(len(s)):
#         if i != j and s[i] == s[j]:
#             a = True
#             break
#     if not a:
#         result.append(s[i])
#
# for d in result:
#     print(d, end=' ')


# урок 7


# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print('a =', a)
# print('b =', b)
# a.append(20)
# print('a =', a)
# print('b =', b)
# b.append(120)
# print('a =', a)
# print('b =', b)


# a = [5, 4, 1, 2, 3]
# print(a)
# # a.reverse()  # перестраивает списки в обратном порядке
# # print(a)
# #
# #
# # a.sort()  # метод для сортировки
# # print(a)
# a.sort(reverse=True)
# print(a)


# b = ['bob', 'dog', 'qwe', 'jastin']
# b.sort(key=len, reverse=True)
# print(b)


# a = [5, 4, 1, 2, 3]
# print(a)
#
# sort = sorted(a)
# print(sort)


# a = [5, 4, 1, 2, 3]
# print(a)
# a.sort()
# print(a)


# a = [5, 4, 1, 2, 3]
# print('a =', a)
# print(id(a))
# a.sort()
# print(id(a))
# sort = sorted(a)
# print(sort)
# print(id(sort))


# генерация случайных данных

# import random
# print(random.random())
# print(random.randint(3, 9))  # (3, 9) - от 3 по 9
# print(random.randrange(3, 9, 2))  # (3, 9) - от 3 до 9
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ('qwrr', 'djhf', 'iuwh', 'bfbsh', 'hfbhjk')
# # print(random.choice(city_list))
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)
#
# s = [55, 66, 77, 88, 99, 3, 5, 6, 4, 2, 7, 9, 7]
# print(random.choices(s, k=5))


# lst = ['5', '4', '3', '2', '1']
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))


# a = ['5', '4', '3', '2', '1']
# # # res = 0
# # # for i in a:
# # #     res += i
# # # print(res)
# # print(sum(a))


# sum_ = 5
# print(sum_)
#
# s = [55, 66, 77, 88, 99, 3, 5, 6, 4, 2, 7, 9, 7]
# print(sum(s))


# import random
# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)


# import random
# my_list = []
# for _ in range(10):
#     my_list.append(random.randint(1, 100))
# max_element = max(my_list)
# print(max_element)
# my_list.remove(max_element)
# my_list.insert(0, max_element)
# print(my_list)


# import random
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print('min = ', min_ch)
#
# ind_min = lst.index(min_ch)
# print('index min =', ind_min)
#
# del lst[0: ind_min]
# print(lst)
# # print(lst[ind_min:])


# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
#
# print('a' not in x)
# print('e' not in x)


# lst = [5]
# print(bool(lst))
# # if len(lst) == 0:
# if not lst:
#     print('список пустой')
# else:
#     print('в списке есть элементы')


# import random
#
# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print('первый список: ', a)
# print('второй список: ', b)
# c = a + b
# print('третий список: ', c)
#
#
# c = []
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# print('элемент обоих списков без повторений: ', d)
#
#
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print('элементы общие для двух списков: ', c)
#
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]


# # m = ['hello', 'world']
#
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col], end='\t')
# #     print()
#
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()


# урок 8

# w, h = 4, 3
# # matrix = [[0 for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# w, h = 4, 3
# matrix = [[random.randint(-20, 10) for x in range(w)]for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#         if x < 0:
#             m += 1
#     print()
#
# print('кол-во отрицательных элементов: ', m)


# for x, y in [[1.9, 2.2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)


# import math
# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# import math as m
# from math import sqrt, ceil
# from math import *
#
# num1 = sqrt(4)
# num2 = ceil(3.1)
# print(num1)
# print(num2)


# import time
# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
#
# seconds = time.time()
# print('кол-во секунд: ', seconds)
#
# locale_time = time.ctime(seconds)
# print('местное время: ', locale_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep="")
#
# print(time.strftime('Сегодня: %B %d, %Y'))
# # print(time.strftime('%d.%m.%Y, %H:%M:%S'))

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# Function
# print()
#
#
# def hello(name):
#     print('hello,', name)
#
#
# hello('irina')
# hello('igor')


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'def')


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'x', '0')


# def get_sum(a, b):
# #     print('sum: ', end='')
# #     return a + b
# #
# #
# # x = 2
# # y = 5
# # res = get_sum(x, y)
# # print(res * 2)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def print_cubes():
#     for num in range(1, 11):
#         cube = num ** 3
#         print(cube)
#
# print_cubes()

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# def cube(a):
#     str = ''
#     for i in range(0, a + 1):
#         str += f'{i} в кубе = {i ** 3}\n'
#     return str
#
#
# res = cube(10)
#
# print(res)


# def change(lst):
#     print(lst)
#     symbol1 = lst.pop(0)
#     symbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def change(lst):
#     symbol1 = lst.pop(0)
#     symbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0, symbol2)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 10
# b = 15
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, 'больше', b)
# else:
#     print(b, 'больше', a)


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('введите пароль:')
# if check_password(p):
#     print('это надёжный пароль')
# else:
#     print('это ненадёжный пароль')


# урок 9


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(n1, n2, d=n4))


# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, '*')
# set_param(s='#')


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print('Сумма чётных цифр:')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print('\nСумма нечётных цифр:')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# display_info('Bob', age=23, name='Ira')  # typeerror


# Изменяемые и неизменяемые объекты


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # true
# print(lt1 is lt2)  # false
#
# a = 'Hello'
# b = 'Hello'
# print(id(a))
# print(id(b))
# print(a == b)  # true
# print(a is b)  # true

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# # 72
# # 48


# n = ['hello', 'python']
# b = tuple('n')
# print(type(b))
# print(b)

#
# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])
# print(a[1:3])
# # a[1] = 3  # не работает - typeerror


# from random import randint
# s = tuple(randint(0, 100) for i in range(5))
# # s = tuple(int(input('-> ')) for i in range(5))
# print(s)


# t1 = tuple('hello')
# t2 = tuple('world')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)


# t1 = tuple('hello')
# t2 = tuple('world')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# for i in t3:
#     print(i, end=' ')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             ...
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))


# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# print(x, y, z)


# t = (1, 2, 3)
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# first_name, year, married = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)


# урок 10


# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# print(ptl1)


# countries = (
#     ('bali', 80.2, (('berlin', 3.326), ('dubai', 1.718))),
#     ('moscow', 66, (('phuket', 2.2), ('chili', 1.6)))
# )
# print(countries, end='\n\n')
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:', country_name, 'население =', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'население =', city_population)























