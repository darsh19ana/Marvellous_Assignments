# write a program which accept one number for user and check whether number is prime or not

def chkprime(num):
    if num <= 1:
        print("It is not a prime number")
        return

    for i in range(2, num):
        if num % i == 0:
            print("It is not a prime number")
            return  
    print("It is a prime number")  

print("enter a number: ")
a = int(input())
chkprime(a)

        
