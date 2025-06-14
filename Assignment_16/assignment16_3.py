# write a python script to count the number of lines, words, and characters in a given file

def fun():
    file = "data.txt"

    try:
        with open(file, "r") as fobj:
            contents = fobj.read()

        with open(file, "r") as fobj:
            lines = fobj.readlines()
        num_lines = len(lines)

        words = contents.split()
        num_words = len(words)

        num_characters = len(contents)

        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("Number of characters:", num_characters)

    except FileNotFoundError:
        print(f"The file '{file}' does not exist.")

if __name__ == "__main__":
    fun()



        