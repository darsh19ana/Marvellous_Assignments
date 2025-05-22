# accept age from the user and check whether the person is eligible to vote. (age should be 18 or above)
# expected input: enter age: 19
# expected output: eligible to vote

def voting(age):
    if age >= 18:
        print("eligible to vote")
    else:
        print("not eligible to vote")

age1 = 1
try:
    print("enter your age: ")
    age1 = int(input())

    def main():
        voting(age1)

    if __name__== "__main__":
        main()

except:
    print("enter a valid age")


