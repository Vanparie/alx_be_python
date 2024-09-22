# daily_reminder.py

# Prompt for a single task
task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is this task time-sensitive? (yes or no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Reminder: Your task: '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: Your task: '{task}' is of medium priority."
    case "low":
        reminder = f"Reminder: Your task: '{task}' is of low priority."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Check if the task is time-bound and modify the reminder
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Provide the customized reminder
print(reminder)
