# Для запроса ввода числа
def input_number(input_text):
    print(input_text)
    while True:
        try:
            number = int(input())
            if number <= 0 or number > 100000:
                print("Ошибка: введите число от 1 до 100000")
            else:
                return number
        except ValueError:
            print("Ошибка: введите целое число")

# Для проверки числа на простоту
def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = input_number("Введите целое число от 1 до 100000: ")

if check_prime(number):
    print("Число", number, "является простым")
else:
    print("Число", number, "является составным")