# design automation script which accept directory name and write names of duplicate files from that directory into log file named as log.txt. 
# log.txt should be created into cureent directory
# usage: directoryduplicate.py demo
# demo is the name of directory

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

def directorywatcher(directoryname = "Marvellous"):
    flag = os.path.isabs(directoryname)

    if(flag == False):
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)
    if(flag==False):
        print("the path is invalid")
        exit()

    flag = os.path.isdir(directoryname)
    if flag == False:
        print("the path is valid but the traget is not a directory")
        exit()

    for foldername, subfoldername, filenames in os.walk(directoryname):
        for fname in filenames:
            fname = os.path.join(foldername, fname)
            checksum = calculatechecksum(fname)
            print("filename: ", fname)
            print("checksum: ", checksum)
            print()

def findduplicate(directoryname):
    flag = os.path.isabs(directoryname)

    if(flag == False):
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)
    if(flag==False):
        print("the path is invalid")
        exit()

    flag = os.path.isdir(directoryname)
    if flag == False:
        print("the path is valid but the traget is not a directory")
        exit()

    duplicate = {}

    for foldername, subfoldername, filenames in os.walk(directoryname):
        for fname in filenames:
            fname = os.path.join(foldername, fname)
            checksum = calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum] = [fname]

    return duplicate

def main():        
    result = findduplicate(sys.argv[1])
    filename = "log.txt"
    fobj = open(filename, "w")
    fobj.write(str(result))

if __name__ == "__main__":
    main()