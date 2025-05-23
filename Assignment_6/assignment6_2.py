# print sum of even numbers between 1 and 100. use a loop to find and print the sum of all even numbers from 1 to 100
# expected output: 
#  sum of even numbers between 1 to 100 is: 2550

total = 0

for i in range(2, 101, 2):
    total += i

print("sum of even numbers between to 100 is: ", total)



