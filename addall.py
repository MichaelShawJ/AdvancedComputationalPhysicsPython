# The follwoing script is intended to take command line inputs of numbers
# and add everything together. It is an Add All function updated to P3

import sys

# Define a function to convert command-line arguments to floats and calculate their sum
def calculate_sum(arguments):
    # Convert each argument to a float and calculate the sum
    return sum(float(arg) for arg in arguments)

# Check if at least one number was provided
if len(sys.argv) > 1:
    # Calculate the sum using the function defined above
    total_sum = calculate_sum(sys.argv[1:])
    # Join the numbers into a space-separated string for printing
    numbers_str = ' '.join(sys.argv[1:])
    # Print the sum and the original numbers using f-string for formatting
    print(f'The sum of {numbers_str} is {total_sum}')
else:
    # Print an error message if no numbers were provided
    print("Please provide at least one number as an argument.")
