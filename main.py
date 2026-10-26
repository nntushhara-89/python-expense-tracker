
expenses = []


def add_expense():
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()

        if not category:
            category = "Other"

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== YOUR EXPENSES =====")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ₹{total:.2f}")


def show_category_totals():
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\n===== CATEGORY TOTALS =====")

    for category, amount in totals.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total expenses")
        print("4. Show category totals")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            show_category_totals()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
