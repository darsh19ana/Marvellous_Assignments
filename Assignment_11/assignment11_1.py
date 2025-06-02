# write a recursive function to print numbers from 1 to N.

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(6)
