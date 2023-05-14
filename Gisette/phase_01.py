import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: GISETTE is a handwritten digit recognition problem. The problem is to separate the highly confusible digits '4' and '9'. This dataset is one of five datasets of the NIPS 2003 feature selection challenge.


Data Set Characteristics:  

Multivariate

Number of Instances:

13500

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

5000

Date Donated

2008-02-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

141835


Source:

a. Original owners
The data set was constructed from the MNIST data that is made available by Yann LeCun and Corinna Cortes at http://yann.lecun.com/exdb/mnist/.

b. Donor of database
This version of the database was prepared for the NIPS 2003 variable and feature selection benchmark by Isabelle Guyon, 955 Creston Road, Berkeley, CA 94708, USA (isabelle '@' clopinet.com).


Data Set Information:

The digits have been size-normalized and centered in a fixed-size image of dimension 28x28. The original data were modified for the purpose of the feature selection challenge. In particular, pixels were samples at random in the middle top part of the feature containing the information necessary to disambiguate 4 from 9 and higher order features were created as products of these pixels to plunge the problem in a higher dimensional feature space. We also added a number of distractor features called 'probes' having no predictive power. The order of the features and patterns were randomized.

GISETTE -- Positive ex. -- Negative ex. -- Total
Training set -- 3000 -- 3000 -- 6000
Validation set -- 500 -- 500 -- 1000
Test set -- 3250 -- 3250 -- 6500
All -- 6750 -- 6750 -- 13500

Number of variables/features/attributes:
Real: 2500
Probes: 2500
Total: 5000

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