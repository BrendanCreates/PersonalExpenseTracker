"""
PersonalExpenseManager - Author: BrendanCreates

Features:
    1. Add an expense (amount, category, description)
    2. View all expenses
    3. Calculate total spending
    4. Filter expenses by category
    5. Save and load expenses from file (also clear file function)

License: MIT License

"""

class manager:
    def __init__(self):
        self.expenses = {} # category : amount, description

    def check_catagories(self, category):
        return category in self.expenses # cehck if category is a key in expenses
    
    def all_catagories(self):
        return [category for category in self.expeses]

    def add_expense(self, amount, category, desc):
        if not self.check_categories(self, category):
            catagories = self.all_catagories(self)
            if (not isinstance(input("This catagory does not exist yet.\n"
                  "Do you want to create this catagory? (y/n): "), str)):
                
            

        try: 
            amount = input("What is expense cost?: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")
        
        try: 
            
            category = input("Enter an amount: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")

        try: 
            amount = input("Enter an amount: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")
        