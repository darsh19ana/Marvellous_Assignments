# create a file marks.txt with student name and marks. 
# then read the file and display students who scored more than 75 marks

def fun():
    file = "marks.txt"

    with open(file, "w") as fobj:
        fobj.write("student name: darshana\nmarks: 98\n\n")
        fobj.write("student name: sunidhi\nmarks: 75\n\n")
        fobj.write("student name: digvijay\nmarks: 82\n\n")
        fobj.write("student name: rohit\nmarks: 64\n")

    with open(file, "r") as fobj:
        lines = fobj.readlines()
        
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("student name:"):
            name = line.split(":")[1].strip()
            marks_line = lines[i + 1].strip()
            if marks_line.startswith("marks:"):
                marks = int(marks_line.split(":")[1].strip())
                if marks > 75:
                    print(f"{name} scored {marks}")
            i += 2
        else:
            i += 1

fun()

