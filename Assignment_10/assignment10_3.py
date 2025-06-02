# write a program which contains filter(), map() and reduce() in it. 
# python application which contains one list of numbers. 
# list contains the numbers which are accepted from user. 
# filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. 
# map function will increase each number by 10. 
# rduce will return product of all that numbers. 

from functools import reduce

print("enter number of elements: ")
num = int(input())

elements = list()
print("enter the elements: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("input list: ", elements)

def fun1(no):
    return 70 <= no <= 90

def fun2(no):
    return no + 10

def fun3(x, y):
    return x * y

FData = list(filter(fun1, elements))
print("filter output: ", FData)

MData = list(map(fun2, FData))
print("map output: ", MData)

RData = reduce(fun3, MData)
print("reduce output: ", RData)