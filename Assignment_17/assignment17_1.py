# write a python script that prints "jay ganesh" every 2 seconds. use the schedule.every(2).seconds.do(..) function
import schedule
import time

def toprint():
    print("jay ganesh")

def fun():
    schedule.every(2).seconds.do(toprint)

    print("application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

fun()


