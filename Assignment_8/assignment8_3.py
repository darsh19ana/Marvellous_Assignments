# design python application which creates two threads as evenlist and oddlist. 
# both the threads accept list of integers as paaremter. 
# evenlist thread add all even elements from input list and display the addition. 
# oddlist thread all odd elements from input list and display the addition. 

import threading

def evenlist(num):
    print("even thread started")
    evensum = 0
    for i in num:
        if i%2 == 0:
            evensum = evensum+i
    print("sum of even numbers: ", evensum)
    print("even thread ended")

def oddlist(num):
    print("odd thread started")
    oddsum = 0
    for i in num:
        if i%2 == 1:
            oddsum = oddsum+i
    print("sum of odd numbers: ", oddsum)
    print("odd thread ended")

def main():
    print("enter a list of numbers: ")
    input_list = input()
    nums = list(map(int, input_list.split()))

    T1 = threading.Thread(target=evenlist, args = (nums,))
    T2 = threading.Thread(target=oddlist, args = (nums,))
    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()