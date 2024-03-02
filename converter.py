import numpy as np
import pyvista as pv
from tkinter import filedialog
import pandas as pd

def select_file():
    global input_file
    input_file = filedialog.askopenfilename(title="Select input file",
                                            filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    if input_file:
        return True
    else:
        return False


def convert_to_stl(checkbox_action=False):

    global input_file

    if not input_file:
        print("No input file selected. Please select an input file.")
        return

    if checkbox_action:
        df = pd.read_csv(input_file)
        df['X'] = df['X'] / 111320
        df['Y'] = df['Y'] / (111320 * np.cos(df['X'] * np.pi / 180))
        df['Z'] = df['Z'] - 12000

        df.to_csv(input_file, index=False)
    

    output_file = filedialog.asksaveasfilename(title="Select output file",
                                               defaultextension=".stl",
                                               filetypes=(("STL files", "*.stl"), ("all files", "*.*")))

    if not output_file:
        print("No output file selected. Please select an output file.")
        return

    # Load the point cloud from the input file
    points = np.genfromtxt(input_file, delimiter=",", dtype=np.float32)
    point_cloud = pv.PolyData(points)

    # Reconstruct the surface and save the mesh to the output file
    mesh = point_cloud.reconstruct_surface()
    mesh.save(output_file)