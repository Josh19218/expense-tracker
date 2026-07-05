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
