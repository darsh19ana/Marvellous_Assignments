# design automation script which accept directory name from user and create log file in that directory which contains information of running processes as its name, PID, username
# usage: procinfolog.py demo

import psutil
import sys
import os

def createlog(foldername):

    if not os.path.exists(foldername):
        print("the path does not exist")

def displayinfo(foldername):
    foldername = sys.argv[1]

    createlog(foldername)

    filename = "log.txt"
    fobj = open(filename, "w")

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs = ['pid', 'name', 'username'])
            fobj.write(str(info))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def main():
    displayinfo(sys.argv[1])

if __name__ == "__main__":
    main()


