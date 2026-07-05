# Learning Log — Expense Tracker

## Day 1 — Environment Setup & First Commit

**What I did:**

- Installed Python, VS Code, and Git
- Configured git with my name/email
- Created a GitHub repo and connected it to my local project
- Made my first commit and push
- Wrote a basic main.py with a main() function

**Commands I learned:**

- git init — turns a folder into a git repository
- git status — shows what's changed/untracked
- git add . — stages all changes for commit
- git commit -m "message" — saves a snapshot with a description
- git push -u origin main — uploads commits to GitHub (first time only needs -u)
- python main.py — runs a Python file

**Concepts I learned:**

- .gitignore tells git which files to never track
- if **name** == "**main**": means "only run this code if the file is run directly"

## Day 2 — Adding Expenses

**What I did:**

- Built add_expense() function using input(), a dictionary, and a list
- Debugged a real bug: main() wasn't calling add_expense(), so nothing happened after the welcome message

**Concepts I learned:**

- Dictionaries store key-value pairs, e.g. {"amount": 20, "category": "food"}
- Lists can hold multiple dictionaries — expenses.append(expense) adds one to the list
- input() always returns a string, even for numbers
- Python uses indentation to define what's inside a function — a function existing isn't enough, it has to actually be called
- Mixing indentation styles (spaces vs tabs, 2 vs 4 spaces) causes IndentationError

## Day 3 — Type Conversion & Error Handling

**What I did:**

- Fixed a bug where I hadn't saved the file before running it (VS Code shows an unsaved dot on the tab)
- Converted amount input from a string to a float using float()
- Intentionally crashed the program by entering non-numeric input, then read the traceback to find the cause
- Added try/except to handle invalid input gracefully instead of crashing

**Concepts I learned:**

- input() always returns a string — float() converts it to a real number for math
- "20" + "30" gives "2030" (text joining) but 20 + 30 gives 50 (real math) — this is why type matters
- Python tracebacks read bottom-to-top for the actual error, top-to-bottom for the call chain
- try/except lets code fail gracefully: try the risky code, and except catches a specific error type instead of crashing
- return inside a function exits it immediately — used here to stop before adding bad data to the list
- Always save the file before running it — an unsaved VS Code tab shows a dot instead of an X

## Day 4 — Menu Loop & Viewing Expenses

**What I did:**

- Built a while True loop that shows a menu and keeps running until the user exits
- Added if/elif/else to route user choice to different functions
- Built view_expenses() to loop through and display all stored expenses

**Concepts I learned:**

- while True: creates an infinite loop that only stops when something inside it calls break
- User input from input() is always a string, so menu choices need to be compared as strings (e.g. "1", not 1)
- if not expenses: checks if a list is empty
- for expense in expenses: loops through each dictionary in the list
- f-strings (f"...") let you insert variables directly into text using {curly braces}
