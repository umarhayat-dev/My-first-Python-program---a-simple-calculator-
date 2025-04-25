import tkinter as tk

# Create the window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# First number input
label1 = tk.Label(root, text="Enter the first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# Second number input
label2 = tk.Label(root, text="Enter the second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Function to do the calculation
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            result = "Unknown operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Buttons
tk.Button(root, text="+", command=lambda: calculate('+')).pack()
tk.Button(root, text="-", command=lambda: calculate('-')).pack()
tk.Button(root, text="*", command=lambda: calculate('*')).pack()
tk.Button(root, text="/", command=lambda: calculate('/')).pack()

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Start the GUI loop
root.mainloop()
