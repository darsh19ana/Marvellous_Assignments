# accept a list of integers from the user and use map() function to double each value
# expected input: enter list: 1 2 3 4 5 
# expected list: [2, 4, 6, 8, 10]

print("enter number of elements: ")
num = int(input())

elements = list()
print("enter the elements: ")

for i in range(num):
    val = int(input())
    elements.append(val)

print("input list: ", elements)

def double(no):
    result = 2*no
    return result

MData = list(map(double, elements))
print("map output: ", MData)