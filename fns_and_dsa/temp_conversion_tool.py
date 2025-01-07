# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # User input for temperature
        user_input = input("Enter the temperature to convert: ")
        
        # Validate if the input is a number
        temperature = float(user_input)
        
        # Ask for the unit of temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on the unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(temperature,"°F is",converted_temp,"°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(temperature,"°C is",converted_temp,"°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}. Invalid temperature. Please enter a numeric value.")

# Run the script
if __name__ == "__main__":
    main()

