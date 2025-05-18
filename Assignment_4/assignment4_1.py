# write a program which contains one lambda function which accepts one parameter and return power of two
# input: 4          output: 16
# input: 6          output: 64

power = lambda x: (x**2)

print("enter a num: ")
num = int(input())

print("the power of two for the given number is: ", power(num))