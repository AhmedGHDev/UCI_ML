import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The problem consists of classifying all the blocks of the page layout of a document that has been detected by a segmentation process.

Data Set Characteristics:  

Multivariate

Number of Instances:

5473

Area:

Computer

Attribute Characteristics:

Integer, Real

Number of Attributes:

10

Date Donated

1995-07-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

123140


Source:

Original Owner:

Donato Malerba
Dipartimento di Informatica
University of Bari
via Orabona 4
70126 Bari - Italy
phone: +39 - 80 - 5443269
fax: +39 - 80 - 5443196
malerbad '@' vm.csata.it

Donor:

Donato Malerba


Data Set Information:

The 5473 examples comes from 54 distinct documents. Each observation concerns one block. All attributes are numeric. Data are in a format readable by C4.5.


Attribute Information:

height: integer. | Height of the block.
lenght: integer. | Length of the block.
area: integer. | Area of the block (height * lenght);
eccen: continuous. | Eccentricity of the block (lenght / height);
p_black: continuous. | Percentage of black pixels within the block (blackpix / area);
p_and: continuous. | Percentage of black pixels after the application of the Run Length Smoothing Algorithm (RLSA) (blackand / area);
mean_tr: continuous. | Mean number of white-black transitions (blackpix / wb_trans);
blackpix: integer. | Total number of black pixels in the original bitmap of the block.
blackand: integer. | Total number of black pixels in the bitmap of the block after the RLSA.
wb_trans: integer. | Number of white-black transitions in the original bitmap of the block.


Relevant Papers:

Malerba, D., Esposito, F., and Semeraro, G. "A Further Comparison of Simplification Methods for Decision-Tree Induction." In D. Fisher and H. Lenz (Eds.), "Learning from Data: Artificial Intelligence and Statistics V", Lecture Notes in Statistics, Springer Verlag, Berlin, 1995.
[Web Link]

Esposito F., Malerba D., & Semeraro G. Multistrategy Learning for Document Recognition. Applied Artificial Intelligence, 8, pp. 33-84, 1994
[Web Link]


Papers That Cite This Data Set1:


Steven Eschrich and Nitesh V. Chawla and Lawrence O. Hall. Generalization Methods in Bioinformatics. BIOKDD. 2002. [View Context].

Adil M. Bagirov and Julien Ugon. An algorithm for computation of piecewise linear function separating two sets. CIAO, School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

C. Titus Brown and Harry W. Bullen and Sean P. Kelly and Robert K. Xiao and Steven G. Satterfield and John G. Hagedorn and Judith E. Devaney. Visualization and Data Mining in an 3D Immersive Environment: Summer Project 2003. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

names = ['height', 'lenght', 'area', 'eccen', 'p_black', 'p_and', 'mean_tr', 'blackpix', 'blackand', 'wb_trans']