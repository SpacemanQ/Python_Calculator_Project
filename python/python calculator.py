
# Get operands from user
num1 = int(input("Enter first number: "))
op = input("Enter operator (+, -, * /): ")
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
    print("Invalid operator")
