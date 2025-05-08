# write a program which contains one function that accepts one number from user and
# returns true if the number is divisibe by 5 otherwise return false

def chcknum(num):
    if num%5 == 0:
        print("True")
    else:
        print("False")
    
print("Enter a number: ")
number = int(input())
result = chcknum(number)

