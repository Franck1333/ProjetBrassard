#AIDES: https://stackoverflow.com/questions/18047636/python-is-it-possible-to-create-an-tkinter-label-which-has-a-dynamic-string-whe

import tkinter as tk

# You will need the ttk module for this
from tkinter import ttk

def update_status(step):

    # Step here is how much to increment the progressbar by.
    # It is in relation to the progressbar's length.
    # Since I made the length 100 and I am increasing by 10 each time,
    # there will be 10 times it increases before it restarts
    progress.step(step)

    # You can call 'update_status' whenever you want in your script
    # to increase the progressbar by whatever amount you want.
    root.after(1000, lambda: update_status(10))

root = tk.Tk()

progress = ttk.Progressbar(root, length=100)
progress.pack()

progress.after(1, lambda: update_status(10))

root.mainloop()
