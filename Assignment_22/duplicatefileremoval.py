import time
import sys
import os
from datetime import datetime
import userdefinedmodules

def main():
    if len(sys.argv) != 4:
        print('''Usage: python DuplicateFileRemoval.py <DirectoryPath> <DelayInMinutes> <ReceiverEmail>

Example:
    python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

This script scans a directory for duplicate files, deletes them, logs the details, and sends an email report.
''')
        return

    directory = sys.argv[1]
    try:
        delay = int(sys.argv[2])
    except ValueError:
        print("Please provide delay time in minutes as a number.")
        return

    email = sys.argv[3]

    print(f"[INFO] Script will run in {delay} minutes...")
    time.sleep(delay * 60)

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    duplicates, total_scanned = userdefinedmodules.findduplicate(directory)
    deleted_files = userdefinedmodules.delete_duplicates(duplicates)
    log_file_path = userdefinedmodules.create_log(deleted_files)

    userdefinedmodules.send_mail(email, log_file_path, start_time, total_scanned, len(deleted_files))
    print(f"Duplicate removal complete. Log file emailed to {email}.")

if __name__ == "__main__":
    main()
