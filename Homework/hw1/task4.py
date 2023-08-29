from random import randint

# Нижняя и верхняя границы
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

# Число, которое нужно угадать
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

# Кол-во попыток
attempts = 10


# Проверка на ввод корректного числа
def input_number(input_text):
    while True:
        try:
            number = int(input("Введите число от {} до {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
            if LOWER_LIMIT <= number <= UPPER_LIMIT:
                return number
            else:
                print("Число должно быть от {} до {}".format(LOWER_LIMIT, UPPER_LIMIT))
        except ValueError:
            print("Введите целое число")


# Выводим сообщение о начале игры
print("Угадайте число от", LOWER_LIMIT, "до", UPPER_LIMIT, "за", attempts, "попыток")

# Начинаем цикл, в котором пользователь будет угадывать число
while attempts > 0:
    # Запрашиваем у пользователя ввод числа
    guess = input_number("Введите число: ")

    # Уменьшаем счетчик попыток на 1
    attempts -= 1

    if guess == secret_number:
        print("Вы угадали число!")
        break

    if guess < secret_number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

    print("Осталось попыток:", attempts)

# Если цикл закончился, а число не угадано, выводим сообщение о проигрыше
if attempts == 0:
    print("Вы проиграли. Загаданное число было", secret_number)
