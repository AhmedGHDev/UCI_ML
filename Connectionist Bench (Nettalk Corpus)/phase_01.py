import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The file "nettalk.data" contains a list of 20,008 English words, along with a phonetic transcription for each word. The task is to train a network to produce the proper phonemes

Data Set Characteristics:  

Multivariate

Number of Instances:

20008

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

4

Date Donated

N/A

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

57434


Source:

The data set was contributed to the benchmark collection by Terry Sejnowski, now at the Salk Institute and the University of California at San Deigo. The data set was developed in collaboration with Charles Rosenberg of Princeton. Approximately 250 person-hours went into creating and testing this database.


Data Set Information:

This is an updated and corrected version of the data set used by Sejnowski and Rosenberg in their influential study of speech generation using a neural network [1]. The file "nettalk.data" contains a list of 20,008 English words, along with a phonetic transcription for each word. The task is to train a network to produce the proper phonemes, given a string of letters as input. This is an example of an input/output mapping task that exhibits strong global regularities, but also a large number of more specialized rules and exceptional cases.

Please see original readme file for more information.


Attribute Information:

The pronouncing dictionary was created to study the translation process between written English, using graphemes or letters as units, and spoken English, using phonemes as units. The dictionary includes 20008 aligned letter and phonetic representations with stresses.

The dictionary contains four tab separated fields of information for each word. The fields are:

1) a letter representation
2) a phonemic representation
3) stress and syllabic structure
4) an integer indicating foreign and irregular words

Please see original readme file for more information.


Relevant Papers:

Sejnowski, T.J., and Rosenberg, C.R. (1987). "Parallel networks that learn to pronounce English text" in Complex Systems, 1, 145-168.
[Web Link]


Papers That Cite This Data Set1:


Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Kai Ming Ting and Boon Toh Low. Model Combination in the Multiple-Data-Batches Scenario. ECML. 1997. [View Context].

Steven Salzberg. On Comparing Classifiers: Pitfalls to Avoid and a Recommended Approach. Data Min. Knowl. Discov, 1. 1997. [View Context].

Dietrich Wettschereck and David W. Aha. Weighting Features. ICCBR. 1995. [View Context].

Thomas G. Dietterich and Ghulum Bakiri. Solving Multiclass Learning Problems via Error-Correcting Output Codes. CoRR, csAI/9501101. 1995. [View Context].

Rong Jin and Yan Liu and Luo Si and Jaime Carbonell and Alexander G. Hauptmann. A New Boosting Algorithm Using Input-Dependent Regularizer. School of Computer Science, Carnegie Mellon University. [View Context].

Wl/odzisl/aw Duch and Jerzy J. Korczak. Optimization and global minimization methods suitable for neural networks. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Rayid Ghani. KDD Project Report Using Error-Correcting Codes for Efficient Text Classification with a Large Number of Categories. Center for Automated Learning and Discovery, School of Computer Science, Carnegie Mellon University. [View Context].

Kai Ming Ting and Boon Toh Low. Theory Combination: an alternative to Data Combination. University of Waikato. [View Context].

Sherrie L. W and Zijian Zheng. A BENCHMARK FOR CLASSIFIER LEARNING. Basser Department of Computer Science The University of Sydney. [View Context].

Steve Whittaker and Loren G. Terveen and Bonnie A. Nardi. Let's stop pushing the envelope and start addressing it: a reference task agenda for HCI. a Senior Research Scientist in the Human Computer Interaction Department of AT&T LabsResearch. [View Context].



Citation Request:

Copyright (C) 1988 by Terrence J. Sejnowski. Permission is hereby given to use the included data for non-commercial research purposes. Contact The Johns Hopkins University, Cognitive Science Center, Baltimore MD, USA for information on commercial use.
"""
names=['letter', 'phonemic', 'stree_syllabic', 'foreign_irregular']
