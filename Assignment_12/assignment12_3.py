# write a program which contains one class named as Arithmetic
# Arithmetic class contains three instance variables as Value1, Value2
# Inside init method initialise all instnace variables to 0
# There are three instnace methods inside class as Accept(), Addition(), Subtraction(), Multiplication() and Division()
# Accept method will accept value of Value1, value2 from the user 
# Addition() will perform addition and return result
#  same for Multiplication(), division, subtarction
# After designing the above class call all instnace methods by creating multiple objects

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first value: ")
        self.Value1 = float(input())
        print("Enter the second value: ")
        self.Value2 = float(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "division by zero is not allowed"

print("Object 1:")
obj1 = Arithmetic()
obj1.Accept()
print("Addition:", obj1.Addition())
print("Subtraction:", obj1.Subtraction())
print("Multiplication:", obj1.Multiplication())
print("Division:", obj1.Division())

print("Object 2:")
obj2 = Arithmetic()
obj2.Accept()
print("Addition:", obj2.Addition())
print("Subtraction:", obj2.Subtraction())
print("Multiplication:", obj2.Multiplication())
print("Division:", obj2.Division())
