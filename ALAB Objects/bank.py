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
                raise InsufficientFundsError()
        else:
            raise ValueError("Withdrawal amount must be positive.")
        
        
    def __str__(self):
        return f"BankAccount(owner={self.owner}, account_number={self.account_number}, balance={self.balance})"
    

#Savings account class that inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0, interest_rate=0.01):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. New balance is {self.balance}.")
        
    def __str__(self):
        return f"SavingsAccount(owner={self.owner}, account_number={self.account_number}, balance={self.balance}, interest_rate={self.interest_rate})"


#Custom exception for insufficient funds
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account."):
        self.message = message
        super().__init__(self.message)
        
        
        

bank_account = BankAccount("John Doe", "123456789", 1000)

print(bank_account)
try:
    #Deposit and withdraw some money
    bank_account.deposit(500)
    bank_account.withdraw(200)

    #Try to withdraw more money than available
    bank_account.withdraw(1500)
except InsufficientFundsError as e:
    print(e)
except ValueError as e:
    print(e)
