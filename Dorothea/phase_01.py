import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: DOROTHEA is a drug discovery dataset. Chemical compounds represented by structural molecular features must be classified as active (binding to thrombin) or inactive. This is one of 5 datasets of the NIPS 2003 feature selection challenge.


Data Set Characteristics:  

Multivariate

Number of Instances:

1950

Area:

Life

Attribute Characteristics:

Integer

Number of Attributes:

100000

Date Donated

2008-02-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

132042


Source:

a. Original owners
The dataset with which DOROTHEA was created is one of the KDD (Knowledge Discovery in Data Mining) Cup 2001. The original dataset and papers of the winners of the competition are available at: http://www.cs.wisc.edu/~dpage/kddcup2001/. DuPont Pharmaceuticals graciously provided this data set for the KDD Cup 2001 competition. All publications referring to analysis of this data set should acknowledge DuPont Pharmaceuticals Research Laboratories and KDD Cup 2001.

b. Donor of database
This version of the database was prepared for the NIPS 2003 variable and feature selection benchmark by Isabelle Guyon, 955 Creston Road, Berkeley, CA 94708, USA (isabelle '@' clopinet.com).


Data Set Information:

Drugs are typically small organic molecules that achieve their desired activity by binding to a target site on a receptor. The first step in the discovery of a new drug is usually to identify and isolate the receptor to which it should bind, followed by testing many small molecules for their ability to bind to the target site. This leaves researchers with the task of determining what separates the active (binding) compounds from the inactive (non-binding) ones. Such a determination can then be used in the design of new compounds that not only bind, but also have all the other properties required for a drug (solubility, oral absorption, lack of side effects, appropriate duration of action, toxicity, etc.).
The original data were modified for the purpose of the feature selection challenge. In particular, we added a number of distractor feature called 'probes' having no predictive power. The order of the features and patterns were randomized.

DOROTHEA -- Positive ex. -- Negative ex. -- Total
Training set -- 78 -- 722 -- 800
Validation set -- 34 -- 316 -- 350
Test set -- 78 -- 722 -- 800
All -- 190 -- 1760 -- 1950

We mapped Active compounds to the target value +1 (positive examples) and Inactive compounds to the target value –1 (negative examples).

Number of variables/features/attributes:
Real: 50000
Probes: 50000
Total: 100000

This dataset is one of five datasets used in the NIPS 2003 feature selection challenge. Our website [Web Link] is still open for post-challenge submissions. Information about other related challenges are found at: [Web Link]. The CLOP package includes sample code to process these data: [Web Link].

All details about the preparation of the data are found in our technical report: Design of experiments for the NIPS 2003 variable selection benchmark, Isabelle Guyon, July 2003, [Web Link] (also included in the dataset archive). Such information was made available only after the end of the challenge.

The data are split into training, validation, and test set. Target values are provided only for the 2 first sets. Test set performance results are obtained by submitting prediction results to: [Web Link].

The data are in the following format:
dataname.param: Parameters and statistics about the data
dataname.feat: Identities of the features (withheld, to avoid biasing feature selection).
dataname_train.data: Training set (a sparse binary matrix, patterns in lines, features in columns: the number of the non-zero features are provided).
dataname_valid.data: Validation set.
dataname_test.data: Test set.
dataname_train.labels: Labels (truth values of the classes) for training examples.
dataname_valid.labels: Validation set labels (withheld during the benchmark, but provided now).
dataname_test.labels: Test set labels (withheld, so the data can still be use as a benchmark).


Attribute Information:

We do not provide attribute information to avoid biasing feature selection.


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