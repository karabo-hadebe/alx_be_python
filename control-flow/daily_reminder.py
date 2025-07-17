task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no)")

match priority:
    case "high": 
        if time == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")

        