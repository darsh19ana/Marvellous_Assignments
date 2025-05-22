# accept the length and width of a rectangle. calculate and display the area and perimeter. 
# expected input: enter length: 5
#                 enter width: 3
# expected output: area: 15
#                  perimeter: 16

print("enter length: ")
l = float(input())
print("enter width: ")
w = float(input())

def area(length, width):
    result = length*width
    return result

def perimeter(length, width):
    result = 2*(length+width)
    return result

def main():
    ret = area(l, w)
    print("area: ", ret)
    ret = perimeter(l,w)
    print("perimeter: ", ret)

if __name__ == "__main__":
    main()
