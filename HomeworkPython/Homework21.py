
print("Вычислить количество отрицательных чисел в списке \n[-2, 3, 8, -11, 5, -3]")


def count_negative_numbers(arr):
    if not arr:
        return 0
    count = 1 if arr[0] < 0 else 0
    return count + count_negative_numbers(arr[1:])


arr = [-2, 3, 8, -11, 5, -3]
count = count_negative_numbers(arr)
print("Количество отрицательных чисел в списке:", count)
