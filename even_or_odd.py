# lab-cake1: checking for even or odd
# writting a program that will use a number then, check if the number is EVEN or ODD

number = int(input("Please enter a number between 1-100: "))

# Check if the number is even or odd
if 1 <= number <= 100:
    if number % 2 == 0:
        print(f"Your number {number} is even.")
    else:
        print(f"Your number {number} is odd.")
else:
    print(f"The number {number} is invalid, input a number between 1 and 100.")



    


