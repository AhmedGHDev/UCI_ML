import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: AutoUniv is an advanced data generator for classifications tasks. The aim is to reflect the nuances and heterogeneity of real data. Data can be generated in .csv, ARFF or C4.5 formats.

Data Set Characteristics:  

Multivariate

Number of Instances:

N/A

Area:

N/A

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

N/A

Date Donated

2010-11-03

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

71740


Source:

AutoUniv was developed by Ray. J. Hickey. Email: ray.j.hickey '@' gmail.com
AutoUniv web-site: http://sites.google.com/site/autouniv/.


Data Set Information:

The user first creates a classification model and then generates classified examples from it.
To create a model, the following are specified: the number of attributes (up to 1000) and their type (discrete or continuous), the number of classes (up to 10), the complexity of the underlying rules and the noise level. AutoUniv then produces a model through a process of constrained randomised search to satisfy the user's requirements. A model can have up to 3000 rules. Rare class models can be designed. A sequence of models can be designed to reflect concept and/or population drift.

AutoUniv creates three text files for a model: a Prolog specification of the model used to generate examples (.aupl); a user-friendly statement of the classification rules in an 'if ... then' format (.aurules); a statistical summary of the main properties of the model, including its Bayes rate (.auprops).


Attribute Information:

Attributes may be discrete with up to 10 values or continuous. A discrete attribute can be nominal with values v1, v2, v3 ... or integer with values 0, 1, 2 , ... .


Relevant Papers:

Marrs, G, Hickey, RJ and Black, MM (2010) Modeling the example life-cycle in an online classification learner. In Proceedings of HaCDAIS 2010: International Workshop on Handling Concept Drift in Adaptive Information Systems.
[Web Link]#proc .

Marrs, G, Hickey, RJ and Black, MM (2010) The Impact of Latency on Online Classification Learning with Concept Drift. In Y. Bi and M.A. Williams (Eds.): KSEM 2010, LNAI 6291, Springer-Verlag, Berlin, pp. 459â€“469.

Hickey, RJ (2007) Structure and Majority Classes in Decision Tree Learning. Journal of Machine Learning Research, 8, pp. 1747-1768.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
from zipfile import ZipFile
import io
from urllib.request import urlopen
import pandas as pd

r = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/00197/AU.zip")
r = r.read()
file = ZipFile(io.BytesIO(r))
df_au8_500 = pd.read_csv(file.open('AU/Data Sets/au8_500.data')
, encoding='latin1'
,names=['Attrib_'+str(i) for i in range(1, 1001)] + ['class']
)

df_au3_25000 = pd.read_csv(file.open('AU/Data Sets/au3_25000.data')
, encoding='latin1'
,names=['Attrib_'+str(i) for i in range(1, 45)] + ['class']
)

print(df_au8_500.info())
print(df_au3_25000.info())
"""

#LOACL
from zipfile import ZipFile
import pandas as pd

file = ZipFile("../ics.uci.edu/ml/machine-learning-databases/00197/AU.zip")
df_au8_500 = pd.read_csv(file.open('AU/Data Sets/au8_500.data')
, encoding='latin1'
,names=['Attrib_'+str(i) for i in range(1, 1001)] + ['class']
)

df_au3_25000 = pd.read_csv(file.open('AU/Data Sets/au3_25000.data')
, encoding='latin1'
,names=['Attrib_'+str(i) for i in range(1, 45)] + ['class']
)

print(df_au8_500.info())
print(df_au3_25000.info())