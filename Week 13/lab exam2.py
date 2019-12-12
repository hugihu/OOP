# OOP Lab exam 2
# Written by Hugh O'Carroll-Macri
# C17316046
#12/12/2019

class Vector3D:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # String representation
    def __str__(self):
        return '<%s, %s, %s>' % (self.x, self.y, self.z)

    # Addition
    def __add__(self, number):
        return Vector3D(self.x + number, self.y + number, self.z + number)

    # Subtraction
    def __sub__(self, number):
        return Vector3D(self.x - number, self.y - number, self.z + number)

    # Scalar Multiplication
    def __mul__(self, number):
        return Vector3D(self.x * number, self.y * number, self.z * number)

    # Magnitude
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (.5)