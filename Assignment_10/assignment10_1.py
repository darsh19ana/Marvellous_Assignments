# write a program which contains one lambda function which accepts one paarmeter and return power of two.

two_power = lambda x: x**2

print("enter a number: ")
num = int(input())

result = two_power(num)
print("the result is: ", result)