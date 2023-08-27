import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Nursery Database was derived from a hierarchical decision model originally developed to rank applications for nursery schools.

Data Set Characteristics:  

Multivariate

Number of Instances:

12960

Area:

Social

Attribute Characteristics:

Categorical

Number of Attributes:

8

Date Donated

1997-06-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

260588


Source:

Creator:

Vladislav Rajkovic et al. (13 experts)

Donors:

Marko Bohanec (marko.bohanec '@' ijs.si)
Blaz Zupan (blaz.zupan '@' ijs.si)


Data Set Information:

Nursery Database was derived from a hierarchical decision model originally developed to rank applications for nursery schools. It was used during several years in 1980's when there was excessive enrollment to these schools in Ljubljana, Slovenia, and the rejected applications frequently needed an objective explanation. The final decision depended on three subproblems: occupation of parents and child's nursery, family structure and financial standing, and social and health picture of the family. The model was developed within expert system shell for decision making DEX (M. Bohanec, V. Rajkovic: Expert system for decision making. Sistemica 1(1), pp. 145-157, 1990.).

The hierarchical model ranks nursery-school applications according to the following concept structure:

NURSERY Evaluation of applications for nursery schools
. EMPLOY Employment of parents and child's nursery
. . parents Parents' occupation
. . has_nurs Child's nursery
. STRUCT_FINAN Family structure and financial standings
. . STRUCTURE Family structure
. . . form Form of the family
. . . children Number of children
. . housing Housing conditions
. . finance Financial standing of the family
. SOC_HEALTH Social and health picture of the family
. . social Social conditions
. . health Health conditions

Input attributes are printed in lowercase. Besides the target concept (NURSERY) the model includes four intermediate concepts: EMPLOY, STRUCT_FINAN, STRUCTURE, SOC_HEALTH. Every concept is in the original model related to its lower level descendants by a set of examples (for these examples sets see [Web Link]).

The Nursery Database contains examples with the structural information removed, i.e., directly relates NURSERY to the eight input attributes: parents, has_nurs, form, children, housing, finance, social, health.

Because of known underlying concept structure, this database may be particularly useful for testing constructive induction and structure discovery methods.


Attribute Information:

parents: usual, pretentious, great_pret
has_nurs: proper, less_proper, improper, critical, very_crit
form: complete, completed, incomplete, foster
children: 1, 2, 3, more
housing: convenient, less_conv, critical
finance: convenient, inconv
social: non-prob, slightly_prob, problematic
health: recommended, priority, not_recom


Relevant Papers:

M. Olave, V. Rajkovic, M. Bohanec: An application for admission in public school systems. In (I. Th. M. Snellen and W. B. H. J. van de Donk and J.-P. Baquiast, editors) Expert Systems in Public Administration, pages 145-160. Elsevier Science Publishers (North Holland), 1989.
[Web Link]

B. Zupan, M. Bohanec, I. Bratko, J. Demsar: Machine learning by function decomposition. ICML-97, Nashville, TN. 1997
[Web Link]


Papers That Cite This Data Set1:


Daniel J. Lizotte and Omid Madani and Russell Greiner. Budgeted Learning of Naive-Bayes Classifiers. UAI. 2003. [View Context].

Michael G. Madden. Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. CoRR, csLG/0211003. 2002. [View Context].

Marina Meila and Michael I. Jordan. Learning with Mixtures of Trees. Journal of Machine Learning Research, 1. 2000. [View Context].

Jinyan Li and Guozhu Dong and Kotagiri Ramamohanarao. Instance-Based Classification by Emerging Patterns. PKDD. 2000. [View Context].

Jie Cheng and Russell Greiner. Comparing Bayesian Network Classifiers. UAI. 1999. [View Context].

Nikunj C. Oza and Stuart J. Russell. Online Bagging and Boosting. Computer Science Division University of California. [View Context].

Daniel J. Lizotte and Omid Madani and Russell Greiner. Budgeted Learning, Part II: The Na#ve-Bayes Case. Department of Computing Science University of Alberta. [View Context].

Shi Zhong and Weiyu Tang and Taghi M. Khoshgoftaar. Boosted Noise Filters for Identifying Mislabeled Data. Department of Computer Science and Engineering Florida Atlantic University. [View Context].

M. A. Galway and Michael G. Madden. DEPARTMENT OF INFORMATION TECHNOLOGY technical report NUIG-IT-011002 Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. Department of Information Technology National University of Ireland, Galway. [View Context].

Daniel J. Lizotte. Library Release Form Name of Author. Budgeted Learning of Naive Bayes Classifiers. [View Context].

Jinyan Li and Kotagiri Ramamohanarao and Guozhu Dong. ICML2000 The Space of Jumping Emerging Patterns and Its Incremental Maintenance Algorithms. Department of Computer Science and Software Engineering, The University of Melbourne, Parkville. [View Context].

Gustavo E. A and Gustavo E A P A Batista and Ronaldo C. Prati and Maria Carolina Monard. A Study of the Behavior of Several Methods for Balancing Machine Learning Training Data. Instituto de Ci ^ encias Matem aticas e de Computac~ ao. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data", names=['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data", names=['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health'])

print(df.info())