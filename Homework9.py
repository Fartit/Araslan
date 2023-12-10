

def create_tuples():
    first_tuple = (1, 3, 3, 5, 4, 4, 4, 4, 2, 0)
    second_tuple = (-2, -3, -3, 0, -1, 0, -2, 0, -5, -1)
    third_tuple = first_tuple + second_tuple
    zero_count = third_tuple.count(0)
    return first_tuple, second_tuple, third_tuple, zero_count

first_tuple, second_tuple, result_tuple, zero_count = create_tuples()
print("Первый кортеж:", first_tuple)
print("Второй кортеж:", second_tuple)
print("Третий кортеж:", result_tuple)
print("Количество нулей:", zero_count)