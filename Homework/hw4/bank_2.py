def bankomat():
    """
    Пополняет баланс. Каждая третья операция облагается комиссией 3% от вносимой суммы (не менее 30, но не более 600).
    Если баланс больше 5_000_000, то действует налог на богатство - 10% от вносимой или снимаемой суммы.
    При этом комиссия в 1,5% или 3% уже не действует.
    Уменьшает баланс. Каждая третья операция облагается комиссией 3% от снимаемой суммы (не менее 30, но не более 600).
    Если операция снятия суммы не кратна 3, то взимается комиссия 1,5% от снимаемой суммы
    Каждая операция вносится в список, который в любой момент можно вывести в терминале
    """
    balance = 10000
    count_add = 0
    count_withdraw = 0
    operations = []

    def add_balance(balance, amount):
        """
        Функция пополнения счёта. Принимает текущий баланс и пополняемую сумму
        """
        nonlocal count_add  # 'count' является нелокальной переменной и должна быть доступна
        # из внешней области видимости.
        if amount % 50 == 0:  # Если введенная сумма (amount) делится на 50 без остатка,
            # то она добавляется к текущему балансу (balance)
            balance += amount
            count_add += 1
            operations.append("Пополнение на сумму: " + str(amount))  # Логирование операций
            if balance > 5000000:  # если баланс более 5_000_000, то вычитается налог на богатство 10%
                tax = 0.1 * amount
                balance -= tax
                print("Налог 10% на богатство: ", tax)
                operations.append("Налог на богатство: " + str(tax))
            if count_add % 3 == 0:  # Действие для каждой третьей операции
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
        return balance, count_add, operations

    def withdraw_balance(balance, amount):
        """
        Функция снятия со счёта. Принимает текущий баланс и сумму для снятия
        """
        nonlocal count_withdraw
        if amount % 50 == 0:
            if amount <= balance:  # сумма снятия должна быть не меньше баланса
                if balance > 5000000:
                    tax = 0.1 * amount
                    balance -= tax
                    print("Налог 10% на богатство: ", tax)
                    operations.append("Налог на богатство: " + str(tax))
                elif count_withdraw % 3 == 0 and count_withdraw != 0:
                    commission = min(0.03 * amount, 600)
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                    balance -= (amount + commission)
                    count_withdraw += 1
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
                    count_withdraw += 1
                    print("Снято: ", amount)
                    print("Комиссия 1.5% за операцию: ", commission)
                    operations.append("Снято средств: " + str(amount))
                    operations.append("Комиссия за операцию снятия: " + str(commission))
            else:
                print("Недостаточно средств на счете")
        else:
            print("Сумма снятия должна быть кратна 50")
        return balance, count_withdraw, operations

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
            while True:
                try:
                    amount = int(input("Введите сумму пополнения: "))
                    break
                except ValueError:
                    print("Неверный формат суммы. Повторите ввод.")
            balance, count_add, operations = add_balance(balance, amount)

        elif action == "2":
            while True:
                try:
                    amount = int(input("Введите сумму снятия: "))
                    break
                except ValueError:
                    print("Неверный формат суммы. Повторите ввод.")
            balance, count_withdraw, operations = withdraw_balance(balance, amount)

        elif action == "3":
            show_operations(operations)

        elif action == "0":
            break

        else:
            print("Неверное действие")

    print("Итоговый баланс: ", balance)


bankomat()
