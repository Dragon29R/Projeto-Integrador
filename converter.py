import numpy as np
from tkinter import filedialog
import pandas as pd
import pyvista as pv
from stl_to_obj import stl_to_obj 
import trimesh
import os
import math


def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(title="Select input file",filetypes=(("All files", "*.*"),))
    if input_file:
        return True
    else:
        return False
        
def convert_to_stl(checkbox_action=False, center_action=False, scale_factor=-1):

    global input_file

    if not input_file:
        print("No input file selected. Please select an input file.")
        return

    df = pd.read_csv(input_file)
    df_copy = df.copy()

    # Convert the coordinates from meters to latitude/longitude/bathymetry
    if checkbox_action:
        df_copy['X'] = df_copy['X'] / 111320
        df_copy['Y'] = df_copy['Y'] / (111320 * np.cos(df_copy['X'] * np.pi / 180))
        df_copy['Z'] = (df_copy['Z'] - 12000) / 100000

        output_csv_file = os.path.splitext(input_file)[0] + "_modified.csv"
        df_copy.to_csv(output_csv_file, index=False)
    
    first_coord_before_scaling = df_copy.iloc[0][['X', 'Y','Z']]
    
    if scale_factor == -1:
            
            first_coord = df_copy.iloc[0][['X', 'Y']]
            print(first_coord)
            last_coord = df_copy.iloc[-1][['X', 'Y']]
            print(last_coord)
            distance = np.linalg.norm(first_coord - last_coord)
            
            distance *= 100
            print(f"Distance between the first and last coordinates: {distance:.2f} km")

            distance *= 1000
            distance = math.ceil(distance)
            df_copy['X'] = df_copy['X'] * distance
            df_copy['Y'] = df_copy['Y'] * distance
            df_copy['Z'] = df_copy['Z'] * distance

    else:

        # Scale the coordinates if received input
        df_copy['X'] = df_copy['X'] * scale_factor
        df_copy['Y'] = df_copy['Y'] * scale_factor
        df_copy['Z'] = df_copy['Z'] * scale_factor

    output_csv_file = os.path.splitext(input_file)[0] + "_modified_scaled.csv"
    df_copy.to_csv(output_csv_file, index=False)


    first_coord_after_scaling = df_copy.iloc[0][['X', 'Y','Z']]

    coord_diff = first_coord_after_scaling - first_coord_before_scaling


    # Center the point cloud
    if center_action:
        df_copy['X'] = df_copy['X'] - coord_diff['X']
        df_copy['Y'] = df_copy['Y'] - coord_diff['Y']
        df_copy['Z'] = df_copy['Z'] - coord_diff['Z']

    output_csv_file = os.path.splitext(input_file)[0] + "_modified_centered.csv"
    df_copy.to_csv(output_csv_file, index=False)

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
    
def convert_stl_to_glb(file_name, rotation_angle=0):
  
    input_file = file_name
    # Load the STL file
    mesh = trimesh.load_mesh(input_file)

    # Repair the mesh
    mesh.remove_degenerate_faces()

    #Change object from vertically oriented to horizontally oriented
    mesh.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 2, (1, 0, 0)))

    # Make the mesh double-sided
    mesh = trimesh.Trimesh(vertices=np.concatenate([mesh.vertices, mesh.vertices]),
                           faces=np.concatenate([mesh.faces, mesh.faces[:, ::-1]]))

    # Rotate the mesh
    mesh.apply_transform(trimesh.transformations.rotation_matrix(np.radians(float(rotation_angle)), (0, 1, 0)))

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