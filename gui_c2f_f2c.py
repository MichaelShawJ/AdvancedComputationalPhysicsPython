'''
The GUI will allow the user to input a temperature and select whether
it's in Celsius or Fahrenheit. The program will then convert it to the other 
temperature scale and display the result. It will also include checks to 
ensure that the temperature is above absolute zero when provided in Celsius.
'''

# Import Libraries
import tkinter as tk
from tkinter import messagebox

# Constants for temperature limits
ABSOLUTE_ZERO_C = -273.15

def convert_temperature():
    """Convert between Celsius and Fahrenheit."""
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

# Set up the root window
root = tk.Tk()
root.title("Temperature Converter")

# Create an entry field for the temperature
temp_entry = tk.Entry(root, width=4)
temp_entry.pack(side='left')

# Create a variable to hold the temperature unit
temp_unit_var = tk.StringVar(value='C')

# Create the radio buttons for unit selection
celsius_button = tk.Radiobutton(root, text='Celsius', variable=temp_unit_var, value='C')
fahrenheit_button = tk.Radiobutton(root, text='Fahrenheit', variable=temp_unit_var, value='F')
celsius_button.pack(side='left')
fahrenheit_button.pack(side='left')

# Create the convert button
convert_button = tk.Button(root, text='Convert', command=convert_temperature)
convert_button.pack(side='left', padx=4)

# Create the label to display the result
result_label = tk.Label(root, width=20, text="Enter value and select unit")
result_label.pack(side='left')

# Start the main loop
root.mainloop()

