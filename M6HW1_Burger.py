# CTI-110
# M6HW1 - Test Grading Program
# 11/9/2017
# Jacob Burger


# Obtain test grades from user.
def main():
    grade1 = int(input('Enter a grade for a test: '))
    grade2 = int(input('Enter a grade for a test: '))
    grade3 = int(input('Enter a grade for a test: '))
    grade4 = int(input('Enter a grade for a test: '))
    grade5 = int(input('Enter a grade for a test: '))
    total = grade1 + grade2 + grade3 + grade4 + grade5
   
def calc_average():
    calc_average = total/5
    print('Your', calc_average, 'average test grade is ') 

# Call the main function.
main()
