# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = int(input("Is this temperature in Celsius or Fahrenheit? (1 or 2): "))
    if unit == 2:
        converted_temp = convert_to_celsius(temperature)
        print(temperature,"°F is",converted_temp,"°C")
    elif unit == 1:
        converted_temp = convert_to_fahrenheit(temperature)
        print(temperature,"°C is",converted_temp,"°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
