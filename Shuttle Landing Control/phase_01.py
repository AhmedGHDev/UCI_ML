import pandas as pd


#Step 00: Loading data
#FROM URL

# INFO
"""
Abstract: Tiny database; all nominal values


Data Set Characteristics:  

Multivariate

Number of Instances:

15

Area:

Physical

Attribute Characteristics:

Categorical

Number of Attributes:

6

Date Donated

1988-11-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

134540


Source:

Original source:

unknown
NASA: Mr. Roger Burke's autolander design team

Donor:

Bojan Cestnik
Jozef Stefan Institute
Jamova 39
61000 Ljubljana
Yugoslavia (tel.: (38)(+61) 214-399 ext.287)


Data Set Information:

This is a tiny database. Michie reports that Burke's group used RULEMASTER to generate comprehendable rules for determining the conditions under which an autolanding would be preferable to manual control of the spacecraft.


Attribute Information:

1. Class: noauto, auto
-- that is, advise using manual/automatic control
2. STABILITY: stab, xstab
3. ERROR: XL, LX, MM, SS
4. SIGN: pp, nn
5. WIND: head, tail
6. MAGNITUDE: Low, Medium, Strong, OutOfRange
7. VISIBILITY: yes, no


Relevant Papers:

Michie,D. (1988). The Fifth Generation's Unbridged Gap. In Rolf Herken (Ed.) The Universal Turing Machine: A Half-Century Survey, 466-489, Oxford University Press.


Papers That Cite This Data Set1:


Adil M. Bagirov and Julien Ugon. An algorithm for computation of piecewise linear function separating two sets. CIAO, School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

Christophe Giraud and Tony Martinez. ADYNAMIC INCREMENTAL NETWORK THAT LEARNS BY DISCRIMINATION. AA. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/shuttle-landing-control/shuttle-landing-control.data" ,names=['Class', 'STABILITY', 'ERROR', 'SIGN', 'WIND', 'MAGNITUDE', 'VISIBILITY']
)

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/shuttle-landing-control/shuttle-landing-control.data" ,names=['Class', 'STABILITY', 'ERROR', 'SIGN', 'WIND', 'MAGNITUDE', 'VISIBILITY']
)

print(df.info())