import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Image data described by high-level numeric-valued attributes, 7 classes

Data Set Characteristics:  

Multivariate

Number of Instances:

2310

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

19

Date Donated

1990-11-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

251043


Source:

Creators:

Vision Group, University of Massachusetts

Donor:

Vision Group (Carla Brodley, brodley '@' cs.umass.edu)


Data Set Information:

The instances were drawn randomly from a database of 7 outdoor images. The images were handsegmented to create a classification for every pixel.

Each instance is a 3x3 region.


Attribute Information:

1. region-centroid-col: the column of the center pixel of the region.
2. region-centroid-row: the row of the center pixel of the region.
3. region-pixel-count: the number of pixels in a region = 9.
4. short-line-density-5: the results of a line extractoin algorithm that counts how many lines of length 5 (any orientation) with low contrast, less than or equal to 5, go through the region.
5. short-line-density-2: same as short-line-density-5 but counts lines of high contrast, greater than 5.
6. vedge-mean: measure the contrast of horizontally adjacent pixels in the region. There are 6, the mean and standard deviation are given. This attribute is used as a vertical edge detector.
7. vegde-sd: (see 6)
8. hedge-mean: measures the contrast of vertically adjacent pixels. Used for horizontal line detection.
9. hedge-sd: (see 8).
10. intensity-mean: the average over the region of (R + G + B)/3
11. rawred-mean: the average over the region of the R value.
12. rawblue-mean: the average over the region of the B value.
13. rawgreen-mean: the average over the region of the G value.
14. exred-mean: measure the excess red: (2R - (G + B))
15. exblue-mean: measure the excess blue: (2B - (G + R))
16. exgreen-mean: measure the excess green: (2G - (R + B))
17. value-mean: 3-d nonlinear transformation of RGB. (Algorithm can be found in Foley and VanDam, Fundamentals of Interactive Computer Graphics)
18. saturatoin-mean: (see 17)
19. hue-mean: (see 17)


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Anthony K H Tung and Xin Xu and Beng Chin Ooi. CURLER: Finding and Visualizing Nonlinear Correlated Clusters. SIGMOD Conference. 2005. [View Context].

Xiaoli Z. Fern and Carla Brodley. Cluster Ensembles for High Dimensional Clustering: An Empirical Study. Journal of Machine Learning Research n, a. 2004. [View Context].

Manoranjan Dash and Huan Liu and Peter Scheuermann and Kian-Lee Tan. Fast hierarchical clustering and its validation. Data Knowl. Eng, 44. 2003. [View Context].

Aristidis Likas and Nikos A. Vlassis and Jakob J. Verbeek. The global k-means clustering algorithm. Pattern Recognition, 36. 2003. [View Context].

James Tin and Yau Kwok. Moderating the Outputs of Support Vector Machine Classifiers. Department of Computer Science Hong Kong Baptist University Hong Kong. [View Context].

Thomas T. Osugi and M. S. EXPLORATION-BASED ACTIVE MACHINE LEARNING. Faculty of The Graduate College at the University of Nebraska In Partial Fulfillment of Requirements. [View Context].

Nikos A. Vlassis and Aristidis Likas. A greedy EM algorithm for Gaussian mixture. Intelligent Autonomous Systems, IAS. [View Context].

Amund Tveit. Empirical Comparison of Accuracy and Performance for the MIPSVM classifier with Existing Classifiers. Division of Intelligent Systems Department of Computer and Information Science, Norwegian University of Science and Technology. [View Context].

Je Scott and Mahesan Niranjan and Richard W. Prager. Realisable Classifiers: Improving Operating Performance on Variable Cost Problems. Cambridge University Department of Engineering. [View Context].

C. Titus Brown and Harry W. Bullen and Sean P. Kelly and Robert K. Xiao and Steven G. Satterfield and John G. Hagedorn and Judith E. Devaney. Visualization and Data Mining in an 3D Immersive Environment: Summer Project 2003. [View Context].

Adil M. Bagirov and Alex Rubinov and A. N. Soukhojak and John Yearwood. Unsupervised and supervised data classification via nonsmooth and global optimization. School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

K. A. J Doherty and Rolf Adams and Neil Davey. Unsupervised Learning with Normalised Data and Non-Euclidean Norms. University of Hertfordshire. [View Context].

Adil M. Bagirov and John Yearwood. A new nonsmooth optimization algorithm for clustering. Centre for Informatics and Applied Optimization, School of Information Technology and Mathematical Sciences, University of Ballarat. [View Context].

K. A. J Doherty and Rolf Adams and Neil Davey. Non-Euclidean Norms and Data Normalisation. Department of Computer Science, University of Hertfordshire, College Lane. [View Context].

Michael Lindenbaum and Shaul Markovitch and Dmitry Rusakov. Selective Sampling Using Random Field Modelling. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/image/segmentation.data"
,names=['region_centroid_col', 'region_centroid_row', 'region_pixel_count', 'short_line_density_5', 'short_line_density_2', 'vedge_mean', 'vegde_sd', 'hedge_mean', 'hedge_sd', 'intensity_mean', 'rawred_mean', 'rawblue_mean', 'rawgreen_mean', 'exred_mean', 'exblue_mean', 'exgreen_mean', 'value_mean', 'saturatoin_mean', 'hue_mean'])

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/image/segmentation.data"
, names=['region_centroid_col', 'region_centroid_row', 'region_pixel_count', 'short_line_density_5', 'short_line_density_2', 'vedge_mean', 'vegde_sd', 'hedge_mean', 'hedge_sd', 'intensity_mean', 'rawred_mean', 'rawblue_mean', 'rawgreen_mean', 'exred_mean', 'exblue_mean', 'exgreen_mean', 'value_mean', 'saturatoin_mean', 'hue_mean'])

print(df.info())
print(df_test.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/image/segmentation.data"
,names=['region_centroid_col', 'region_centroid_row', 'region_pixel_count', 'short_line_density_5', 'short_line_density_2', 'vedge_mean', 'vegde_sd', 'hedge_mean', 'hedge_sd', 'intensity_mean', 'rawred_mean', 'rawblue_mean', 'rawgreen_mean', 'exred_mean', 'exblue_mean', 'exgreen_mean', 'value_mean', 'saturatoin_mean', 'hue_mean'])

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/image/segmentation.data"
, names=['region_centroid_col', 'region_centroid_row', 'region_pixel_count', 'short_line_density_5', 'short_line_density_2', 'vedge_mean', 'vegde_sd', 'hedge_mean', 'hedge_sd', 'intensity_mean', 'rawred_mean', 'rawblue_mean', 'rawgreen_mean', 'exred_mean', 'exblue_mean', 'exgreen_mean', 'value_mean', 'saturatoin_mean', 'hue_mean'])

print(df.info())
print(df_test.info())