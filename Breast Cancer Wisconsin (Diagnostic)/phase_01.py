import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data", names=['ID', 'Diagnosis', 'cell_nucleus_f01', 'cell_nucleus_f02','cell_nucleus_f03','cell_nucleus_f04','cell_nucleus_f05', 'cell_nucleus_f06', 'cell_nucleus_f07', 'cell_nucleus_f08', 'cell_nucleus_f09', 'cell_nucleus_f10', 'radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 'concavity','concave_points', 'symmetry', 'fractal_dimension'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data", names=['ID', 'Diagnosis', 'cell_nucleus_f01', 'cell_nucleus_f02','cell_nucleus_f03','cell_nucleus_f04','cell_nucleus_f05', 'cell_nucleus_f06', 'cell_nucleus_f07', 'cell_nucleus_f08', 'cell_nucleus_f09', 'cell_nucleus_f10', 'radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 'concavity','concave_points', 'symmetry', 'fractal_dimension'])

print(df.info())