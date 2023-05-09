import pandas as pd


#Step 00: Loading data
#FROM URL

# INFO
"""
Abstract: This data consists of synthetically generated control charts.

Data Set Characteristics:  

Time-Series

Number of Instances:

600

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

N/A

Date Donated

1999-06-08

Associated Tasks:

Classification, Clustering

Missing Values?

No

Number of Web Hits:

95854


Source:

Dr Robert Alcock
rob '@' skyblue.csd.auth.gr


Data Set Information:

This dataset contains 600 examples of control charts synthetically generated by the process in Alcock and Manolopoulos (1999). There are six different classes of control charts:

1. Normal
2. Cyclic
3. Increasing trend
4. Decreasing trend
5. Upward shift
6. Downward shift

The following image shows ten examples from each class: data.jpeg, where (A) Downward Trend. (B) Cyclic. (C) Normal. (D) Upward Shift. (E) Upward Trend. (F) Downward Shift.


Attribute Information:

The data is stored in an ASCII file, 600 rows, 60 columns, with a single chart per line. The classes are organized as follows:

1-100 Normal
101-200 Cyclic
201-300 Increasing trend
301-400 Decreasing trend
401-500 Upward shift
501-600 Downward shift


Relevant Papers:

Alcock R.J. and Manolopoulos Y. Time-Series Similarity Queries Employing a Feature-Based Approach. 7th Hellenic Conference on Informatics. August 27-29. Ioannina,Greece 1999.
[Web Link]

D.T. Pham and A.B. Chan "Control Chart Pattern Recognition using a New Type of Self Organizing Neural Network" Proc. Instn, Mech, Engrs. Vol 212, No 1, pp 115-127 1998.



Citation Request:

Image courtesy of Eamonn Keogh.
"""

"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/synthetic_control-mld/synthetic_control.data"
,delimiter='\s+'
,names=['C_'+str(i) for i in range(1, 61)]
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/synthetic_control-mld/synthetic_control.data"
,delimiter='\s+'
,names=['C_'+str(i) for i in range(1, 61)]
)

print(df.info())