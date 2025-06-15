# schedule a function that performs file backup every hour and writes a log entry into backup_log.txt

import schedule
import time
import shutil
import datetime
import os

sourcefile = "marvellous.txt"
backup_dir = "D:\\Marvellous_Assignments\\Assignment_17\\backups"
logfile = "backup_log.txt"

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

def backup_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(backup_dir, f"backup_{timestamp}.txt")
    
    try:
        shutil.copy(sourcefile, backup_filename)
        
        with open(logfile, "a") as log:
            log.write(f"Backup created at {timestamp}: {backup_filename}\n")
        
        print(f"Backup successful at {timestamp}")
    except FileNotFoundError:
        print(f"Source file '{sourcefile}' not found.")

def main():
    schedule.every().hour.do(backup_file) 

    print("Backup scheduler running... Press Ctrl+C to stop.")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
