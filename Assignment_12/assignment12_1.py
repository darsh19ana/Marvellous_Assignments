# write a program which contains one class named as Demo. 
# Demo class contains two instance variables as no1, no2.
# that class contains one class variable as Value. 
# there are two instnace methods of class as Fun and Gun which displays values of instance variables
# initilaise instance varible in init method by accepting the values from the user.

# after creating the class create the two objects of Demo class
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)

# now call the instance methods as 
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    Value = 0

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print(f"Fun method called:")
        print("no1 =", self.no1) 
        print("no2 =", self.no2)

    def Gun(self):
        print("Gun method called:")
        print("no1 =", self.no1) 
        print("no2 =", self.no2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
