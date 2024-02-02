import tkinter as tk

def display_button_name(button_name):
    label.config(text=f"Button Clicked: {button_name}")

root = tk.Tk()
root.title("Button Name Display")

# Function to create and configure buttons
def create_button(button_name):
    return tk.Button(root, text=button_name, command=lambda: display_button_name(button_name))

# Creating four buttons with different names
button1 = create_button("Button 1")
button2 = create_button("Button 2")
button3 = create_button("Button 3")
button4 = create_button("Button 4")

# Packing buttons
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# Label to display button name
label = tk.Label(root, text="Click a button!")
label.pack()

root.mainloop()
