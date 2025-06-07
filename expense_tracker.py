import csv
from datetime import datetime

FILENAME = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Bills", "Fun", "Other"]

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input(f"Category {CATEGORIES}: ")
    if category not in CATEGORIES:
        print("Unknown category! Adding as 'Other'.")
        category = "Other"
    amount = float(input("Amount: $"))
    description = input("Description: ")
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print("Expense added.")

def view_expenses():
    total = 0
    by_category = {cat: 0 for cat in CATEGORIES}
    print("\nExpenses:")
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            if row:
                total += float(row[2])
                by_category[row[1]] += float(row[2])
    print(f"\nTotal spent: ${total:.2f}")
    print("By category:", by_category)

def main():
    while True:
        choice = input("\n1: Add expense\n2: View expenses\n3: Quit\nChoose: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

