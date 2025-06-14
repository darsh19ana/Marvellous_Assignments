# write a program which accepts two file names from the user and compare contents of both the files. 
# if both files contains the same contents then display success otherwise display failure.
# accept names of both the files from command line
# input: demo.txt  hello.txt
# comapre contents of demo.txt and hello.txt

import sys
import os

def fun(file1):
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    flag = os.path.exists(file1)
    if(flag==False):
        print("the path doesn't exist")
        exit()

    else:
        fobj1 = open(file1, "r")
        contents = fobj1.read()
        fobj2 = open(file2, "r")
        contents2 = fobj2.read()

        if contents == contents2:
            print("success")
        else:
            print("failure")

def main():
    if (len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this application is used for copying file content of file 1 to another file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("use the given script as ")
            print("scriptname.py nameoffile1 nameoffile2")

        else:
            fun(sys.argv[1])
    else:   
            print("invalid number of command line arguments")
            print("use the given flags as: ")
            print("--h : used to display help")
            print("--u: used to display usage")

if __name__ == "__main__":
    main()