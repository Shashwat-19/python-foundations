class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self):
        debit_amount = float(input("Enter the amount you want to debit: "))
        self.balance -= debit_amount
        print(f"Your current balance is Rs {self.balance}")

    def credit(self):
        credit_amount = float(input("Enter the amount you want to credit: "))
        self.balance += credit_amount
        print(f"Your current balance is Rs {self.balance}")

    def display_amount(self):
        print(f"Your current balance is Rs {self.balance}")

account1 = BankAccount(float(input("Enter your initial balance: ")), input("Enter your account number: "))
account1.debit()
account1.credit()
account1.display_amount()
