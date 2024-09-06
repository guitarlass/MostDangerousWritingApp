import tkinter as tk

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

# Run the Tkinter event loop
root.mainloop()

