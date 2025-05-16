# write a program which accepts N numbers from user and store it into a list. return addition of all elements from that list.
# input: number of elements: 6
# input elemnts: 13  5  45  7  4  56
# output: 130

print("enter number of elements: ")
num = int(input())

elements = list()
print("enter the elements: ")

for i in range(num):
    val = int(input())
    elements.append(val)

result = 0
for i in elements:
    result += i

print("Sum of elements is:", result)