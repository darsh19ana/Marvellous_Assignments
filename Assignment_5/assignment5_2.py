# accept a single character from the user and check if it is a vowel(a, e, i, o, u). if not, print it as a consonant.
# expected input: enter a character: e
# expected output: 'e' is a vowel

def ChckVowel(val):
    if val in 'AEIOUaeiou':
        print(val," is a vowel")
    else:
        print(val," is a consonant")

print("enter a character: ")
value = input()

if len(value) == 1 and value.isalpha():
    ChckVowel(value)
else:
    print("please enter a valid single character input")
