
def sum_numbers(*args):
    return sum(args)


def average_decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result / len(args)
    return wrapper


@average_decorator
def sum_and_average(*args):
    return sum(args)


numbers = [2, 3, 3, 4]
total_sum = sum_and_average(*numbers)
average = sum_numbers(*numbers)

print("Сумма чисел 2, 3, 3, 4 будет равно", average)
print("Среднее арифметическое чисел 2, 3, 3, 4 будет равно", total_sum)