class circle:

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius

r = int(input("Enter radius of circle: "))
obj = circle(r)
print("area of circle is", obj.area)
print("circumference of circle is", obj.circumference())