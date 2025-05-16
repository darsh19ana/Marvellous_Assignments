# write a program which accepts N numbers from user and store it in a list. return maximum number from that list. 
# input: number of elements 7
# input elements: 13  5  45  7  4  56  34
# output: 56

print("enter a number: ")
num = int(input())

elements = list()
print("enter the elements in a list: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("the maximum number from the list is: ", max(elements))


    