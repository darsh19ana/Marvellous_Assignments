## Create a module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. write a python program which call all the functions from Arithmetic module by accepting the parameters from user.

from Arithmetic import Add, Sub, Mult, Div

print("Enter any two numbers: ")
num1 = int(input())
num2 = int(input())

addition = Add(num1, num2)
print("addition: ", addition)
subtraction = Sub(num1, num2)
print("subtraction: ", subtraction)
multiplication = Mult(num1, num2)
print("multiplication: ", multiplication)
division = Div(num1, num2)
print("division: ", division)
