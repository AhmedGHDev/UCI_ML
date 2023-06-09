import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The dataset consists of 384 features extracted from CT images. The class variable is numeric and denotes the relative location of the CT slice on the axial axis of the human body.

Data Set Characteristics:  

Domain-Theory

Number of Instances:

53500

Area:

Computer

Attribute Characteristics:

Real

Number of Attributes:

386

Date Donated

2011-07-07

Associated Tasks:

Regression

Missing Values?

N/A

Number of Web Hits:

71239


Source:

F. Graf, H.-P. Kriegel, M. Schubert, S. Poelsterl, A. Cavallaro

Ludwig-Maximilians-UniversitÃ¤t Munich
Database Systems Group
OettingenstraÃŸe 67
80538 Munich, Germany


Data Set Information:

The data was retrieved from a set of 53500 CT images from 74 different
patients (43 male, 31 female).

Each CT slice is described by two histograms in polar space.
The first histogram describes the location of bone structures in the image,
the second the location of air inclusions inside of the body.
Both histograms are concatenated to form the final feature vector.
Bins that are outside of the image are marked with the value -0.25.

The class variable (relative location of an image on the axial axis) was
constructed by manually annotating up to 10 different distinct landmarks in
each CT Volume with known location. The location of slices in between
landmarks was interpolated.


Attribute Information:

1. patientId: Each ID identifies a different patient
2. - 241.: Histogram describing bone structures
242. - 385.: Histogram describing air inclusions
386. reference: Relative location of the image on the axial axis (class
value). Values are in the range [0; 180] where 0 denotes
the top of the head and 180 the soles of the feet.


Relevant Papers:

1. F. Graf, H.-P. Kriegel, M. Schubert, S. Poelsterl, A. Cavallaro
2D Image Registration in CT Images using Radial Image Descriptors
In Medical Image Computing and Computer-Assisted Intervention (MICCAI),
Toronto, Canada, 2011.

The data was used to predict the relative location of CT slices on
the axial axis using k-nearest neighbor search.

2. F. Graf, H.-P. Kriegel, S. PÃ¶lsterl, M. Schubert, A. Cavallaro
Position Prediction in CT Volume Scans
In Proceedings of the 28th International Conference on Machine
Learning (ICML) Workshop on Learning for Global Challenges,
Bellevue, Washington, WA, 2011.

Here, the data was used to apply weighted combinations of image
features for the localization of small sub volumes in CT scans.

3. Cheng, Ming-Yen, and Hau-tieng Wu. "Local Linear Regression on Manifolds and its Geometric Interpretation." arXiv preprint (2012).



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00206/slice_localization_data.zip")

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00206/slice_localization_data.zip")

print(df.info())