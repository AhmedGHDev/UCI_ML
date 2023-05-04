import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: A set of three artificial domains over the same attribute space; Used to test a wide range of induction algorithms

Data Set Characteristics:  

Multivariate

Number of Instances:

432

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

7

Date Donated

1992-10-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

242430


Source:

Donor:

Sebastian Thrun
School of Computer Science
Carnegie Mellon University
Pittsburgh, PA 15213, USA
E-mail: thrun '@' cs.cmu.edu


Data Set Information:

The MONK's problem were the basis of a first international comparison of learning algorithms. The result of this comparison is summarized in "The MONK's Problems - A Performance Comparison of Different Learning algorithms" by S.B. Thrun, J. Bala, E. Bloedorn, I. Bratko, B. Cestnik, J. Cheng, K. De Jong, S. Dzeroski, S.E. Fahlman, D. Fisher, R. Hamann, K. Kaufman, S. Keller, I. Kononenko, J. Kreuziger, R.S. Michalski, T. Mitchell, P. Pachowicz, Y. Reich H. Vafaie, W. Van de Welde, W. Wenzel, J. Wnek, and J. Zhang has been published as Technical Report CS-CMU-91-197, Carnegie Mellon University in Dec. 1991.

One significant characteristic of this comparison is that it was performed by a collection of researchers, each of whom was an advocate of the technique they tested (often they were the creators of the various methods). In this sense, the results are less biased than in comparisons performed by a single person advocating a specific learning method, and more accurately reflect the generalization behavior of the learning techniques as applied by knowledgeable users.

There are three MONK's problems. The domains for all MONK's problems are the same (described below). One of the MONK's problems has noise added. For each problem, the domain has been partitioned into a train and test set.


Attribute Information:

1. class: 0, 1
2. a1: 1, 2, 3
3. a2: 1, 2, 3
4. a3: 1, 2
5. a4: 1, 2, 3
6. a5: 1, 2, 3, 4
7. a6: 1, 2
8. Id: (A unique symbol for each instance)


Relevant Papers:

Wnek, J., "Hypothesis-driven Constructive Induction," PhD dissertation, School of Information Technology and Engineering, Reports of Machine Learning and Inference Laboratory, MLI 93-2, Center for Artificial Intelligence, George Mason University, March 1993.
[Web Link]

Wnek, J. and Michalski, R.S., "Comparing Symbolic and Subsymbolic Learning: Three Studies," in Machine Learning: A Multistrategy Approach, Vol. 4., R.S. Michalski and G. Tecuci (Eds.), Morgan Kaufmann, San Mateo, CA, 1993.
[Web Link]

See File: thrun.comparison.ps.Z


Papers That Cite This Data Set1:


Jianbin Tan and David L. Dowe. MML Inference of Decision Graphs with Multi-way Joins and Dynamic Attributes. Australian Conference on Artificial Intelligence. 2003. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Ensembles of Similarity-based Models. Intelligent Information Systems. 2001. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

Alexey Tsymbal and Seppo Puuronen and Vagan Y. Terziyan. Arbiter Meta-Learning with Dynamic Selection of Classifiers and Its Experimental Investigation. ADBIS. 1999. [View Context].

Blai Bonet and Hector Geffner. Learning Sorting and Decision Trees with POMDPs. ICML. 1998. [View Context].

Jan C. Bioch and D. Meer and Rob Potharst. Bivariate Decision Trees. PKDD. 1997. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Geoffrey I. Webb. OPUS: An Efficient Admissible Algorithm for Unordered Search. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

Ron Kohavi and Brian Frasca. Useful Feature Subsets and Rough Set Reducts. the Third International Workshop on Rough Sets and Soft Computing. [View Context].

Chotirat Ann and Dimitrios Gunopulos. Scaling up the Naive Bayesian Classifier: Using Decision Trees for Feature Selection. Computer Science Department University of California. [View Context].

Wl odzisl/aw Duch and Rafal Adamczak and Krzysztof Grabczewski and Norbert Jankowski. Control and Cybernetics. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Ron Kohavi and Dan Sommerfield. To Appear in KDD-98 Targeting Business Users with Decision Table Classifiers. Data Mining and Visualization Silicon Graphics, Inc. [View Context].

Wl odzisl and Rafal Adamczak and Krzysztof Grabczewski and Grzegorz Zal. A hybrid method for extraction of logical rules from data. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Karol Grudzi nski and Wl/odzisl/aw Duch. SBL-PM: A Simple Algorithm for Selection of Reference Instances in Similarity Based Methods. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Meta-learning: searching in the model space. Department of Computer Methods, Nicholas Copernicus University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-1.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-2.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_3 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-3.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-1.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-2.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t3 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-3.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_train = pd.concat([df_t1, df_t2, df_t3], axis=0)

df_test = pd.concat([df_1, df_2, df_3], axis=0)


print(df_train.info())
print(df_test.info())

"""

#LOACL
df_1 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-1.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_2 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-2.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_3 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-3.test", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t1 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-1.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t2 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-2.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_t3 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/monks-problems/monks-3.train", names=['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'id'], delimiter='\s+')

df_train = pd.concat([df_t1, df_t2, df_t3], axis=0)

df_test = pd.concat([df_1, df_2, df_3], axis=0)


print(df_train.info())
print(df_test.info())