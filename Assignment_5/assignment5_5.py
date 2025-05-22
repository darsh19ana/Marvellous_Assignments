# write a program to check whether the entered number is even or odd.
# expected input: enter a number: 17
# expected output: 17 is an odd number

def ChckEven(num):
    if num%2 == 0:
        print(num, " is a even number")
    elif num%2 == 1:
        print(num, " is an odd number")

try:
    print("enter a number: ")
    no = int(input())
    ChckEven(no)
except ValueError as vobj:
    print("enter a valid numeric input", vobj)