def safe_divide(numerator, denominator):
    
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        division = num1 / num2
        print("The result of the division is",division)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
