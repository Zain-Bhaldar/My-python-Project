'''
====== Calculator ======

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Choose: 1

Enter first number: 10
Enter second number: 20

Result: 30
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def addition():
    result = a + b
    print(f"Result: {result}")

def subtraction():
    result = a - b
    print(f"Result: {result}")

def multiplication():
    result = a * b
    print(f"Result: {result}")

def division():
    if b != 0:
        result = a / b
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")

def main_menu():
    print("====== Calculator ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
