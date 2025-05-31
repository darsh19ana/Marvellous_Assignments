# design python application which contains two threads named as thread1 and thread2. 
# thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on screen. 
# after execution of thread1 gets complteed then schedule thread2

import threading
import time

def display_1_to_50():
    print("Thread1 started")
    for i in range(1, 51):
        print(i)
    print("Thread1 ended")

def display_50_to_1():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print(i)
    print("Thread2 ended")

def main():
    t1 = threading.Thread(target=display_1_to_50)
    t2 = threading.Thread(target=display_50_to_1)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Main thread ended.")

if __name__ == "__main__":
    main()
