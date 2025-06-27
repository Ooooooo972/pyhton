class Vector:
    def _init_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def _add_(self, other):
        # Vector addition
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def _mul_(self, other):
        # Dot product
        return self.x * other.x + self.y * other.y + self.z * other.z

    def _str_(self):
        # String representation
        return f"({self.x}, {self.y}, {self.z})"

v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1+v2)
print(v1*v2)

v_sum = v1 + v2
print("v1 + v2 =", v_sum)
v_dot = v1 * v2
print("v1 · v2 =", v_dot)
print("v1 + v3 =", v1 + v3)

