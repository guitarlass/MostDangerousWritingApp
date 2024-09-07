import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("The Most Dangerous Random Prompt Generator")

# Set the window size
root.geometry("600x400")

# Create a label on top
label = tk.Label(root, text="The Most Dangerous Random Prompt Generator", font=("Arial", 16))
label.pack(pady=10)

# Create a large textarea
text_area = tk.Text(root, wrap="word", font=("Arial", 24), height=15, width=28)
text_area.pack(pady=20)

type_timer = None

def hide_all():
    text_area.delete("1.0", "end")
    messagebox.showerror("You waited too long!", "Your text is gone! Start all over.")


def on_key_release(event):
    global type_timer

    if type_timer:
        root.after_cancel(type_timer)

    type_timer = root.after(2000, hide_all)


text_area.bind("<KeyRelease>", on_key_release)

# Run the Tkinter event loop
root.mainloop()
