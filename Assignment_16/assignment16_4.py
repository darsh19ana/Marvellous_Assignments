# accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line

def fun():
    file = "numbers.txt"

    print("Enter 10 numbers separated by space:")
    nums = input().split()

    if len(nums) != 10:
        print("Please enter exactly 10 numbers.")
        return

    with open(file, "w") as fobj:
        for num in nums:
            fobj.write(num + "\n")

    print("Numbers written to numbers.txt")

fun()