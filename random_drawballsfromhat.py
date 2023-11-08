'''
The Python code snippet provided is a simple simulation 
to calculate the probability of drawing at least two black balls 
from a hat containing an equal number of black, red, and blue balls. 
The three different draw_ball functions in the original code illustrate 
three different ways to randomly select an item from a list:

By Index: 
    Generates a random index and pops the element at that index from the list.
By Element with del: 
    Chooses a random index, accesses the element directly, 
    and then deletes the element at that index.
By Element with remove: 
    Chooses a random element and removes it directly.
These methods should theoretically yield the same probabilities 
since they all remove a random element from the list. 
However, implementing each method and comparing the results 
can be a good exercise to confirm this expectation.

Let's implement these three functions separately and then run the simulation 
for each to compare the probabilities. We will name them draw_ball_by_index, 
draw_ball_by_element_del, and draw_ball_by_element_remove for clarity.
The simulation was run for 10,000 experiments, drawing 5 balls in each, 
and calculate the probability of drawing at least two black balls from the hat

'''

# Import Libraries
import random

# Function to create a new hat with balls
def new_hat():
    """Create a new hat filled with 4 balls of each color."""
    colors = ('black', 'red', 'blue')  # Tuple of strings
    # List comprehension to create a hat with 4 balls of each color
    return [color for color in colors for _ in range(4)]

# Three methods for drawing a ball from the hat
def draw_ball_by_index(hat):
    """Draw a ball using list index and pop."""
    index = random.randint(0, len(hat) - 1)
    color = hat.pop(index)
    return color, hat

def draw_ball_by_element_del(hat):
    """Draw a ball using list index and delete."""
    index = random.randint(0, len(hat) - 1)
    color = hat[index]
    del hat[index]
    return color, hat

def draw_ball_by_element_remove(hat):
    """Draw a ball using list element and remove."""
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

# Function to run experiments given a draw ball function
def run_experiments(draw_function, num_balls_drawn, num_experiments):
    successes = 0  # Count of successes
    for _ in range(num_experiments):
        hat = new_hat()
        balls_drawn = [draw_function(hat)[0] for _ in range(num_balls_drawn)]
        if balls_drawn.count('black') >= 2:  # At least two black balls?
            successes += 1
    probability = float(successes) / num_experiments
    return probability

# Predefined values for demonstration
num_balls_drawn = 5
num_experiments = 10000

# Run experiments for each drawing method and calculate probabilities
prob_by_index = run_experiments(draw_ball_by_index, num_balls_drawn, num_experiments)
prob_by_element_del = run_experiments(draw_ball_by_element_del, num_balls_drawn, num_experiments)
prob_by_element_remove = run_experiments(draw_ball_by_element_remove, num_balls_drawn, num_experiments)

print (prob_by_index, prob_by_element_del, prob_by_element_remove)
