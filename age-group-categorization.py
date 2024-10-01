# age-group-categorization.py

def categorize_age(age):
    if age < 0 or age > 150:
        return "Invalid age"
    if 0 <= age <= 1:
        return "Infant"
    elif 2 <= age <= 3:
        return "Toddler"
    elif 4 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 64:
        return "Adult"
    elif age >= 65:
        return "Senior"
    else:
        return "Invalid age"

# Prompt the user for their age
try:
    age = int(input("Enter your age: "))
    category = categorize_age(age)
    print(f"Your Life stage: {category}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
