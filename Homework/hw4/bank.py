def bankomat():
    balance = 0

    while True:
        print("Текущий баланс:", balance)
        action = input("Выберите действие (пополнить (1), снять (2), выйти (0)): ")

        if action == "пополнить" or action == "1":
            amount = int(input("Введите сумму пополнения: "))
            if amount % 50 == 0:
                balance += amount
            else:
                print("Сумма пополнения должна быть кратна 50 у.е.")


bankomat()
