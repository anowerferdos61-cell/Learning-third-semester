class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.minimum_withdraw = 500
        self.minimum_deposit = 100
        self.maximum_withdraw = 100000

    def show_balance(self):
        print(f"Your current balance is {self.balance}.")
    
    def deposit(self,amount):
        if amount < self.minimum_deposit:
            print("Your deposit amount is too low, please deposit more money.")
        else:
            self.balance += amount
            print(f"Your balance is {self.balance} after deposit.")
    
    def withdraw(self,amount):
        if amount < self.minimum_withdraw:
            print("Your withdrawal amount is too low, please withdraw more money.")
        elif amount >= self.maximum_withdraw or amount > self.balance:
            print("Your withdrawal amount is too high, please withdraw less money.")
        else:
            self.balance -= amount
            print(f"Your balance is {self.balance} after withdrawal.")
    
my_account = Bank(500)
my_account.deposit(50), my_account.deposit(200),my_account.deposit(150) ,my_account.show_balance()
my_account.withdraw(200), my_account.withdraw(50), my_account.withdraw(150),my_account.withdraw(659), my_account.show_balance()  


