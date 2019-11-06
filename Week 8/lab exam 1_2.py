# Lab test re-submission 05/11/2019
# Written by Hugh O'Carroll-Macri
# C17316046
# Pascal's triangle

# Appending old rows with new rows
def make_new_row(old_row):
    if old_row == []:
        return [1]
    if old_row == [1]:
        return [1,1]
    new_row = [1]
    for i in range(len(old_row)-1):
        new_row.append(old_row[i] + old_row[i+1])
    else:
        new_row.append(1)
    return new_row

n = 0

# User interaction with program to request a certain number of rows
while True:
    user_row = input("Please enter how many rows you would like(Greater than 2):")
    user_row = int(user_row)
    if user_row < 2:
        print("Please enter a valid number of rows greater than 2 ")
        continue
    elif user_row == 2:
        print("Please enter a valid number of rows greater than 2 ")
        continue
    else:
        n = 0
        n = int(user_row)
        break

# Calling functions to make rows and compile them as a list
L = [[1]]
r = [1,1]
for i in range(n-2):
    L.append(r)
    r = make_new_row(r)
else:
    L.append(r)

# Printing output as a list
print("Printing whole list of lists:")
print(L)

# Printing each row on individual lines
print("Printing list of lists, one list at a time:")
for i in L:
    print(i)

# Printing rows on individual lines centered
print("Printing lists as strings")
for i in L:
    row = ' '.join([str(j) for j in i])
    print(row.center(100))
