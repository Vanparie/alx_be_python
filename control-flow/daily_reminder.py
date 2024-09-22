# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: '{task}' is of medium priority."
    case "low":
        reminder = f"Reminder: '{task}' is of low priority."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Check if the task is time-bound and modify the reminder
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Provide the customized reminder
print(reminder)
