import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation! Use +, -, *, or /")
            return

        label_result.config(text="Result: " + str(result))
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")
root.config(bg="#FFEBE6")

# Input fields and labels
tk.Label(root, text="Number 1:", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Number 2:", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

tk.Label(root, text="Operation (+, -, *, /):", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_operation = tk.Entry(root)
entry_operation.pack(pady=5)

# Button to perform calculation
tk.Button(root, text="Calculate", command=calculate, fg="white", bg="#34A853", font=("Helvetica", 10, "bold")).pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result:", bg="#FFEBE6", font=("Helvetica", 10, "bold"))
label_result.pack(pady=5)

# Run the main loop
root.mainloop()
