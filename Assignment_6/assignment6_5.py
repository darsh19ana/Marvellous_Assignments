# accept a number from the user and check whether it is prime or not
# expected input: enter a number: 11
# expected output: 11 is a prime number

print("enter a number: ")
num = int(input())

if num <= 1:
    print("not a prime number neither composite")
for i in range(2, num):
    if num % i == 0:
        print("not a prime number")
print("prime number")