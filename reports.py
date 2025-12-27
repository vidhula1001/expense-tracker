from storage import load_data

def show_summary():
    data = load_data()

    if not data:
        print("No data available.")
        return

    total = sum(item["amount"] for item in data)

    category_totals = {}
    for item in data:
        category = item["category"]
        category_totals[category] = category_totals.get(category, 0) + item["amount"]

    print("\n==== Expense Summary ====")
    print(f"Total Spent: ₹{total}")

    print("\nCategory-wise:")
    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt}")
