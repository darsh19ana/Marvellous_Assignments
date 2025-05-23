# write a function that accepts a list of integers and returns a list of prime numbers using filter()
# expected input: enter list: 10 11 12 13 14 15 16 17
# expected output: prime numbers: [11, 13, 17]

input_list = input("Enter list: ").split()

numbers = list(map(int, input_list))
def chckprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

prime_numbers = list(filter(chckprime, numbers))
print("prime numbers:", prime_numbers)