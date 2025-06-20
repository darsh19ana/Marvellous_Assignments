# design automation script which accept process name and display information of that process if its running
# usage: procinfo.py notepad

import psutil
import sys

def displayinfo(name):
    name = sys.argv[1]
    found = False
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            if info['name'].lower() == name.lower():
                print(f"PID: {info['pid']}, Name: {info['name']}, User: {info['username']}")
                found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    if not found:
        print(f"No running process found with the name: {name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python procinfo.py <process_name>")
        return

    name = sys.argv[1]
    displayinfo(name)

if __name__ == "__main__":
    main()