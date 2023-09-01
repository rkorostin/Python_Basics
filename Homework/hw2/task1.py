number = int(input("Введите целое число: "))

# Для проверки результата через hex - делаем доп переменную, которая ссылается на введённое число
check = number

# Создаем словарь для соответствия чисел и букв
digits = {
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f'
}

# Создаем список для хранения остатков от деления
remainder_list = []

# Остаток от деления на 16 добавляем в список и производим целочисленное деление
while number > 0:
    remainder = number % 16
    remainder_list.append(remainder)
    number = number // 16

# Создаем строку для хранения шестнадцатеричного представления
hex_string = '0x'

# Проходим по списку остатков в обратном порядке и добавляем символы в строку
for remainder in reversed(remainder_list):
    if remainder < 10:
        hex_string += str(remainder)
    else:
        hex_string += digits[remainder]

print("Шестнадцатеричное представление:", hex_string)
print("Шестнадцатеричное представление (через hex):", hex(check))
