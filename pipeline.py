from pickle import FRAME
from stl_to_obj import stl_to_obj 
import tkinter as tk
from types import FrameType
from converter import select_input_file, convert_to_stl, convert_to_obj, convert_stl_to_glb
from tkinter import Frame, font as tkFont
from tkinter import DoubleVar
import sys
import os


# sys.argv[1] = file_name
# sys.argv[2] = 0 to obj/ 1 to glb
# sys.argv[3] = scale factor
# sys.argv[4] = rotation angle
#csv->stl->obj/glb

if len(sys.argv) < 3:
    print("Usage: python pipeline.py <filename> <0 for OBJ or 1 for GLB> [scale factor] [rotation angle]")
    sys.exit(1)

file_name = sys.argv[1]
output_type = sys.argv[2]
scale_factor = sys.argv[3] if len(sys.argv) > 3 else 1.0
rotation_angle = sys.argv[4] if len(sys.argv) > 4 else 0.0

print("Filename: ", file_name)
print("Output Type: ", "OBJ" if output_type == "0" else "GLB")

if output_type == "0":
    print("Converting to OBJ...")
    stl_to_obj(file_name, "new.obj")
elif output_type == "1":
    print("Converting to GLB...")
    convert_stl_to_glb(file_name, rotation_angle)
else:
    print("Invalid format choice; use '0' for OBJ or '1' for GLB.")
    sys.exit(1)
  
# example = python3 pipeline.py cc.stl 0