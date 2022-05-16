class BankAccount:

    all_accounts = []

    def __init__(self, int_rate = .05, balance = 0):
        self.account_int_rate = int_rate
        self.account_balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if (self.account_balance - amount) > 0:
            self.account_balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        return f"{self.account_balance}"

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.account_int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print("Account Info: ", "Interest Rate: ", account.account_int_rate," ", "Balance: ",account.account_balance)


class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(),
            "saving" : BankAccount(),
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['saving'].display_account_info()}")
        return self


# TestCase

summer = User("Summer")

summer.account["checking"].deposit(100)
summer.account["saving"].deposit(100)

summer.display_user_balance()

summer.account["checking"].deposit(50).withdraw(25)
summer.account["saving"].withdraw(15)

BankAccount.print_all_accounts()

summer.account["checking"].withdraw(200)
