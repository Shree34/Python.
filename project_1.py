# Daily Task Organizer
# This program helps you organize your tasks into two categories:
# 1. Completed tasks
# 2. Incomplete tasks

print("Welcome to your Daily Task Organizer")

# Step 1: Create your checklist
num_tasks = int(input("How many tasks do you want to add today? "))

tasks = []
for i in range(num_tasks):
    task = input(f"Enter task {i+1}: ")
    tasks.append(task)

# Step 2: Separate tasks into completed and incomplete
completed_tasks = []
incomplete_tasks = []

print("\nNow, let's review your tasks.")
for task in tasks:
    answer = input(f"Did you complete '{task}'? (yes/no): ").strip().lower()
    if answer == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Step 3: Show results
print("\nSummary of your day:")

print("\nCompleted Tasks:")
if completed_tasks:
    for ct in completed_tasks:
        print(" -", ct)
else:
    print("None")

print("\nIncomplete Tasks:")
if incomplete_tasks:
    for it in incomplete_tasks:
        print(" -", it)
else:
    print("None")

print("\nEnd of day review complete.")