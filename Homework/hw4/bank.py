def bankomat():
    balance = 0
    count = 0

    while True:
        print("Текущий баланс:", balance)
        action = input("Выберите действие (пополнить (1), снять (2), выйти (0)): ")

        if action == "1":
            amount = int(input("Введите сумму пополнения: "))
            if amount % 50 == 0:  # Если введенная сумма (amount) делится на 50 без остатка,
                # то она добавляется к текущему балансу (balance)
                balance += amount
                count += 1
                if count % 3 == 0:
                    commission = min(0.03 * balance, 600)
                    balance -= commission
                    print("Комиссия за операцию: ", commission)
            else:
                print("Сумма пополнения должна быть кратна 50 у.е.")

        elif action == "снять" or action == "2":
            amount = int(input("Введите сумму снятия: "))
            if amount % 50 == 0:
                if amount <= balance:
                    balance -= amount
            else:
                print("Недостаточно средств на счете")


bankomat()
