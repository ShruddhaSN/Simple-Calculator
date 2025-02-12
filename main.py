import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(entry.get())

        # Convert result to string and limit length
        if isinstance(result, float):
            result = f"{result:.14g}"  # Rounds to max 14 significant digits
        else:
            result = str(result)[:14]  # Trim integers if they exceed 14 characters

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to append characters to the input field
def append_to_expression(char):
    entry.insert(tk.END, char)

# Function to clear the input field
def clear_entry(event=None):
    entry.delete(0, tk.END)

# Function for backspace (removes last character)
def backspace(event=None):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.configure(bg="#2C2B2C")
root.resizable(True, True)

# Configure grid to make buttons expand
for i in range(6):  
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  
    root.grid_columnconfigure(j, weight=1)

# Entry field with styling
entry = tk.Entry(root, font=("Arial", 30), bd=10, relief=tk.FLAT, bg="#1C1C1C", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="nsew")

# Button configurations
button_config = {
    'font': ("Arial", 20),
    'height': 2,
    'bd': 0,
    'fg': 'white',
    'bg': '#4E4E4E',
    'activebackground': '#666666',
    'highlightthickness': 0
}

# Special button colors
special_button_config = {
    '=': {'bg': '#507d2a', 'activebackground': '#00E676'},
    'C': {'bg': '#8B0000', 'activebackground': '#FF1744'},
    '←': {'bg': '#CC5500', 'activebackground': '#FF8F00'},
    '/': {'bg': '#2E5A88'},
    '*': {'bg': '#2E5A88'},
    '-': {'bg': '#2E5A88'},
    '+': {'bg': '#2E5A88'}
}

# Button layout including Backspace
buttons = [
    ('C', 1, 0), ('', 1, 1), ('', 1, 2), ('←', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('-', 5, 3)
] 

# Add buttons to the window
for btn in buttons:
    text, row, col = btn[0], btn[1], btn[2]

    if text == '':
        continue

    config = button_config.copy()
    if text in special_button_config:
        config.update(special_button_config[text])

    if text == '=':
        action = evaluate_expression
    elif text == 'C':
        action = clear_entry
    elif text == '←':
        action = backspace
    else:
        action = lambda t=text: append_to_expression(t)

    button = tk.Button(root, text=text, command=action, **config)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Keyboard Bindings
root.bind('<Return>', evaluate_expression)  # Enter key for "="
root.bind('<BackSpace>', backspace)  # Backspace key
root.bind('<Escape>', clear_entry)  # Esc key for "C"

# Bind number keys and operators
for key in '0123456789+-*/().':
    root.bind(key, lambda event, char=key: append_to_expression(char))

# Run the calculator
root.mainloop()
