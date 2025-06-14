# write a python program to copy the contents of one line(source.txt) into another file(destination.txt)

import sys
import os

def fun():
    file1 = "source.txt"
    file2 = "destination.txt"

    fobj = open(file1, "w")
    content = fobj.write("hello world")
    fobj = open(file1, "r")
    contents = fobj.read()
    fobj2 = open(file2, "x")
    fobj2.write(contents)

    print(f"Contents of '{file1}' have been copied to '{file2}'.")

fun()