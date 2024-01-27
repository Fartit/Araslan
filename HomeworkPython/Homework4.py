def guess_number():
    min_number = 1
    max_number = 100
    secret_number = 13
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать.")

    while True:
        attempts += 1
        user_input = input("Введите число от 1 до 100 (или 0 для выхода): ")

        if user_input == '0':
            print("Вы вышли из игры.")
            break

        try:
            guess = int(user_input)
        except ValueError:
            print("Ошибка! Введите целое число.")
            continue

        if guess < min_number or guess > max_number:
            print("Число должно быть в диапазоне от 1 до 100.")
            continue

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print("Вы угадали загаданное число с", attempts, "попытки.")
            break


guess_number()












