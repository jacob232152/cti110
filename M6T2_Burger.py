# CTI-110
# M6T2 - Feet to Inches
# Jacob Burger
# 11/9/2017

# Constant for the number of inches per foot.
INCHES_PER_FOOT = 12

# Main function
def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()
