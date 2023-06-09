import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data contains general demographic information on internet users in 1997.

Data Set Characteristics:  

Multivariate

Number of Instances:

10104

Area:

Computer

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

72

Date Donated

1999-06-30

Associated Tasks:

N/A

Missing Values?

No

Number of Web Hits:

145927


Source:

Original Owner:

Graphics, Visualization, & Usability Center
College of Computing
Geogia Institute of Technology
Atlanta, GA
http://www.gvu.gatech.edu/gvu/user_surveys/survey-1997-10/

Donor:

Dr Di Cook
Department of Statistics
Iowa State University
http://www.public.iastate.edu/~dicook/


Data Set Information:

This data comes from a survey conducted by the Graphics and Visualization Unit at Georgia Tech October 10 to November 16, 1997. The full details of the survey are available here: [Web Link]

The particular subset of the survey provided here is the "general demographics" of internet users. The data have been recoded as entirely numeric, with an index to the codes described in the "Coding" file.

The full survey is available from the web site above, along with summaries, tables and graphs of their analyses. In addition there is information on other parts of the survey, including technology demographics and web commerce.

The data is stored in an ASCII files with one observation per line. Spaces separate fields.


Attribute Information:

N/A


Relevant Papers:

This data was used in the American Statistical Association Statistical Graphics and Computing Sections 1999 Data Exposition.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/internet_usage-mld/final_general.dat.gz"
,delimiter='\s+'
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 76)]
)
# on line 183 there is 74 fields
# on line 2772 there is 75 fields

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/internet_usage-mld/final_general.dat.gz"
,delimiter='\s+'
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 76)]
)
# on line 183 there is 74 fields
# on line 2772 there is 75 fields

print(df.info())