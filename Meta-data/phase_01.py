import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Meta-Data was used in order to give advice about which classification method is appropriate for a particular dataset (taken from results of Statlog project).

Data Set Characteristics:  

Multivariate

Number of Instances:

528

Area:

N/A

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

22

Date Donated

1996-03-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

96249


Source:

Creator:

LIACC - University of Porto
R.Campo Alegre 823
4150 PORTO

Donor:

P.B.Brazdil or J.Gama
LIACC, University of Porto
Rua Campo Alegre 823
4150 Porto, Portugal
Tel.: +351 600 1672
Fax.: +351 600 3654
Email: statlog-adm '@' ncc.up.pt


Data Set Information:

This DataSet is about the results of Statlog project. The project performed a comparative study between Statistical, Neural and Symbolic learning algorithms.

Project StatLog (Esprit Project 5170) was concerned with comparative studies of different machine learning, neural and statistical classification algorithms. About 20 different algorithms were evaluated on more than 20 different datasets. The tests carried out under project produced many interesting results.

The results of these tests are comprehensively described in a book (D.Michie et.al, 1994).


Attribute Information:

1. DS_Name categorical Name of DataSet
2. T continuous Number of examples in test set
3. N continuous Number of examples
4. p continuous Number of attributes
5. k continuous Number of classes
6. Bin continuous Number of binary Attributes
7. Cost continuous Cost (1=yes,0=no)
8. SDratio continuous Standard deviation ratio
9. correl continuous Mean correlation between attributes
10. cancor1 continuous First canonical correlation
11. cancor2 continuous Second canonical correlation
12. fract1 continuous First eigenvalue
13. fract2 continuous Second eigenvalue
14. skewness continuous Mean of |E(X-Mean)|^3/STD^3
15. kurtosis continuous Mean of |E(X-Mean)|^4/STD^4
16. Hc continuous Mean entropy of attributes
17. Hx continuous Entropy of classes
18. MCx continuous Mean mutual entropy of class and attributes
19. EnAtr continuous Equivalent number of attributes
20. NSRatio continuous Noise-signal ratio
21. Alg_Name categorical Name of Algorithm
22. Norm_error continuous Normalized Error (continuous class)


Relevant Papers:

"Machine Learning, Neural and Statistical Learning". Eds. D.Michie,D.J.Spiegelhalter and C.Taylor Ellis Horwood-1994

P. Brazdil, J.Gama and B.Henery. "Characterizing the Applicability of Classification Algorithms Using Meta-Level Learning", in Proc. of Machine Learning - ECML-94, ed. F.Bergadano and L.de Raedt,LNAI Vol.784 Springer-Verlag.
[Web Link]

J.Gama, P.Brazdil. "Characterization of Classification Algorithms" in Proc. of EPIA 95, LNAI Vol.990 Springer-Verlag, 1995
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/meta-data/meta.data", names=['DS_Name', 'T', 'N', 'p', 'k', 'Bin', 'Cost', 'SDratio', 'correl', 'cancor1', 'cancor2', 'fract1', 'fract2', 'skewness', 'kurtosis', 'Hc', 'Hx', 'MCx', 'EnAtr', 'NSRatio', 'Alg_Name', 'Norm_error'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/meta-data/meta.data", names=['DS_Name', 'T', 'N', 'p', 'k', 'Bin', 'Cost', 'SDratio', 'correl', 'cancor1', 'cancor2', 'fract1', 'fract2', 'skewness', 'kurtosis', 'Hc', 'Hx', 'MCx', 'EnAtr', 'NSRatio', 'Alg_Name', 'Norm_error'])

print(df.info())