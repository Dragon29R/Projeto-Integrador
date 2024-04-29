from pickle import FRAME
import tkinter as tk
from types import FrameType
from converter import select_input_file, convert_to_stl, convert_to_obj, convert_stl_to_glb
from tkinter import Frame, font as tkFont
from tkinter import DoubleVar


# Using the tkinter library to create a simple GUI
# https://docs.python.org/3/library/tkinter.html#the-window-manager

# Aux Functions

def on_select_file():
    if select_input_file():
        convert_button.config(state='normal')
        convert_obj_button.config(state='normal')
        convert_glb_button.config(state='normal')
    else:
        convert_button.config(state='disabled')
        convert_obj_button.config(state='disabled')
        convert_glb_button.config(state='disabled')



# Create a root window
root = tk.Tk()
root.geometry("920x640")
root.title("CSV to STL/OBJ Converter")
root.configure(bg='beige')  
checkbox_action = tk.BooleanVar() 
center_action = tk.BooleanVar()
scale_factor = DoubleVar(value=-1.0)
rotation_angle = DoubleVar(value=0.0)
resize_1km = tk.BooleanVar()



# Create a label
label = tk.Label(root, text="Convert a CSV to STL file", bg='beige', font='Arial 20 bold italic')
label.pack(padx=20, pady=20)

# Define a custom font
customFont = tkFont.Font(family="Helvetica", size=12)

# Use frames for organization
frame = tk.Frame(root, bg='beige')
frame.pack(pady=10)

select_button = tk.Button(frame, text="Select file", command=on_select_file, bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT)

checkbox = tk.Checkbutton(frame, text="Convert from meters to latitude/longitude/bathymetry", variable=checkbox_action, bg='beige', font=customFont)

center_checkbox = tk.Checkbutton(frame, text="Center the point cloud", variable=center_action, bg='beige', font=customFont)

resize_1km_checkbox = tk.Checkbutton(frame, text="Resize to 1 km width", variable=resize_1km, bg='beige', font=customFont)

scale_label = tk.Label(frame, text="Scale factor:", bg='beige', font=customFont)

scale_entry = tk.Entry(frame, textvariable=scale_factor, bg='white', font=customFont)

rotation_label = tk.Label(frame, text="Rotation angle to GLB file:", bg='beige', font=customFont)

rotation_entry = tk.Entry(frame, textvariable=rotation_angle, bg='white', font=customFont)

convert_button = tk.Button(frame, text="Convert to STL", command=lambda: convert_to_stl(checkbox_action.get(),center_action.get(), scale_factor.get(), resize_1km.get() ), bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT, state=tk.DISABLED)

convert_obj_button = tk.Button(frame, text="Convert from STL to OBJ", command=lambda: convert_to_obj(), bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT, state=tk.DISABLED)

convert_glb_button = tk.Button(frame, text="Convert from STL to GLB", command=lambda: convert_stl_to_glb(rotation_entry.get()), bg='#0052cc', fg='white', font=customFont, relief=tk.FLAT, state=tk.DISABLED)

close_button = tk.Button(frame, text="Close", command=root.destroy, bg='#d9534f', fg='white', font=customFont, relief=tk.FLAT)



# Arrange buttons with consistent padding
select_button.pack(fill=tk.X, padx=30, pady=7)

checkbox.pack(padx=30, pady=7)
center_checkbox.pack(padx=30, pady=7)
resize_1km_checkbox.pack(padx=30, pady=7)
scale_label.pack(padx=30, pady=7)
scale_entry.pack(fill=tk.X, padx=30, pady=7)
convert_button.pack(fill=tk.X, padx=30, pady=7)
convert_obj_button.pack(fill=tk.X, padx=30, pady=7)
rotation_label.pack(padx=30, pady=7)
rotation_entry.pack(fill=tk.X, padx=30, pady=7)
convert_glb_button.pack(fill=tk.X, padx=30, pady=7)
close_button.pack(fill=tk.X, padx=30, pady=7)
# Start the main loop
root.mainloop()