# design automation script which accepts directory name and file extension from user. 
# display all files with that extenson.
# usage: directoryfilesearch.py "demo" ".txt"

import sys
import os

def showdir():
    if len(sys.argv) != 3:
        print("Usage: directoryfilesearch.py directory_name file_extension")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.isabs(directory):
        directory = os.path.abspath(directory)

    if not os.path.exists(directory):
        print("The path doesn't exist.")
        sys.exit(1)
    else:
        print("The path exists.")

    if not os.path.isdir(directory):
        print("The path is not a directory.")
        sys.exit(1)

    print(f"\nFiles with extension '{extension}' in '{directory}':")
    found = False
    for foldername, subfoldername, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                print(filename)
                found = True

    if not found:
        print("No files with the given extension were found.")

if __name__ == "__main__":
    showdir()





