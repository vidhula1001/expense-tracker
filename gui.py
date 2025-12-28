import tkinter as tk
from tkinter import messagebox
from expense_manager import add_expense, view_expenses, delete_expense, search_expense, export_to_csv


def add_expense_gui():
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()

    if not amount or not category or not description:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    # reuse logic
    from storage import load_data, save_data
    from datetime import datetime

    data = load_data()
    data.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    })
    save_data(data)

    messagebox.showinfo("Success", "Expense added successfully!")

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)


def show_expenses():
    from storage import load_data
    data = load_data()

    output.delete("1.0", tk.END)

    if not data:
        output.insert(tk.END, "No expenses found.")
        return

    for e in data:
        output.insert(
            tk.END,
            f"{e['date']} | ₹{e['amount']} | {e['category']} | {e['description']}\n"
        )


def export_csv_gui():
    export_to_csv()
    messagebox.showinfo("Export", "Expenses exported to CSV successfully!")

def delete_expense_gui():
    from storage import load_data, save_data

    index = delete_entry.get()

    if not index.isdigit():
        messagebox.showerror("Error", "Enter a valid expense number")
        return

    index = int(index) - 1
    data = load_data()

    if index < 0 or index >= len(data):
        messagebox.showerror("Error", "Expense number not found")
        return

    deleted = data.pop(index)
    save_data(data)

    messagebox.showinfo("Deleted", f"Deleted: {deleted['description']}")
    show_expenses()

def search_gui():
    keyword = search_entry.get().lower()
    from storage import load_data

    output.delete("1.0", tk.END)

    if not keyword:
        output.insert(tk.END, "Enter something to search.")
        return

    found = False
    for e in load_data():
        if keyword in e["category"].lower() or keyword in e["description"].lower():
            output.insert(
                tk.END,
                f"{e['date']} | ₹{e['amount']} | {e['category']} | {e['description']}\n"
            )
            found = True

    if not found:
        output.insert(tk.END, "No matching expenses found.")



# ---------------- GUI layout ----------------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x650")
root.configure(bg="#f4f6f8")


title = tk.Label(
    root,
    text="Expense Tracker",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f6f8"
)

title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1)

tk.Label(frame, text="Category").grid(row=1, column=0)
category_entry = tk.Entry(frame)
category_entry.grid(row=1, column=1)

tk.Label(frame, text="Description").grid(row=2, column=0)
description_entry = tk.Entry(frame)
description_entry.grid(row=2, column=1)

tk.Button(
    root,
    text="Add Expense",
    width=20,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=add_expense_gui
).pack(pady=4)

tk.Button(
    root,
    text="View Expense",
    width=20,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=show_expenses
).pack(pady=4)

tk.Button(
    root,
    text="Export to CSV",
    width=20,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=export_csv_gui
).pack(pady=4)


delete_frame = tk.Frame(root)
delete_frame.pack(pady=5)

tk.Label(delete_frame, text="Delete #").grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame, width=10)
delete_entry.grid(row=0, column=1)

tk.Button(delete_frame, text="Delete Expense", command=delete_expense_gui)\
    .grid(row=0, column=2, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Label(search_frame, text="Search").grid(row=0, column=0)
search_entry = tk.Entry(search_frame, width=25)
search_entry.grid(row=0, column=1)

tk.Button(search_frame, text="Search", command=search_gui)\
    .grid(row=0, column=2, padx=5)


output_frame = tk.Frame(root)
output_frame.pack(pady=10)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output = tk.Text(
    output_frame,
    height=15,
    width=65,
    yscrollcommand=scrollbar.set
)
output.pack(side=tk.LEFT)

scrollbar.config(command=output.yview)


root.mainloop()
