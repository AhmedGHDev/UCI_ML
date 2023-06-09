import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: E. Coli promoter gene sequences (DNA) with partial domain theory


Data Set Characteristics:  

Sequential, Domain-Theory

Number of Instances:

106

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

58

Date Donated

1990-06-30

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

96313


Source:

Creators:

1. promoter instances: C. Harley (CHARLEY '@' McMaster.CA) and R. Reynolds

2. non-promoter instances and domain theory: M. Noordewier
-- (non-promoters derived from work of lab of Prof. Tom Record, University of Wisconsin Biochemistry Department)

Donor:

M. Noordewier and J. Shavlik, {noordewi,shavlik}@cs.wisc.edu


Data Set Information:

This dataset has been developed to help evaluate a "hybrid" learning algorithm ("KBANN") that uses examples to inductively refine preexisting knowledge. Using a "leave-one-out" methodology, the following errors were produced by various ML algorithms. (See Towell, Shavlik, & Noordewier, 1990, for details.)

System -- Errors -- Comments
----------------------------------------------------------------
KBANN -- 4/106 -- a hybrid ML system
BP -- 8/106 -- std backprop with one hidden layer
O'Neill -- 12/106 -- ad hoc technique from the bio. lit.
Near-Neigh -- 13/106 -- a nearest-neighbor algo (k=3)
ID3 -- 19/106 -- Quinlan's decision-tree builder

Type of domain: non-numeric, nominal (one of A, G, T, C)


Note: DNA nucleotides can be grouped into a hierarchy, as shown below:

X (any)
/ \
(purine) R Y (pyrimidine)
/ \ / \
A G T C


Here is that hierachy in a text-friendly format:

X (any)
. R (purine)
. . A
. . G
. Y (pyrimidine)
. . T
. . C


Attribute Information:

1. One of {+/-}, indicating the class ("+" = promoter).
2. The instance name (non-promoters named by position in the 1500-long nucleotide sequence provided by T. Record).
3-59. The remaining 57 fields are the sequence, starting at position -50 (p-50) and ending at position +7 (p7). Each of these fields is filled by one of {a, g, t, c}.


Relevant Papers:

Harley, C. and Reynolds, R. 1987. "Analysis of E. Coli Promoter Sequences." Nucleic Acids Research, 15:2343-2361.
[Web Link]

Towell, G., Shavlik, J. and Noordewier, M. 1990. "Refinement of Approximate Domain Theories by Knowledge-Based Artificial Neural Networks." In Proceedings of the Eighth National Conference on Artificial Intelligence (AAAI-90).
[Web Link]


Papers That Cite This Data Set1:


Ken Tang and Ponnuthurai N. Suganthan and Xi Yao and A. Kai Qin. Linear dimensionalityreduction using relevance weighted LDA. School of Electrical and Electronic Engineering Nanyang Technological University. 2005. [View Context].

Wei-Chun Kao and Kai-Min Chung and Lucas Assun and Chih-Jen Lin. Decomposition Methods for Linear Support Vector Machines. Neural Computation, 16. 2004. [View Context].

Jinyan Li and Limsoon Wong. Using Rules to Analyse Bio-medical Data: A Comparison between C4.5 and PCL. WAIM. 2003. [View Context].

Aik Choon Tan and David Gilbert. An Empirical Comparison of Supervised Machine Learning Techniques in Bioinformatics. APBC. 2003. [View Context].

Giorgio Valentini. Ensemble methods based on bias--variance analysis Theses Series DISI-TH-2003. Dipartimento di Informatica e Scienze dell'Informazione . 2003. [View Context].

Zoubin Ghahramani and Hyun-Chul Kim. Bayesian Classifier Combination. Gatsby Computational Neuroscience Unit University College London. 2003. [View Context].

Mukund Deshpande and George Karypis. Evaluation of Techniques for Classifying Biological Sequences. PAKDD. 2002. [View Context].

Takashi Matsuda and Hiroshi Motoda and Tetsuya Yoshida and Takashi Washio. Mining Patterns from Structured Data by Beam-Wise Graph-Based Induction. Discovery Science. 2002. [View Context].

Michael G. Madden. Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. CoRR, csLG/0211003. 2002. [View Context].

