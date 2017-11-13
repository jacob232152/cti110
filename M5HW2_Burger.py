# CTI-110
# M5HW2 - Running Total
# 10/17/2017
# Jacob Burger

# Initialized the accumulator.
total = 0
s = 1

# Get input to determine the total.
while total != -1:            
    total = float(input('Enter a number? '))        
    s = s + total

# Display the total.
print('Total Sum =', s)
