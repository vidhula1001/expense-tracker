from expense_manager import (
    add_expense,
    view_expenses,
    delete_expense,
    search_expense,
    export_to_csv,
    monthly_summary
)

from reports import show_summary

def menu():
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Monthly expense summary")
    print("4. Delete expense")
    print("5. Search expense")
    print("6. Export to CSV")
    print("7. Exit")



def main():
    while True:
        menu()
        choice = input("Enter choice (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            from expense_manager import delete_expense
            delete_expense()

        elif choice == "5":
            from expense_manager import search_expense
            search_expense()

        elif choice == "6":
            export_to_csv()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
