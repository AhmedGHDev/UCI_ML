import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset records 640 time series of 12 LPC cepstrum coefficients taken from nine male speakers.

Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

640

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

12

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

148269


Source:

Original Owner and Donor:

Mineichi Kudo, Jun Toyama, Masaru Shimbo
Information Processing Laboratory
Division of Systems and Information Engineering
Graduate School of Engineering
Hokkaido University, Sapporo 060-8628, JAPAN
{mine,jun,shimbo}@main.eng.hokudai.ac.jp


Data Set Information:

The data was collected for examining our newly developed classifier for multidimensional curves (multidimensional time series). Nine male speakers uttered two Japanese vowels /ae/ successively. For each utterance, with the analysis parameters described below, we applied 12-degree linear prediction analysis to it to obtain a discrete-time series with 12 LPC cepstrum coefficients. This means that one utterance by a speaker forms a time series whose length is in the range 7-29 and each point of a time series is of 12 features (12 coefficients).

The number of the time series is 640 in total. We used one set of 270 time series for training and the other set of 370 time series for testing.

Number of Instances (Utterances):

* Training: 270 (30 utterances by 9 speakers. See file 'size_ae.train'.)
* Testing: 370 (24-88 utterances by the same 9 speakers in different opportunities. See file 'size_ae.test'.)

Length of Time Series:

* 7 - 29 depending on utterances

Analysis parameters:

* Sampling rate : 10kHz
* Frame length : 25.6 ms
* Shift length : 6.4ms
* Degree of LPC coefficients : 12

Files:

* Training file: ae.train
* Testing file: ae.test

Format:

Each line in ae.train or ae.test represents 12 LPC coefficients in the increasing order separated by spaces. This corresponds to one analysis frame.

Lines are organized into blocks, which are a set of 7-29 lines separated by blank lines and corresponds to a single speech utterance of /ae/ with 7-29 frames.

Each speaker is a set of consecutive blocks. In ae.train there are 30 blocks for each speaker. Blocks 1-30 represent speaker 1, blocks 31-60 represent speaker 2, and so on up to speaker 9. In ae.test, speakers 1 to 9 have the corresponding number of blocks: 31 35 88 44 29 24 40 50 29. Thus, blocks 1-31 represent speaker 1 (31 utterances of /ae/), blocks 32-66 represent speaker 2 (35 utterances of /ae/), and so on.


Attribute Information:

12 Real Attributes


Relevant Papers:

M. Kudo, J. Toyama and M. Shimbo. (1999). "Multidimensional Curve Classification Using Passing-Through Regions". Pattern Recognition Letters, Vol. 20, No. 11--13, pages 1103--1111.
[Web Link]



Citation Request:

If you publish any work using the dataset, please inform the donor. Use for commercial purposes requires donor permission.
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/JapaneseVowels-mld/ae.train"
,delimiter='\s+'
,names=['LPC_'+str(i) for i in range(1, 13)]
)
df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/JapaneseVowels-mld/ae.test"
,delimiter='\s+'
,names=['LPC_'+str(i) for i in range(1, 13)]
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/JapaneseVowels-mld/ae.train"
,delimiter='\s+'
,names=['LPC_'+str(i) for i in range(1, 13)]
)
df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/JapaneseVowels-mld/ae.test"
,delimiter='\s+'
,names=['LPC_'+str(i) for i in range(1, 13)]
)

print(df_train.info())
print(df_test.info())