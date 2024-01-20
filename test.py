import tkinter as tk
from tkinter import messagebox

def calculate_gradient():
    try:
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        y1 = float(entry_y1.get())
        y2 = float(entry_y2.get())

        difference_resulty = y2 - y1
        difference_resultx = x2 - x1

        if difference_resultx == 0:
            messagebox.showerror("Error", "Division by zero. The gradient is undefined.")
        else:
            quotient_result = difference_resulty / difference_resultx
            rounded_result = round(quotient_result, 2)
            result_label.config(text=f"Gradient: {rounded_result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
window = tk.Tk()
window.title("Slope Calculator")

# Create and place widgets in the window
label_x1 = tk.Label(window, text="Enter x1:")
label_x1.grid(row=0, column=0)
entry_x1 = tk.Entry(window)
entry_x1.grid(row=0, column=1)

label_x2 = tk.Label(window, text="Enter x2:")
label_x2.grid(row=1, column=0)
entry_x2 = tk.Entry(window)
entry_x2.grid(row=1, column=1)

label_y1 = tk.Label(window, text="Enter y1:")
label_y1.grid(row=2, column=0)
entry_y1 = tk.Entry(window)
entry_y1.grid(row=2, column=1)

label_y2 = tk.Label(window, text="Enter y2:")
label_y2.grid(row=3, column=0)
entry_y2 = tk.Entry(window)
entry_y2.grid(row=3, column=1)

calculate_button = tk.Button(window, text="Calculate Gradient", command=calculate_gradient)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Start the main loop
window.mainloop()
