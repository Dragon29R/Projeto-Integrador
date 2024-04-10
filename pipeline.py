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

if len(sys.argv) == 2:
  file_name = sys.argv[1]

if len(sys.argv) == 3:
  file_name = sys.argv[1]
  obj_or_stl = sys.argv[2]

if len(sys.argv) == 4:
  file_name = sys.argv[1]
  obj_or_stl = sys.argv[2]
  scale_factor = sys.argv[3]

if len(sys.argv) == 5:
  file_name = sys.argv[1]
  obj_or_stl = sys.argv[2]
  scale_factor = sys.argv[3]
  rotation_angle = sys.argv[4]


print("Arg0: ", sys.argv[0])
print("Arg1: ", sys.argv[1])
print("Arg2: ", sys.argv[2])


if sys.argv[2] == "0":
  print("Converting to obj")
  stl_to_obj(file_name, "new.obj")

if obj_or_stl == "1":
    print("Converting to glb")
    convert_stl_to_glb(file_name, rotation_angle)

  
# example = python3 pipeline.py cc.stl 0