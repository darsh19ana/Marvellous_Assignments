# write a program which accepts number from user and check whether that number is positive or negative or zero.

print("Enter a number: ")
number = int(input())

if number< 0:
    print("Negative number")
elif number> 0:
    print("Positive number")
else:
    print ("Zero")