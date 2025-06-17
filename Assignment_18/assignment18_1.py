# write a program which accepts file name from the user and check whether that file exists in current directory or not
# input: demo.txt
# check whether demo.txt exists or not

import os

def directorywatcher(directoryname):
    flag = os.path.isabs(directoryname)

    if(flag == False):
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)
    if(flag==False):
        print("the path doesn't exist")
        exit()

    else:
        print("the path exists")

def main():
    print("enter the file you want to check: ")
    dirname = input()
    result = directorywatcher(dirname)

if __name__ == "__main__":
    main()