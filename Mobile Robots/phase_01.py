import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Learning concepts from sensor data of a mobile robot; set of data sets


Data Set Characteristics:  

Domain-Theory

Number of Instances:

N/A

Area:

Computer

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

N/A

Date Donated

1995-07-15

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

95600


Source:

Donors:

Volker Klingspor, Katharina J. Morik, Anke D. Rieger
Computer Science Dept. LS VIII
University of Dortmund, Germany


Data Set Information:

Please view the associated .names file


Attribute Information:

Tr (Trace) (integer)
T (Time) (integer)
S (Sensor) (integer 0-23)
Or (Orientation) (real 0-360)
Sa (S-Orientation) (real 0-360)
Gr (Gradient) (real)
Dist (Distance) (real)
Sx,Sy
(Sensor-coordinates) (real)
Obj (Object) (integer)
E (Edge) (integer)
S_C (Sensorclass) (set of front_side,right_side,back_side,left_side ...)
Mv (Movement) (set of parallel, diagonal)
MD (MoveDirection) (set of forward, backward, right, left)
PD (PerceptionDir.) (set of front, rear, right, left)
Perc (perceptual features)
"""

names=['Trace', 'Time', 'Sensor', 'Orientation', 'S-Orientation', 'Gradient', 'Distance', 'Sensor-coordinates', 'Object', 'Edge', 'Sensorclass', 'Movement', 'MoveDirection', 'PerceptionDir.', 'perceptual_features']