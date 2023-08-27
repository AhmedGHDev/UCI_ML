import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data set used in the CoIL 2000 Challenge contains information on customers of an insurance company. The data consists of 86 variables and includes product usage data and socio-demographic data

Data Set Characteristics:  

Multivariate

Number of Instances:

9000

Area:

Social

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

86

Date Donated

2000-07-03

Associated Tasks:

Regression, Description

Missing Values?

No

Number of Web Hits:

196235


Source:

Original Owner and Donor:

Peter van der Putten
Sentient Machine Research
Baarsjesweg 224
1058 AA Amsterdam
The Netherlands
+31 20 6186927
pvdputten '@' hotmail.com, putten '@' liacs.nl

TIC Benchmark Homepage: http://www.liacs.nl/~putten/library/cc2000/


Data Set Information:

Information about customers consists of 86 variables and includes product usage data and socio-demographic data derived from zip area codes. The data was supplied by the Dutch data mining company Sentient Machine Research and is based on a real world business problem. The training set contains over 5000 descriptions of customers, including the information of whether or not they have a caravan insurance policy. A test set contains 4000 customers of whom only the organisers know if they have a caravan insurance policy.

The data dictionary ([Web Link]) describes the variables used and their values.

Note: All the variables starting with M are zipcode variables. They give information on the distribution of that variable, e.g. Rented house, in the zipcode area of the customer.

One instance per line with tab delimited fields.

TICDATA2000.txt: Dataset to train and validate prediction models and build a description (5822 customer records). Each record consists of 86 attributes, containing sociodemographic data (attribute 1-43) and product ownership (attributes 44-86).The sociodemographic data is derived from zip codes. All customers living in areas with the same zip code have the same sociodemographic attributes. Attribute 86, "CARAVAN:Number of mobile home policies", is the target variable.

TICEVAL2000.txt: Dataset for predictions (4000 customer records). It has the same format as TICDATA2000.txt, only the target is missing. Participants are supposed to return the list of predicted targets only. All datasets are in tab delimited format. The meaning of the attributes and attribute values is given below.

TICTGTS2000.txt Targets for the evaluation set.


Attribute Information:

N/A


Relevant Papers:

P. van der Putten and M. van Someren (eds). CoIL Challenge 2000: The Insurance Company Case. Published by Sentient Machine Research, Amsterdam. Also a Leiden Institute of Advanced Computer Science Technical Report 2000-09. June 22, 2000.
[Web Link]


Papers That Cite This Data Set1:


Bianca Zadrozny and Charles Elkan. Transforming classifier scores into accurate multiclass probability estimates. KDD. 2002. [View Context].

Stephen D. Bay and Dennis F. Kibler and Michael J. Pazzani and Padhraic Smyth. The UCI KDD Archive of Large Data Sets for Data Mining Research and Experimentation. SIGKDD Explorations, 2. 2000. [View Context].

Stefan R uping. A Simple Method For Estimating Conditional Probabilities For SVMs. CS Department, AI Unit Dortmund University. [View Context].



Citation Request:

Data is (c) Sentient Machine Research 2000
This dataset is owned and supplied by the Dutch datamining company Sentient Machine Research, and is based on real world business data. You are allowed to use this dataset and accompanying information for non commercial research and education purposes only. It is explicitly not allowed to use this dataset for commercial education or demonstration purposes.

Please cite/acknowledge:

P. van der Putten and M. van Someren (eds) . CoIL Challenge 2000: The Insurance Company Case. Published by Sentient Machine Research, Amsterdam. Also a Leiden Institute of Advanced Computer Science Technical Report 2000-09. June 22, 2000.
[Web Link]
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/tic-mld/ticdata2000.txt"
,delimiter='\s+'
,names=['SG_'+str(i) for i in range(1, 44)]+['PO_'+str(i) for i in range(1,44)]
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/tic-mld/ticeval2000.txt"
,delimiter='\s+'
,names=['SG_'+str(i) for i in range(1, 44)]+['PO_'+str(i) for i in range(1,43)]
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/tic-mld/ticdata2000.txt"
,delimiter='\s+'
,names=['SG_'+str(i) for i in range(1, 44)]+['PO_'+str(i) for i in range(1,44)]
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/tic-mld/ticeval2000.txt"
,delimiter='\s+'
,names=['SG_'+str(i) for i in range(1, 44)]+['PO_'+str(i) for i in range(1,43)]
)

print(df_train.info())
print(df_test.info())