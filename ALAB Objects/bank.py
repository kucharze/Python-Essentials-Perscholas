class BankAccount:
    def __init__(self, owner, account_number,balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number