#Bo lontum
#'Homework2-even_or_odd_checkers.py:

   # Function to check if a number is even or odd
    # Returns "Even" if number is even, "Odd" if number is odd

def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
# let's say if,
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 21, 100,105,106, 1001]
for num in numbers:
    result = check_number(num)
    print(f"{num} is {result}")