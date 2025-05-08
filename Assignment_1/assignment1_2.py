# Write a program which contains one function named as ChkNum() which accept one parameter as number.
# If number is even then it should display "Even number" otherwise display "Odd number" on console.
# Input: 11       Output: Odd number
# Input: 8        Output: Even number

def ChkNum(num):
    if num%2 == 0:
        print("Even Number")
    else:
        print("Odd number")

print("Enter a number: ")
number = int(input())

ChkNum(number)