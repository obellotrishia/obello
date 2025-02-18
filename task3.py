class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
       if amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew {amount}. Current balance:{self.balance}")
       else:
            print("Insufficent balance.")

    def display_balance(self):
       print(f"Account Balance: {self.balance}")
        
# Creating a BankAccount object
my_account = BankAccount("09353206479", "Obello Trishia", 2500)

# Performing transactions
my_account.deposite(1000)
my_account.withdraw(500)
my_account.display_balance()