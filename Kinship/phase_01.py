import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Relational dataset


Data Set Characteristics:  

Relational

Number of Instances:

104

Area:

Social

Attribute Characteristics:

Categorical

Number of Attributes:

12

Date Donated

1990-07-01

Associated Tasks:

Relational-Learning

Missing Values?

No

Number of Web Hits:

95851


Source:

Creator:

Geoff Hinton

Donor:

J. Ross Quinlan


Data Set Information:

This relational database consists of 24 unique names in two families (they have equivalent structures). Hinton used one unique output unit for each person and was interested in predicting the following relations: wife, husband, mother, father, daughter, son, sister, brother, aunt, uncle, niece, and nephew. Hinton used 104 input-output vector pairs (from a space of 12x24=288 possible pairs). The prediction task is as follows: given a name and a relation, have the outputs be on for only those individuals (among the 24) that satisfy the relation. The outputs for all other individuals should be off.

Hinton's results: Using 100 vectors as input and 4 for testing, his results on two passes yielded 7 correct responses out of 8. His network of 36 input units, 3 layers of hidden units, and 24 output units used 500 sweeps of the training set during training.

Quinlan's results: Using FOIL, he repeated the experiment 20 times (rather than Hinton's 2 times). FOIL was correct 78 out of 80 times on the test cases.


Attribute Information:

-- The relation names are:
wife
husband
mother
father
daughter
son
sister
brother
aunt
uncle
niece
nephew


Relevant Papers:

Hinton, G.E (1986). Learning distributed representations of concepts, Proceedings of CogSci 1986.
[Web Link]

Quinlan, J.R. (1989). Learning relations: Comparison of a symbolic and a connectionist approach.
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
#FROM URL
"""
names = ['wife', 'husband', 'mother', 'father', 'daughter', 'son', 'sister', 'brother', 'aunt', 'uncle', 'niece', 'nephew']