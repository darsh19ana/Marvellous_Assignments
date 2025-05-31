# create a python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def factorial(no):
    result = 1
    for i in range(1, no+1):
        result = result*i
    return result

def main():
    data = [23, 42, 2, 55]
    result = []

    p = multiprocessing.Pool()
    result = p.map(factorial, data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()