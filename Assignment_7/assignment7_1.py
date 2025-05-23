# write two lambda functions
# one to calculate the square of a number
# another to calculate cube of a number

# expected input: enter a number: 3
# expected output: square: 9
# cube: 27

print("enter a number: ")
num = int(input())

square = lambda x: x**2
cube = lambda x: x**3

def main():
    ret = square(num)
    print("square: ",ret)
    ret = cube(num)
    print("cube: ",ret)

if __name__ == "__main__":
    main()