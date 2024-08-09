import random
import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Number Guessing Game")

rand_num = random.randint(0,100)
attempts = 0

def guess_num_check():
    global attempts
    try:
        num = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

    attempts += 1
    
    if num==rand_num:
        messagebox.showinfo("Correct!", f"You guessed the number!\nYou took {attempts} attempt{'s' if attempts > 1 else ''} to guess this number.")
        root.destroy()
    elif num < rand_num:
        feedback_label.config(text="The guess is too low! Try again")
    else:
        feedback_label.config(text="The guess is too high! Try again")
    
instruction_label = tk.Label(root, text="Enter a number between 0 and 100 to guess:")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_num_check)
guess_button.pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack()

root.mainloop()
