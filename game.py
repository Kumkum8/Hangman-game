import random
import tkinter as tk
from tkinter import messagebox

def choose_word():
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'hello']
    return random.choice(words)

def update_display():
    display_word = " ".join([char if char in guesses else "_" for char in word])
    word_label.config(text=display_word)
    if "_" not in display_word:
        messagebox.showinfo("Hangman", f"You Win, {player_name}! The word is: {word}")
        root.quit()

def guess_character():
    global turns
    guess = entry.get().lower()
    if len(guess) == 1:
        if guess in guesses:
            messagebox.showwarning("Hangman", "You already guessed that character.")
        elif guess in word:
            guesses.append(guess)
        else:
            guesses.append(guess)
            turns -= 1
            draw_hangman()
            turns_label.config(text=f"Turns left: {turns}")
            if turns == 0:
                messagebox.showinfo("Hangman", f"You Lose, {player_name}. The word was: {word}")
                root.quit()
    elif len(guess) == len(word):
        if guess == word:
            messagebox.showinfo("Hangman", f"You Win, {player_name}! The word is: {word}")
            root.quit()
        else:
            turns -= 1
            draw_hangman()
            turns_label.config(text=f"Turns left: {turns}")
            if turns == 0:
                messagebox.showinfo("Hangman", f"You Lose, {player_name}. The word was: {word}")
                root.quit()
    else:
        messagebox.showwarning("Hangman", "Invalid guess length.")
        
    entry.delete(0, tk.END)
    update_display()

def draw_hangman():
    parts = [
        canvas.create_line(50, 150, 150, 150, fill="white"),  # Base
        canvas.create_line(100, 150, 100, 50, fill="white"),  # Pole
        canvas.create_line(100, 50, 150, 50, fill="white"),   # Top
        canvas.create_line(150, 50, 150, 70, fill="white"),   # Rope
        canvas.create_oval(140, 70, 160, 90, outline="white"),   # Head
        canvas.create_line(150, 90, 150, 120, fill="white"),  # Body
        canvas.create_line(150, 100, 140, 110, fill="white"), # Left Arm
        canvas.create_line(150, 100, 160, 110, fill="white"), # Right Arm
        canvas.create_line(150, 120, 140, 130, fill="white"), # Left Leg
        canvas.create_line(150, 120, 160, 130, fill="white")  # Right Leg
    ]
    if turns <= 11:
        canvas.itemconfigure(parts[0], state='normal')  # Base
    if turns <= 10:
        canvas.itemconfigure(parts[1], state='normal')  # Pole
    if turns <= 9:
        canvas.itemconfigure(parts[2], state='normal')  # Top
    if turns <= 8:
        canvas.itemconfigure(parts[3], state='normal')  # Rope
    if turns <= 7:
        canvas.itemconfigure(parts[4], state='normal')  # Head
    if turns <= 6:
        canvas.itemconfigure(parts[5], state='normal')  # Body
    if turns <= 5:
        canvas.itemconfigure(parts[6], state='normal')  # Left Arm
    if turns <= 4:
        canvas.itemconfigure(parts[7], state='normal')  # Right Arm
    if turns <= 3:
        canvas.itemconfigure(parts[8], state='normal')  # Left Leg
    if turns <= 2:
        canvas.itemconfigure(parts[9], state='normal')  # Right Leg

def submit_name():
    global player_name
    player_name = name_entry.get()
    if player_name:
        name_dialog.withdraw()  # Hide the name entry dialog
        messagebox.showinfo("Welcome", f"Good Luck, {player_name}!", parent=root)
        setup_game()

def start_game():
    global name_dialog, name_entry
    name_dialog = tk.Toplevel(root)
    name_dialog.title("Enter Your Name")
    name_dialog.geometry("300x200")
    name_dialog.config(bg="#2d2d2d")
    
    name_label = tk.Label(name_dialog, text="What is your name?", font=("Helvetica", 18), bg="#2d2d2d", fg="#ffffff")
    name_label.pack(pady=20)
    
    name_entry = tk.Entry(name_dialog, font=("Helvetica", 18), bg="#404040", fg="#ffffff", justify='center')
    name_entry.pack(pady=10)
    
    submit_button = tk.Button(name_dialog, text="Submit", command=submit_name, font=("Helvetica", 18), bg="#61dafb", fg="#000000")
    submit_button.pack(pady=10)

def setup_game():
    global word, guesses, turns, word_label, entry, guess_button, turns_label, canvas
    word = choose_word()
    guesses = []
    turns = 12
    
    # Set up GUI components
    root.title("Hangman Game")
    root.config(bg="#2d2d2d")

    word_label = tk.Label(root, text="_ " * len(word), font=("Helvetica", 24), bg="#2d2d2d", fg="#ffffff")
    word_label.pack(pady=20)

    entry = tk.Entry(root, font=("Helvetica", 18), bg="#404040", fg="#ffffff", justify='center')
    entry.pack(pady=10)

    guess_button = tk.Button(root, text="Guess", command=guess_character, font=("Helvetica", 18), bg="#61dafb", fg="#000000")
    guess_button.pack(pady=10)

    turns_label = tk.Label(root, text=f"Turns left: {turns}", font=("Helvetica", 18), bg="#2d2d2d", fg="#ffffff")
    turns_label.pack(pady=20)

    canvas = tk.Canvas(root, width=200, height=200, bg="#2d2d2d", highlightthickness=0)
    canvas.pack()

    update_display()

# Initialize the main window
root = tk.Tk()
root.geometry("400x500")
root.config(bg="#2d2d2d")

# Display the name entry dialog when the program starts
start_game()

# Run the main event loop
root.mainloop()
