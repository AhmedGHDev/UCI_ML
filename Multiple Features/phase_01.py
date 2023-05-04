import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset consists of features of handwritten numerals (`0'--`9') extracted from a collection of Dutch utility maps

Data Set Characteristics:  

Multivariate

Number of Instances:

2000

Area:

Computer

Attribute Characteristics:

Integer, Real

Number of Attributes:

649

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

146646


Source:

Robert P.W. Duin
Department of Applied Physics
Delft University of Technology
P.O. Box 5046, 2600 GA Delft
The Netherlands

email: duin '@' ph.tn.tudelft.nl
http : //www.ph.tn.tudelft.nl/~duin
tel +31 15 2786143


Data Set Information:

This dataset consists of features of handwritten numerals (`0'--`9') extracted from a collection of Dutch utility maps. 200 patterns per class (for a total of 2,000 patterns) have been digitized in binary images. These digits are represented in terms of the following six feature sets (files):

1. mfeat-fou: 76 Fourier coefficients of the character shapes;
2. mfeat-fac: 216 profile correlations;
3. mfeat-kar: 64 Karhunen-Love coefficients;
4. mfeat-pix: 240 pixel averages in 2 x 3 windows;
5. mfeat-zer: 47 Zernike moments;
6. mfeat-mor: 6 morphological features.

In each file the 2000 patterns are stored in ASCI on 2000 lines. The first 200 patterns are of class `0', followed by sets of 200 patterns for each of the classes `1' - `9'. Corresponding patterns in different feature sets (files) correspond to the same original character.

The source image dataset is lost. Using the pixel-dataset (mfeat-pix) sampled versions of the original images may be obtained (15 x 16 pixels).


Attribute Information:

6 Files:
1. mfeat-fou: 76 Fourier coefficients of the character shapes;
2. mfeat-fac: 216 profile correlations;
3. mfeat-kar: 64 Karhunen-Love coefficients;
4. mfeat-pix: 240 pixel averages in 2 x 3 windows;
5. mfeat-zer: 47 Zernike moments;
6. mfeat-mor: 6 morphological features.


Relevant Papers:

M. van Breukelen, R.P.W. Duin, D.M.J. Tax, and J.E. den Hartog, Handwritten digit recognition by combined classifiers, Kybernetika, vol. 34, no. 4, 1998, 381-386.
[Web Link]

M. van Breukelen and R.P.W. Duin, Neural Network Initialization by Combined Classifiers, in: A.K. Jain, S. Venkatesh, B.C. Lovell (eds.), ICPR'98, Proc. 14th Int. Conference on Pattern Recognition (Brisbane, Aug. 16-20),

A.K. Jain, R.P.W. Duin, J. Mao, Statisitcal Pattern Recognition: A Review, in preparation


Papers That Cite This Data Set1:


Xiaoli Z. Fern and Carla Brodley. Cluster Ensembles for High Dimensional Clustering: An Empirical Study. Journal of Machine Learning Research n, a. 2004. [View Context].

Jaakko Peltonen and Samuel Kaski. Discriminative Components of Data. IEEE. 2004. [View Context].

Xiaofeng He and Partha Niyogi. Locality Preserving Projections. NIPS. 2003. [View Context].

Simon Perkins and James Theiler. Online Feature Selection using Grafting. ICML. 2003. [View Context].

Pavel Paclik and Robert P W Duin and Geert M. P. van Kempen and Reinhard Kohlus. On Feature Selection with Measurement Cost and Grouped Features. Pattern Recognition Group, Delft University of Technology. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data", names=['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data", names=['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat'])

print(df.info())