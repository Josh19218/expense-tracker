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

## Day 5 — Saving & Loading Data with JSON

**What I did:**

- Added save_expenses() using json.dump() to write the expenses list to a file
- Added load_expenses() using json.load() to read it back on startup
- Hit and fixed a NameError caused by calling load_expenses() before it was defined
- Confirmed data persists correctly across program restarts

**Concepts I learned:**

- Python executes files top to bottom — a function must be defined before it's called, unless the call is inside another function (like main()) that only runs later
- with open(...) as file: safely opens a file and automatically closes it afterward
- "w" mode writes/overwrites a file, "r" mode reads it
- json.dump() converts Python data into JSON and writes it to a file
- json.load() reads JSON from a file back into Python data (lists/dictionaries)
- try/except FileNotFoundError handles the case where a file doesn't exist yet, instead of crashing

## Day 6 — Deleting Expenses & List Indexing

**What I did:**

- Built delete_expense() to remove an item from the expenses list
- Displayed expenses with user-friendly numbering while using real list indexes behind the scenes
- Validated user input for invalid or out-of-range choices

**Concepts I learned:**

- List items are numbered starting at 0 (index), not 1 — so I show i + 1 to users but convert back with choice - 1 for the real index
- enumerate(list) gives both the index and the item while looping, e.g. for i, expense in enumerate(expenses)
- expenses.pop(index) removes an item at that index AND returns it, so I can confirm what was deleted
- del list[index] also removes an item but doesn't return it — pop is more useful when you need the removed value
- Checking choice < 1 or choice > len(expenses) prevents crashes from out-of-range input

## Day 7 — Summary View & Feature-Complete v1

**What I did:**

- Built view_summary() to calculate total spending and a breakdown by category
- Completed the core feature set: add, view, delete, save/load, and summarize expenses

**Concepts I learned:**

- += is shorthand for "add to the existing value" (total += x means total = total + x)
- dict.get(key, default) safely reads a dictionary value, returning a default instead of crashing if the key doesn't exist yet
- dict.items() loops through a dictionary giving both the key and value at once
- Building a "grouped total" (category -> amount) is a common pattern: start with an empty dict, then accumulate into it as you loop

## Day 8 — README & Wrapping Up v1

**What I did:**

- Wrote a proper README.md explaining what the project does, how to run it, and what I learned
- Viewed the finished repo on GitHub as a rendered project page for the first time

**Concepts I learned:**

- Code fences (\`\`\`) make text render as a formatted code block on GitHub
- A good README is often the first thing an employer or visitor sees — it should explain what, how, and why, not just be an afterthought
