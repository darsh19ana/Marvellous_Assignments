# write a program to read and display the contents of a file data.txt

def fun():
    file = "data.txt"

    fobj = open(file, "r")
    contents = fobj.read()
    print(contents)

fun()