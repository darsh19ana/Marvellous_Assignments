# write a program that schedules a function to print "do coding" every 30 minutes

import schedule
import time

def toprint():
    print("do coding")

def main():
    schedule.every(1).minutes.do(toprint)

    print("application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

main()