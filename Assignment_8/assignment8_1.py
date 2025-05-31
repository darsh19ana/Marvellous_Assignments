# design python application which creates two thread named as even and odd. 
# even thread will display first 10 even numbers and odd thread will display first 10 odd numbers. 

import threading

def Even():
    print("even thread started")
    for i in range(0, 10, 2):
        print(i)
    print("even thread ended")

def Odd():
    print("odd thread started")
    for i in range(1, 10, 2):
        print(i)
    print("odd thread ended")

def main():
    T1 = threading.Thread(target=Even)
    T2 = threading.Thread(target=Odd)
    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("main thread end")

if __name__ == "__main__":
    main()