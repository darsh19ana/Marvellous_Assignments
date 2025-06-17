# design automation script which accept directory name and two file extensions from the user. 
# rename all files with first file extension with the second file extension
# usage: directoryrename.py "demo" ".txt" ".doc"

import sys
import os

def showdir():
    if len(sys.argv) != 4:
        print("Usage: directoryfilesearch.py directory_name file_extension1 file_extension2")
        sys.exit(1)

    directory = sys.argv[1]
    extension1 = sys.argv[2]
    extension2 = sys.argv[3]

    if not os.path.isdir(directory):
        print("The path is not a directory.")
        sys.exit(1)

    print(f"\nFiles with extension '{extension1}' in '{directory}':")
    found = False
    for foldername, subfoldername, filenames in os.walk(directory):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext == extension1:
                found = True
                print(filename)
                old_file = os.path.join(foldername, filename)
                new_filename = name + extension2
                new_file = os.path.join(foldername, new_filename)

                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} -> {new_file}")

    if not found:
        print("No files with the given extension were found.")

if __name__ == "__main__":
    showdir()

