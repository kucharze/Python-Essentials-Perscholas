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
        
        
    def __str__(self):
        return f"BankAccount(owner={self.owner}, account_number={self.account_number}, balance={self.balance})"
    
    

bank_account = BankAccount("John Doe", "123456789", 1000)

print(bank_account)

#Deposit and withdraw some money
bank_account.deposit(500)
bank_account.withdraw(200)

#Try to withdraw more money than available
try:
    bank_account.withdraw(1500)
except ValueError as e:
    print(e)