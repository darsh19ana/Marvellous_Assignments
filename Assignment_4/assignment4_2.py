# write a program which contains one lambda function which accepts two parameters and returns its multiplication
# input: 4  3         output: 12
# input: 6  3         output: 18

multiplication = lambda x, y: (x*y)

print("enter two numbers: ")
num1 = int(input())
num2 = int(input())

result = multiplication(num1, num2)

print("the multiplication of these two numbers is: ", result)