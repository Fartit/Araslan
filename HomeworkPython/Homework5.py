n = int(input("n = "))
a = []
sum_non_zero = 0
count_non_zero = 0

for _ in range(n):
    num = int(input("-> "))
    if num != 0:
        a = a + [num]
        sum_non_zero += num
        count_non_zero += 1

if count_non_zero != 0:
    average = sum_non_zero / count_non_zero
    print(f"Среднее арифметическое ненулевых элементов: {average}")
else:
    print("Введены только нулевые элементы.")













