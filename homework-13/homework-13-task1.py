"""
Создать «банковский счёт» в классе. Класс BankAccount с полями owner, balance (__init__), методами deposit(amount),
withdraw(amount) и show(). Метод withdraw не должен позволять уйти в минус: если сумма больше остатка — выводить
сообщение и ничего не менять. Создать 2 счёта, проверить операции на каждом.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Операция отклонена. Выводимая сумма больше остатка.")
        else:
            self.balance -= amount

    def show(self):
        print(f"У владельца \"{self.owner}\" остаток на счету: {self.balance} руб.")

bc1 = BankAccount("Владелец 1", 100)
bc2 = BankAccount("Владелец 2", 200)

bc1.deposit(100)
bc1.show()
bc2.withdraw(300)
bc2.show()

