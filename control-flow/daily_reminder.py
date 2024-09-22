# Prompt for a single task

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority. Consider attending to it as soon as you can."
    case "low":
        reminder = f"'{task}' is a low priority."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Check if the task is time-bound and modify the reminder
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
else:
    reminder += "Take your time. This is not urgent"

# Provide the customized reminder
print(reminder)
