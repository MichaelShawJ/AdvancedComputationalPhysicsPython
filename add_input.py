# Prompt user to enter two numbers
# check if it can convert to a number format
# Print out the numbers and resulting sum

def convert_to_number(input_string):
    """Attempt to convert a string to an integer, float, or complex number."""
    try:
        # First, try to convert to an integer
        return int(input_string)
    except ValueError:
        try:
            # Next, try to convert to a float
            return float(input_string)
        except ValueError:
            try:
                # Finally, try to convert to a complex number
                return complex(input_string)
            except ValueError:
                # If all conversions fail, raise an error
                raise ValueError("Input is not a number")

# Ask for input and convert it using the function defined above
try:
    i1 = convert_to_number(input('Give input: '))
    i2 = convert_to_number(input('Give input: '))
except ValueError as e:
    print(e)
    exit(1)

# Calculate the result
r = i1 + i2

# Print the result with the types of the inputs and the result
print(f'{type(i1)} + {type(i2)} becomes {type(r)}\nwith value {r}')

