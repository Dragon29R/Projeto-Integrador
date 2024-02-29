import tkinter as tk
from converter import select_file, convert_to_stl

# Using the tkinter library to create a simple GUI
# https://docs.python.org/3/library/tkinter.html#the-window-manager

# Aux Functions

def on_select_file():
    if select_file():
        convert_button.config(state='normal')
    else:
        convert_button.config(state='disabled')



# Create a root window
root = tk.Tk()
root.geometry("1260x720")
root.title("CSV to STL Converter")
root.configure(bg='white')  

# Create a label
label = tk.Label(root, text="Convert a point cloud from a CSV file to an STL file", bg='white', font='Arial 20 bold italic')
label.pack(padx=20, pady=20)


# Create the buttons and the labels
select_button_label = tk.Label(root, text="Select the input file", bg='white', font='Arial 12')
select_button = tk.Button(root, text="Select file", command=on_select_file, bg='#00B2EE')

convert_button_label = tk.Label(root, text="Convert the file to STL", bg='white', font='Arial 12')
convert_button = tk.Button(root, text="Convert to STL", command=convert_to_stl, bg='#00B2EE', state=tk.DISABLED)

close_button_label = tk.Label(root, text="Close the App", bg='white', font='Arial 12')
close_button = tk.Button(root, text="Close", command=root.destroy, bg='red')

# Pack the buttons and labels into the window

select_button_label.pack()
select_button.pack(pady=(0, 10))

convert_button_label.pack()
convert_button.pack(pady=(0, 10))

close_button_label.pack()
close_button.pack(pady=(0, 10))

# Start the main loop
root.mainloop()


