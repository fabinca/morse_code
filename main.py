import tkinter as tk
from playsound import playsound
import pandas as pd
from tkinter import messagebox

# TO-DO'S

# 1. create Morse dictionary for translation
file = pd.read_csv("morse.csv")
TO_MORSE = {row[0]: row[1] for (index, row) in file.iterrows()}
FROM_MORSE = {row[1]: row[0] for (index, row) in file.iterrows()}

# function for translating - text to morse and morse to text
translating = False
output = ""
playing = False
text = ""


def translate():
    global text, translating, output
    if not translating:
        text = text_entry.get()
        output = ""
        translating = True
    char = text[0]
    text = text[1:]
    if char == " ":
        output += " "
    else:
        try:
            output += TO_MORSE[char.upper()] + " "
        except KeyError:
            messagebox.showwarning(title="Nonvalid character", message=f"Character '{char}' "
                                                                       f"is not translatable & is skipped")
    morse_entry.insert(1.0, output)
    if len(text) > 0:
        screen.after(1, translate)
    else:
        translating = False


# function for playing the morse sound
def scan_to_play():
    global text
    if playing:
        char = text[0]
        text = text[1:]
        if char == "-":
            playsound("beeep.mp3")
        elif char == ".":
            playsound("bip.mp3")
        else:
            screen.after(600)
    if len(text) > 0:
        screen.after(1, scan_to_play)


def play():
    global playing, text
    text = morse_entry.get(1.0, "end")
    playing = True
    scan_to_play()


def stop():
    global playing
    playing = False


# user interface
screen = tk.Tk()
screen.title("Morse Code Generator")
screen.config(bg="black", padx=50, pady=50)
title_label = tk.Label(text="Morse Code Translator", bg="black", fg="cyan", padx=50, pady=50,
                       font=("Courier", 40, "bold"))
title_label.grid(column=0, row=0, columnspan=4)
text_label = tk.Label(text="Text", bg="black", fg="cyan", pady=25, padx=5, font=("Courier", 15, "bold"))
text_label.grid(column=0, row=1, sticky="w")
text_label = tk.Label(text="Morse Code", bg="black", fg="cyan", pady=25, padx=5, font=("Courier", 15, "bold"))
text_label.grid(column=0, row=2, sticky="w")
text_entry = tk.Entry(width=30, bg="cyan", fg="black", font=("Courier", 12),
                      highlightthickness=5, highlightbackground="black")
text_entry.focus()
text_entry.grid(column=1, row=1, sticky="w")
morse_entry = tk.Text(height=5, width=30, fg="cyan", bg="black", font=("Courier", 12),
                      highlightthickness=5, highlightbackground="black")
morse_entry.grid(column=1, row=2, sticky="w")

tl_button = tk.Button(text="  Translate  ", command=translate, bg="cyan", fg="black", padx=5,
                      font=("Courier", 15, "bold"))
tl_button.grid(row=1, column=2, columnspan=2)
play_button = tk.Button(text="Play", command=play, bg="cyan", fg="black", font=("Courier", 15, "bold"))
play_button.grid(row=2, column=2)
play_button = tk.Button(text="Stop", command=stop, bg="cyan", fg="black", font=("Courier", 15, "bold"))
play_button.grid(row=2, column=3)

screen.mainloop()
