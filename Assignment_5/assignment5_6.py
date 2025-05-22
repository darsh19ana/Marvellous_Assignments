# accept temperature in celcius and convert it to fahrenheit using the formula 
# F = (C * 9/5) + 32
# expected input: enter temperature in celcius: 25
# expected output: temperature in fahrenheit: 77.0 F

print("enter the temperature(in celsius): ")
temp = int(input())

def tempconverter(temperature):
    tempinf = (temperature * 9/5) + 32
    return tempinf

def main():
    fah = tempconverter(temp)
    print("temperature in fahrenheit: ", fah)

if __name__ == "__main__":
    main()
