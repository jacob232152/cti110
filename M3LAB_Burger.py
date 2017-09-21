# CTI-110
# M3-LAB-Debugging
# Jacob Burger
# 9/21/2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    
    # TO DO: define the rest of the score

    score = int(input("What is the test score? "))

# Input test score
score = int(input("What is the test score? "))

# Determine what letter grade the test score translates to.    
if score >= 90:
    print('Your grade is: A')
elif score >= 80 and score <= 89:
    print('Your grade is: B')
elif score >= 70 and score <= 79:
    print('Your grade is: C')
elif score >= 60 and score <= 69:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this







# program start
main()
