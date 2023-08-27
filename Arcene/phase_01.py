import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: ARCENE's task is to distinguish cancer versus normal patterns from mass-spectrometric data. This is a two-class classification problem with continuous input variables. This dataset is one of 5 datasets of the NIPS 2003 feature selection challenge.


Data Set Characteristics:  

Multivariate

Number of Instances:

900

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

10000

Date Donated

2008-02-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

163414


Source:

a. Original owners
The data were obtained from two sources: The National Cancer Institute (NCI) and the Eastern Virginia Medical School (EVMS). All the data consist of mass-spectra obtained with the SELDI technique. The samples include patients with cancer (ovarian or prostate cancer), and healthy or control patients.

b. Donor of database
This version of the database was prepared for the NIPS 2003 variable and feature selection benchmark by Isabelle Guyon, 955 Creston Road, Berkeley, CA 94708, USA (isabelle '@' clopinet.com).


Data Set Information:

ARCENE was obtained by merging three mass-spectrometry datasets to obtain enough training and test data for a benchmark. The original features indicate the abundance of proteins in human sera having a given mass value. Based on those features one must separate cancer patients from healthy patients. We added a number of distractor feature called 'probes' having no predictive power. The order of the features and patterns were randomized.

ARCENE -- Positive ex. -- Negative ex. -- Total
Training set -- 44 -- 56 -- 100
Validation set -- 44 -- 56 -- 100
Test set -- 310 -- 390 -- 700
All -- 398 -- 502 -- 900

Number of variables/features/attributes:
Real: 7000
Probes: 3000
Total: 10000

This dataset is one of five datasets used in the NIPS 2003 feature selection challenge. Our website [Web Link] is still open for post-challenge submissions. Information about other related challenges are found at: [Web Link]. The CLOP package includes sample code to process these data: [Web Link].

All details about the preparation of the data are found in our technical report: Design of experiments for the NIPS 2003 variable selection benchmark, Isabelle Guyon, July 2003, [Web Link] (also included in the dataset archive). Such information was made available only after the end of the challenge.

The data are split into training, validation, and test set. Target values are provided only for the 2 first sets. Test set performance results are obtained by submitting prediction results to: [Web Link].

The data are in the following format:
dataname.param: Parameters and statistics about the data
dataname.feat: Identities of the features (withheld, to avoid biasing feature selection).
dataname_train.data: Training set (a coma delimited regular matrix, patterns in lines, features in columns).
dataname_valid.data: Validation set.
dataname_test.data: Test set.
dataname_train.labels: Labels (truth values of the classes) for training examples.
dataname_valid.labels: Validation set labels (withheld during the benchmark, but provided now).
dataname_test.labels: Test set labels (withheld, so the data can still be use as a benchmark).


Attribute Information:

We do not provide attribute information to avoid biasing the feature selection process.


Relevant Papers:

The best challenge entrants wrote papers collected in the book:
Isabelle Guyon, Steve Gunn, Masoud Nikravesh, Lofti Zadeh (Eds.), Feature Extraction, Foundations and Applications. Studies in Fuzziness and Soft Computing. Physica-Verlag, Springer. [Web Link]

See also:
Isabelle Guyon, et al, 2007. Competitive baseline methods set new standards for the NIPS 2003 feature selection benchmark. Pattern Recognition Letters 28 (2007) 14381444.
and the associated technical report:
Isabelle Guyon, et al. 2006. Feature selection with the CLOP package. Technical Report. [Web Link].



Citation Request:

Isabelle Guyon, Steve R. Gunn, Asa Ben-Hur, Gideon Dror, 2004. Result analysis of the NIPS 2003 feature selection challenge. In: NIPS. [Web Link].
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_train.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

df_valid = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_valid.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_test.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

print(df_train.info())
print(df_valid.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_train.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

df_valid = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_valid.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/arcene/ARCENE/arcene_test.data"
,delimiter='\s+'
,names=['X_'+str(i) for i in range(1, 10001)]
)

print(df_train.info())
print(df_valid.info())
print(df_test.info())