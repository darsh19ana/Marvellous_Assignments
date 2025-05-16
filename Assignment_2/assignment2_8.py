# write a program which takes a number from the user and print the below pattern
# input: 5
# output: 1
#         1 2
#         1 2 3
#         1 2 3 4
#         1 2 3 4 5

def numpattern(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

print("enter a number: ")
a = int(input())
numpattern(a)