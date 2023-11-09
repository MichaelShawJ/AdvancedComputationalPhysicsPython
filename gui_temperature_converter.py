'''
Author:
    Michael Shaw
    
Background:
    This module provides a GUI to convert temperatures between Celsius and Fahrenheit.
    It checks that the input temperature is above absolute zero when provided in Celsius.

Usage:
    Can be run as a script or imported in other modules 
    to use the conversion functionality.
command line: python gui_temperature_converter.py --temp 20 --unit C
Spyder: runfile('gui_temperature_converter.py', args='--temp 20 --unit C')

'''

import tkinter as tk
from tkinter import messagebox
import argparse

# Constants for temperature limits
ABSOLUTE_ZERO_C = -273.15

def convert_temperature(temp_entry, temp_unit_var, result_label):
    """Convert between Celsius and Fahrenheit and update the result label."""
    try:
        temp = float(temp_entry.get())
        if temp_unit_var.get() == 'C':
            if temp < ABSOLUTE_ZERO_C:
                raise ValueError("Celsius temperature cannot be below absolute zero")
            result = (9.0 / 5) * temp + 32
            result_label.config(text=f"{result:.1f} Fahrenheit")
        elif temp_unit_var.get() == 'F':
            result = (temp - 32) * (5 / 9.0)
            if result < ABSOLUTE_ZERO_C:
                raise ValueError("Resulting Celsius temperature cannot be below absolute zero")
            result_label.config(text=f"{result:.1f} Celsius")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        result_label.config(text="Error")

def setup_gui(root, default_temp, default_unit):
    """Set up the GUI components and initialize with default values."""
    # Create an entry field for the temperature
    temp_entry = tk.Entry(root, width=4)
    temp_entry.insert(0, str(default_temp))
    temp_entry.pack(side='left')

    # Create a variable to hold the temperature unit
    temp_unit_var = tk.StringVar(value=default_unit)

    # Create the radio buttons for unit selection
    celsius_button = tk.Radiobutton(root, text='Celsius', variable=temp_unit_var, value='C')
    fahrenheit_button = tk.Radiobutton(root, text='Fahrenheit', variable=temp_unit_var, value='F')
    celsius_button.pack(side='left')
    fahrenheit_button.pack(side='left')

    # Create the label to display the result
    result_label = tk.Label(root, width=20, text="Enter value and select unit")
    result_label.pack(side='left')

    # Create a lambda function to pass arguments to the convert_temperature function
    convert_command = lambda: convert_temperature(temp_entry, temp_unit_var, result_label)

    # Create the convert button
    convert_button = tk.Button(root, text='Convert', command=convert_command)
    convert_button.pack(side='left', padx=4)

def main(default_temp=0.0, default_unit='C'):
    """Main function to run the GUI application."""
    root = tk.Tk()
    root.title("Temperature Converter")
    
    # Set up the GUI components
    setup_gui(root, default_temp, default_unit)
    
    # Start the main loop
    root.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Temperature Converter GUI.')
    parser.add_argument('--temp', type=float, default=0.0, help='Initial temperature value.')
    parser.add_argument('--unit', choices=['C', 'F'], default='C', help='Initial temperature unit (Celsius or Fahrenheit).')
    args = parser.parse_args()

    # Pass command-line arguments to the main function
    main(default_temp=args.temp, default_unit=args.unit)
