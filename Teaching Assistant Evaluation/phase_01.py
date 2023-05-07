import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The data consist of evaluations of teaching performance; scores are "low", "medium", or "high"

Data Set Characteristics:  

Multivariate

Number of Instances:

151

Area:

N/A

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

5

Date Donated

1997-06-07

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

204411


Source:

Collector:

Wei-Yin Loh (Department of Statistics, UW-Madison)

Donor:

Tjen-Sien Lim (limt '@' stat.wisc.edu)


Data Set Information:

The data consist of evaluations of teaching performance over three regular semesters and two summer semesters of 151 teaching assistant (TA) assignments at the Statistics Department of the University of Wisconsin-Madison. The scores were divided into 3 roughly equal-sized categories ("low", "medium", and "high") to form the class variable.


Attribute Information:

1. Whether of not the TA is a native English speaker (binary); 1=English speaker, 2=non-English speaker
2. Course instructor (categorical, 25 categories)
3. Course (categorical, 26 categories)
4. Summer or regular semester (binary) 1=Summer, 2=Regular
5. Class size (numerical)
6. Class attribute (categorical) 1=Low, 2=Medium, 3=High


Relevant Papers:

Loh, W.-Y. & Shih, Y.-S. (1997). Split Selection Methods for Classification Trees, Statistica Sinica 7: 815-840.
[Web Link]

Lim, T.-S., Loh, W.-Y. & Shih, Y.-S. (1999). A Comparison of Prediction Accuracy, Complexity, and Training Time of Thirty-three Old and New Classification Algorithms. Machine Learning. ([Web Link] or [Web Link])
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/tae/tae.data"
,names=['native_English_speaker', 'Course_instructor', 'Course', 'Summer_or_regular_semester', 'Class_size', 'Class']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/tae/tae.data"
,names=['native_English_speaker', 'Course_instructor', 'Course', 'Summer_or_regular_semester', 'Class_size', 'Class']
)

print(df.info())