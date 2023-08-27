import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: DEXTER is a text classification problem in a bag-of-word representation. This is a two-class classification problem with sparse continuous input variables. This dataset is one of five datasets of the NIPS 2003 feature selection challenge.


Data Set Characteristics:  

Multivariate

Number of Instances:

2600

Area:

N/A

Attribute Characteristics:

Integer

Number of Attributes:

20000

Date Donated

2008-02-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

123598


Source:

a. Original owners
The original data set we used is a subset of the well-known Reuters text categorization benchmark. The data was originally collected and labeled by Carnegie Group, Inc. and Reuters, Ltd. in the course of developing the CONSTRUE text categorization system. It is hosted by the UCI KDD repository: http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html. David D. Lewis is hosting valuable resources about this data (see http://www.daviddlewis.com/resources/testcollections/reuters21578/). We used the “corporate acquisition” text classification class pre-processed by Thorsten Joachims <thorsten '@' joachims.org>. The data is one of the examples of the software package SVM-Light., see http://svmlight.joachims.org/. The example can be downloaded from ftp://ftp-ai.cs.uni-dortmund.de/pub/Users/thorsten/svm_light/examples/example1.tar.gz.

b. Donor of database
This version of the database was prepared for the NIPS 2003 variable and feature selection benchmark by Isabelle Guyon, 955 Creston Road, Berkeley, CA 94708, USA (isabelle '@' clopinet.com).


Data Set Information:

The original data were formatted by Thorsten Joachims in the “bag-of-words” representation. There were 9947 features (of which 2562 are always zeros for all the examples) representing frequencies of occurrence of word stems in text. The task is to learn which Reuters articles are about 'corporate acquisitions'. We added a number of distractor feature called 'probes' having no predictive power. The order of the features and patterns were randomized.

DEXTER -- Positive ex. -- Negative ex. -- Total
Training set --150 -- 150 -- 300
Validation set -- 150 -- 150 -- 300
Test set -- 1000 -- 1000 -- 2000
All -- 1300 -- 1300 -- 2600

Number of variables/features/attributes:
Real: 9947
Probes: 10053
Total: 20000

This dataset is one of five datasets used in the NIPS 2003 feature selection challenge. Our website [Web Link] is still open for post-challenge submissions. Information about other related challenges are found at: [Web Link]. The CLOP package includes sample code to process these data: [Web Link].

All details about the preparation of the data are found in our technical report: Design of experiments for the NIPS 2003 variable selection benchmark, Isabelle Guyon, July 2003, [Web Link] (also included in the dataset archive). Such information was made available only after the end of the challenge.

The data are split into training, validation, and test set. Target values are provided only for the 2 first sets. Test set performance results are obtained by submitting prediction results to: [Web Link].

The data are in the following format:
dataname.param: Parameters and statistics about the data
dataname.feat: Identities of the features (withheld, to avoid biasing feature selection).
dataname_train.data: Training set (a sparse matrix, patterns in lines, features in columns: feature number followed by value).
dataname_valid.data: Validation set.
dataname_test.data: Test set.
dataname_train.labels: Labels (truth values of the classes) for training examples.
dataname_valid.labels: Validation set labels (withheld during the benchmark, but provided now).
dataname_test.labels: Test set labels (withheld, so the data can still be use as a benchmark).


Attribute Information:

We do not provide feature information to avoid biasing feature selection.


Relevant Papers:

The best challenge entrants wrote papers collected in the book:
Isabelle Guyon, Steve Gunn, Masoud Nikravesh, Lofti Zadeh (Eds.), Feature Extraction, Foundations and Applications. Studies in Fuzziness and Soft Computing. Physica-Verlag, Springer. [Web Link]

See also:
Isabelle Guyon, et al, 2007. Competitive baseline methods set new standards for the NIPS 2003 feature selection benchmark. Pattern Recognition Letters 28 (2007) 1438–1444.
and the associated technical report:
Isabelle Guyon, et al. 2006. Feature selection with the CLOP package. Technical Report. [Web Link].



Citation Request:

Isabelle Guyon, Steve R. Gunn, Asa Ben-Hur, Gideon Dror, 2004. Result analysis of the NIPS 2003 feature selection challenge. In: NIPS. [Web Link].
"""