

s = input("Введите рандомно текст и я выведу количество гласных букв: ")
count = 0
str_1 = set("оаиюяуеэ")
for str_2 in s:
    if str_2 in str_1:
        count += 1
print("Количество гласных букв равно: ", (count), ", зуб даю")