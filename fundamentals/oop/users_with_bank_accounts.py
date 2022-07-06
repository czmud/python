
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

class Users():
    def __init__(self, name, email, number_of_accounts=1):
        self.name = name
        self.email = email
        self.accounts = {}
        for account in range(number_of_accounts):
            self.accounts[account + 71000] = (BankAccount(int_rate=0.02, balance=0))
        print(str(len(self.accounts))+' account(s) created:')
        for key, account in self.accounts.items():
            print('Account Number:',key,account.__dict__)

    def make_deposit(self, amount, account_number=0):
        self.accounts[account_number].deposit(amount)
        return self
    
    def make_withdrawal(self, amount, account_number=0):
        self.accounts[account_number].withdraw(amount)
        return self
    def display_user_balance(self, account_number=0):
        self.accounts[account_number].display_account_info()

    def transfer_balance(self, self_account_number, amount, other_user, 
                        other_user_account_number):
        if amount <= 0:
            print('Must enter positive value to transfer.')
        elif amount > self.accounts[self_account_number].balance:
            print('Transfer amount greater than account balance.')
            print('No transaction made.')
        else:
            self.make_withdrawal(amount, self_account_number)
            other_user.make_deposit(amount, other_user_account_number)
            print('function called alright')
        return self


bilbo = Users('Bilbo','bilbobaggie@gmail.com', 3)
frodo = Users('Frodo','frodojr@gmail.com', 1)


bilbo.make_deposit(200, 71000)
bilbo.make_deposit(500, 71002)


bilbo.display_user_balance(71000)
bilbo.display_user_balance(71001)
bilbo.display_user_balance(71002)
frodo.display_user_balance(71000)

bilbo.transfer_balance(71000, 100, frodo, 71000)
bilbo.transfer_balance(71002, 250, frodo, 71000)

bilbo.display_user_balance(71000)
bilbo.display_user_balance(71001)
bilbo.display_user_balance(71002)
frodo.display_user_balance(71000)
