import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Amazon's InfoSec is getting smarter about the way Access data is leveraged. This is an anonymized sample of access provisioned within the company.

Data Set Characteristics:  

Time-Series, Domain-Theory

Number of Instances:

30000

Area:

Business

Attribute Characteristics:

N/A

Number of Attributes:

20000

Date Donated

2011-09-13

Associated Tasks:

Regression, Clustering, Causal-Discovery

Missing Values?

N/A

Number of Web Hits:

254922


Source:

Dataset creator and donator: Ken Montanez email: kenmonta[at]cal.berkeley.edu institution: Information Security, Amazon Corp.


Data Set Information:

This is a sparse data set, less than 10% of the attributes are used for each sample. The link is to a '*.tgz' file which contains two files:
[amzn-anon-access-samples-2.0.csv] this file contains the access for users
[amzn-anon-access-samples-history-2.0.csv] this file contains the access history for a given user


Attribute Information:

__amzn-anon-access-samples-2.0.csv__
This is a sparse data set containing users and their assigned access. The file contains 4 categories of attributes.
1) [PERSON_{ATTRIBUTE}] This category describes the 'user' who was given access. The [PERSON_ID] column is the primary key column for the file. There is one row per user.
PERSON_ID: id of the user
PERSON_MGR_ID: id of the user's manager
PERSON_ROLLUP_1: user grouping id
PERSON_ROLLUP_2: user grouping id
PERSON_ROLLUP_3: user grouping id
PERSON_DEPTNAME: department desciption id
PERSON_LOCATION: region id
PERSON_BUSINESS_TITLE: title id
PERSON_BUSINESS_TITLE_DETAIL: description id
PERSON_JOB_CODE: job code id
PERSON_COMPANY: company id
PERSON_JOB_FAMILY: job family id

2) [RESOURCE_{ID}] This category of attributes are the resources that a users can possibly have access to. A user will have a 1 in this column if the have access to it otherwise it will be 0.

3) [GROUP_{ID}] - This category of attributes are the groups that a users can possibly have access to. A user will have a 1 in this column if the have access to it otherwise it will be 0.

4) [SYSTEM_SUPPORT_{ID}] - This category of attributes are the system that a user can possibly be supporting. A user will have a 1 in this column if the have can possibly be supporting it, otherwise it will be 0.

__amzn-anon-access-samples-history-2.0.csv__
Permissions Time series data. Here is a short description of the columns:
ACTION: either 'remove_access' or 'add_access'
TARGET_NAME: either the {RESOURCE_ID} or {GROUP_ID}
LOGIN: the id of the user that is obtaining or losing access
REQUEST_DATE: YYYY-MM-DD HH:MM:SS
AUTHORIZATION_DATE: YYYY-MM-DD HH:MM:SS


Relevant Papers:

N/A



Citation Request:

Please refer to the Machine Learning Repository's citation policy.
"""