from expense_manager import add_expense, view_expenses
from reports import show_summary

def menu():
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Expense summary")
    print("4. Delete expense")
    print("5. Search expense")
    print("6. Exit")



def main():
    while True:
        menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            from expense_manager import delete_expense
            delete_expense()

        elif choice == "5":
            from expense_manager import search_expense
            search_expense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
