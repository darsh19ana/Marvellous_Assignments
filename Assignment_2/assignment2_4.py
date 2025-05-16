# write a program which accepts one number from the user and return addition of its factors

def factors(a):
    result = 0
    for i in range(1, a+1):
        if a % i == 0:
            result += i
    return result

print("enter a number: ")
num = int(input())
addition = factors(num)
print("the addition of factors is:", addition)
