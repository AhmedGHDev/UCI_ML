import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset is created by reading out 200 files from the 10 largest Reuters classes and using an Automatic Speech Recognition system to create corresponding transcriptions.

Data Set Characteristics:  

Text

Number of Instances:

200

Area:

Business

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

2008-03-08

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

63743


Source:

Shourya Roy
shourya.roy '@' gmail.com
and
Shantanu Godbole
shantanu '@' godbole.net


Data Set Information:

Data Characteristics:
--------------------
This data was created by selecting 20 files each from the 10 largest classes
in the Reuters-21578 collection
([Web Link]).
The files were read out by 3 Indian speakers and an Automatic Speech
Recognition (ASR) system was used to generate the transcripts. More about the
ASR system can be found in [1]. Such a dataset will be really helpful to
study the effect of speech recognition noise on text mining algorithms.
The first work which refered to this dataset was on noisy text classification[2].

Data Format:
----------
There are 10 directories labeled by the topic name.
Each contains 20 files of transcriptions.

References:
----------
[1] L. R. Bahl, S. Balakrishnan-Aiyer, J. Bellegarda, M. Franz,
P. Gopalakrishnan, D. Nahamoo, M. Novak, M. Padmanabhan,
M. Picheny, and S. Roukos,
Performance of the IBM large vocabulary continuous speech recognition system on
the ARPA wall street journal task.
In Proc. of ICASSP ’95,
pages 41–44, Detroit, MI, 1995.
[2] S. Agarwal, S. Godbole, D. Punjani and S. Roy,
How Much Noise is too Much: A Study in Automatic Text Classification',
In Proc. of ICDM 2007


Attribute Information:

Provide information about each attribute in your data set.


Relevant Papers:

'“How Much Noise in Text is too Much: A Study in Automatic Document Classification”, ICDM 2007, Sumeet Agarwal, Shantanu Godbole, Diwakar Punjani and Shourya Roy



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""