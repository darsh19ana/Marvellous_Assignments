# write a script to remove all blank lines from a file. save the cleaned output to a new file.

def fun(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if line.strip(): 
                    outfile.write(line)
        print(f"Blank lines removed. Cleaned data saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

fun("data.txt", "cleaned_data.txt")
