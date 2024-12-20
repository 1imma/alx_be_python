number = int(input("Enter a number to see its multiplication table: "))

for multiplier in range(1, 11):  # Iterate from 1 to 10
    product = number * multiplier
    print(str(number) + " * " + str(multiplier) + " = " + str(product))
