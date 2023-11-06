# Import necessary functions and constants from the math module
from math import sinh, exp, e, pi

# Set x to 2 times pi
x = 2*pi

# Calculate the hyperbolic sine of x using the built-in sinh function
r1 = sinh(x)

# Calculate the hyperbolic sine of x using the formula with exp function
r2 = 0.5*(exp(x) - exp(-x))

# Calculate the hyperbolic sine of x using the formula with the e constant
r3 = 0.5*(e**x - e**(-x))

# Print the results from the three methods
print (r1, r2, r3)

# Print the complete representation of the results using repr function
print (repr(r1), repr(r2), repr(r3))

# Print the results with a specific number of decimal places (16 in this case)
print ('%.16f %.16f %.16f' % (r1,r2,r3))

# Calculate the differences between the results of the methods
diff1 = r1 - r2
diff2 = r2 - r3

# Print the calculated differences
print (diff1, diff2)
