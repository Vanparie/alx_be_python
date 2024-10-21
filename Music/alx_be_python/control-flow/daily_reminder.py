# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print("Reminder: This is your task.")
# Process the task based on priority and time sensitivity
match priority:
    case "high":
        Reminder = f"Reminder: '{task}' is of high priority"
    case "medium":
        Reminder = f"Reminder: '{task}' is of medium priority."
    case "low":
        Reminder = f"Reminder: '{task}' is of low priority."
    case _:
        Reminder = "Invalid priority level. Please enter high, medium, or low."

# Check if the task is time-bound and modify the reminder
if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
elif time_bound == "no":
    Reminder += " This is not time-sensitive and can be done at your convenience."

# Provide the customized reminder
print(f"Reminder: '{task}' is high-priority.")
print(Reminder)
