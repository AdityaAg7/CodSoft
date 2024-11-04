import tkinter as tk
from tkinter import messagebox

# Initialize the contacts dictionary
contacts = {}

# Function to add a contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact {name} added successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")

# Function to view all contacts
def view_contacts():
    if contacts:
        contacts_str = "\n".join([f"{name}: {info['Phone']}" for name, info in contacts.items()])
        messagebox.showinfo("Contact List", contacts_str)
    else:
        messagebox.showinfo("Contact List", "No contacts found.")

# Function to search for a contact
def search_contact():
    name = entry_name.get()
    if name in contacts:
        info = contacts[name]
        result = f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}"
        messagebox.showinfo("Search Result", result)
    else:
        messagebox.showerror("Error", "Contact not found.")

# Function to update a contact
def update_contact():
    name = entry_name.get()
    if name in contacts:
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        messagebox.showinfo("Success", f"Contact {name} updated successfully.")
    else:
        messagebox.showerror("Error", "Contact not found.")

# Function to delete a contact
def delete_contact():
    name = entry_name.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
        clear_entries()
    else:
        messagebox.showerror("Error", "Contact not found.")

# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")
root.config(bg="#FFEBE6")  # Light peach background

# Labels and Entry widgets for contact information with colorful background
tk.Label(root, text="Name:", fg="black", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_name = tk.Entry(root, fg="black", bg="#FFF2CC", insertbackground="black")
entry_name.pack(pady=5)

tk.Label(root, text="Phone:", fg="black", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_phone = tk.Entry(root, fg="black", bg="#FFF2CC", insertbackground="black")
entry_phone.pack(pady=5)

tk.Label(root, text="Email:", fg="black", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_email = tk.Entry(root, fg="black", bg="#FFF2CC", insertbackground="black")
entry_email.pack(pady=5)

tk.Label(root, text="Address:", fg="black", bg="#FFD966", font=("Helvetica", 10, "bold")).pack(pady=5)
entry_address = tk.Entry(root, fg="black", bg="#FFF2CC", insertbackground="black")
entry_address.pack(pady=5)

# Buttons for operations with vibrant colors
tk.Button(root, text="Add Contact", command=add_contact, fg="white", bg="#34A853", font=("Helvetica", 10, "bold")).pack(pady=5)
tk.Button(root, text="View Contacts", command=view_contacts, fg="white", bg="#4285F4", font=("Helvetica", 10, "bold")).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact, fg="white", bg="#FBBC05", font=("Helvetica", 10, "bold")).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, fg="white", bg="#EA4335", font=("Helvetica", 10, "bold")).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, fg="white", bg="#F45342", font=("Helvetica", 10, "bold")).pack(pady=5)

# Run the main loop
root.mainloop()
