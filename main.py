import PersonalExpenseManager as manager

def main_menu(tracker):
    while True:
        print("\nWelcome to the Peresonal Expense Manager!")
        print("What would you like to do?: ")
        print("     1) Add expense")
        print("     2) View expenses")
        print("     0) Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            category = input("What is the category of the expense?: ")
            amount = float(input("What is the amount of the expense?: ").strip())
            desc = input("What is the description of the expense?: ")
            tracker.add_expense(amount, category, desc)
        elif choice == "2":
            tracker.print_all_expenses()
        elif choice == "0":
            break
        else:
            print("\nNo valid choice selected")

if __name__ == "__main__":
    expense_manager = manager.manager()
    main_menu(expense_manager)
