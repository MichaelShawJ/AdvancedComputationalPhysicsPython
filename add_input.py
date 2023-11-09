'''
Author: Michael Shaw

Background: To test the updated Python script that prompts the user 
for two numbers, adds them together, and then prints out the numbers 
and resulting sum, you can simply run the script from the command line. 
Since the script is interactive and expects user input, 
you won't be able to pass the numbers directly as command-line arguments. 
Instead, you'll run the script, and it will prompt you to enter the numbers 
one by one.

Usage: python add_input.py
Followed by answering prompts for two numbers

Test Cases:
TRunning the script, you should expect the following in your terminal:
Enter first number: 5
Enter second number: 10
int + int results in a int with value 15
If you enter one integer and one float, like 5 and 10.5, the output would be:
    int + float results in a float with value 15.5
If you enter complex numbers like 5+2j and 3-4j, the output would look like:
    complex + complex results in a complex with value (8-2j)

Enter first number: a -> Input 'a' is not a number.
'''

def convert_to_number(input_string):
    """
    Attempt to convert a string to a numerical type.
    
    Tries to convert to an integer, then a float, then a complex number.
    If all conversions fail, it raises a ValueError.

    :param input_string: The string to convert.
    :return: The converted number as an int, float, or complex.
    """
    for conversion in (int, float, complex):
        try:
            return conversion(input_string)
        except ValueError:
            continue
    raise ValueError(f"Input '{input_string}' is not a number.")

def main():
    # Gather user inputs and attempt to convert them to numbers
    try:
        i1 = convert_to_number(input('Enter first number: '))
        i2 = convert_to_number(input('Enter second number: '))
    except ValueError as e:
        print(e)
        exit(1)

    # Calculate the sum of the two numbers
    result = i1 + i2

    # Print the result with the types of the inputs and the result
    print(f'{type(i1).__name__} + {type(i2).__name__} results in a {type(result).__name__} with value {result}')

if __name__ == "__main__":
    main()


