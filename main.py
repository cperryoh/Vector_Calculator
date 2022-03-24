import math


def isNumber(str):
    try:
        float(str)
        return True
    except Exception:
        return False


def strToVector(vector):
    vector = vector.replace("<", "")
    vector = vector.replace(">", "")
    vector = vector.replace("(", "")
    vector = vector.replace(")", "")

    vector = vector.split(",")
    return vector


def getVector(name, prev):
    valid = False

    vector = input(
        f"Enter vector(Ex. 1,2,3) {name} or enter [p] to use the last calculated vector assuming there is one: ")
    if (vector.lower() == 'p' and prev != ''):
        return prev
    elif (prev == '' and vector.lower() == 'p'):
        print("There is no previous vector continue to enter a new vector\n")
        vector = input(f"Enter vector(Ex. 1,2,3) {name}: ")
    vector = strToVector(vector)
    while not valid:
        allValid = True

        # make sure all entered values are numbers
        for i in vector:
            if not isNumber(i):
                allValid = False
        valid = allValid

        # Determain if amount of numbers in vector is valid
        if len(vector) != 3:
            if len(vector) == 2:
                vector.add('0')
            else:
                valid = False

        # if not valid tell user and get input again and loop again
        if not valid:
            print("Vector is invalid try again\n")
            vector = input(f"Enter vector(Ex. 1,2,3) {name}: ")
            vector = strToVector(vector)
    return Vector(float(vector[0]), float(vector[1]), float(vector[2]))


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.mag = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
        if (self.mag != 1 and self.mag != 0):
            try:
                self.unitVector = Vector(x / self.mag, y / self.mag, z / self.mag)
            except ZeroDivisionError:
                self.unitVector = Vector(0, 0, 0)
        else:
            self.unitVector = "N\\a"

    def dotProduct(self, v):
        outVar = v.x * self.x
        outVar = outVar + (v.y * self.y)
        outVar = outVar + (v.z * self.z)
        return outVar
    def vectorAsString(self):
        return f"<{self.x},{self.y},{self.z}>"
    def __str__(self):
        return f"<{self.x},{self.y},{self.z}>\nMagnitude: {round(self.mag, 4)}"

    def cross(self, v):
        x = (self.y * v.z) - (self.z * v.y)
        y = -((self.x * v.z) - (self.z * v.x))
        z = (self.x * v.y) - (self.y * v.x)

        # deal with negative 0s(floats can a have a negative 0)
        if x == -0.0:
            x = 0.0
        if y == -0.0:
            y = 0.0
        if z == -0.0:
            z = 0.0

        return Vector(x, y, z)


userIn = ''
prev = ''
while not userIn == 'q':

    userIn = input("Choose a operation [q- quit, c-cross product, d-dot product]").lower()

    v1 = getVector("v1", prev)
    v2 = getVector("v2", prev)

    if userIn == 'c':
        v3 = v1.cross(v2)
        prev = v3
        theta = math.asin((v3.mag / (v1.mag * v2.mag))) * (180 / math.pi)
        print(f"\nV1\n{str(v1)}\n\nV2\n{str(v2)}\n")
        print(f"Cross product outcome:\n{v1.vectorAsString()}X{v2.vectorAsString()}={v3.vectorAsString()}\nMagnitude: {round(v3.mag,4)}\nTheta between the two vectors: {round(theta, 5)} degrees\n")
    elif userIn == 'd':
        dot = v1.dotProduct(v2)
        print(f"\n{v1.vectorAsString()}•{v2.vectorAsString()}={dot}\n")
