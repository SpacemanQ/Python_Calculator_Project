while True:
    # Get operands from user
    num1 = int(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = int(input("Enter second number: "))

    # Perform calculation
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("That is not a recognized operator")

    # Ask if user wants to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Goodbye!")
        break
