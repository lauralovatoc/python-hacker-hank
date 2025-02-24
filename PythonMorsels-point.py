class Point:
    def  __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self,other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self,other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self,other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __rmul__(self,other):
        return Point(self.x * other, self.y * other, self.z * other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
