def safe_divide(numerator, denominator):
    
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        division = num1 / num2
        return("The result of the division is " + str(division))
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
    except ValueError:
        return("Error: Please enter numeric values only.")
