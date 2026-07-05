import json

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
  save_expenses()

def view_expenses():
  if not expenses:
    print("No expenses recorded yet.")
    return
  
  for expense in expenses:
    print(f"{expense['description']} - {expense['amount']}  ({expense['category']})")

def save_expenses():
  with open("expenses.json", "w") as file:
    json.dump(expenses, file)

def load_expenses():
  try:
    with open("expenses.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return[]

expenses = load_expenses()

def delete_expense():
  if not expenses:
    print("No expenses to delete.")
    return
  
  for i, expense in enumerate(expenses):
    print(f"{i + 1}. {expense['description']} - {expense['amount']} ({expense['category']})")

  try:
    choice = int(input("Enter the number of the expense to delete: "))
  except ValueError:
    print("That's not a valid number.")
    return
  
  if choice < 1 or choice > len(expenses):
    print("Invalid choice.")
    return
  
  removed = expenses.pop(choice - 1)
  save_expenses()
  print(f"Deleted: {removed['description']}")


def main():
  while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Exit")

    choice = input("Choose an option:")

    if choice == "1":
      add_expense()
    elif choice == "2":
      view_expenses()
    elif choice == "3":
      delete_expense()
    elif choice == "4":
      print("Goodbye!")
      break
    else:
      print("Invalid option, try again")

if __name__ == "__main__":
    main()