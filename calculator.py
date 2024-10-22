'''''''''
Bo Lontum
function3
Homework3 - calculator.py:
Write a calculator program.
Your code will provide two numbers and and the user will select what type of operation needed.'''''
def perform_operation(x, y, z):
    if z == '1':
        return f"{x} + {y} = {x + y}"
    elif z == '2':
        return f"{x} - {y} = {x - y}"
    elif z == '3':
        return f"{x} * {y} = {x * y}"
    elif z == '4':
        if y != 0:
            return f"{x} / {y} = {x / y: .3f}"
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation selection"
# Main program
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print("\nSelect the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

z = input("Enter the number corresponding to the operation (1/2/3/4): ")
# Call the function and display the result
result = perform_operation(x, y, z)
print(result)
