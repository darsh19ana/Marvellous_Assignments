# write a program which contains one lambda function which accepts two parameters and return its multiplication.

mult = lambda x, y: x*y

print("enter first number: ")
num1 = int(input())

print("enter second number: ")
num2 = int(input())

result = mult(num1, num2)
print("the result is: ", result)