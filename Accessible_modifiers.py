class BankAccount:
    def __init__(self, name, balance):        # constructor
        self.name = name            # public
        self.__balance = balance    # private - data mangling

    def get_balance(self):          # getter
        return self.__balance

    def set_balance(self, newBalance):     # setter
        self.__balance = newBalance

acc1 = BankAccount("Sarvesh Pingale", 10000)
acc1.set_balance(20000)
print(acc1.name, acc1._BankAccount__balance)