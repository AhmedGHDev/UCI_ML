import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Domain Theory on Economic Sanctions; Undocumented


Data Set Characteristics:  

Domain-Theory

Number of Instances:

N/A

Area:

Financial

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

N/A

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

74099


Source:

Michael Pazzani
pazzani '@' ICS.UCI.EDU


Data Set Information:

I think you'll find some limited documentation on Mike's database in his papers. His dissertation would be a good reference (UCLA). Perhaps pages 152-153 in the EWSL-1988 proceedings should help with understanding the data format. Pages 713-718 of IJCAI-1989 should help even more.


Attribute Information:

N/A


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Sally Jo Cunningham. Dataset cataloging metadata for machine learning applications and research. Department of Computer Science University of Waikato. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data", names=['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data", names=['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

print(df.info())