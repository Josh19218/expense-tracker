expenses = []

def add_expense():
  try:
    amount = float(input("Enter amount: "))
  except ValueError:
    print("That's not a valid number. Please enter a numeric amount.")
    return
  category = input("Enter category: ")
  description = input("Enter description: ")

  expense = {
    "amount": amount,
    "category": category,
    "description": description
  }

  expenses.append(expense)
  print("Expense added!")

def view_expenses():
  if not expenses:
    print("No expenses recorded yet.")
    return
  
  for expense in expenses:
    print(f"{expense['description']} - {expense['amount']}  ({expense['category']})")

def main():
  while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option:")

    if choice == "1":
      add_expense()
    elif choice == "2":
      view_expenses()
    elif choice == "3":
      print("Goodbye!")
      break
    else:
      print("Invalid option, try again")

if __name__ == "__main__":
    main()