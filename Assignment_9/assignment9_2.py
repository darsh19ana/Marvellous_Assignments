# write a python program using multiprocessing. 
# process to square a list of numbers using multiple processes.

import multiprocessing

def square(no):
    return no*no

def main():
    data = [23, 42, 2, 55]
    result = []

    p = multiprocessing.Pool()
    result = p.map(square, data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()