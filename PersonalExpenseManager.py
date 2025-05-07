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
    
    def check_for_category(self, category):
        return category in self.expenses # check if category is a key in expenses
    
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
        expense = [amount, desc.strip()]
        clean_category = category.strip()

        if (expense in self.expenses[clean_category]): 
            return False
        if (clean_category in self.expenses):
            self.expenses[clean_category].append(expense)
            self.total += amount # add the amount to the total spending
            return True

    def get_all_expenses_by_category(self, category):
        result = []
        for dict_category, expenses in self.expenses.items():
            if dict_category == category:
                result.append(expenses)
        return result

    def print_all_expenses(self):
        if self.check_empty():
            print("\nThere are currently no expenses.")
            return

        for category in self.expenses:
            print("\n" + category + ":")
            expenses = self.expenses[category]
            for [amount, desc] in expenses:
                print("     $" + str(amount) + "    " + desc)

    # def print_all_expenses_by_category
    
    """ ----------------- """


    """ File Functions """
    def write_csv(self):
        with open("Expenses.csv", "w", newline="") as file: # newline="" forces to handle newlines normally not Windows way with carriage return
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
        self.expenses = {}
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
            


    


