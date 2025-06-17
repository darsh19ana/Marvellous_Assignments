# write a program which accepts file name from the userand create new file named as demo.txt and copy all contents from existing file into new file. 
# accept file name through command line arguments.
# input: abc.txt
# create a new file as demo.txt and copy the contents of abc.txt in demo.txt

import sys
import os

def fun(file1):
    file1 = sys.argv[1]
    file2 = "demo.txt"

    flag = os.path.exists(file1)
    if(flag==False):
        print("the path doesn't exist")
        exit()

    else:
        fobj1 = open(file1, "r")
        contents = fobj1.read()
        fobj2 = open(file2, "x")
        fobj2.write(contents)

        print(f"Contents of '{file1}' have been copied to '{file2}'.")

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