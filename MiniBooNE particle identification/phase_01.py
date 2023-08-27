import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset is taken from the MiniBooNE experiment and is used to distinguish electron neutrinos (signal) from muon neutrinos (background).

Data Set Characteristics:  

Multivariate

Number of Instances:

130065

Area:

Physical

Attribute Characteristics:

Real

Number of Attributes:

50

Date Donated

2010-12-13

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

65057


Source:

Byron Roe (byronroe '@' umich.edu)
Department of Physics University of Michigan
Ann Arbor, MI 48109


Data Set Information:

The submitted file is set up as follows. In the first line is the the number of signal events followed by the number of background events. The signal events come first, followed by the background events. Each line, after the first line has the 50 particle ID variables for one event.


Attribute Information:

50 particle ID variables (real) for each event.


Relevant Papers:

B. Roe et al., 'Boosted Decision Trees, an Alternative to Artificial Neural Networks' <[Web Link]>,
arXiv:physics/0408124, Nucl. Instrum. Meth. A543, 577 (2005).



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00199/MiniBooNE_PID.txt"
,delimiter = '\s+'
,names=['ID_'+str(i) for i in range(1, 51)]
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00199/MiniBooNE_PID.txt"
,delimiter = '\s+'
,names=['ID_'+str(i) for i in range(1, 51)]
)

print(df.info())