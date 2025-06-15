# schedule a job that runs every 5 minutes to write the current time to a file marvellous.txt

import schedule
import datetime
import time

def toprint():
    file = "marvellous.txt"

    fobj = open(file, "a")
    content = fobj.write(str(datetime.datetime.now())+"\n")

def main():
    schedule.every(5).minutes.do(toprint)

    print("application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
