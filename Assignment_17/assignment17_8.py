# write a script that simulates checking for email updates every 10 seconds. (use print statement like "checking mail...") instead of real email logic

import schedule
import time

def check_mail():
    print("Checking mail...")

def main():
    schedule.every(10).seconds.do(check_mail)

    print("Mail checker started... Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