Marina Meila and Michael I. Jordan. Learning with Mixtures of Trees. Journal of Machine Learning Research, 1. 2000. [View Context].

Mark A. Hall and Lloyd A. Smith. Feature Selection for Machine Learning: Comparing a Correlation-Based Filter Approach to the Wrapper. FLAIRS Conference. 1999. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

Jie Cheng and Russell Greiner. Comparing Bayesian Network Classifiers. UAI. 1999. [View Context].

Ismail Taha and Joydeep Ghosh. Symbolic Interpretation of Artificial Neural Networks. IEEE Trans. Knowl. Data Eng, 11. 1999. [View Context].

Cesar Guerra-Salcedo and L. Darrell Whitley. Genetic Approach to Feature Selection for Ensemble Creation. GECCO. 1999. [View Context].

Foster J. Provost and Tom Fawcett and Ron Kohavi. The Case against Accuracy Estimation for Comparing Induction Algorithms. ICML. 1998. [View Context].

Andreas L. Prodromidis. On the Management of Distributed Learning Agents Ph.D. Thesis Proposal CUCS-032-97. Department of Computer Science Columbia University. 1998. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Daphne Koller and Mehran Sahami. Toward Optimal Feature Selection. ICML. 1996. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Ron Kohavi and Dan Sommerfield. Feature Subset Selection Using the Wrapper Method: Overfitting and Dynamic Search Space Topology. KDD. 1995. [View Context].

Chih-Wei Hsu and Cheng-Ru Lin. A Comparison of Methods for Multi-class Support Vector Machines. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Rudy Setiono. Extracting M-of-N Rules from Trained Neural Networks. School of Computing National University of Singapore. [View Context].

Ron Kohavi and Dan Sommerfield. To Appear in KDD-98 Targeting Business Users with Decision Table Classifiers. Data Mining and Visualization Silicon Graphics, Inc. [View Context].

Warodom Geamsakul and Takashi Matsuda and Tetsuya Yoshida and Hiroshi Motoda and Takashi Washio. Constructing a Decision Tree for Graph Structured Data. Institute of Scientific and Industrial Research, Osaka University. [View Context].

Ivor W. Tsang and James T. Kwok. Distance Metric Learning with Kernels. Department of Computer Science Hong Kong University of Science and Technology Clear Water Bay Hong Kong. [View Context].

Norbert Jankowski. Survey of Neural Transfer Functions. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Ron Kohavi and George H. John. Automatic Parameter Selection by Minimizing Estimated Error. Computer Science Dept. Stanford University. [View Context].

Ron Kohavi and Barry G. Becker and Dan Sommerfield. Improving Simple Bayes. Data Mining and Visualization Group Silicon Graphics, Inc. [View Context].

Vikas Sindhwani and P. Bhattacharya and Subrata Rakshit. Information Theoretic Feature Crediting in Multiclass Support Vector Machines. [View Context].

C. esar and Cesar Guerra-Salcedo and Darrell Whitley. Feature Selection Mechanisms for Ensemble Creation : A Genetic Search Perspective. Department of Computer Science Colorado State University. [View Context].

Alain Rakotomamonjy. Analysis of SVM regression bounds for variable ranking. P.S.I CNRS FRE 2645, INSA de Rouen Avenue de l'Universite. [View Context].

Cesar Guerra-Salcedo and Stephen Chen and Darrell Whitley and Sarah Smith. Fast and Accurate Feature Selection Using Hybrid Genetic Strategies. Department of Computer Science Colorado State University. [View Context].

Chotirat Ann and Dimitrios Gunopulos. Scaling up the Naive Bayesian Classifier: Using Decision Trees for Feature Selection. Computer Science Department University of California. [View Context].

M. A. Galway and Michael G. Madden. DEPARTMENT OF INFORMATION TECHNOLOGY technical report NUIG-IT-011002 Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. Department of Information Technology National University of Ireland, Galway. [View Context].

Kuan-ming Lin and Chih-Jen Lin. A Study on Reduced Support Vector Machines. Department of Computer Science and Information Engineering National Taiwan University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data", names=['class', 'instance_name', 'sequence'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/molecular-biology/promoter-gene-sequences/promoters.data", names=['class', 'instance_name', 'sequence'])

print(df.info())