import date_determination

while True:
    date = input("Введите дату в формате DD.MM.YYYY: ")
    if "." not in date:
        print("Некорректный ввод. Пожалуйста, введите дату с точками в формате 'DD.MM.YYYY'")
        continue
    if not date.replace(".", "").isdigit():
        print("Некорректный ввод. Пожалуйста, введите дату только цифрами.")
        continue
    if date_determination.is_valid_date(date):
        print("Дата существует")
        break
    else:
        print("Дата не существует")

'''
Введите дату в формате DD.MM.YYYY: 29.2.1959
Дата не существует
Введите дату в формате DD.MM.YYYY: 29.2.1960
Дата существует
'''
