import pandas as pd


#Step 00: Loading data
#FROM URL

# INFO
"""
Abstract: Speaker independent recognition of the eleven steady state vowels of British English using a specified training set of lpc derived log area ratios.

Data Set Characteristics:  

N/A

Number of Instances:

528

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

10

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

90422


Source:

David Deterding (data and non-connectionist analysis)
Mahesan Niranjan (first connectionist analysis)
Tony Robinson (description, program, data, and results) - "ajr '@' dsl.eng.cam.ac.uk"


Data Set Information:

The problem is specified by the accompanying data file, "vowel.data". This consists of a three dimensional array: voweldata [speaker, vowel, input]. The speakers are indexed by integers 0-89. (Actually, there are fifteen individual speakers, each saying each vowel six times.) The vowels are indexed by integers 0-10. For each utterance, there are ten floating-point input values, with array indices 0-9.

The problem is to train the network as well as possible using only on data from "speakers" 0-47, and then to test the network on speakers 48-89, reporting the number of correct classifications in the test set.

For a more detailed explanation of the problem, see the excerpt from Tony Robinson's Ph.D. thesis in the COMMENTS section. In Robinson's opinion, connectionist problems fall into two classes, the possible and the impossible. He is interested in the latter, by which he means problems that have no exact solution. Thus the problem here is not to see how fast a network can be trained (although this is important), but to maximise a less than perfect performance.


Attribute Information:

N/A


Relevant Papers:

[Deterding89] D. H. Deterding, 1989, University of Cambridge, "Speaker Normalisation for Automatic Speech Recognition", submitted for PhD.
[Web Link]

[NiranjanFallside88] M. Niranjan and F. Fallside, 1988, Cambridge University Engineering Department, "Neural Networks and Radial Basis Functions in Classifying Static Speech Patterns", CUED/F-[Web Link].
[Web Link]

[RenalsRohwer89-ijcnn] Steve Renals and Richard Rohwer, "Phoneme Classification Experiments Using Radial Basis Functions", International Joint Conference on Neural Networks, Washington, 1989.
[Web Link]


Papers That Cite This Data Set1:


M. Layton and M. J. F Gales. CAMBRIDGE UNIVERSITY ENGINEERING DEPARTMENT Maximum Margin Training of Generative Kernels. CUED. 2004. [View Context].

Matthew Brand. Pattern discovery via entropy minimization. MERL -- A MITSUBISHI ELECTRIC RESEARCH LABORATORY. 1998. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""