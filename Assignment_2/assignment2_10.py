# write a program which accept number from user and return addition of digits in that number

print("enter a number: ")
num = input()

result=0
for i in num:
    i = int(i)
    result = result + i

print("the sum of digits is: ",result)