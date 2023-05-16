import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Prediction of the release year of a song from audio features. Songs are mostly western, commercial tracks ranging from 1922 to 2011, with a peak in the year 2000s.


Data Set Characteristics:  

Multivariate

Number of Instances:

515345

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

90

Date Donated

2011-02-07

Associated Tasks:

Regression

Missing Values?

N/A

Number of Web Hits:

229883


Source:

This data is a subset of the Million Song Dataset:
http://labrosa.ee.columbia.edu/millionsong/
a collaboration between LabROSA (Columbia University) and The Echo Nest.
Prepared by T. Bertin-Mahieux <tb2332 '@' columbia.edu>


Data Set Information:

You should respect the following train / test split:
train: first 463,715 examples
test: last 51,630 examples
It avoids the 'producer effect' by making sure no song
from a given artist ends up in both the train and test set.


Attribute Information:

90 attributes, 12 = timbre average, 78 = timbre covariance
The first value is the year (target), ranging from 1922 to 2011.
Features extracted from the 'timbre' features from The Echo Nest API.
We take the average and covariance over all 'segments', each segment
being described by a 12-dimensional timbre vector.


Relevant Papers:

see the website: [Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
import pandas as pd
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip"
,compression="zip"
,names=['year'] + ['timber_average_'+str(i) for i in range(1, 13)] + ['timber_covariance_'+str(i) for i in range(1, 79)]
)

print(df.info())
"""

#LOACL
# the file is 200 MB
import pandas as pd
df = pd.read_csv("..ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip"
,compression="zip"
,names=['year'] + ['timber_average_'+str(i) for i in range(1, 13)] + ['timber_covariance_'+str(i) for i in range(1, 79)]
)

print(df.info())