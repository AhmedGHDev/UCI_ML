import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The objective is to determine the set of boolean rules that describe the interactions of the nodes within this plant signaling network. The dataset includes 300 separate boolean pseudodynamic simulations using an asynchronous update scheme.

Data Set Characteristics:  

Multivariate

Number of Instances:

300

Area:

Life

Attribute Characteristics:

Integer

Number of Attributes:

43

Date Donated

2008-04-03

Associated Tasks:

Causal-Discovery

Missing Values?

N/A

Number of Web Hits:

67599


Source:

Jerry W. Jenkins, Ph.D.
Systems Biology and Bioinformations Group
CFD Research Corporation
215 Wynn Drive
Huntsville, AL 35805
email: jwj '@' cfdrc.com

Abhishek Soni, Ph.D.
Systems Biology and Bioinformations Group
CFD Research Corporation
215 Wynn Drive
Huntsville, AL 35805
email: axs '@' cfdrc.com


Data Set Information:

The objective is to determine the set of boolean rules that describe the interactions of the nodes within this plant signaling network. The dataset includes 300 separate boolean pseudodynamic simulations of the true rules, using an asynchronous update scheme. Each of the 300 simulations begin with a randomly generated initial condition, in order to ensure sampling of all of the steady states of the system. There are a total of 43 nodes in this dataset, with 5 ndoes being constants.

The results for 300 separate simulations are included in the dataset. Each simulation consists of a matrix of 0's and 1's, with 21 rows and 43 columns. The first row is the randomly generated initial condition for the particular simulation, with the next 20 rows being the output from the boolean pseudodynamics simulation. Each of the 43 columns represent the transient response of a particular node. The nodal names are identified at the top of the data file. A line of asterisks is used to separate the simulations from one another. An example set of data is included below:

***************************
1011101110101101101101001010001011000011001
1100001110111101101101111111011001011101011
1100011110111110101101100011010001110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010
1100001110111110101101100011000011110101010



Attribute Information:

Each node can have a value of 0 or 1. 38 of the 43 nodes are allowed to vary, with 5 nodes held constant throughout the simulation.



Relevant Papers:

Li S, Assman SM, Albert R (2006) Predicting essential components of signal transduction networks: a dynamic model of guard cell abscisic acid signaling. Plos Biology 4: p. 1732-1748

Soni, A.S., Jenkins, J.W., and Sundaram, S.S.: ”Determination of critical network interactions: An augmented Boolean pseudo-dynamics approach”, IET Systems Biology, vol. 2, p. 55-63 (2008).



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""