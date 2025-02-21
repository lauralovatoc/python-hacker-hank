from math import pi
class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter/2

    @property
    def area(self):
        return pi *self.radius* self.radius

    def __repr__(self):
        return f"Circle({self.radius})"
