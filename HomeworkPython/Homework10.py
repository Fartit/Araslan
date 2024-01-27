
num = list(input("Введите по порядку, без пробелов, элементы кортежа: "))
count_dict = {}
a = len(num)
print(num, "- количество элементов кортежа равно", a)
for n in num:
    count_dict[n] = count_dict.get(n, 0) + 1

for key, value in count_dict.items():
    print("количество", key, "=", value)

# num = input("Введите по порядку, без пробелов, элементы кортежа: ")
# count_dict = {}
#
# for n in num:
#     count_dict[n] = num.count(n)
#
# a = len(num)
# print(num, "- количество элементов кортежа равно", a)
#
# for key, value in count_dict.items():
#     print("количество", key, "=", value)