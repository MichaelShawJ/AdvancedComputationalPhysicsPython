# The follwoing script is intended to take command line inputs of numbers
# and add everything together. It is an Add All function updated to P3

import argparse

def calculate_sum(numbers):
    """
    Convert a list of strings to floats and calculate their sum.
    :param numbers: List of strings to be converted to floats.
    :return: Sum of the numbers as a float.
    """
    try:
        return sum(float(num) for num in numbers)
    except ValueError as e:
        raise ValueError(f"Error: All arguments must be numbers.") from e

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Add all provided numbers together.")
    parser.add_argument('numbers', nargs='+', help="Numbers to add", type=float)
    args = parser.parse_args()

    # Calculate the sum using the provided numbers
    total_sum = calculate_sum(args.numbers)

    # Create a string representation of the numbers
    numbers_str = ' + '.join(map(str, args.numbers))

    # Print the sum of the numbers
    print(f"The sum of {numbers_str} is {total_sum}")

if __name__ == '__main__':
    main()