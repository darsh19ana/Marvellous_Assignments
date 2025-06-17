# write a program which accepts file name from user and open that file and display the contents of that file on the screen

import os

def main():
    print("enter the name of file that you want to read: ")
    fname = input()

    ret = os.path.exists(fname)

    if ret == True:
        print("file is present in the current directory")
        fobj = open(fname, "r")
        data = fobj.read()
        print("data from file is: ", data)
        fobj.close()
    else:
        print("there is no such file")

if __name__ == "__main__":
    main()