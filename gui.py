import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def on_button_click():
    messagebox.showinfo("Hello", "Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a button and associate the on_button_click function with it
button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
window.mainloop()