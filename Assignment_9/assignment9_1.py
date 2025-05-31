# create a python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. 
# use threading.thread

import threading
import time

def print_numbers():
    thread_name = threading.current_thread().name
    for i in range(1, 6):
        print(thread_name, "prints: ", i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=print_numbers, name="thread1")
    t2 = threading.Thread(target=print_numbers, name="thread2")
    t3 = threading.Thread(target=print_numbers, name="thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All threads completed.")

if __name__ == "__main__":
    main()
