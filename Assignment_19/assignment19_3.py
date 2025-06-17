# design automation script which accept two directory names. 
# copy all files from first directory into second directory.
# second diretory should be created at run time
# usage: directorycopy.py "demo" "temp"
# demo is the name of directory which is existing and contains files in it. 
# we have to create new directory as temp and copy all files from demo to temp

import sys
import os
import shutil

def main():
    if len(sys.argv) != 3:
        print("Usage: directoryfilesearch.py directory_name1 directory_name2")
        sys.exit(1)

    directory1 = sys.argv[1]
    directory2 = sys.argv[2]

    if not os.path.isdir(directory1):
        print("the path is not a directory")
        sys.exit(1)

    if not os.path.exists(directory2):
        os.mkdir(directory2)
        print(f"Created target directory: {directory2}")
    else:
        print(f"Target directory already exists: {directory2}")

    for foldername, subfoldername, filename in os.walk(directory1):
        for fname in filename:
            print(fname)
            source_pth = os.path.join(foldername, fname)
            target_pth = os.path.join(directory2, fname)
            shutil.copy(source_pth, target_pth)
            print(f"Copied: {source_pth} to {target_pth}")

if __name__ == "__main__":
    main()
    


