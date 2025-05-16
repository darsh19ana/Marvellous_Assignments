# write a program which accepts one number and display below pattern
# input: 5
# output: 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5

def numpattern(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(j, end = " ")
        print()

print("enter a number: ")
a = int(input())
numpattern(a)