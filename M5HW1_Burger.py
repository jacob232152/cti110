# CTI-110
# M5HW1 - Distance Traveled
# Jacob Burger
# 10/17/2017

# Input speed of vehicle and hours traveled.
speed = int(input('What is the speed of the vehicle in mph? '))
time = int(input('How many hours has it traveled? '))

# Distance formula.
distance = time * speed
t = time + 1

# Display in table format.
DataString = "Hour      Distance Traveled"
print (DataString)
DataString = "---------------------------"
print (DataString)

# Determine distance.
for time in range(1, t):
    print(time, distance) 
    

