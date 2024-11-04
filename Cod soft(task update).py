import tkinter as tk
from tkinter import messagebox

# Initialize the list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to update the listbox with current tasks
def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, task)

# Set up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")
root.config(bg="#FFF8DC")

# Entry field and add button for tasks
frame_top = tk.Frame(root, bg="#FFF8DC")
frame_top.pack(pady=10)

entry_task = tk.Entry(frame_top, width=30, font=("Helvetica", 12))
entry_task.pack(side=tk.LEFT, padx=10)
btn_add = tk.Button(frame_top, text="Add Task", command=add_task, bg="#32CD32", fg="white", font=("Helvetica", 10, "bold"))
btn_add.pack(side=tk.LEFT)

# Listbox to display tasks and scrollbar
frame_middle = tk.Frame(root)
frame_middle.pack(pady=10)

scrollbar = tk.Scrollbar(frame_middle)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(frame_middle, width=40, height=10, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
listbox_tasks.pack()
scrollbar.config(command=listbox_tasks.yview)

# Remove button
frame_bottom = tk.Frame(root, bg="#FFF8DC")
frame_bottom.pack(pady=10)

btn_remove = tk.Button(frame_bottom, text="Remove Task", command=remove_task, bg="#FF6347", fg="white", font=("Helvetica", 10, "bold"))
btn_remove.pack()

# Run the main loop
root.mainloop()
