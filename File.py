import csv
import os
from datetime import datetime

CSV_FILE = "expenses.csv"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])
        print(f"Created {CSV_FILE}")

def add_expense():
    date = input("Date (YYYY-MM-DD) [today]: ") or datetime.today().strftime("%Y-%m-%d")
    category = input("Category (Food, Transport, Bills, etc.): ")
    amount = float(input("Amount: "))
    note = input("Note: ")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
    print("Expense added!")

def show_summary():
    if not os.path.exists(CSV_FILE):
        print("No expenses yet.")
        return
    total = 0
    by_category = {}
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = float(row["amount"])
            total += amt
            cat = row["category"]
            by_category[cat] = by_category.get(cat, 0) + amt
    print(f"\nTotal spent: {total:.2f}")
    print("By category:")
    for cat, amt in by_category.items():
        print(f"  {cat}: {amt:.2f}")

def main():
    init_csv()
    while True:
        print("\nOptions: [1] Add expense [2] Show summary [3] Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
