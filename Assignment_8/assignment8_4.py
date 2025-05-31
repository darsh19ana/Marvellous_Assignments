# design python application which creates three threads as small, capital, digits. 
# all the threads accepts string as paarmter. 
# small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. 
# display id and name of ecah thread. 

import threading

def small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print(f"thread Name: {threading.current_thread().name}")
    print(f"thread ID: {threading.get_ident()}")
    print(f"number of small characters: {count}")

def capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print(f"thread Name: {threading.current_thread().name}")
    print(f"thread ID: {threading.get_ident()}")
    print(f"number of capital characters: {count}")

def digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print(f"thread Name: {threading.current_thread().name}")
    print(f"thread ID: {threading.get_ident()}")
    print(f"number of digit characters: {count}")

def main():
    print("enter a string:")
    enteredstr = input()

    # Create threads
    t1 = threading.Thread(target=small, args=(enteredstr,))
    t2 = threading.Thread(target=capital, args=(enteredstr,))
    t3 = threading.Thread(target=digits, args=(enteredstr,))

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for threads to complete
    t1.join()
    t2.join()
    t3.join()

    print("main thread ended.")

if __name__ == "__main__":
    main()
