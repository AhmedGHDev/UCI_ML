import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Multiple, labelled samples of pen tip trajectories recorded whilst writing individual characters. All samples are from the same writer, for the purposes of primitive extraction. Only characters with a single pen-down segment were considered.


Data Set Characteristics:  

Time-Series

Number of Instances:

2858

Area:

Computer

Attribute Characteristics:

Real

Number of Attributes:

3

Date Donated

2008-08-20

Associated Tasks:

Classification, Clustering

Missing Values?

N/A

Number of Web Hits:

176841


Source:

Ben H Williams
School of Informatics,
University of Edinburgh,
ben.williams '@' ed.ac.uk


Data Set Information:

The characters here were used for a PhD study on primitive extraction using HMM based models. The data consists of 2858 character samples, contained in the cell array 'mixout'. The struct variable 'consts' contains a field consts.charlabels which provides ennummerated labels for the characters. consts.key provides the key for each label. The data was captured using a WACOM tablet. 3 Dimensions were kept - x, y, and pen tip force. The data has been numerically differentiated and Gaussian smoothed, with a sigma value of 2. Data was captured at 200Hz. The data was normalised with consts.datanorm. Only characters with a single 'PEN-DOWN' segment were considered. Character segmentation was performed using a pen tip force cut-off point. The characters have also been shifted so that their velocity profiles best match the mean of the set.


Attribute Information:

Each character sample is a 3-dimensional pen tip velocity trajectory. This is contained in matrix format, with 3 rows and T columns where T is the length of the character sample.


Relevant Papers:

B.H. Williams, M.Toussaint, and A.J. Storkey. Extracting motion primitives from natural handwriting data. In ICANN, volume 2, pages 634–643, 2006.

B.H. Williams, M.Toussaint, and A.J. Storkey. A primitive based generative model to infer timing information in unpartitioned handwriting data. In IJCAI, pages 1119–1124, 2007.

B.H. Williams, M. Toussaint, and A.J. Storkey. Modelling motion primitives and their timing in biologically executed movements. In J.C. Platt, D. Koller, Y. Singer, and S. Roweis, editors, Advances in Neural Information Processing Systems 20, pages 1609–1616. MIT Press, Cambridge, MA, 2008.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""