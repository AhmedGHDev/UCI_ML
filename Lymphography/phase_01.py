import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This lymphography domain was obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. (Restricted access)

Data Set Characteristics:  

Multivariate

Number of Instances:

148

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

18

Date Donated

1988-11-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

119485


Source:

Donors:

1. Igor Kononenko,
University E.Kardelj
Faculty for electrical engineering
Trzaska 25
61000 Ljubljana (tel.: (38)(+61) 265-161

2. Bojan Cestnik
Jozef Stefan Institute
Jamova 39
61000 Ljubljana
Yugoslavia (tel.: (38)(+61) 214-399 ext.287)


Data Set Information:

This is one of three domains provided by the Oncology Institute that has repeatedly appeared in the machine learning literature. (See also breast-cancer and primary-tumor.)


Attribute Information:

--- NOTE: All attribute values in the database have been entered as numeric values corresponding to their index in the list of attribute values for that attribute domain as given below.
1. class: normal find, metastases, malign lymph, fibrosis
2. lymphatics: normal, arched, deformed, displaced
3. block of affere: no, yes
4. bl. of lymph. c: no, yes
5. bl. of lymph. s: no, yes
6. by pass: no, yes
7. extravasates: no, yes
8. regeneration of: no, yes
9. early uptake in: no, yes
10. lym.nodes dimin: 0-3
11. lym.nodes enlar: 1-4
12. changes in lym.: bean, oval, round
13. defect in node: no, lacunar, lac. marginal, lac. central
14. changes in node: no, lacunar, lac. margin, lac. central
15. changes in stru: no, grainy, drop-like, coarse, diluted, reticular, stripped, faint,
16. special forms: no, chalices, vesicles
17. dislocation of: no, yes
18. exclusion of no: no, yes
19. no. of nodes in: 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, >=70


Relevant Papers:

Cestnik,G., Konenenko,I, & Bratko,I. (1987). Assistant-86: A Knowledge-Elicitation Tool for Sophisticated Users. In I.Bratko & N.Lavrac (Eds.) Progress in Machine Learning, 31-45, Sigma Press.
[Web Link]

Clark,P. & Niblett,T. (1987). Induction in Noisy Domains. In I.Bratko & N.Lavrac (Eds.) Progress in Machine Learning, 11-30, Sigma Press.
[Web Link]

Michalski,R., Mozetic,I. Hong,J., & Lavrac,N. (1986). The Multi-Purpose Incremental Learning System AQ15 and its Testing Applications to Three Medical Domains. In Proceedings of the Fifth National Conference on Artificial Intelligence, 1041-1045. Philadelphia, PA: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Marcus Hutter and Marco Zaffalon. Distribution of Mutual Information from Complete and Incomplete Data. CoRR, csLG/0403025. 2004. [View Context].

Michael G. Madden. Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. CoRR, csLG/0211003. 2002. [View Context].

Marco Zaffalon and Marcus Hutter. Robust Feature Selection by Mutual Information Distributions. CoRR, csAI/0206006. 2002. [View Context].

Thomas G. Dietterich. An Experimental Comparison of Three Methods for Constructing Ensembles of Decision Trees: Bagging, Boosting, and Randomization. Machine Learning, 40. 2000. [View Context].

Mark A. Hall and Lloyd A. Smith. Feature Selection for Machine Learning: Comparing a Correlation-Based Filter Approach to the Wrapper. FLAIRS Conference. 1999. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

Yk Huhtala and Juha Kärkkäinen and Pasi Porkka and Hannu Toivonen. Efficient Discovery of Functional and Approximate Dependencies Using Partitions. ICDE. 1998. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Pedro Domingos. Control-Sensitive Feature Selection for Lazy Learners. Artif. Intell. Rev, 11. 1997. [View Context].

Geoffrey I. Webb. OPUS: An Efficient Admissible Algorithm for Unordered Search. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

M. A. Galway and Michael G. Madden. DEPARTMENT OF INFORMATION TECHNOLOGY technical report NUIG-IT-011002 Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. Department of Information Technology National University of Ireland, Galway. [View Context].

Geoffrey I Webb. Learning Decision Lists by Prepending Inferred Rules. School of Computing and Mathematics Deakin University. [View Context].



Citation Request:

This lymphography domain was obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. Thanks go to M. Zwitter and M. Soklic for providing the data. Please include this citation if you plan to use this database.
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/lymphography/lymphography.data", names=['class', 'lymphatics', 'block_of_affere', 'bl._of_lymph._c', 'bl._of_lymph._s', 'by_pass', 'extravasates', 'regeneration_of', 'early_uptake_in', 'lym.nodes_dimin', 'lym.nodes_enlar', 'changes_in_lym.', 'defect_in_node', 'changes_in_node', 'changes_in_stru', 'special_forms', 'dislocation_of', 'exclusion_of_no', 'no._of_nodes_in'])

print(df.info())

"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/lymphography/lymphography.data", names=['class', 'lymphatics', 'block_of_affere', 'bl._of_lymph._c', 'bl._of_lymph._s', 'by_pass', 'extravasates', 'regeneration_of', 'early_uptake_in', 'lym.nodes_dimin', 'lym.nodes_enlar', 'changes_in_lym.', 'defect_in_node', 'changes_in_node', 'changes_in_stru', 'special_forms', 'dislocation_of', 'exclusion_of_no', 'no._of_nodes_in'])

print(df.info())