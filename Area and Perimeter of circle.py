class Circle:
    def __init__(self, r):
        self.r = r
        self.pi = 3.14159 

    def area(self):
        return self.pi * (self.r ** 2)

    def perimeter(self):
        return 2 * self.pi * self.r
    
radius = float(input("Enter radius: "))
my_circle = Circle(radius)
print(f"Area: {my_circle.area():.2f}")
print(f"Perimeter: {my_circle.perimeter():.2f}")