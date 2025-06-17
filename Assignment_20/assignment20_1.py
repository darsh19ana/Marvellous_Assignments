# design automation script which accepts directory name and display checksum of all files
# usage: directorychecksum.py demo
# demo is the name of the directory

import os
import sys
import hashlib

def calculatechecksum(path):
    fobj = open(path, "rb")  #rb is for read in binary mode
    hobj = hashlib.md5()

    buffer = fobj.read(1024)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)
    fobj.close()

    return hobj.hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: directorychecksum.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print("The given path is not a directory.")
        sys.exit(1)

    for foldername, subfoldername, filename in os.walk(directory):
        for fname in filename:
            filepath = os.path.join(foldername, fname)
            chksum = calculatechecksum(filepath)
            print(f"the checksum of{filepath} is {chksum}")
    print()

if __name__ == "__main__":
    main()

