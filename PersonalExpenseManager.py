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
import pandas as pd

class manager:
    """ Expense Manager Constructor """
    def __init__(self):
        self.expenses = {} # category : amount, description
        self.data = [
            ["Category", "Amount", "Description"],
        ]
        df = pd.DataFrame(self.data[1:], columns=self.data[0])    
    """ --------------------------- """       


    """ Category Funtions """
    def check_for_category(self, category):
        return category in self.expenses # check if category is a key in expenses
    
    def get_all_categories(self):
        return [category for category in self.expeses]

    def print_all_categories(self):
        categories = self.get_all_categories(self)
        print(", ".join(categories)) # prints the elements of categories with the the string in between
    """ ----------------- """


    """ Expense Functions """
    def add_expense(self, amount, category, desc):
        try:
            amount = float(amount)
        except:
            return False
        if ([amount, desc] in self.expenses[category]):
            return False
        if (category in self.expenses):
            self.expenses[category].append([amount, desc])
            self.data.append([category, str(amount), desc])
            return True
        else:
            self.expenses[category] = [[amount, desc]]
            self.data.append([category, str(amount), desc])

    def get_all_expenses_by_category(self, category):
        result = []
        for key, value in self.expenses.items():
            if key == category:
                result.append(value)
        return result

    def print_all_expenses(self):
        if not self.expenses:
            print("There are currently no expenses.")

        for category in self.expenses:
            print(category + ":")
            for [amount, desc] in len(self.expenses[category]):
                print("     $" + str(amount) + "    " + desc)
            print()

    def calculate_total_spending(self):
        total = 0.00
        for expense in self.expenses.values():
            total += expense[0]
        return total
    """ ----------------- """


    """ General Functions """
    # def sync_data_expenses(self):
    def write_to_file(self, file_name):
        with open(file_name, "w") as file:
            for key, value in self.expenses.items():
                file.write(key + ", " + str(value[0]) + " " + )
            

        try: 
            amount = input("What is expense cost?: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")
            return
        
        try: 
            
            category = input("Enter an amount: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")
            return

        try: 
            amount = input("Enter an amount: ")
            amount = float(amount) 
        except ValueError:
            print("Error: Please enter a valid number")
            return
        