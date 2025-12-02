print("=== SIMPLE BUDGET TRACKER ===")

income = 0
expenses = []

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        income += amount
        print("Income added.")

    elif choice == "2":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
        print("Expense added.")

    elif choice == "3":
        print("\n--- SUMMARY ---")
        total_expenses = sum(x[1] for x in expenses)
        balance = income - total_expenses

        print("Total Income:", income)
        print("Total Expenses:", total_expenses)
        print("Balance:", balance)

        print("\nExpense List:")
        for e in expenses:
            print(f"- {e[0]} : {e[1]}")

    elif choice == "4":
        break

    else:
        print("Invalid option, try again.")