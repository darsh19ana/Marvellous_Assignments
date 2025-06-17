# design automation script which accepts two directory names and one file extsneion. 
# copy all files with the specified extension from the first directory into the sceond diretory.
# second directory should be create at the run time
# usage: directorycopyext.py "demo" "temp" ".exe"
# demo is the name of directory which is existing and contains files in it. we have to create new directory as temp and copy all files fwith extension .exe from demo to temp

import sys
import os
import shutil

def main():
    if len(sys.argv) != 4:
        print("Usage: directoryfilesearch.py directory_name1 directory_name2 extension")
        sys.exit(1)

    directory1 = sys.argv[1]
    directory2 = sys.argv[2]
    extension = sys.argv[3]

    if not os.path.isdir(directory1):
        print("the path is not a directory")
        sys.exit(1)

    if not os.path.exists(directory2):
        os.mkdir(directory2)
        print(f"Created target directory: {directory2}")
    else:
        print(f"Target directory already exists: {directory2}")

    found = False
    for foldername, subfolders, filenames in os.walk(directory1):
        for fname in filenames:
            name, ext = os.path.splitext(fname)
            if ext.lower() == extension.lower():
                found = True
                source_pth = os.path.join(foldername, fname)
                target_pth = os.path.join(directory2, fname)
                shutil.copy(source_pth, target_pth)
                print(f"Copied: {source_pth} to {target_pth}")

if __name__ == "__main__":
    main()

