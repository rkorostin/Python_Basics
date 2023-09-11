def bankomat():
    balance = 0
    count = 0
    operations = []

    def add_balance(balance, amount):
        """
        Функция пополнения счёта. Принимает текущий баланс и пополняемую сумму
        """
        nonlocal count  # 'count' является нелокальной переменной и должна быть доступна
        # из внешней области видимости.
        if amount % 50 == 0:  # Если введенная сумма (amount) делится на 50 без остатка,
            # то она добавляется к текущему балансу (balance)
            balance += amount
            count += 1
            operations.append("Пополнение на сумму: " + str(amount))  # Логирование операций
            if balance > 5000000:  # если баланс более 5_000_000, то вычитается налог на богатство 10%
                tax = 0.1 * amount
                balance -= tax
                print("Налог 10% на богатство: ", tax)
                operations.append("Налог на богатство: " + str(tax))
            if count % 3 == 0:  # Действие для каждой третьей операции
                commission = min(0.03 * amount, 600)  # Комиссия за пополнение счёта 3%,
                # но не менее 30 и не более 600
                if commission < 30:
                    commission = 30
                elif commission > 600:
                    commission = 600
                balance -= commission
                print("Комиссия 3% за каждую третью операцию пополнения: ", commission)
                operations.append("Комиссия за каждую третью операцию пополнения: " + str(commission))
        else:
            print("Сумма пополнения должна быть кратна 50")
        return balance, count, operations

    def withdraw_balance(balance, amount):
        """
        Функция снятия со счёта. Принимает текущий баланс и сумму для снятия
        """
        nonlocal count
        if amount % 50 == 0:
            if amount <= balance:  # сумма снятия должна быть не меньше баланса
                if balance > 5000000:
                    tax = 0.1 * amount
                    balance -= tax
                    print("Налог 10% на богатство: ", tax)
                    operations.append("Налог на богатство: " + str(tax))
                elif count % 3 == 0:
                    commission = min(0.03 * amount, 600)
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                    balance -= commission
                    print("Комиссия 3% за каждую третью операцию: ", commission)
                    operations.append("Комиссия за каждую третью операцию снятия: " + str(commission))
                else:
                    commission = min(0.015 * amount, 600)  # комиссия за снятие 1,5%,
                    # но не менее 30 и не более 600
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                    balance -= (amount + commission)
                    count += 1
                    print("Снято: ", amount)
                    print("Комиссия 1.5% за операцию: ", commission)
                    operations.append("Снято средств: " + str(amount))
                    operations.append("Комиссия за операцию снятия: " + str(commission))
            else:
                print("Недостаточно средств на счете")
        else:
            print("Сумма снятия должна быть кратна 50")
        return balance, count, operations

    def show_operations(operations):
        """
        Функция для просмотра истории операций
        """
        print("Операции:")
        for i in range(len(operations)):
            print("Операция", i + 1, ": ", operations[i])

    while True:
        print("Текущий баланс:", balance)
        action = input("Выберите действие (пополнить (1), снять (2), история операций(3), выйти (0)): ")

        if action == "1":
            amount = int(input("Введите сумму пополнения: "))
            balance, count, operations = add_balance(balance, amount)

        elif action == "2":
            amount = int(input("Введите сумму снятия: "))
            balance, count, operations = withdraw_balance(balance, amount)

        elif action == "3":
            show_operations(operations)

        elif action == "0":
            break

        else:
            print("Неверное действие")

    print("Итоговый баланс: ", balance)


bankomat()
