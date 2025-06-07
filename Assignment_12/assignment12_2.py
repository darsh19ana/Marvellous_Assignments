# write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius, Area, Circumference. 
# That class contains one class variable as PI which is initialised to 3.14 
# Inside init method initilaise all instance variables to 0.0
# there are three instnace methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display()
# Accept method will accept value of radius from the user. 
# CalculateArea() method will calculate area of circle and store it in the instance variable Area
# CalculateCircumference() method will calculate circumference of circle and store it in the instance variable Circumference
# After designing the above class call all instance methods by creating multiple objects

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the radius of the circle: ")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius: ",self.Radius)
        print("Area: ", self.Area)
        print("Circumference: ",self.Circumference)


circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

print() 

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()
