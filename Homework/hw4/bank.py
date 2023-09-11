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
                if count % 3 == 0:  # Действие для каждой третьей операции
                    commission = min(0.03 * amount, 600)  # Комиссия за пополнение счёта 3%,
                    # но не менее 30 и не более 600
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                    balance -= commission
                    print("Комиссия за каждую третью операцию: ", commission)
            else:
                print("Сумма пополнения должна быть кратна 50 у.е.")

        elif action == "2":
            amount = int(input("Введите сумму снятия: "))
            if amount % 50 == 0:
                if amount <= balance:  # сумма снятия должна быть не меньше баланса
                    commission = min(0.015 * amount, 600)  # комиссия за снятие 1,5%,
                    # но не менее 30 и не более 600
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                    balance -= (amount + commission)
                    count += 1
                    print("Снято: ", amount)
                    print("Комиссия за операцию: ", commission)
                    if count % 3 == 0:
                        commission = min(0.03 * amount, 600)
                        if commission < 30:
                            commission = 30
                        elif commission > 600:
                            commission = 600
                        balance -= commission
                        print("Комиссия за каждую третью операцию: ", commission)
                else:
                    print("Недостаточно средств на счете")
            else:
                print("Сумма снятия должна быть кратна 50 у.е.")

        elif action == "0":
            break

        else:
            print("Неверное действие")


bankomat()
