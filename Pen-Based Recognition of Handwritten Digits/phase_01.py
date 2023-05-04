import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Digit database of 250 samples from 44 writers

Data Set Characteristics:  

Multivariate

Number of Instances:

10992

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

16

Date Donated

1998-07-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

283307


Source:

E. Alpaydin, Fevzi. Alimoglu
Department of Computer Engineering
Bogazici University, 80815 Istanbul Turkey
alpaydin '@' boun.edu.tr


Data Set Information:

We create a digit database by collecting 250 samples from 44 writers. The samples written by 30 writers are used for training, cross-validation and writer dependent testing, and the digits written by the other 14 are used for writer independent testing. This database is also available in the UNIPEN format.

We use a WACOM PL-100V pressure sensitive tablet with an integrated LCD display and a cordless stylus. The input and display areas are located in the same place. Attached to the serial port of an Intel 486 based PC, it allows us to collect handwriting samples. The tablet sends $x$ and $y$ tablet coordinates and pressure level values of the pen at fixed time intervals (sampling rate) of 100 miliseconds.

These writers are asked to write 250 digits in random order inside boxes of 500 by 500 tablet pixel resolution. Subject are monitored only during the first entry screens. Each screen contains five boxes with the digits to be written displayed above. Subjects are told to write only inside these boxes. If they make a mistake or are unhappy with their writing, they are instructed to clear the content of a box by using an on-screen button. The first ten digits are ignored because most writers are not familiar with this type of input devices, but subjects are not aware of this.

In our study, we use only ($x, y$) coordinate information. The stylus pressure level values are ignored. First we apply normalization to make our representation invariant to translations and scale distortions. The raw data that we capture from the tablet consist of integer values between 0 and 500 (tablet input box resolution). The new coordinates are such that the coordinate which has the maximum range varies between 0 and 100. Usually $x$ stays in this range, since most characters are taller than they are wide.

In order to train and test our classifiers, we need to represent digits as constant length feature vectors. A commonly used technique leading to good results is resampling the ( x_t, y_t) points. Temporal resampling (points regularly spaced in time) or spatial resampling (points regularly spaced in arc length) can be used here. Raw point data are already regularly spaced in time but the distance between them is variable. Previous research showed that spatial resampling to obtain a constant number of regularly spaced points on the trajectory yields much better performance, because it provides a better alignment between points. Our resampling algorithm uses simple linear interpolation between pairs of points. The resampled digits are represented as a sequence of T points ( x_t, y_t )_{t=1}^T, regularly spaced in arc length, as opposed to the input sequence, which is regularly spaced in time.

So, the input vector size is 2*T, two times the number of points resampled. We considered spatial resampling to T=8,12,16 points in our experiments and found that T=8 gave the best trade-off between accuracy and complexity.


Attribute Information:

All input attributes are integers in the range 0..100.
The last attribute is the class code 0..9


Relevant Papers:

F. Alimoglu (1996) Combining Multiple Classifiers for Pen-Based Handwritten Digit Recognition, MSc Thesis, Institute of Graduate Studies in Science and Engineering, Bogazici University. [Web Link]
[Web Link]

F. Alimoglu, E. Alpaydin, "Methods of Combining Multiple Classifiers Based on Different Representations for Pen-based Handwriting Recognition," Proceedings of the Fifth Turkish Artificial Intelligence and Artificial Neural Networks Symposium (TAINN 96), June 1996, Istanbul, Turkey. [Web Link]
[Web Link]


Papers That Cite This Data Set1:


Ken Tang and Ponnuthurai N. Suganthan and Xi Yao and A. Kai Qin. Linear dimensionalityreduction using relevance weighted LDA. School of Electrical and Electronic Engineering Nanyang Technological University. 2005. [View Context].

Mikhail Bilenko and Sugato Basu and Raymond J. Mooney. Integrating constraints and metric learning in semi-supervised clustering. ICML. 2004. [View Context].

Fabian Hoti and Lasse Holmström. A semiparametric density estimation approach to pattern classification. Pattern Recognition, 37. 2004. [View Context].

Manoranjan Dash and Huan Liu and Peter Scheuermann and Kian-Lee Tan. Fast hierarchical clustering and its validation. Data Knowl. Eng, 44. 2003. [View Context].

Dennis DeCoste. Anytime Query-Tuned Kernel Machines via Cholesky Factorization. SDM. 2003. [View Context].

Greg Hamerly and Charles Elkan. Learning the k in k-means. NIPS. 2003. [View Context].

Thomas Serafini and G. Zanghirati and Del Zanna and T. Serafini and Gaetano Zanghirati and Luca Zanni. DIPARTIMENTO DI MATEMATICA. Gradient Projection Methods for. 2003. [View Context].

Marina Meila and Michael I. Jordan. Learning with Mixtures of Trees. Journal of Machine Learning Research, 1. 2000. [View Context].

Ethem Alpaydin. Combined 5 x 2 cv F Test for Comparing Supervised Classification Learning Algorithms. Neural Computation, 11. 1999. [View Context].

Georg Thimm and Emile Fiesler. IDIAP Technical report High Order and Multilayer Perceptron Initialization. IEEE Transactions. 1994. [View Context].

Adil M. Bagirov and John Yearwood. A new nonsmooth optimization algorithm for clustering. Centre for Informatics and Applied Optimization, School of Information Technology and Mathematical Sciences, University of Ballarat. [View Context].

Ahmed Hussain Khan and Intensive Care. Multiplier-Free Feedforward Networks. 174. [View Context].

Adil M. Bagirov and Alex Rubinov and A. N. Soukhojak and John Yearwood. Unsupervised and supervised data classification via nonsmooth and global optimization. School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

Georg Thimm and Emile Fiesler. High Order and Multilayer Perceptron Initialization. [View Context].

Adil M. Bagirov and Julien Ugon. An algorithm for computation of piecewise linear function separating two sets. CIAO, School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

Charles Campbell and Nello Cristianini. Simple Learning Algorithms for Training Support Vector Machines. Dept. of Engineering Mathematics. [View Context].

Perry Moerland. Mixtures of latent variable models for density estimation and classification. E S E A R C H R E P R O R T I D I A P D a l l e M o l l e I n s t i t u t e f o r Pe r cep t ua l A r t i f i c i a l Intelligence . [View Context].

Luca Zanni. An Improved Gradient Projection-based Decomposition Technique for Support Vector Machines. Dipartimento di Matematica, Universitdi Modena e Reggio Emilia. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tra" ,names=[str(i) for i in range(1, 16)]+['digit'])

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tes", names=[str(i) for i in range(1, 16)]+['digit'])

print(df_train.info())
print(df_test.info())
"""

#LOACL
import pandas
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tra" ,names=[str(i) for i in range(1, 16)]+['digit'])

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/pendigits/pendigits.tes", names=[str(i) for i in range(1, 16)]+['digit'])

print(df_train.info())
print(df_test.info())