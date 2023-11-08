"""
Author: 
    Michael Shaw

Background:
   The code calculates the hyperbolic sine (sinh) of a value (2π) using three different methods:
   1) Using the built-in 'sinh' function from the 'math' module.
   2) Using the formula sinh(x) = 1/2(exp(x) − exp(−x))
   3) Using the formula with the base of the natural logarithm, e: sinh(x) = 1/2(e^x − e^−x)
   The code then prints the results of these three methods in different formats 
   and finally calculates the differences between the results.

Usage: 
    Command line: python sinh_calculation.py
"""

import math

def calculate_sinh_methods(value):
    """
    Calculate the hyperbolic sine of a value using three different methods.
    
    Args:
        value (float): The input value for which to calculate the hyperbolic sine.
    
    Returns:
        tuple: A tuple containing the results of the hyperbolic sine calculations using
               the built-in function, the exp formula, and the e constant formula.
    """
    # Using the built-in sinh function
    result_builtin = math.sinh(value)
    
    # Using the formula with exp function
    result_exp_formula = 0.5 * (math.exp(value) - math.exp(-value))
    
    # Using the formula with the e constant
    result_e_formula = 0.5 * (math.e ** value - math.e ** (-value))
    
    return result_builtin, result_exp_formula, result_e_formula

def main():
    # Set the value to 2 times pi
    value = 2 * math.pi
    
    # Calculate the hyperbolic sine of the value using three methods
    sinh_builtin, sinh_exp, sinh_e = calculate_sinh_methods(value)
    
    # Print the results from the three methods
    print(sinh_builtin, sinh_exp, sinh_e)
    
    # Print the complete representation of the results using repr function
    print(repr(sinh_builtin), repr(sinh_exp), repr(sinh_e))
    
    # Print the results with a specific number of decimal places (16 in this case)
    print(f'{sinh_builtin:.16f} {sinh_exp:.16f} {sinh_e:.16f}')
    
    # Calculate the differences between the results of the methods
    diff_builtin_exp = sinh_builtin - sinh_exp
    diff_exp_e = sinh_exp - sinh_e
    
    # Print the calculated differences
    print(diff_builtin_exp, diff_exp_e)

# Check if the script is executed directly (i.e., not imported as a module)
if __name__ == '__main__':
    main()
