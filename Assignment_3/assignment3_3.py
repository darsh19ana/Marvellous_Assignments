# write a program which accepts N numbers from user and store it into list. return minimum number from that list
# input: number of elements: 4
# input elements: 13  5  45  7  
# output: 5

print("enter a number: ")
num = int(input())

elements = list()
print("enter the elements in a list: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("the minimum number from the list is: ", min(elements))