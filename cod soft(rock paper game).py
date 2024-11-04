import tkinter as tk
import random

# Function to handle the game's logic
def play(choice):
    user_choice.set(choice)
    computer = random.choice(["Rock", "Paper", "Scissors"])
    computer_choice.set(computer)
    
    # Determine the outcome
    if choice == computer:
        result.set("It's a tie!")
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Scissors" and computer == "Paper") or \
         (choice == "Paper" and computer == "Rock"):
        result.set("You win!")
        user_score.set(user_score.get() + 1)
    else:
        result.set("Computer wins!")
        computer_score.set(computer_score.get() + 1)

# Function to reset the game
def reset():
    user_choice.set("")
    computer_choice.set("")
    result.set("")

# Function to quit the game
def quit_game():
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Game variables
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()
user_score = tk.IntVar(value=0)
computer_score = tk.IntVar(value=0)

# Title Label
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16))
title_label.pack(pady=10)

# Instructions Label
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors to play against the computer.", font=("Helvetica", 10))
instructions.pack()

# Choice Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Display Choices
choices_frame = tk.Frame(root)
choices_frame.pack(pady=10)
tk.Label(choices_frame, text="Your Choice:").grid(row=0, column=0)
tk.Label(choices_frame, textvariable=user_choice).grid(row=0, column=1)
tk.Label(choices_frame, text="Computer's Choice:").grid(row=1, column=0)
tk.Label(choices_frame, textvariable=computer_choice).grid(row=1, column=1)

# Display Result
result_label = tk.Label(root, textvariable=result, font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

# Scoreboard
score_frame = tk.Frame(root)
score_frame.pack(pady=10)
tk.Label(score_frame, text="Your Score:").grid(row=0, column=0)
tk.Label(score_frame, textvariable=user_score).grid(row=0, column=1)
tk.Label(score_frame, text="Computer's Score:").grid(row=1, column=0)
tk.Label(score_frame, textvariable=computer_score).grid(row=1, column=1)

# Control Buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=10)
tk.Button(control_frame, text="Play Again", command=reset).grid(row=0, column=0, padx=5)
tk.Button(control_frame, text="Quit", command=quit_game).grid(row=0, column=1, padx=5)

# Start the main loop
root.mainloop()
