# CTI-110
# M3HW2 - Software Sales
# Jacob Burger
# 09/19/2017

def main():
    # This program determines the cost of your total purchase.
    # It is also determined if the purchase qualifies for a discount.
    packages = int(input('Enter the amount of packages purchased: '))

# Amount of packages purchased
packages = int(input('Enter the amount of packages purchased: '))

# The cost of a package
packagecost = 99

# The total cost with no discount
totalNd = packages * packagecost

# The total cost with 10% discount
total10 = totalNd * .90

# The total cost with 20% discount
total20 = totalNd * .80

# The total cost with 30% discount
total30 = totalNd * .70

# The total cost with 40% discount
total40 = totalNd * .60

# Calculating the totals

if packages < 10:
    print('Your total is:' ,totalNd)
elif packages >= 10 and packages <= 19:
    print('Your discount is: 10%')
    print('Your total with this discount is:' ,total10)
elif packages >= 20 and packages <= 49:
    print('Your discount is 20%')
    print('Your total with this discount is:' ,total20)
elif packages >= 50 and packages <= 99:
    print('Your discount is 30%')
    print('Your total with this discount is:' ,total30)
else:
    print('Your discount is 40%')
    print('Your total with this discount is:' ,total40)
    
# program start
main()
