import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Bills", "Entertainment", "Other"]

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])
        print(f"Created {CSV_FILE}")

def add_expense():
    date = input("Date (YYYY-MM-DD) [today]: ").strip() or datetime.today().strftime("%Y-%m-%d")
    
    category = input(f"Category {CATEGORIES}: ").strip()
    if category not in CATEGORIES:
        print(f"Unknown category, set to 'Other'.")
        category = "Other"
    
    while True:
        try:
            amount = float(input("Amount: ").strip())
            break
        except ValueError:
            print("Please enter a valid number.")
    
    note = input("Note: ").strip()
    
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
        percent = (amt / total) * 100 if total > 0 else 0
        print(f"  {cat}: {amt:.2f} ({percent:.0f}%)")
    
    if by_category:
        categories = list(by_category.keys())
        amounts = list(by_category.values())
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct='%1.0f%%', startangle=90)
        plt.title("Expenses by Category")
        plt.show()

def delete_all_data():
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)
        init_csv()
        print("All expenses deleted!")
    else:
        print("No data to delete.")

def main():
    init_csv()
    while True:
        print("\nOptions: [1] Add expense [2] Show summary [3] Delete all data [4] Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            delete_all_data()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
