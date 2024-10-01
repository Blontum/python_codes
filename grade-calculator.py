# Grade calculator for 5 subjects

def calculate_average(grades):
    return sum(grades) / len(grades)
def get_grade(average):
    return 'A' if average > 90 else 'B' if average > 80 else 'C' if average > 70 else 'D' if average > 60 else 'E (Failed)'

def main():
    #getting grades for each subkject
    English_grade = float(input("English grade is: "))
    Maths_grade   = float(input("Maths grade is: "))
    History_grade = float(input("History grate is: "))
    Chemist_grade = float(input("Chemist grade is: "))
    Geology_grade = float(input("Geology grade is: "))

#  sum all grades
    total_grades = English_grade + Maths_grade + History_grade + Chemist_grade + Geology_grade
    
    # Calculate the average
    average = total_grades / 5  # There are 5 subjects
    # Get the final grade
    final_grade = get_grade(average)

    # Print results
    print(f"\nYour average grade is: {average:.2f}") # 2 decimal pls and floatx pt No
    print(f"\nYour final grade is: {final_grade}")

# Check if this script is being run directly
if __name__ == "__main__":
    main()