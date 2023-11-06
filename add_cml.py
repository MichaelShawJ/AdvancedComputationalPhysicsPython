# The goal of this program is to be able to add two values form the command line
# As named, Add_CommandLine. Usage: python add_cml.py <input1> <input2>

# Import the sys module to access command-line arguments
import sys
# Import the ast module to safely evaluate string literals
import ast

# Check if exactly two additional arguments have been provided (excluding the script name)
if len(sys.argv) != 3:
    # If not, print usage information
    print("Usage: python add_cml.py <input1> <input2>")
    # Exit the script with a non-zero exit code to indicate an error
    sys.exit(1)

# Try to safely evaluate the command-line arguments as Python literals
try:
    # Safely evaluate the first command-line argument after the script name
    i1 = ast.literal_eval(sys.argv[1])
    # Safely evaluate the second command-line argument
    i2 = ast.literal_eval(sys.argv[2])
except ValueError as e:
    # If evaluation fails, print an error message and exit with an error code
    print(f"Error: {e}")
    sys.exit(1)

# Add the two inputs together and store the result in 'r'
r = i1 + i2

# Construct the output string using f-string formatting for better readability
# F-strings are a more modern and concise way to format strings in Python 3.6+
output = (f"{type(i1)} + {type(i2)} becomes {type(r)}\nwith value {r}")

# Print the output string to the console
print(output)