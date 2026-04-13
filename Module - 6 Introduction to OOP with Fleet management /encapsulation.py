# Encapsulation is one of the fundamental principles of object-oriented programming (OOP).
# access modifiers -- > public, private, protected.


class Bank:
    def __init__(self, name, balance):
        self.name = name  # Public attribute
        self._branch = "Main Branch"  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}.\n New balance: {self.__balance}\n")
        else:
            print("Deposit amount must be positive.\n")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}\n")
        else:
            print("Insufficient funds or invalid withdrawal amount.\n")

    def get_balance(self):
        return self.__balance  # Public method to access the private attribute
    
# Example usage
anower = Bank("Alice",10000)
anower.deposit(5000)
anower.get_balance()
print(anower._Bank__balance)
anower.withdraw(2000)
anower.get_balance()