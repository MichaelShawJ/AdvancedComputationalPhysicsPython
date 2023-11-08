"""
Author: 
    Michael Shaw

Background:
    This script calculates the Fibonacci sequence 
    up to a specified position in the sequence.

Usage: 
    Command line: python Tutorial_ACP_unified_fibonacci.py
    Spyder Console: runfile('Tutorial_ACP_unified_fibonacci.py', args='255')
"""

# Import Libraries
import argparse
import numpy as np

import time
start_time = time.time()
def compute_fibonacci(N, data_type=np.int64):
    """
    Compute the Fibonacci sequence up to the Nth number using the given data type.

    Parameters:
    - N (int): Position in the Fibonacci sequence
    - data_type (data-type, optional): The desired data-type for the array. Default is np.int64.

    Returns:
    - sequence (ndarray): Numpy array of Fibonacci sequence numbers up to the Nth number.
    """
    sequence = np.zeros(N + 1, dtype=data_type)
    sequence[1] = 1  # Fibonacci sequence starts with 1, 1, ...
    for n in range(2, N + 1):
        sequence[n] = sequence[n - 1] + sequence[n - 2]
    return sequence

def main():
    # Set up argument parser for command line options
    parser = argparse.ArgumentParser(description='Compute Fibonacci sequence.')
    parser.add_argument('N', type=int, help='The position in the Fibonacci sequence to compute up to.')
    parser.add_argument('--float', action='store_true', help='Use floating-point numbers for computation.')

    # Parse arguments
    args = parser.parse_args()

    # Determine the data type for computation
    data_type = np.float64 if args.float else np.int64

    # Compute the Fibonacci sequence
    fibonacci_sequence = compute_fibonacci(args.N, data_type)

    # Print the sequence up to the Nth number
    for n in range(args.N + 1):
        print(f'Fibonacci number {n}: {fibonacci_sequence[n]}')

# Python best practice to check if this script is the main program
if __name__ == '__main__':
    main()
    
    # ... your code ...
    elapsed_time = time.time() - start_time
    print(f"--- {elapsed_time} seconds ---")

