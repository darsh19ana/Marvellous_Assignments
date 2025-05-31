# design python application which creates two threads as evenfactor and oddfactor. 
# both the thread accept one paramter as integer. 
# evenfactor thread will display addition of even factors of given number and 
# oddfactor will display addition of odd factors of given number. 
# after execution of both the thread gets completed main threads should dsplay message as "exit from main"

import threading

def Factors(no):
    result = []
    for i in range(1, no + 1):
        if no % i == 0:
            result.append(i)
    return result

def EvenFact(no):
    print("even thread started")
    factors = Factors(no)
    evensum = 0
    for i in factors:
        if i%2 == 0:
            evensum = evensum + i
    print("even factors sum of", no, "is: ", evensum)
    print("even thread ended")

def OddFact(no):
    print("odd thread started")
    factors = Factors(no)
    oddsum = 0
    for i in factors:
        if i%2 == 1:
            oddsum = oddsum + i
    print("odd factors sum of", no, "is: ", oddsum)
    print("odd thread ended")

def main():
    print("enter a number: ")
    num = int(input())

    T1 = threading.Thread(target=EvenFact, args = (num,))
    T2 = threading.Thread(target=OddFact, args = (num,))
    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")

if __name__ == "__main__":
    main()