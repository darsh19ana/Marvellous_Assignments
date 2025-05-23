# accept 5 numbers from the user. find out print the largest number.
# expected input: enter 5 numbers: 23 89 12 56 45
# expected output: maximum number is: 89

num1, num2, num3, num4, num5 = map(int, input("Enter 5 numbers: ").split())

if num1> num2:
    if num1>num3 and num1>num4 and num1>num5:
        print("maximum number is: ", num1)
if num2> num3:
    if num2>num4 and num2>num5 and num2>num1:
        print("maximum number is: ", num2)
if num3>num4:
    if num3>num5 and num3>num2 and num3>num1:
        print("maximum number is: ", num3)
if num4>num5:
    if num4>num1 and num4>num3 and num4>num2:
        print("maximum number is: ", num4)
if num5>num1:
    if num5>num4 and num5>num3 and num5>num2:
        print("maximum number is: ", num5)