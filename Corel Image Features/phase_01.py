import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset contains image features extracted from a Corel image collection. Four sets of features are available based on the color histogram, color histogram layout, color moments, and co-occurence


Data Set Characteristics:  

Multivariate

Number of Instances:

68040

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

89

Date Donated

1999-07-01

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

103256


Source:

Original Owner:

Michael Ortega-Binderberger
Information and Computer Science
University of California at Irvine
Irvine, CA 92697-3425
USA
miki '@' ics.uci.edu

Donor:

Kriengkrai Porkaew and Sharad Mehrotra
Information and Computer Science
University of California at Irvine
Irvine, CA 92697-3425
USA
nid '@' ics.uci.edu,sharad '@' ics.uci.edu



Data Set Information:

The original image collection was obtained from Corel at [Web Link]. There are 68,040 photo images from various categories.

Each set of features is stored in a separate file. For each file, a line corresponds to a single image. The first value in a line is is the image ID and the subsequent values are the feature vector (e.g. color histogram, etc.) of the image. The same image has the same ID in all files but the image ID is not the same as the image filename.


Attribute Information:

From each image four sets of features were extracted:

- Color Histogram
- Color Histogram Layout
- Color Moments
- Co-occurrence Texture

Color Histogram: 32 dimensions (8 x 4 = H x S)
- HSV color space is divided into 32 subspaces (32 colors : 8 ranges of H and 4 ranges of S).
- the value in each dimension in a ColorHistogram of an image is the density of each color in the entire image.
- Histogram intersection (overlap area between ColorHistograms of two images) can be used to measure the similarity between two images.

Color Histogram Layout: 32 dimensions (4 x 2 x 4 = H x S x sub-images)
- each image is divided into 4 sub-images (one horizontal split and one vertical split).
- 4x2 Color Histogram for each sub-image is computed.
- Histogram Intersection can be used to measure the similarity between two images.

Color Moments: 9 dimensions (3 x 3)
- the 9 values are: (one for each of H,S, and V in HSV color space)
-- mean,
-- standard deviation, and
-- skewness.
- Euclidean distance between Color Moments of two images can be used to represent the dis-similarity (distance) between two images.

Co-occurrence Texture: 16 dimensions (4 x 4)
- images are converted to 16 gray-scale images.
- co-ocurrence in 4 directions is computed (horizontal, vertical, and two diagonal directions). the 16 values are: (one for each direction).
-- Second Angular Moment,
-- Contrast,
I -- nverse Difference Moment, and
-- Entropy.
-Euclidean distance between ColorMoments of two images can be used to measure the dis-similarity (distance) between two images.


Relevant Papers:

Michael Ortega, Yong Rui, Kaushik Chakrabarti, Kriengkrai Porkaew, Sharad Mehrotra, and Thomas S. Huang, Supporting Ranked Boolean Similarity Queries in MARS, IEEE Transaction on Knowledge and Data Engineering, Vol. 10, No. 6, Pages 905-925, December 1998.
[Web Link]

Kaushik Chakrabarti, and Sharad Mehrotra, The Hybrid Tree: An Index Structure for High Dimensional Feature Spaces, 1999 IEEE International Conference on Data Engineering (ICDE), Pages 440-447, February, 1999.
[Web Link]

Kriengkrai Porkaew, Kaushik Chakrabarti, and Sharad Mehrotra, Query Refinement for Multimedia Retrieval and its Evaluation Techniques in MARS, 1999 ACM International Multimedia Conference, Orlando, Florida, Oct 30 - Nov 4, 1999.
[Web Link]

Kaushik Chakrabarti, Kriengkrai Porkaew, and Sharad Mehrotra, Efficient Query Refinement in Multimedia Databases, ICDE, 2000
[Web Link]


Papers That Cite This Data Set1:


Thomas T. Osugi and M. S. EXPLORATION-BASED ACTIVE MACHINE LEARNING. Faculty of The Graduate College at the University of Nebraska In Partial Fulfillment of Requirements. [View Context].



Citation Request:

This data may be used for non-commercial purposes only.
"""

#FROM URL
"""
df_c = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/ColorHistogram.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['c_'+str(i) for i in range(1, 33)]
)

df_l = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/LayoutHistogram.asc.gz"
,compression='gzip'
,delimiter='\s+'
,skiprows=62481
,names=['l_'+str(i) for i in range(1, 34)]
)

df_m = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/ColorMoments.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['H', 'S', 'V', 'mean', 'std', 'skewness','dis_01', 'dis_02', 'dis_03'])

df_t = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/CoocTexture.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['t_'+str(i) for i in range(1, 17)]
)

df = pd.concat([df_c, df_l, df_m, df_t], axis=1)

print(df.info())
"""

#LOACL
df_c = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/ColorHistogram.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['c_'+str(i) for i in range(1, 33)]
)

df_l = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/LayoutHistogram.asc.gz"
,compression='gzip'
,delimiter='\s+'
,skiprows=62481
,names=['l_'+str(i) for i in range(1, 34)]
)

df_m = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/CorelFeatures-mld/ColorMoments.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['H', 'S', 'V', 'mean', 'std', 'skewness','dis_01', 'dis_02', 'dis_03'])

df_t = pd.read_csv("../uci.edu/ml/machine-learning-databases/CorelFeatures-mld/CoocTexture.asc.gz"
,compression='gzip'
,delimiter='\s+'
,names=['t_'+str(i) for i in range(1, 17)]
)

df = pd.concat([df_c, df_l, df_m, df_t], axis=1)
print(df.info())
