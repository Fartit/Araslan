symbol = input('Введите символ: ')
count = int(input('Введите количество символов: '))
orientation = int(input('Выберите ориентацию линии (0 - горизонтальная, 1 - вертикальная): '))

if orientation == 0:
    line = symbol * count
    print(line)
elif orientation == 1:
    while count > 0:
        print(symbol)
        count -= 1
else:
    print('Ошибка: некорректная ориентация линии')

