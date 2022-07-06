


class BankAccount():
    
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.interest_rate = int_rate
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print('Cannot deposit a negative amount, try withdrawing instead?')
        return self
    def withdraw(self, amount):
        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print('Cannot withdraw more than is in the account')
                self.display_account_info()
        else:
            print('Cannot withdraw a negative amount. Enter amount as a positive value.')
        return self
    def display_account_info(self):
        print('Balance: $'+str(self.balance))
        return self
    def yield_interest(self):
        self.balance = self.balance * (1+self.interest_rate)
        return self

    @classmethod
    def display_all_accounts(cls):
        print('Instances of '+cls.__name__+' class:')
        for account in cls.all_accounts:
            print(account.__dict__)


account1 = BankAccount(0.01, 5000)
account2 = BankAccount(0.01, 200)

account1.deposit(350).withdraw(5).withdraw(50).withdraw(90).yield_interest() \
        .display_account_info()

account2.deposit(20).deposit(403.90).withdraw(84).withdraw(40).withdraw(23) \
        .withdraw(12.75).yield_interest().display_account_info()

BankAccount.display_all_accounts()
