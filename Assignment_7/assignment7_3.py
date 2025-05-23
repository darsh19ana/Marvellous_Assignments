# accept a list of integers and use filter() to keep only even numbers.
# expected input: enter list: 1 2 3 4 5 6
# expected output: even numbers: [2, 4, 6]

input_list = input("Enter list: ").split()

numbers = list(map(int, input_list))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even numbers:", even_numbers)