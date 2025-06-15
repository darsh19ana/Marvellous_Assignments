# schedule a task that displays the current date and time every minute using datetime module

import schedule
import datetime
import time

def toprint():
    print("current time is: ",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(toprint)

    print("application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

main()