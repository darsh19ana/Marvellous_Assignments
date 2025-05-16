# write a program which accepts N numbers from user and store it into list. return addition of all prime numbers from that list. 
# main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined module named as MarvellousNum.
# name of the function from main python file should be ListPrime()

# input: number of elements: 11
# input elements: 13  5  45  7  4  56  10  34  2  5  8
# output: 54(13 + 5+ 7+ 2+ 5)

from MarvellousNum import ChkPrime

def ListPrime():
    print("Enter number of elements: ")
    n = int(input())

    elements = []
    print("Enter the elements:")
    for i in range(n):
        val = int(input())
        elements.append(val)

    result = 0
    for num in elements:
        if ChkPrime(num):
            result += num

    print("Addition of all prime numbers is:", result)

# Call the function
ListPrime()
