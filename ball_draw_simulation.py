'''
Author: Michael Shaw

Background:
    This script simulates drawing balls from a hat containing a specified number 
    of black, red, and blue balls to calculate the probability of drawing a 
    specified number of a particular color. It compares three different methods 
    for ball selection: by index, by element with 'del', and by element with 'remove'.

Usage:
    Run the script with optional command-line arguments:
    python ball_draw_simulation.py --num_balls_drawn 5 --num_experiments 10000 
        --balls_per_color 4 --success_color black --num_successes 2
    Spyder: 
        runfile('ball_draw_simulation.py', args='--num_balls_drawn 5 --num_experiments 10000 
            --balls_per_color 4 --success_color black --num_successes 2')
'''

import random
import argparse

def new_hat(balls_per_color):
    """Create a new hat filled with the specified number of balls of each color."""
    return ['black']*balls_per_color + ['red']*balls_per_color + ['blue']*balls_per_color

def draw_ball_by_index(hat):
    """Draw a ball using list index and pop."""
    index = random.randint(0, len(hat) - 1)
    return hat.pop(index)

def draw_ball_by_element_del(hat):
    """Draw a ball using list index and delete."""
    index = random.randint(0, len(hat) - 1)
    color = hat[index]
    del hat[index]
    return color

def draw_ball_by_element_remove(hat):
    """Draw a ball using list element and remove."""
    color = random.choice(hat)
    hat.remove(color)
    return color

def run_experiments(draw_function, num_balls_drawn, num_experiments, balls_per_color, success_color, num_successes):
    """Run simulation experiments and calculate the probability."""
    successes = sum(
        1 for _ in range(num_experiments)
        if [draw_function(new_hat(balls_per_color)) for _ in range(num_balls_drawn)].count(success_color) >= num_successes
    )
    return successes / num_experiments

def main(num_balls_drawn, num_experiments, balls_per_color, success_color, num_successes):
    """Run simulations with different ball drawing methods and print results."""
    prob_by_index = run_experiments(draw_ball_by_index, num_balls_drawn, num_experiments, balls_per_color, success_color, num_successes)
    prob_by_element_del = run_experiments(draw_ball_by_element_del, num_balls_drawn, num_experiments, balls_per_color, success_color, num_successes)
    prob_by_element_remove = run_experiments(draw_ball_by_element_remove, num_balls_drawn, num_experiments, balls_per_color, success_color, num_successes)

    print(f"Probability by index: {prob_by_index:.4f}")
    print(f"Probability by element with del: {prob_by_element_del:.4f}")
    print(f"Probability by element with remove: {prob_by_element_remove:.4f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a ball drawing probability simulation.')
    parser.add_argument('--num_balls_drawn', type=int, default=5, help='Number of balls drawn per experiment.')
    parser.add_argument('--num_experiments', type=int, default=10000, help='Number of experiments to run.')
    parser.add_argument('--balls_per_color', type=int, default=4, help='Number of balls of each color in the hat.')
    parser.add_argument('--success_color', default='black', choices=['black', 'red', 'blue'], help='The ball color considered as a success.')
    parser.add_argument('--num_successes', type=int, default=2, help='Number of successful color draws required for a successful experiment.')
    
    args = parser.parse_args()
    
    main(args.num_balls_drawn, args.num_experiments, args.balls_per_color, args.success_color, args.num_successes)
