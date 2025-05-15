# write a program which accepts one number from user and return its factorial

def factorial(num):
    if num <= 0:
        print("enter a number greater than 0")
    else:
        result = 1
        for i in range(1, num+1):
            result = i*result
        print("the factorial of the given number is: ",result)

print("enter a number: ")
number = int(input())

factorial(number)