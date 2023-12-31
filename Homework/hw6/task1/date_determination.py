import sys


def is_leap_year(year):
    """
    Функция для проверки, является ли год високосным.
    Принимает год в качестве аргумента и возвращает True, если год високосный,
    False - если год не високосный.
    """
    if year % 4 != 0:  # Если год не делится на 4 без остатка, то он не високосный
        return False
    elif year % 100 != 0:  # Если год не делится на 100 без остатка, то он високосный
        return True
    elif year % 400 != 0:  # Если год не делится на 400 без остатка, то он не високосный
        return False
    else:
        return True  # В остальных случаях год високосный


def is_valid_date(date):
    """
    Функция для проверки, является ли дата корректной.
    Принимает дату в формате "DD.MM.YYYY" и возвращает True, если дата корректная,
    False, если дата неверная.
    """
    day, month, year = map(int, date.split('.'))  # Разбиваем строку на отдельные числа дня, месяца и года

    if year < 1 or year > 9999:  # Год должен быть в диапазоне от 1 до 9999
        return False

    if month < 1 or month > 12:  # Месяц должен быть в диапазоне от 1 до 12
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:  # Если месяц содержит 31 день
        if day < 1 or day > 31:  # День должен быть в диапазоне от 1 до 31
            return False
    elif month in [4, 6, 9, 11]:  # Если месяц содержит 30 дней
        if day < 1 or day > 30:  # День должен быть в диапазоне от 1 до 30
            return False
    elif month == 2:  # Февраль
        if is_leap_year(year):  # Если год високосный
            if day < 1 or day > 29:  # День должен быть в диапазоне от 1 до 29
                return False
        else:  # Если год не високосный
            if day < 1 or day > 28:  # День должен быть в диапазоне от 1 до 28
                return False

    return True


if __name__ == "__main__":
    date = sys.argv[1]  # Получаем дату из аргументов командной строки
    if is_valid_date(date):
        print("Дата существует")
    else:
        print("Дата не существует")
