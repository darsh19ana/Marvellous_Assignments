# write a program to read a file line by line and display only those lines that contain more than 5 words

def fun():
    file = "data.txt"

    try:
        with open(file, "r") as fobj:
            for line in fobj:
                word_count = len(line.strip().split())
                if word_count > 5:
                    print(line.strip())

    except FileNotFoundError:
        print(f"The file '{file}' does not exist.")

fun()
