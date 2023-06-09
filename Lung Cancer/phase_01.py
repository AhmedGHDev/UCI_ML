import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Lung cancer data; no attribute definitions


Data Set Characteristics:  

Multivariate

Number of Instances:

32

Area:

Life

Attribute Characteristics:

Integer

Number of Attributes:

56

Date Donated

1992-05-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

421477


Source:

Data was published in :

Hong, Z.Q. and Yang, J.Y. "Optimal Discriminant Plane for a Small Number of Samples and Design Method of Classifier on the Plane",
Pattern Recognition, Vol. 24, No. 4, pp. 317-324, 1991.

Donor:

Stefan Aeberhard, stefan '@' coral.cs.jcu.edu.au


Data Set Information:

This data was used by Hong and Young to illustrate the power of the optimal discriminant plane even in ill-posed settings. Applying the KNN method in the resulting plane gave 77% accuracy. However, these results are strongly biased (See Aeberhard's second ref. above, or email to stefan '@' coral.cs.jcu.edu.au). Results obtained by Aeberhard et al. are :

RDA : 62.5%, KNN 53.1%, Opt. Disc. Plane 59.4%

The data described 3 types of pathological lung cancers. The Authors give no information on the individual variables nor on where the data was originally used.

Notes:
- In the original data 4 values for the fifth attribute were -1. These values have been changed to ? (unknown). (*)
- In the original data 1 value for the 39 attribute was 4. This value has been changed to ? (unknown). (*)


Attribute Information:

Attribute 1 is the class label.

All predictive attributes are nominal, taking on integer values 0-3


Relevant Papers:

Hong, Z.Q. and Yang, J.Y. "Optimal Discriminant Plane for a Small Number of Samples and Design Method of Classifier on the Plane", Pattern Recognition, Vol. 24, No. 4, pp. 317-324, 1991.
[Web Link]

Aeberhard, S., Coomans, D, De Vel, O. "Comparisons of Classification Methods in High Dimensional Settings", submitted to Technometrics.

Aeberhard, S., Coomans, D, De Vel, O. "The Dangers of Bias in High Dimensional Settings", submitted to pattern Recognition.


Papers That Cite This Data Set1:


Jinyan Li and Limsoon Wong. Using Rules to Analyse Bio-medical Data: A Comparison between C4.5 and PCL. WAIM. 2003. [View Context].

Manoranjan Dash and Huan Liu. Hybrid Search of Feature Subsets. PRICAI. 1998. [View Context].

Glenn Fung and Sathyakama Sandilya and R. Bharat Rao. Rule extraction from Linear Support Vector Machines. Computer-Aided Diagnosis & Therapy, Siemens Medical Solutions, Inc. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/lung-cancer/lung-cancer.data", names=['class']+['X'+str(i) for i in range(1, 57)])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/lung-cancer/lung-cancer.data", names=['class']+['X'+str(i) for i in range(1, 57)])

print(df.info())