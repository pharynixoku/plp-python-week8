# PLP Python Week 8 Final Project
# Personal Mini-Toolkit


# Tool 1: Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = first_number + second_number
            print(f"Result: {first_number} + {second_number} = {result}")

        elif operation == "2":
            result = first_number - second_number
            print(f"Result: {first_number} - {second_number} = {result}")

        elif operation == "3":
            result = first_number * second_number
            print(f"Result: {first_number} * {second_number} = {result}")

        elif operation == "4":
            if second_number == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {result}")

        else:
            print("Invalid operation. Please choose 1, 2, 3, or 4.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: To-Do List
# This tool allows the user to add, view, and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                task = input("Enter the task to remove: ")

                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' has been removed.")
                else:
                    print(f"Sorry, '{task}' is not on your list.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Tool 3: Even Number Checker
# This tool checks whether a number is even or odd.
def even_checker():
    print("\n--- Even Number Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Tool 4: Name Formatter
# This tool formats the user's name in a clean way.
def name_formatter():
    print("\n--- Name Formatter ---")

    name = input("Enter your full name: ")

    formatted_name = name.strip().title()

    print(f"Your formatted name is: {formatted_name}")
    print(f"Nice to meet you, {formatted_name}!")


# Main menu
# This loop keeps the toolkit running until the user chooses Quit.
print("-----------------------------------")
print("     WELCOME TO MY MINI-TOOLKIT")
print("-----------------------------------")

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Even Number Checker")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        even_checker()

    elif choice == "4":
        name_formatter()

    elif choice == "5":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice.")
        print("Please choose a number from 1 to 5.")