import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        output_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the password length.")

# Initialize the tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.config(bg="black")

# Label for user instructions
instruction_label = tk.Label(root, text="Enter the desired length for the password:", fg="green", bg="black")
instruction_label.pack(pady=10)

# Entry widget for password length input
entry_length = tk.Entry(root, fg="green", bg="black", insertbackground="green")
entry_length.pack(pady=5)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, fg="green", bg="black")
generate_button.pack(pady=10)

# Label to display the generated password
output_label = tk.Label(root, text="", fg="green", bg="black")
output_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
