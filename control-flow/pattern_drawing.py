# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="")  # Print without advancing to a new line
    print()  # Print a newline after completing the row
    row += 1

