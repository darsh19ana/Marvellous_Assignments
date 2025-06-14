# write a python program to craete a text file named student.txt and write the names of 5 students into it

def fun():
    file = "student.txt"

    fobj = open(file, "w")
    fobj.write("darshana,\n sunidhi,\n abhishek,\n abhijeet,\n mudra")

fun()
