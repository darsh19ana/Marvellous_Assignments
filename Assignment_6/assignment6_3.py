# accept a number from the user and print its multiplication table up to 10
# expected input: enyer a number: 7
# expected output: 
# 7 * 1 = 7
# 7 * 2 = 14
# ..
# 7 * 10 = 70

print("enter a number: ")
num = int(input())

for i in range(1, 11):
    mult = num*i
    print(num, "*", i, ": ", mult)