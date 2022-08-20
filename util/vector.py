import math

class Vector3():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def dist(self, other: 'Vector3') -> float:
        return (self - other).length()