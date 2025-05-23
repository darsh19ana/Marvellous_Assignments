# accept a number and print its factorial using a for loop
# expected input: enter a number: 5
# expected output: factorial of 5 is: 120

print("enter a number: ")
num = int(input())

fact = 1
for i in range(num):
    fact = fact*(i+1)
print("factorial of", num, "is: ", fact)