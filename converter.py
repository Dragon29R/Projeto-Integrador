import numpy as np
from tkinter import filedialog
import pandas as pd
import pyvista as pv
from stl_to_obj import stl_to_obj 
import trimesh
import os


def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(title="Select input file",filetypes=(("All files", "*.*"),))
    if input_file:
        return True
    else:
        return False
        


def convert_to_stl(checkbox_action=False, center_action=False, scale_factor=1):

    global input_file

    if not input_file:
        print("No input file selected. Please select an input file.")
        return

    df = pd.read_csv(input_file)
    df_copy = df.copy()

    if checkbox_action:
        df_copy['X'] = df_copy['X'] / 111320
        df_copy['Y'] = df_copy['Y'] / (111320 * np.cos(df_copy['X'] * np.pi / 180))
        df_copy['Z'] = df_copy['Z'] - 12000

    if center_action:
        df_copy['X'] = df_copy['X'] - df_copy['X'].mean()
        df_copy['Y'] = df_copy['Y'] - df_copy['Y'].mean()
        df_copy['Z'] = df_copy['Z'] - df_copy['Z'].mean()

    # Scale the coordinates
    df_copy['X'] = df_copy['X'] * scale_factor
    df_copy['Y'] = df_copy['Y'] * scale_factor
    df_copy['Z'] = df_copy['Z'] * scale_factor

    output_file = filedialog.asksaveasfilename(title="Select output file",
                                               defaultextension=".stl",
                                               filetypes=(("STL files", "*.stl"), ("all files", "*.*")))

    if not output_file:
        print("No output file selected. Please select an output file.")
        return

    temp = "temp.csv"
    df_copy.to_csv(temp, index=False)

    # Load the point cloud from the input file
    points = np.genfromtxt(temp, delimiter=",", dtype=np.float32)

    point_cloud = pv.PolyData(points)

    # To visualize the point cloud
    point_cloud.plot(render_points_as_spheres=True)

    # Reconstruct the surface and save the mesh to the output file
    mesh = point_cloud.reconstruct_surface()
    mesh.save(output_file)
    
    os.remove(temp)

def convert_to_obj():
    global input_file
    
    stl_to_obj(input_file)
    print("Obj done.")
    
def convert_stl_to_glb():
    global input_file

    # Load the STL file
    mesh = trimesh.load_mesh(input_file)

    # Reorient the mesh
    mesh.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 2, (1, 0, 0)))

    # Rotate 180 degrees to the left
    mesh.apply_transform(trimesh.transformations.rotation_matrix(np.pi, (0, 1, 0)))

    # Repair the mesh
    mesh.remove_degenerate_faces()

    # Stl to GLB 
    glb = mesh.export(file_type='glb')

    #Save
    output_file = filedialog.asksaveasfilename(title="Select output file",
                                               defaultextension=".glb",
                                               filetypes=(("GLB files", "*.glb"), ("all files", "*.*")))

    if not output_file:
        print("No output file selected. Please select an output file.")
        return

    with open(output_file, 'wb') as f:
        f.write(glb)

    print("GLB done.")

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    