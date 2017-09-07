# CTI-110
# M2HW2-Tip Tax Total
# Jacob Burger
# 9/7/2017
# Get user input
foodCost = int(input('Input cost of food: '))

# tipAmount
tipAmount = foodCost * .18
print('tipAmount is:' ,tipAmount)

#salesTax
salesTax = foodCost * .07
print('salesTax is:' ,salesTax)

#totalCost
totalCost = foodCost + tipAmount + salesTax
print('totalCost is:' ,totalCost)

