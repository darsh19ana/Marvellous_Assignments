# accept file name and one string from the user and return the frequency of that string from file. 
# input: demo.txt        Marvellous
# search "marvellous" in demo.txt

import sys
import os

def fun(file, string):
    file = sys.argv[1]
    string = sys.argv[2]

    flag = os.path.exists(file)
    if(flag==False):
        print("the path doesn't exist")
        exit()
    else:
        fobj1 = open(file, "r")
        contents = fobj1.read()
        frequency = contents.lower().count(string.lower())
        print(f"The word '{string}' occurs {frequency} time(s) in '{file}'.")

def main():
    fun()
    if (len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this application is used to check frequency of a string in a file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("use the given script as ")
            print("scriptname.py nameoffile nameofstring")

        else:
            fun(sys.argv[1])
    else:   
            print("invalid number of command line arguments")
            print("use the given flags as: ")
            print("--h : used to display help")
            print("--u: used to display usage")

if __name__ == "__main__":
    main()           