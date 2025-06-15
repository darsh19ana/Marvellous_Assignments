# create a task that runs once every day at 9.00 am and prints "namaskar"

import schedule
import time

def toprint():
    print("namaskar")

schedule.every().day.at("09:00").do(toprint)

while True:
    schedule.run_pending()
    time.sleep(1)  
