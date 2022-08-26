
class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(self.name, self.balance)
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self,amount):
        self.balance += amount

a1 = BankAccount()
a1.set_details('Mike',200)



