import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: From CMU connectionist bench repository; Classifies secondary structure of certain globular proteins


Data Set Characteristics:  

Sequential

Number of Instances:

128

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

N/A

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

68015


Source:

The data set was contributed to the benchmark collection by Terry Sejnowski, now at the Salk Institute and the University of California at San Deigo. The data set was developed in collaboration with Ning Qian of Johns-Hopkins University.


Data Set Information:

This is a data set used by Ning Qian and Terry Sejnowski in their study using a neural net to predict the secondary structure of certain globular proteins [1]. The idea is to take a linear sequence of amino acids and to predict, for each of these amino acids, what secondary structure it is a part of within the protein. There are three choices: alpha-helix, beta-sheet, and random-coil. The data set contains both a large set of training data and a distinct set of data that can be used for testing the resulting network. Qian and Sejnowski use a Nettalk-like approach and report an accuracy of 64.3% on the test set, and they speculate that this is about the best that can be done using only local context.

There is also a domain theory in the folder, donated and created by Jude Shavlik & Rich Maclin


Attribute Information:

N/A


Relevant Papers:

Ning Qian and Terrnece J. Sejnowski (1988), "Predicting the Secondary Structure of Globular Proteins Using Neural Network Models" in Journal of Molecular Biology 202, 865-884. Academic Press.
[Web Link]


Papers That Cite This Data Set1:


Jianbin Tan and David L. Dowe. MML Inference of Decision Graphs with Multi-way Joins and Dynamic Attributes. Australian Conference on Artificial Intelligence. 2003. [View Context].

Mukund Deshpande and George Karypis. Evaluation of Techniques for Classifying Biological Sequences. PAKDD. 2002. [View Context].

Steven Eschrich and Nitesh V. Chawla and Lawrence O. Hall. Generalization Methods in Bioinformatics. BIOKDD. 2002. [View Context].

Andreas L. Prodromidis. On the Management of Distributed Learning Agents Ph.D. Thesis Proposal CUCS-032-97. Department of Computer Science Columbia University. 1998. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Kuan-ming Lin and Chih-Jen Lin. A Study on Reduced Support Vector Machines. Department of Computer Science and Information Engineering National Taiwan University. [View Context].



Citation Request:

Copyright (C) 1988 by Terrence J. Sejnowski. Permission is hereby given to use the included data for non-commercial research purposes. Contact the John Hopkins University, Cognitive Science Center, Baltimore MD, USA for information on commercial use.
"""