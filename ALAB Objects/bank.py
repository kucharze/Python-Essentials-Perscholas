class BankAccount:
    def __init__(self, owner, account_number,balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            raise ValueError("Deposit amount must be positive.")
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")