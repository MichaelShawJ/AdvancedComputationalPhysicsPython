'''
All four scripts calculate the Fibonacci sequence up to the Nth term, 
which is input by the user as a command-line argument.

This script includes the functionality of the original scripts 
and adds improvements such as argument parsing and
the ability to choose between integer and floating-point computation.

Here's how to use the new script:

To compute the Fibonacci sequence up to the Nth term with integers: 
    python unified_fibonacci.py N
To compute using floating-point numbers: 
    python unified_fibonacci.py N --float

'''

# Import Libraries
import argparse
import numpy as np

def compute_fibonacci(N, data_type):
    '''Compute the Fibonacci sequence up to the Nth number with the given data type.'''
    sequence = np.zeros(N + 1, dtype=data_type)
    sequence[0], sequence[1] = 1, 1
    for n in range(2, N + 1):
        sequence[n] = sequence[n - 1] + sequence[n - 2]
    return sequence

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Compute Fibonacci sequence.')
    parser.add_argument('N', type=int, help='The length of the Fibonacci sequence to compute.')
    parser.add_argument('--float', action='store_true', help='Use floating point numbers for computation.')
    args = parser.parse_args()

    # Determine the data type
    data_type = np.float64 if args.float else np.int64

    # Compute the Fibonacci sequence
    fibonacci_sequence = compute_fibonacci(args.N, data_type)

    # Print the sequence
    for n in range(args.N + 1):
        print(f'Fibonacci number {n} is {fibonacci_sequence[n]}')

if __name__ == '__main__':
    main()
