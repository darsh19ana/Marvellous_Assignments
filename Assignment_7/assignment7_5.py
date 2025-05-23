# write a function that accepts a string and checks whether it is a palindrome
# expected input: enter a string: radar
# expected output: radar is a palindrome

print("enter a string: ")
pal = input()

def checkpal(val):
    if val == val[::-1]:
        print(val, " is a palindrome")
    else:
        print(val, " is not a palindrome")

checkpal(pal)
