import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Each record represents 100 points on a two-dimensional graph. When plotted in order (from 1 through 100) as the Y co-ordinate, the points will create either a Hill (a “bump” in the terrain) or a Valley (a “dip” in the terrain).


Data Set Characteristics:  

Sequential

Number of Instances:

606

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

101

Date Donated

2008-03-20

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

84023


Source:

Lee Graham (lee '@' stellaralchemy.com)

Franz Oppacher (oppacher '@' scs.carleton.ca)
Carleton University, Department of Computer Science
Intelligent Systems Research Unit
1125 Colonel By Drive, Ottawa, Ontario, Canada, K1S5B6


Data Set Information:

Each record represents 100 points on a two-dimensional graph. When plotted in order (from 1 through 100) as the Y co-ordinate, the points will create either a Hill (a “bump” in the terrain) or a Valley (a “dip” in the terrain).

There are six files, as follows:

(a) Hill_Valley_without_noise_Training.data
(b) Hill_Valley_without_noise_Testing.data

These first two datasets (without noise) are a training/testing set pair where the hills or valleys have a smooth transition.

(c) Hill_Valley_with_noise_Training.data
(d) Hill_Valley_with_noise_Testing.data

These next two datasets (with noise) are a training/testing set pair where the terrain is uneven, and the hill or valley is not as obvious when viewed closely.

(e) Hill_Valley_sample_arff.text

The sample ARFF file is useful for setting up experiments, but is not necessary.

(f) Hill_Valley_visual_examples.jpg

This graphic file shows two example instances from the data.


Attribute Information:

1-100: Labeled “X##”. Floating point values (numeric)
101: Labeled “class”. Binary {0, 1} representing {valley, hill}


Relevant Papers:

1. Non-published. Evaluation of dataset by various learning algorithms in the Waikato Environment for Knowledge Analysis (WEKA).



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_without_noise_Training.data")
df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_with_noise_Testing.data")

print(df_train.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_without_noise_Training.data")
df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/hill-valley/Hill_Valley_with_noise_Testing.data")

print(df_train.info())
print(df_test.info())