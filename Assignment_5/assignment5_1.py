# write a program to accept two integers from the user and display their:
# sum, difference, product, division

# expected input: enter first number: 10
# enter second number: 2
# expected output: 
# sum = 12
# difference = 8
# product = 20
# divsion = 5

print("enter first number: ")
num1 = int(input())

print("enter second number: ")
num2 = int(input())

def sum(n1, n2):
    result = n1+n2
    return result

def difference(n1, n2):
    result = n1-n2 
    return result

def product(n1, n2):
    result = n1*n2 
    return result

def division(n1, n2):
    result = n1/n2
    return result

def main():
    sum_result = sum(num1, num2)
    print("Sum = ", sum_result)
    diff_result = difference(num1, num2)
    print("Difference = ", diff_result)
    product_result = product(num1, num2)
    print("Product = ", product_result)
    div_result = division(num1, num2)
    print("Division = ", div_result)

if __name__ == "__main__":
    main()  
