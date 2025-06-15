# write a script that schedules multiple tasks : one to print "lunch time" at 1 pm, and another to print "wrap up work" at 6 pm

import schedule
import time

def lunch_time():
    print("Lunch time")

def wrap_up_work():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch_time)
    schedule.every().day.at("18:00").do(wrap_up_work)

    print("Scheduler is running... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
