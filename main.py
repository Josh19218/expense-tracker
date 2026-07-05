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

def main():
  print("Welcome to your Expense Tracker")
  add_expense()
  print(expenses)

if __name__ == "__main__":
  main()
