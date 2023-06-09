import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: MADELON is an artificial dataset, which was part of the NIPS 2003 feature selection challenge. This is a two-class classification problem with continuous input variables. The difficulty is that the problem is multivariate and highly non-linear.


Data Set Characteristics:  

Multivariate

Number of Instances:

4400

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

500

Date Donated

2008-02-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

161135


Source:

Isabelle Guyon
Clopinet
955 Creston Road
Berkeley, CA 90708
isabelle '@' clopinet.com


Data Set Information:

MADELON is an artificial dataset containing data points grouped in 32 clusters placed on the vertices of a five dimensional hypercube and randomly labeled +1 or -1. The five dimensions constitute 5 informative features. 15 linear combinations of those features were added to form a set of 20 (redundant) informative features. Based on those 20 features one must separate the examples into the 2 classes (corresponding to the +-1 labels). We added a number of distractor feature called 'probes' having no predictive power. The order of the features and patterns were randomized.

MADELON -- Positive ex. -- Negative ex. -- Total
Training set -- 1000 -- 1000 -- 2000
Validation set -- 300 -- 300 -- 600
Test set -- 900 -- 900 -- 1800
All -- 2200 -- 2200 -- 4400

Number of variables/features/attributes:
Real: 20
Probes: 480
Total: 500

This dataset is one of five datasets used in the NIPS 2003 feature selection challenge. Our website [Web Link] is still open for post-challenge submissions. Information about other related challenges are found at: [Web Link]. The CLOP package includes sample code to process these data: [Web Link].

All details about the preparation of the data are found in our technical report: Design of experiments for the NIPS 2003 variable selection benchmark, Isabelle Guyon, July 2003, [Web Link] (also included in the dataset archive). Such information was made available only after the end of the challenge.

The data are split into training, validation, and test set. Target values are provided only for the 2 first sets. Test set performance results are obtained by submitting prediction results to: [Web Link].

The data are in the following format:
dataname.param: Parameters and statistics about the data
dataname.feat: Identities of the features (in the order the features are found in the data).
dataname_train.data: Training set (a space-delimited regular matrix, patterns in lines, features in columns).
dataname_valid.data: Validation set.
dataname_test.data: Test set.
dataname_train.labels: Labels (truth values of the classes) for training examples.
dataname_valid.labels: Validation set labels (withheld during the benchmark, but provided now).
dataname_test.labels: Test set labels (withheld, so the data can still be use as a benchmark).


Attribute Information:

We do not provide attribute information, to avoid biasing the feature selection process.


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