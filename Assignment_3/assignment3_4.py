# write a program which accepts N numbers from user and store it into list. accept one another number from the user and return frequency of that number of list.
# input: number of elements: 11
# input elements: 13  5  45  7  4  56  5  34  2  5  65
# element to search: 5
# output: 3

print("enter a number: ")
num = int(input())

elements = list()
print("enter the elements in a list: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("enter a element to search: ")
searchnum = int(input())

counter = 0
for i in elements:
    if i == searchnum:
        counter = counter+1

print("the element ", searchnum, " has occured ", counter, " times")
