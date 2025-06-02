# write a program which contains filter(), map() and reduce() in it. python application which contains one list of numbers. 
# list contains the numbers which are accepted from user. 
# filter should filter out all such numbers which are even. 
# map function will calculate its square. 
# reduce will return addition of all that numbers. 

from functools import reduce

print("enter number of elements: ")
num = int(input())

elements = list()
print("enter the elements: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("input list: ", elements)

CheckEven= lambda no: no%2 ==0

square = lambda no: no**2

sum = lambda a, b: a+b

FData = list(filter(CheckEven, elements))   
print("filter output: ", FData)

MData = list(map(square, FData))
print("map output: ", MData)

RData = reduce(sum, MData)
print("reduce output: ", RData)