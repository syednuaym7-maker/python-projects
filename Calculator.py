import math
history = []
def show_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Modulus")
    print("8. Factorial")
    print("9. View History")
    print("10. Exit")
while True:
    show_menu()
    choice = input("Enter choice (1-10): ")
    if choice == '10':
        print("Exiting the calculator. Goodbye!")
        break
    elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        num1 = float(input("Enter first number: "))
        if choice != '5' and choice != '8':
            num2 = float(input("Enter second number: "))
        if choice == '1':
            result = num1 + num2
            print("The result of addition is:",result)
        elif choice == '2':
            result = num1 - num2
            print("The result of subtraction is: ",result)
        elif choice == '3':
            result = num1 * num2
            print("The result of multiplication is: ",result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("The result of division is:",result)
            else:
                print("Error! Division by zero.")
        elif choice == '5':
            result = math.sqrt(num1)
            print("The square root of",num1, "is:", result)
        elif choice == '6':
            result = math.pow(num1, num2)
            print(num1, "raised to the power of", num2, "is:", result)
        elif choice == '7':
            result = num1 % num2
            print("The modulus of", num1, "and", num2, "is:", result)
        elif choice == '8':
            if num1 < 0:
                print("Error! Factorial of a negative number doesn't exist.")
            else:
                result = math.factorial(int(num1))
                print("The factorial of", int(num1), "is:", result)
    elif choice == '9':
        print("\n----- Calculation History -----")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        continue
    else:
        print("Invalid input. Please enter a number between 1 and 10.")