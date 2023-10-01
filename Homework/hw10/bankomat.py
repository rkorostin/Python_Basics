# -*- coding: utf-8 -*

# Создаём класс Bankomat с конструктором, который инициализирует свойства balance и operations.
# Затем мы определяем методы add_balance, withdraw_balance и show_operations, которые соответствуют
# функциям add_balance, withdraw_balance и show_operations из исходного кода.
# В методах мы обращаемся к свойствам balance и operations, чтобы получить доступ к текущему балансу и истории операций.
class Bankomat:
    def __init__(self):
        self.balance = 0  # Баланс
        self.balance_inter = None  # Предварительный баланс без учета комиссии и налогов
        self.count_add = 0  # Счётчик для операций пополнения
        self.count_withdraw = 1  # Счётчик для операций снятия
        self.operations = []  # Список операций

    def add_balance(self, amount):
        """
        Метод для пополнения баланса
        """
        if amount % 50 == 0:  # Если введенная сумма (amount) делится на 50 без остатка,
            # то она добавляется к текущему балансу (balance)
            self.balance += amount
            self.count_add += 1
            self.operations.append("Пополнение на сумму: " + str(amount))  # Логирование операций
            if self.balance > 5000000:  # если баланс более 5_000_000, то вычитается налог на богатство 10%
                tax = 0.1 * amount
                self.balance -= tax
                print("Налог 10% на богатство: ", tax)
                print("Пополнение: ", amount - tax)
                self.operations.append("Налог на богатство: " + str(tax))
            if self.count_add % 3 == 0:  # Действие для каждой третьей операции
                commission = min(0.03 * amount, 600)  # Комиссия за пополнение счёта 3%,
                # но не менее 30 и не более 600
                if commission < 30:
                    commission = 30
                elif commission > 600:
                    commission = 600
                self.balance -= commission
                print("Комиссия 3% за каждую третью операцию пополнения: ", commission)
                self.operations.append("Комиссия за каждую третью операцию пополнения: " + str(commission))
        else:
            print("Сумма пополнения должна быть кратна 50")
        return self.balance, self.count_add, self.operations

    def withdraw_balance(self, amount):
        """
        Метод для снятия средств
        """
        if amount % 50 == 0:
            if amount <= self.balance:  # сумма снятия должна быть не меньше баланса
                if self.balance > 5_000_000:  # проверяем баланс на "налог на богатство"
                    tax = 0.1 * amount  # рассчитываем налог
                    balance_inter = self.balance
                    balance_inter -= amount  # рассчитываем предварительный баланс после снятия введённой суммы
                    if tax <= balance_inter:  # проверяем, что хватает средств для снятия налога
                        self.balance -= amount + tax  # снимаем введённую сумму + налог
                        print("Снято: ", amount)
                        print("Налог на богатство (10% от снятой суммы): ", tax)
                        self.operations.append("Налог на богатство: " + str(tax))
                    else:
                        print("Недостаточно средств на счете.")

                elif self.count_withdraw % 3 == 0:  # Если это третья операция, то работает комиссия 3%
                    commission = min(0.03 * amount, 600)  # Рассчитываем комиссию 3% от снимаемой суммы,
                    # но не менее 30 и не более 600
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600

                    balance_inter = self.balance
                    balance_inter -= amount
                    if commission <= balance_inter:
                        self.balance -= commission + amount
                        self.count_withdraw += 1
                        print("Снято: ", amount)
                        print("Комиссия 3% за каждую третью операцию снятия: ", commission)
                        self.operations.append("Комиссия 3% за каждую третью операцию снятия: " + str(commission))
                    else:
                        print("Недостаточно средств на счете.")

                else:  # Если это не третья операция, то работает комиссия 1.5% от снимаемой суммы
                    commission = min(0.015 * amount, 600)
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600

                    balance_inter = self.balance
                    balance_inter -= amount
                    if commission <= balance_inter:
                        self.balance -= commission + amount
                        self.count_withdraw += 1
                        print("Снято: ", amount)
                        print("Комиссия 1.5% за операцию: ", commission)
                        self.operations.append("Комиссия 1.5% за операцию снятия: " + str(commission))
                    else:
                        print("Недостаточно средств на счете.")

            else:
                print("Недостаточно средств на счете")

        else:
            print("Сумма снятия должна быть кратна 50")
        return self.balance, self.count_withdraw, self.operations

    def show_operations(self):
        """
        Метод для просмотра истории операций
        """
        print("Операции:")
        for i, op in enumerate(self.operations):
            print("Операция", i + 1, ": ", op)

    def bankomat(self):
        """
        Метод для работы с банкоматом
        """
        while True:
            print("Текущий баланс:", self.balance)
            action = input("Выберите действие (пополнить (1), снять (2), история операций(3), выйти (0)): ")

            if action == "1":
                while True:
                    try:
                        amount = int(input("Введите сумму пополнения: "))
                        break
                    except ValueError:
                        print("Неверный формат суммы. Повторите ввод.")
                self.add_balance(amount)

            elif action == "2":
                while True:
                    try:
                        amount = int(input("Введите сумму снятия: "))
                        break
                    except ValueError:
                        print("Неверный формат суммы. Повторите ввод.")
                self.withdraw_balance(amount)

            elif action == "3":
                self.show_operations()

            elif action == "0":
                break

            else:
                print("Неверное действие")

        print("Итоговый баланс: ", self.balance)


# Создаем экземпляр класса Bankomat и вызываем метод bankomat для работы с банкоматом.
bankomat = Bankomat()
bankomat.bankomat()
