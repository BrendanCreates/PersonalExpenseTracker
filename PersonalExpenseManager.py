"""
PersonalExpenseManager - Author: BrendanCreates

Features:
    1. Add/remove an expense (amount, category, description)
    2. View all expenses
    3. Calculate total spending
    4. Filter expenses by category
    5. Save and load expenses from file (also clear file function)

License: MIT License

"""
from collections import defaultdict
import csv

class manager:
    """ Expense Manager Constructor """
    def __init__(self):
        self.expenses = defaultdict(list) # category : [[amount, description], ... ]
        self.total = 0.00 # total spending
    
    """ --------------------------- """       


    """ Category Funtions """
    def check_empty(self):
        return not bool(self.expenses)
    
    def get_all_categories(self):
        return [category for category in self.expenses]

    def print_all_categories(self):
        if self.check_empty():
            print("There are currently no categories.")
            return
        categories = self.get_all_categories()
        print("These are the current categories: " + ", ".join(categories)) # prints the elements of categories with the the string in between
    
    """ ----------------- """


    """ Expense Functions """
    def add_expense(self, amount, category, desc): # when using this function, monitor the boolean returns for success of the operation
        if len(desc) > 30 and len(category) > 30:
            print("\nFailed to add expense, category and description is over 30 characters.")
            return
        elif len(category) > 30:
            print("\nFailed to add expense, category is over 30 characters.")
            return
        elif len(desc) > 30:
            print("\nFailed to add expense, description is over 30 characters.")
            return
        
        clean_category = category.strip()
        
        try:
            amount = float(amount) 
            expense = [amount, desc.strip()]
        except (ValueError, TypeError):
            print("\nEnter a valid amount for the expense.")
            return
        
        if expense in self.expenses[clean_category]:
            print("\nFailed to add expense.")
            return

        self.expenses[clean_category].append(expense)
        self.total += amount
        print("\nExpense added successfully!")
        return

    def get_all_expenses_by_category(self, category):
        for dict_category, expenses in self.expenses.items():
            if dict_category == category:
                return expenses

    def print_all_expenses(self):
        if self.check_empty():
            print("\nThere are currently no expenses.")
            return

        for category in self.expenses:
            print("\n" + category + ":")
            expenses = self.expenses[category]
            for [amount, desc] in expenses:
                print("     $" + str(amount) + "    " + desc)

    def print_all_expenses_by_category(self, category):
        expenses_of_category = self.get_all_expenses_by_category(category)
        if not expenses_of_category:
            print("\nThere are currently no expenses in this category.")
            return
        
        print("\n" + category + ":")
        for [amount, desc] in expenses_of_category:
            print("     $" + str(amount) + "    " + desc)

    def remove_expense(self, amount, category, desc): # when using this function, monitor the boolean returns for success of the operation
        if len(desc) > 30 and len(category) > 30:
            print("\nFailed to remove expense, category and description is over 30 characters.")
            return
        elif len(category) > 30:
            print("\nFailed to remove expense, category is over 30 characters.")
            return
        elif len(desc) > 30:
            print("\nFailed to remove expense, description is over 30 characters.")
            return
        
        clean_category = category.strip()
        
        try:
            amount = float(amount) 
            expense = [amount, desc.strip()]
        except (ValueError, TypeError):
            print("\nEnter a valid amount for the expense.")
            return

        if expense not in self.expenses[clean_category]:
            print("\nExpense does not exist.")
            return
        
        self.expenses[clean_category].remove(expense)
        self.total -= amount
        print("\nExpense removed successfully!")
        return
    
    """ ----------------- """


    """ File Functions """
    def write_csv(self):
        with open("Expenses.csv", "w", newline="") as file: # newline="" forces to handle newlines normally not Windows way with carriage return, will create csv if doesnt exist
            writer = csv.writer(file)

            writer.writerow(["Total Spending", self.total, ""]) # empty string at the end to maintain width of csv entries
            
            writer.writerow(["Category", "Amount", "Description"])

            for category, expenses in self.expenses.items():
                for amount, desc in expenses:
                    writer.writerow([category, amount, desc])
            return True
        return False
        
    def read_csv(self):
        # reset the current dictionary of expenses
        # reset the spending
        self.expenses = defaultdict(list)
        self.total = 0.00

        with open("Expenses.csv", "r", newline="") as file:
            spending_line = file.readline() # read one line from objext file, so one string of csv file
            row = next(csv.reader([spending_line]))
            # take the first line string and for each element in the iterable
            # just the one element spending_line, it spits along commas and handles like a csv and stores the fields
            # in a csv.reader objext
            # stores the row into a list of the field strings
            if row and row[0] == "Total Spending":
                try:
                    self.total = float(row[1])
                except:
                    self.total = 0.0

            reader = csv.DictReader(file)
            for row in reader:
                category = row["Category"] # grab category of current row in the file
                amount = float(row["Amount"]) # grab amount of current row in the file
                desc = row["Description"] # grab description of current row in the file

                if category not in self.expenses:
                    self.expenses[category] = []

                self.expenses[category].append([amount, desc]) # add the amount and description to the category in the dictionary
            return True
        return False
            


    


