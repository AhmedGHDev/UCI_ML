import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The goal is to model mutant p53 transcriptional activity (active vs inactive) based on data extracted from biophysical simulations.


Data Set Characteristics:  

Multivariate

Number of Instances:

16772

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

5409

Date Donated

2010-02-09

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

94402


Source:

Richard H. Lathrop, UC Irvine, http://www.ics.uci.edu/~rickl


Data Set Information:

Biophysical models of mutant p53 proteins yield features which can be used to predict p53 transcriptional activity. All class labels are determined via in vivo assays.

K8.data - full dataset, 'K8'

The following files are provided in order to reconstruct this historical subsets of this data set:
K8.instance.tags - provides the precise p53 mutant tag for each instance in the K8.data, for use with the historical definition files:
K1.def - defines instances in the 'K1' set.
K2.def - defines instances in the 'K2' set.
K3.def - defines instances in the 'K3' set.
K4.def - defines instances in the 'K4' set.
K5.def - defines instances in the 'K5' set.
K6.def - defines instances in the 'K6' set.
K7.def - defines instances in the 'K7' set.
K8.def - defines instances in the 'K8' (full) set.


Attribute Information:

There are a total of 5409 attributes per instance.
Attributes 1-4826 represent 2D electrostatic and surface based features.
Attributes 4827-5408 represent 3D distance based features.
Attribute 5409 is the class attribute, which is either active or inactive.
The class labels are to be interpreted as follows: 'active' represents transcriptonally competent, active p53 whereas the 'inactive' label represents cancerous, inactive p53. Class labels are determined experimentally.

More information is provided in the relevant papers cited.


Relevant Papers:

Danziger, S.A., Baronio, R., Ho, L., Hall, L., Salmon, K., Hatfield, G.W., Kaiser, P., and Lathrop, R.H. (2009) Predicting Positive p53 Cancer Rescue Regions Using Most Informative Positive (MIP) Active Learning, PLOS Computational Biology, 5(9), e1000498

Danziger, S.A., Zeng, J., Wang, Y., Brachmann, R.K. and Lathrop, R.H. (2007) Choosing where to look next in a mutation sequence space: Active Learning of informative p53 cancer rescue mutants, Bioinformatics, 23(13), 104-114.

Danziger, S.A., Swamidass, S.J., Zeng, J., Dearth, L.R., Lu, Q., Chen, J.H., Cheng, J., Hoang, V.P., Saigo, H., Luo, R., Baldi, P., Brachmann, R.K. and Lathrop, R.H. (2006) Functional census of mutation sequence spaces: the example of p53 cancer rescue mutants, IEEE/ACM transactions on computational biology and bioinformatics / IEEE, ACM, 3, 114-125.



Citation Request:

If you use this dataset, please cite the relevant papers above. Thank you.
"""

#FROM URL
"""
from zipfile import ZipFile
import io
from urllib.request import urlopen

# ['p53_old_2010/', 'p53_old_2010/K2.def', 'p53_old_2010/K5.def', 'p53_old_2010/p53.names', 'p53_old_2010/K8.data', 'p53_old_2010/K4.def', 'p53_old_2010/K3.def', 'p53_old_2010/K8.instance.tags', 'p53_old_2010/K7.def', 'p53_old_2010/K6.def', 'p53_old_2010/K1.def', 'p53_old_2010/K8.def']

r = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/p53/p53_old_2010.zip").read()
file = ZipFile(io.BytesIO(r))
df_old = pd.read_csv(file.open('p53_old_2010/K8.data')
, encoding='latin1'
)

print(df_old.info())
print(df_old.head())
del df_old

# # ['p53_old_2010/', 'p53_old_2010/K2.def', 'p53_old_2010/K5.def', 'p53_old_2010/p53.names', 'p53_old_2010/K8.data', 'p53_old_2010/K4.def', 'p53_old_2010/K3.def', 'p53_old_2010/K8.instance.tags', 'p53_old_2010/K7.def', 'p53_old_2010/K6.def', 'p53_old_2010/K1.def', 'p53_old_2010/K8.def']

r = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/p53/p53_new_2012.zip").read()
file = ZipFile(io.BytesIO(r))
df_new = pd.read_csv(file.open('Data Sets/K9.data')
, encoding='latin1'
)

print(df_new.info())
print(df_new.head())
del df_new
"""

#LOACL
from zipfile import ZipFile
import io
from urllib.request import urlopen

# ['p53_old_2010/', 'p53_old_2010/K2.def', 'p53_old_2010/K5.def', 'p53_old_2010/p53.names', 'p53_old_2010/K8.data', 'p53_old_2010/K4.def', 'p53_old_2010/K3.def', 'p53_old_2010/K8.instance.tags', 'p53_old_2010/K7.def', 'p53_old_2010/K6.def', 'p53_old_2010/K1.def', 'p53_old_2010/K8.def']

r = urlopen("../ics.uci.edu/ml/machine-learning-databases/p53/p53_old_2010.zip").read()
file = ZipFile(io.BytesIO(r))
df_old = pd.read_csv(file.open('p53_old_2010/K8.data')
, encoding='latin1'
)

print(df_old.info())
print(df_old.head())
del df_old

# # ['p53_old_2010/', 'p53_old_2010/K2.def', 'p53_old_2010/K5.def', 'p53_old_2010/p53.names', 'p53_old_2010/K8.data', 'p53_old_2010/K4.def', 'p53_old_2010/K3.def', 'p53_old_2010/K8.instance.tags', 'p53_old_2010/K7.def', 'p53_old_2010/K6.def', 'p53_old_2010/K1.def', 'p53_old_2010/K8.def']

r = urlopen("../ics.uci.edu/ml/machine-learning-databases/p53/p53_new_2012.zip").read()
file = ZipFile(io.BytesIO(r))
df_new = pd.read_csv(file.open('Data Sets/K9.data')
, encoding='latin1'
)

print(df_new.info())
print(df_new.head())
del df_new
