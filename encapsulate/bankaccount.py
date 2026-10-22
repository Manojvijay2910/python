class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance

account = BankAccount("docker", 1000)
print(account.balance)

account.balance = 2000
print(account.balance)

try:
    account.balance = -200
except ValueError as v:
    print(v)

del account.balance
# print(account.balance) gives error