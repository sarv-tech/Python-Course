# Q. Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance = 0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Deposited = Rs {amount}.")
            else:
                print(f"Deposit must be positive.")

    def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn = Rs {amount}.")
            else:
                print(f"Not sufficient balance.")

    def check_balance(self):
            print(f"Current Balance = Rs {self.balance}.")

acc = BankAccount(12334, "Sarvesh Pingale", 2000)
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

