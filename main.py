from pickle import FRAME
import tkinter as tk
from types import FrameType
from converter import select_input_file, convert_to_obj
from tkinter import Frame, font as tkFont



# Using the tkinter library to create a simple GUI
# https://docs.python.org/3/library/tkinter.html#the-window-manager

# Aux Functions

def on_select_file():
    if select_file():
        convert_stl_button.config(state='normal')
        convert_obj_button.config(state='normal')
    else:
        convert_stl_button.config(state='disabled')
        convert_obj_button.config(state='disabled')



# Create a root window
root = tk.Tk()
root.geometry("460x410")
root.title("CSV to STL Converter")
root.configure(bg='beige')  
checkbox_action = tk.BooleanVar() 
center_action = tk.BooleanVar()

# Create a label
label = tk.Label(root, text="Convert a CSV to STL file", bg='beige', font='Arial 20 bold italic')
label.pack(padx=20, pady=20)

# Define a custom font
customFont = tkFont.Font(family="Helvetica", size=12)

# Use frames for organization
frame = tk.Frame(root, bg='beige')
frame.pack(pady=10)

select_button = tk.Button(frame, text="Select file", command=on_select_file, bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT)

convert_stl_button = tk.Button(frame, text="Convert to STL", command=convert_to_stl, bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT, state=tk.DISABLED)

convert_obj_button = tk.Button(frame, text="Convert to OBJ", command=convert_to_obj, bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT, state=tk.DISABLED)

close_button = tk.Button(frame, text="Close", command=root.destroy, bg='#d9534f', fg='white', font=customFont, relief=tk.FLAT)





# Arrange buttons with consistent padding
select_button.pack(fill=tk.X, padx=30, pady=7)
convert_stl_button.pack(fill=tk.X, padx=30, pady=7)
convert_obj_button.pack(fill=tk.X, padx=30, pady=7)
close_button.pack(fill=tk.X, padx=30, pady=7)
# Start the main loop
root.mainloop()


