class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)


w = int(input("Enter width of rectangle: "))
h = int(input("Enter height of rectangle: "))

obj = rectangle(w, h)
print("area of rectangle is", obj.area)
print("perimeter of rectangle is", obj.perimeter)