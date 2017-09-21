# CTI-110
# M3HW1 - Age Classifier
# Jacob Burger
# 9/18/2017

def main():
    # This program determines whether a person is an infant, child, teenager, or adult.
    age = int(input('Enter the age of the person: '))


# Get the age of the person
age = int(input('Enter the age of the person: '))

# Determine if person is an infant, child, teenager, or adult
if age <= 1:
    print('This person is a infant.')
elif age > 1 and age < 13:
    print('This person is a child.')
elif age >= 13 and age < 20:
    print('This person is a teenager.')
else:
    print('This person is a adult.')

# program start
main()
