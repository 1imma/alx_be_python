# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Check priority and time-bound status
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high-priority task. Try to complete it soon!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium-priority task that can be performed later!")
        else:
            print(f"Reminder: '{task}' is a medium-priority task. It can be deferred but should be done soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low-priority task but still time-sensitive. Plan accordingly.")
        else:
            print(f"Reminder: '{task}' is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use 'high', 'medium', or 'low'.")
