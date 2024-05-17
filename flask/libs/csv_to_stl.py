import numpy as np
from tkinter import filedialog
import pandas as pd
import pyvista as pv
import trimesh
import os
import math


def convert_to_stl(filename,checkbox_action=True, center_action=True, scale_factor=-1, resize_1km = True):

    input_file = filename

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
    
    #Save the original coordinates
    first_coord_before_scaling = df_copy.iloc[0][['X', 'Y','Z']]
    

    # Calculate the distance between the first and last coordinates
    first_coord = df_copy.iloc[0][['X', 'Y']]
    print(first_coord)
    last_coord = df_copy.iloc[-1][['X', 'Y']]
    print(last_coord)
    distance = np.linalg.norm(first_coord - last_coord)
    
    distance *= 100
    print(f"Distance between the first and last coordinates: {distance:.2f} km")

    distance *= 1000
    distance = math.ceil(distance)


    if scale_factor == -1:     
        # Scaling Automatically   
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

    #output_file = filedialog.asksaveasfilename(title="Select output file",
    #                                           defaultextension=".stl",
    #                                           filetypes=(("STL files", "*.stl"), ("all files", "*.*")))

    #if not output_file:
    #    print("No output file selected. Please select an output file.")
    #    return

    temp = "temp.csv"
    df_copy.to_csv(temp, index=False)

    # Load the point cloud from the input file
    points = np.genfromtxt(temp, delimiter=",", dtype=np.float32)

    
    point_cloud = pv.PolyData(points)

    # Reconstruct the surface and save the mesh to the output file
    mesh = point_cloud.reconstruct_surface()
    #mesh.save(output_file)
    
    os.remove(temp)

    if(resize_1km):
        #Resize to 1km with
        df_1km = df_copy.copy()




        # Save the scaled point cloud as an STL file
        temp = "temp.csv"
        df_1km.to_csv(temp, index=False)
        points = np.genfromtxt(temp, delimiter=",", dtype=np.float32)
        point_cloud = pv.PolyData(points)
        mesh = point_cloud.reconstruct_surface()

        # Calculate the scale factor
        original_width = (mesh.points[:, 0].max() - mesh.points[:, 0].min()) / 1000
        original_height = (mesh.points[:, 1].max() - mesh.points[:, 1].min()) / 1000
        original_depth = (mesh.points[:, 2].max() - mesh.points[:, 2].min()) / 1000

        print(original_width, original_height)

        scale_factor_width = 0.5 / min(original_width, original_height)
        scale_factor_height = 1 / max(original_width, original_height)
        scale_factor_depth = 1 / max(original_width, original_height, original_depth)


        # Scale the vertices
        mesh.points[:, 0] *= scale_factor_width
        mesh.points[:, 1] *= scale_factor_height
        mesh.points[:, 2] *= scale_factor_depth

        # Specify output folder
        output_folder = "static/files"


        # Save the scaled mesh to a new STL file
        output_file_1km = os.path.join(output_folder, os.path.splitext(output_file)[0] + "_1km.stl")
        mesh.save(output_file_1km)
        
        os.remove(temp)