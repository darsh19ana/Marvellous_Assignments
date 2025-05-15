# write a program which accept one number and display below pattern
# input: 5
# output: * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

print("enter a number: ")
num1 = int(input())

def starpattern(num):
    for i in range(num):
        for j in range(num):
            print("* ", end = " ")
        print()

starpattern(num1)