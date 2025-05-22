# accept three numbers from the user and print the largest using nested if-else statements. 
# expected input: enter three numbers: 5 9 3
# expected output: largest number is 9

print("enter three numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Print the largest number
print("Largest number is", largest)