"""
Author: 
    Michael Shaw

Background:
   The goal of this program is to be able to add two values from the command line.
   The program is named add_commandline. It expects two inputs and prints their sum.

Usage: 
    Command line: python add_commandline.py <input1> <input2>
"""

import sys
import ast

def add_command_line_args(arg1, arg2):
    """
    Adds two values passed as command line arguments.
    
    Args:
        arg1 (str): The string representation of the first argument.
        arg2 (str): The string representation of the second argument.
    
    Returns:
        str: A formatted string reporting the types and the result of the addition.
    """
    try:
        # Safely evaluate the command-line arguments as Python literals
        value1 = ast.literal_eval(arg1)
        value2 = ast.literal_eval(arg2)
        
        # Add the two inputs together
        result = value1 + value2
        
        # Return the formatted output string
        return f"{type(value1)} + {type(value2)} results in {type(result)} with value {result}"
        
    except (ValueError, SyntaxError) as e:
        # Return an error message if evaluation fails
        return f"Error: {e}"

def main():
    # Check if exactly two additional arguments have been provided
    if len(sys.argv) != 3:
        print("Usage: python add_cml.py <input1> <input2>")
        sys.exit(1)  # Exit with a non-zero exit code to indicate an error

    # Retrieve the arguments
    arg1, arg2 = sys.argv[1], sys.argv[2]

    # Perform the addition and get the result or an error message
    output = add_command_line_args(arg1, arg2)

    # Print the result or an error message
    print(output)

if __name__ == '__main__':
    main()