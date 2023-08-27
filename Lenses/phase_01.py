import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Database for fitting contact lenses

Data Set Characteristics:  

Multivariate

Number of Instances:

24

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

4

Date Donated

1990-08-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

229453


Source:

Original Source:

Cendrowska, J. "PRISM: An algorithm for inducing modular rules", International Journal of Man-Machine Studies, 1987, 27, 349-370

Donor:

Benoit Julien (Julien '@' ce.cmu.edu)


Data Set Information:

The examples are complete and noise free. The examples highly simplified the problem. The attributes do not fully describe all the factors affecting the decision as to which type, if any, to fit.

Notes:

--This database is complete (all possible combinations of attribute-value pairs are represented).

--Each instance is complete and correct.

--9 rules cover the training set.


Attribute Information:

-- 3 Classes
1 : the patient should be fitted with hard contact lenses,
2 : the patient should be fitted with soft contact lenses,
3 : the patient should not be fitted with contact lenses.

1. age of the patient: (1) young, (2) pre-presbyopic, (3) presbyopic
2. spectacle prescription: (1) myope, (2) hypermetrope
3. astigmatic: (1) no, (2) yes
4. tear production rate: (1) reduced, (2) normal


Relevant Papers:

Witten, I. H. & MacDonald, B. A. (1988). Using concept learning for knowledge acquisition. International Journal of Man-Machine Studies, 27, (pp. 349-370).
[Web Link]


Papers That Cite This Data Set1:


Bob Ricks and Dan Ventura. Training a Quantum Neural Network. NIPS. 2003. [View Context].

Jeremy Kubica and Andrew Moore. Probabilistic Noise Identification and Data Cleaning. ICDM. 2003. [View Context].

Ke Wang and Shiyu Zhou and Ada Wai-Chee Fu and Jeffrey Xu Yu. Mining Changes of Classification by Correspondence Tracing. SDM. 2003. [View Context].

Jim Prentzas and Ioannis Hatzilygeroudis and Athanasios K. Tsakalidis. Updating a Hybrid Rule Base with New Empirical Source Knowledge. ICTAI. 2002. [View Context].

Pedro Domingos. Knowledge Discovery Via Multiple Models. Intell. Data Anal, 2. 1998. [View Context].

J. Kent Martin and Daniel S. Hirschberg. Small Sample Statistics for Classification Error Rates I: Error Rate Measurements. Department of Information and Computer Science University of California, Irvine. 1996. [View Context].

Christophe Giraud and Tony Martinez and Christophe G. Giraud-Carrier. University of Bristol Department of Computer Science ILA: Combining Inductive Learning with Prior Knowledge and Reasoning. 1995. [View Context].

Geoffrey I. Webb. OPUS: An Efficient Admissible Algorithm for Unordered Search. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

Anthony D. Griffiths and Derek Bridge. A Yardstick for the Evaluation of Case-Based Classifiers. Department of Computer Science, University of York. [View Context].

Mehmet Dalkilic and Arijit Sengupta. A Logic-theoretic classifier called Circle. School of Informatics Center for Genomics and BioInformatics Indiana University. [View Context].

Christophe G. Giraud-Carrier and Tony Martinez. AN INCREMENTAL LEARNING MODEL FOR COMMONSENSE REASONING. Department of Computer Science Brigham Young University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/lenses/lenses.data", names=['index', 'age', 'spectacle_prescription', 'astigmatic', 'tear_production_rate'], delimiter='\s+')

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/lenses/lenses.data", names=['index', 'age', 'spectacle_prescription', 'astigmatic', 'tear_production_rate'], delimiter='\s+')

print(df.info())