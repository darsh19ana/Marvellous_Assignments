# write a program which accept one number and display below pattern
# input: 5
# output: * * * * * 
#         * * * * 
#         * * * 
#         * * 
#         * 

def starpattern(num):
    for i in range(num, 0, -1):
        for j in range(i):
            print("* ", end = " ")
        print()

print("enter a number: ")
a = int(input())

starpattern(a)