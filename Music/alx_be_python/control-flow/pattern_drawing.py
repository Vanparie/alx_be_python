# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Check if the user entered a valid positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row of the pattern
    row = 0
    while row < size:
        # Use a for loop to print asterisks (*) in each row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after completing the current row
        print()
        row += 1
