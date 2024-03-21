import numpy as np
from tkinter import filedialog
import pandas as pd
import pyvista as pv
from stl_to_obj import stl_to_obj 
import trimesh


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

    if checkbox_action:
        df['X'] = df['X'] / 111320
        df['Y'] = df['Y'] / (111320 * np.cos(df['X'] * np.pi / 180))
        df['Z'] = df['Z'] - 12000

        df.to_csv(input_file, index=False, float_format='%.2f')

    if center_action:
        df['X'] = df['X'] - df['X'].mean()
        df['Y'] = df['Y'] - df['Y'].mean()
        df['Z'] = df['Z'] - df['Z'].mean()

        df.to_csv(input_file, index=False)
        

    # Scale the coordinates
    df['X'] = df['X'] * scale_factor
    df['Y'] = df['Y'] * scale_factor
    df['Z'] = df['Z'] * scale_factor

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

    # To visualize the point cloud
    point_cloud.plot(render_points_as_spheres=True)

    # Reconstruct the surface and save the mesh to the output file
    mesh = point_cloud.reconstruct_surface()
    mesh.save(output_file)
    

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

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    