import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data comes from the main door of the CalIt2 building at UCI.


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

10080

Area:

N/A

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

4

Date Donated

2006-12-01

Associated Tasks:

N/A

Missing Values?

No

Number of Web Hits:

66120


Source:

Creator and Maintainer:
Jon Hutchins
UCI
johutchi '@' uci.edu


Data Set Information:

Observations come from 2 data streams (people flow in and out of the building), over 15 weeks, 48 time slices per day (half hour count aggregates).

The purpose is to predict the presence of an event such as a conference in the building that is reflected by unusually high people counts for that day/time period.


Attribute Information:

1. Flow ID: 7 is out flow, 9 is in flow
2. Date: MM/DD/YY
3. Time: HH:MM:SS
4. Count: Number of counts reported for the previous half hour

Rows: Each half hour time slice is represented by 2 rows: one row for the out flow during that time period (ID=7) and one row for the in flow during that time period (ID=9)

Attributes in .events file ("ground truth")
1. Date: MM/DD/YY
2. Begin event time: HH:MM:SS (military)
3. End event time: HH:MM:SS (military)
4. Event name (anonymized)


Relevant Papers:

"Adaptive event detection with time-varying Poisson processes"
A. Ihler, J. Hutchins, and P. Smyth
Proceedings of the 12th ACM SIGKDD Conference (KDD-06), August 2006.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/CalIt2.data"
,names=['ID', 'DATE', 'NAME', 'COUNT']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/event-detection/CalIt2.data"
,names=['ID', 'DATE', 'NAME', 'COUNT']
)

print(df.info())