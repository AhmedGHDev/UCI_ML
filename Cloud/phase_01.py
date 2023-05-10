import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Little Documentation


Data Set Characteristics:  

Multivariate

Number of Instances:

1024

Area:

Physical

Attribute Characteristics:

Real

Number of Attributes:

10

Date Donated

1989-08-03

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

170710


Source:

Philippe Collard
California Space Institute
A-021, UCSD
La Jolla, CA 92093
(619)534-6369


Data Set Information:

The data sets we propose to analyse are constituted of 1024 vectors, each vector includes 10 parameters. You can think of it as a 1024*10 matrix. To produce these vectors, we proceed as follows:

1. we start with two 512*512 AVHRR images (1 in the visible, 1 in the IR)
2. each images is divided in super-pixels 16*16 and in each super-pixel we compute a set of parameters:
(a) visible: mean, max, min, mean distribution, contrast, entropy, second angular momentum
(b) IR: mean, max, min

The set of 10 parameters we picked to form the vectors is a compromised between various constraints. Actually we are still working on the choice of parameters for the data vectors. The data set I send you has not been normalized. The normalization of the data set is required by our classification scheme but that may not be true for yours. To normalize the data we compute the mean and standard deviation for each parameter on the entire data set then for each parameter of each vector we compute:

Norm. value = (un-norm value - mean)/SD

where

mean = mean value for this particular parameter over the data set
SD = standard deviation .....


Attribute Information:

N/A


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Kristiaan Pelckmans and Jos De Brabanter and J. A. K Suykens and Bart De Moor and K. U. Leuven - ESAT. The Differogram: Non-parametric Noise Variance Estimation and its Use for Model Selection. SCDSISTA. 2004. [View Context].

Stephen D. Bay. Nearest neighbor classification from multiple feature subsets. Intell. Data Anal, 3. 1999. [View Context].

Cesar Guerra-Salcedo and Stephen Chen and Darrell Whitley and Sarah Smith. Fast and Accurate Feature Selection Using Hybrid Genetic Strategies. Department of Computer Science Colorado State University. [View Context].

C. esar and Cesar Guerra-Salcedo and Darrell Whitley. Feature Selection Mechanisms for Ensemble Creation : A Genetic Search Perspective. Department of Computer Science Colorado State University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""