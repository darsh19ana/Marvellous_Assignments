# write a program which accepts number from user and print that number of "*" on screen

print("Enter a number: ")
stars = int(input())

for i in range(stars):
    print("* ", end = "")