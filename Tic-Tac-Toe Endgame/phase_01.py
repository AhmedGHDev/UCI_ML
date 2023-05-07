import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Binary classification task on possible configurations of tic-tac-toe game


Data Set Characteristics:  

Multivariate

Number of Instances:

958

Area:

Game

Attribute Characteristics:

Categorical

Number of Attributes:

9

Date Donated

1991-08-19

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

310931


Source:

Creator:

David W. Aha (aha '@' cs.jhu.edu)

Donor:

David W. Aha (aha '@' cs.jhu.edu)


Data Set Information:

This database encodes the complete set of possible board configurations at the end of tic-tac-toe games, where "x" is assumed to have played first. The target concept is "win for x" (i.e., true when "x" has one of 8 possible ways to create a "three-in-a-row").

Interestingly, this raw database gives a stripped-down decision tree algorithm (e.g., ID3) fits. However, the rule-based CN2 algorithm, the simple IB1 instance-based learning algorithm, and the CITRE feature-constructing decision tree algorithm perform well on it.


Attribute Information:

1. top-left-square: {x,o,b}
2. top-middle-square: {x,o,b}
3. top-right-square: {x,o,b}
4. middle-left-square: {x,o,b}
5. middle-middle-square: {x,o,b}
6. middle-right-square: {x,o,b}
7. bottom-left-square: {x,o,b}
8. bottom-middle-square: {x,o,b}
9. bottom-right-square: {x,o,b}
10. Class: {positive,negative}


Relevant Papers:

Matheus, C.J., & Rendell, L.A. (1989). Constructive induction on decision trees. In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence. (pp. 645--650). Detroit, MI: Morgan Kaufmann.
[Web Link]

Matheus, C.J. (1990). Adding domain knowledge to SBL through feature construction. In Proceedings of the Eighth National Conference on Artificial Intelligence (pp. 803--808). Boston, MA: AAAI Press.
[Web Link]

Aha, D. W. (1991). Incremental constructive induction: An instance-based approach. In Proceedings of the Eighth International Workshop on Machine Learning (pp. 117--121). Evanston, ILL: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Saher Esmeir and Shaul Markovitch. Lookahead-based algorithms for anytime induction of decision trees. ICML. 2004. [View Context].

Bart Hamers and J. A. K Suykens. Coupled Transductive Ensemble Learning of Kernel Models. Bart De Moor. 2003. [View Context].

Michael Bain. Structured Features from Concept Lattices for Unsupervised Learning and Classification. Australian Joint Conference on Artificial Intelligence. 2002. [View Context].

Jinyan Li and Kotagiri Ramamohanarao and Guozhu Dong. Combining the Strength of Pattern Frequency and Distance for Classification. PAKDD. 2001. [View Context].

Jochen Garcke and Michael Griebel and Michael Thess. Data Mining with Sparse Grids. Computing, 67. 2001. [View Context].

Alexey Tsymbal and Seppo Puuronen and Vagan Y. Terziyan. Arbiter Meta-Learning with Dynamic Selection of Classifiers and Its Experimental Investigation. ADBIS. 1999. [View Context].

Stephen D. Bay. Nearest neighbor classification from multiple feature subsets. Intell. Data Anal, 3. 1999. [View Context].

Stephen D. Bay. Combining Nearest Neighbor Classifiers Through Multiple Feature Subsets. ICML. 1998. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Jerome H. Friedman and Ron Kohavi and Youngkeol Yun. To appear in AAAI-96 Lazy Decision Trees. Statistics Department and Stanford Linear Accelerator Center Stanford University. [View Context].

Christophe G. Giraud-Carrier and Tony Martinez. AN INCREMENTAL LEARNING MODEL FOR COMMONSENSE REASONING. Department of Computer Science Brigham Young University. [View Context].

Rafael S. Parpinelli and Heitor S. Lopes and Alex Alves Freitas. PART FOUR: ANT COLONY OPTIMIZATION AND IMMUNE SYSTEMS Chapter X An Ant Colony Algorithm for Classification Rule Discovery. CEFET-PR, Curitiba. [View Context].

Ron Kohavi and George H. John. Automatic Parameter Selection by Minimizing Estimated Error. Computer Science Dept. Stanford University. [View Context].

Jinyan Li and Kotagiri Ramamohanarao and Guozhu Dong. ICML2000 The Space of Jumping Emerging Patterns and Its Incremental Maintenance Algorithms. Department of Computer Science and Software Engineering, The University of Melbourne, Parkville. [View Context].

Masahiro Terabe and Takashi Washio and Hiroshi Motoda. The Effect of Subsampling Rate on S 3 Bagging Performance. Mitsubishi Research Institute. [View Context].

David R. Musicant. DATA MINING VIA MATHEMATICAL PROGRAMMING AND MACHINE LEARNING. Doctor of Philosophy (Computer Sciences) UNIVERSITY. [View Context].

C. Titus Brown and Harry W. Bullen and Sean P. Kelly and Robert K. Xiao and Steven G. Satterfield and John G. Hagedorn and Judith E. Devaney. Visualization and Data Mining in an 3D Immersive Environment: Summer Project 2003. [View Context].

Ron Kohavi and Brian Frasca. Useful Feature Subsets and Rough Set Reducts. the Third International Workshop on Rough Sets and Soft Computing. [View Context].

Shi Zhong and Weiyu Tang and Taghi M. Khoshgoftaar. Boosted Noise Filters for Identifying Mislabeled Data. Department of Computer Science and Engineering Florida Atlantic University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
,names=['top-left-square', 'top-middle-square', 'top-right-square', 'middle-left-square', 'middle-middle-square', 'middle-right-square', 'bottom-left-square', 'bottom-middle-square', 'bottom-right-square', 'Class']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"
,names=['top-left-square', 'top-middle-square', 'top-right-square', 'middle-left-square', 'middle-middle-square', 'middle-right-square', 'bottom-left-square', 'bottom-middle-square', 'bottom-right-square', 'Class']
)

print(df.info())