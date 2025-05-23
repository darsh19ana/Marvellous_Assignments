# accept a list of numbers and use reduce() (from functools) to find the product of all numbers
# expected input: enter list: 2 3 4
# expected output:product: 24

from functools import reduce

input_list = input("Enter list: ").split()

numbers = list(map(int, input_list))

product = reduce(lambda x, y: x*y, numbers)
print("product: ", product)
