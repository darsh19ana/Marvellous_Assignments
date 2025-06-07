# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user. 
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), Sum Factors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self):
        print("enter a number: ")
        self.Value = int(input())

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.Value == self.SumFactors()

    def Factors(self):
        print(f"Factors of {self.Value}: ", end="")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

print("Object 1:")
obj1 = Numbers()
obj1.Factors()
print("Sum of factors:", obj1.SumFactors())
print("Prime?", obj1.ChkPrime())
print("Perfect?", obj1.ChkPerfect())

print("Object 2:")
obj2 = Numbers()
obj2.Factors()
print("Sum of factors:", obj2.SumFactors())
print("Prime?", obj2.ChkPrime())
print("Perfect?", obj2.ChkPerfect())
