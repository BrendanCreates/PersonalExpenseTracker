import PersonalExpenseManager as manager

def main_menu(tracker):
    while True:
        print("\nWelcome to the Peresonal Expense Manager")
        if tracker.check_empty():
            print("Looks like you don't have any expenses logged yet!\n")
        print("What would you like to do?: ")
        print("     1) Add expense")
        print("     2) View expenses")
        print("     3) Save expenses to file")
        print("     4) Load expenses from file")
        print("     5) View total expendature")
        print("     6) View expenses by category")
        print("     7) Delete an expense")
        print("     0) Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            tracker.print_all_categories()
            category = input("What is the category of the expense?: ")
            desc = input("What is the description of the expense?: ")
            amount = float(input("What is the amount of the expense?: ").strip())
            tracker.add_expense(amount, category, desc)
        elif choice == "2":
            tracker.print_all_expenses()
        elif choice == "3":
            if tracker.write_csv():
                print("\nSucessfuly saved!")
            else:
                print("\nFailed to save to file.")
        elif choice == "4":
            if tracker.read_csv():
                print("\nSucessfuly loaded!")
            else:
                print("\nFailed to load expenses from file.")
        elif choice == "5":
            print("\nCurrent total expendature: $" + str(tracker.total))
        elif choice == "6":
            tracker.print_all_categories()
            category = input("What is the category of expense to view?: ")
            tracker.print_all_expenses_by_category(category)
        elif choice == "7":
            tracker.print_all_categories()
            category = input("What is the category of expense to view?: ")
            tracker.print_all_expenses_by_category(category)
        elif choice == "0":
            break
        else:
            print("\nNo valid choice selected")

if __name__ == "__main__":
    expense_manager = manager.manager()
    main_menu(expense_manager)
