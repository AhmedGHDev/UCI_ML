import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Anonymized 120-day subset of the ICML-09 URL data containing 2.4 million examples and 3.2 million features.


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

2396130

Area:

Computer

Attribute Characteristics:

Integer, Real

Number of Attributes:

3231961

Date Donated

2009-10-15

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

161846


Source:

'Identifying Malicious URLs: An Application of Large-Scale Online Learning' (ICML-09)
Justin Ma, Lawrence K. Saul, Stefan Savage, Geoffrey M. Voelker

Please visit [http://sysnet.ucsd.edu/projects/url/] for more information.


Data Set Information:

Uncompressing the archive url_svmlight.tar.gz will yield a directory url_svmlight/ containing the following files:
* FeatureTypes --- A text file list of feature indices that correspond to real-valued features.
* DayX.svm (where X is an integer from 0 to 120) --- The data for day X in SVM-light format. A label of +1 corresponds to a malicious URL and -1 corresponds to a benign URL.


Attribute Information:

Attributes are anonymized, but correspond to lexical and host-based features gathered for each URL.


Relevant Papers:

N/A



Citation Request:

If you use this data set in published work, please cite the ICML-09 paper in which it was first introduced and described:

Justin Ma, Lawrence K. Saul, Stefan Savage, and Geoffrey M. Voelker,
Identifying Suspicious URLs: An Application of Large-Scale Online Learning
Proceedings of the International Conference on Machine Learning (ICML), pages 681-688, Montreal, Quebec, June 2009.
"""