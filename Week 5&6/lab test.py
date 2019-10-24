#Lab test 24/10/2019
#Written by Hugh O'Carroll-Macri
#C17316046
#Pascal's triangle

import math

def calculation(n, r):
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def make_new_row(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(calculation(count, element))
        result.append(row)
    return result

x = 0

while x == 0:
    user_row = input("Please enter how many rows you would like:")
    user_row = int(user_row)
    if user_row == 0:
        print("Please enter a valid number of rows greater than 0 ")
        continue
    else:
        break

print("Printing the list of rows on one line")
print(make_new_row(user_row))
print("Printing rows on own individual lines")

for row in make_new_row(user_row):
    print(row)
