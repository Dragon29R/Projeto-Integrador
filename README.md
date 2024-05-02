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

3-Set the desired options such as scale conversion, centering, and resizing.

4-Convert into STL and save the STL file.

5-Choose the created file in STL and then choose the desired output format OBJ or GLB and initiate the conversion.

6-Save the converted file.
