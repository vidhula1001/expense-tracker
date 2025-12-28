from storage import load_data, save_data
from datetime import datetime


def add_expense():
    data = load_data()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    category = input("Enter category: ")
    description = input("Enter description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    data.append(expense)
    save_data(data)

    print("✅ Expense added successfully!")


def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for i, e in enumerate(data, start=1):
        date = e.get("date", "N/A")
        print(f"{i}. {date} | ₹{e['amount']} | {e['category']} | {e['description']}")


def delete_expense():
    data = load_data()

    if not data:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))
        if 1 <= choice <= len(data):
            deleted = data.pop(choice - 1)
            save_data(data)
            print(f"✅ Deleted expense: {deleted['description']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def search_expense():
    keyword = input("Enter category or description to search: ").lower()
    data = load_data()

    found = False
    for e in data:
        if keyword in e["category"].lower() or keyword in e["description"].lower():
            date = e.get("date", "N/A")
            print(f"{date} | ₹{e['amount']} | {e['category']} | {e['description']}")
            found = True

    if not found:
        print("No matching expenses found.")

import csv


def export_to_csv():
    data = load_data()

    if not data:
        print("No expenses to export.")
        return

    filename = "expenses.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "amount", "category", "description"]
        )
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ Expenses exported successfully to {filename}")

from collections import defaultdict


def monthly_summary():
    data = load_data()

    if not data:
        print("No expenses available.")
        return

    summary = defaultdict(float)

    for e in data:
        month = e["date"][:7]  # YYYY-MM
        summary[month] += e["amount"]

    print("\n--- Monthly Expense Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total}")
