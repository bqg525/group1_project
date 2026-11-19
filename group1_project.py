##create an account
##initialize values 
##define add_income function
##define add_expense function
##define add_expense function
##write a summary that gives all the incomes to the user 
##optional: add default values 
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.savings = 0
        self.total_income = 0
        self.total_expenses = 0

    def add_income(self, amount):
        self.balance += amount
        self.total_income += amount
    def add_expense(self, amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        self.total_expenses += amount
     def deposit_to_savings(self, amount):
        if amount > self.balance:
            print("Not enough money")
            return
        self.balance -= amount
        self.savings += amount

    def summary(self):
        print(f"{self.owner}: balance {self.balance}, savings {self.savings}")
        print(f"income {self.total_income}, expenses {self.total_expenses}")


acc = Account("Shirin")
acc.add_income(500)
acc.add_expense(120)
acc.deposit_to_savings(100)
acc.summary()

    
