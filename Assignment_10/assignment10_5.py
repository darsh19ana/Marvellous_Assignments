# write a program which contains filter(), map() and reduce() in it. python application which contains one list of numbers. list contains the numbers which are accepted from user. 
# filter should filter out all prime numbers. 
# map function will multiply each number by 2. 
# reduce will return maximum number from that numbers. 

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
    if no < 2:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True

def fun2(no):
    return no * 2

def fun3(x, y):
    return max(x, y)

FData = list(filter(fun1, elements))
print("filter output: ", FData)

MData = list(map(fun2, FData))
print("map output: ", MData)

RData = reduce(fun3, MData)
print("reduce output: ", RData)