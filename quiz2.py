# Create a class called PersonAccount.
# It has firstname, lastname, incomes, expenses properties 
# and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
# Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append({"description": description, "amount": amount})

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)
        
    def total_income(self):
        return sum(income["amount"] for income in self.incomes)
  
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        return (f"{self.firstname} {self.lastname}\n"
                f"Total Income: {self.total_income()}\n"
                f"Total Expense: {self.total_expense()}\n"
                f"Account Balance: {self.account_balance()}\n"
                )

person = PersonAccount("Purity", "Masanya")
person.add_income("Net Pay", 15000)
person.add_expense("Car Note", 2000)

print(person.account_info())