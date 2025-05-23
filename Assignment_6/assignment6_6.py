# print triangle pattern using nested loops
# expected output:
# *
# * *
# * * *
# * * * *

for i in range(1, 5):
    for j in range(i):
        print("* ", end = " ")
    print()
