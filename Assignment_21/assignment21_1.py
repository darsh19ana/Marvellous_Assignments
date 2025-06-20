# design automation script which display information of running processes as its name, PID and username
# usage: procInfo.py

import psutil

def displayinfo():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        print(info)
    print()

displayinfo()