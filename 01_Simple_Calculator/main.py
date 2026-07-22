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


====== Calculator ======

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Choose:
'''
print("====== Calculator ======\n")
options = {"1": "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Division", "5": "Exit"}

for key, value in options.items():
    print(f"{key}. {value}")

choice = input("Choose: ")
if choice in options:
    if choice == "5":
        print("Exiting the calculator. Goodbye!")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            result = num1 + num2
            operation = "Addition"
        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"
        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                operation = "Division"
            else:
                print("Error: Division by zero is not allowed.")
                exit()
        
        print(f"\nResult of {operation}: {result}")