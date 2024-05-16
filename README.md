## 3D Models Converter
# Project Description

"3D Models Converter" is a robust tool designed to convert CSV data into 3D model formats such as OBJ and GLB, featuring advanced adjustment and manipulation capabilities. This project is part of the ILIAD initiative, aiming to create an interoperable, data-intensive environment for accurate virtual representations of the ocean and its interactions. The software facilitates the integration of 3D models into immersive platforms, ensuring that models are displayed at the correct scale and with proper accuracy.
# Features

__Coordinate Conversion:__ Transforms measurements from meters to geographic coordinates (latitude/longitude) and bathymetry.

__Point Cloud Centering:__ Automatically centers the point cloud, improving integration with other modeling and visualization tools.

__Resizing to 1 km Width:__ Adjusts the model to a standard width, maintaining the necessary proportions for specific scenarios.

__Customizable Scale Factor:__ Allows users to adjust the scale factor to meet the specific needs of their projects.

__Rotation for GLB:__ Sets a specific angle when converting to GLB format, ensuring the correct orientation of the model.

# Technologies

Python

Tkinter for GUI

PyVista, trimesh for mesh manipulation

Pandas for data manipulation

NumPy for mathematical operations

# Installation
__Ubuntu__

```cmd

sudo apt-get install python3-tk
pip install numpy
pip install pyvista
pip install pandas
pip install trimesh
pip install pyinstaller
pip install auto-py-to-exe
```



__Windows__

Install Python and Tkinter, which are usually included in the standard Python installation for Windows. 

Then install the necessary dependencies via pip, as in the ubuntu guide above.



__macOS__

Ensure to have python and Homebrew installed.

Install Tkinter for python.
```cmd
brew install python-tk

```
Then install the necessary dependencies via pip, as in the ubuntu guide above.


# How to Use

1-Run the program through the graphical interface.

2-Select the desired CSV file for conversion using the "Select file" button.

3-Pressing the button "Convert to STL" will convert the selected CSV file to an STL file, using the following parameters:
 
 - "Convert from meters to latitude/longitude/bathymetry" will convert the coordinates from meters to latitude/longitude and bathymetry. It is necessary to check this box.

 - "Center the point cloud" will center the point cloud. It is necessary to check this box.

 - "Resize to 1 km width" will adjust the model to a standard width of 1 km on at least 2 sides. The remaining sides will be adjusted to 0.5km.  This is optional.

 - "Scale Factor" allows the user to adjust the scale factor. If the user wishes to do this process automatically, leave the value as -1.0 in the box.

4-Pressing the button "Convert from STL to OBJ" will convert the selected CSV file to an OBJ file, which does not require any additional parameters. Remember to select the STL file you want to convert beforehand.

5-Pressing the button "Convert from STL to GLB" will convert the selected CSV file to a GLB file, using the following parameters:

 - "Rotation" allows the user to set a specific angle when converting to GLB format. This is optional.


