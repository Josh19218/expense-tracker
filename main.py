expenses = []

def add_expense():
  amount = input("Enter amount: ")
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
