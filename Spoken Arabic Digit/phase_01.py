import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset contains timeseries of mel-frequency cepstrum coefficients (MFCCs) corresponding to spoken Arabic digits. Includes data from 44 male and 44 female native Arabic speakers.


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

8800

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

13

Date Donated

2010-09-13

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

94253


Source:

Data Collected by the Laboratory of Automatic and Signals,
University of Badji-Mokhtar
Annaba, Algeria.

Direction: Prof.Mouldi Bedda
Participants: H.Dahmani, C.Snani, MC.Amara Korba, S.Atoui
Adapted and preprocessed by :
Nacereddine Hammami and Mouldi Bedda
Faculty of Engineering,
Al-Jouf University
Sakaka, Al-Jouf
Kingdom of Saudi Arabia
e-mail: nacereddine.hammami '@' gmail.com
mouldi_bedda '@' yahoo.fr
Date: October, 2008


Data Set Information:

Dataset from 8800(10 digits x 10 repetitions x 88 speakers) time series of 13 Frequency Cepstral
Coefficients (MFCCs) had taken from 44 males and 44 females Arabic native speakers
between the ages 18 and 40 to represent ten spoken Arabic digit.


Attribute Information:

Each line on the data base represents 13 MFCCs coefficients in the increasing order separated by
spaces. This corresponds to one analysis frame. The 13 Mel Frequency Cepstral Coefficients
(MFCCs) are computed with the following
conditions;
Sampling rate: 11025 Hz, 16 bits
Window applied: hamming
Filter pre-emphasized: 1-0.97Z^(-1)


Relevant Papers:

[1] N. Hammami, M. Bedda ,"Improved Tree model for Arabic Speech Recognition", Proc. IEEE
ICCSIT10 Conference, 2010.
[2] N. Hammami, M. Sellami ,"Tree distribution classifier for automatic spoken Arabic digit
recognition", Proc. IEEE ICITST09 Conference, 2009 , PP 1-4.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00195/Train_Arabic_Digit.txt"
,delimiter='\s+'
,names=['MFCC_'+str(i) for i in range(1, 14)]
)

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00195/Test_Arabic_Digit.txt"
,delimiter='\s+'
,names=['MFCC_'+str(i) for i in range(1, 14)]
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00195/Train_Arabic_Digit.txt"
,delimiter='\s+'
,names=['MFCC_'+str(i) for i in range(1, 14)]
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00195/Test_Arabic_Digit.txt"
,delimiter='\s+'
,names=['MFCC_'+str(i) for i in range(1, 14)]
)

print(df_train.info())
print(df_test.info())