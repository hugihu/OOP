#Lab test 24/10/2019
#Written by Hugh O'Carroll-Macri
#C17316046
#Pascal's triangle

import math

def calculation(a, b):
    return int((math.factorial(a)) / ((math.factorial(b)) * math.factorial(a - b)))

def make_new_row(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(calculation(count, element))
        result.append(row)
    return result
#Building each row

x = 0

while x == 0:
    user_row = input("Please enter how many rows you would like:")
    user_row = int(user_row)
    if user_row == 0:
        print("Please enter a valid number of rows greater than 0 ")
        continue
    else:
        break
#Asking user for how many rows they would like printed
#Also error checking to make sure they enter a valid number

print("Printing the list of rows on one line")
print(make_new_row(user_row))
#Prints list all on one line

print("Printing rows on own individual lines")
for row in make_new_row(user_row):
    print(row)
#Printing rows on own individual lines

print("Now printing without brackets or commas")
print(''.join([str(row) for row in make_new_row(user_row)]))
# Couldn't get the list to center properly

