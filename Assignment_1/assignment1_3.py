# Write a program which contains one function named as Add() 
# which accepts two numbers from user and return addition of that two numbers.

def Add(num1, num2):
    ans = num1 + num2
    return ans

print("Enter first number: ")
value1 = int(input())

print("Enter second number: ")
value2 = int(input())

result = Add(value1, value2)
print("The addition is: ", result)