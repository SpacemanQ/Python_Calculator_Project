while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Division by zero is undefined.")
        else:
            print("That is not a recognized operator.")

    except ValueError:
        print("Invalid input. Please enter numerical values.")

    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Peace!")
        break
