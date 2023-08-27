import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood


Data Set Characteristics:  

Multivariate

Number of Instances:

6435

Area:

Physical

Attribute Characteristics:

Integer

Number of Attributes:

36

Date Donated

1993-02-13

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

166942


Source:

Ashwin Srinivasan
Department of Statistics and Data Modeling
University of Strathclyde
Glasgow
Scotland
UK
ross '@' uk.ac.turing

The original Landsat data for this database was generated
from data purchased from NASA by the Australian Centre
for Remote Sensing, and used for research at:
The Centre for Remote Sensing
University of New South Wales
Kensington, PO Box 1
NSW 2033
Australia.

The sample database was generated taking a small section (82
rows and 100 columns) from the original data. The binary values
were converted to their present ASCII form by Ashwin Srinivasan.
The classification for each pixel was performed on the basis of
an actual site visit by Ms. Karen Hall, when working for Professor
John A. Richards, at the Centre for Remote Sensing at the University
of New South Wales, Australia. Conversion to 3x3 neighbourhoods and
splitting into test and training sets was done by Alistair Sutherland.


Data Set Information:

The database consists of the multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood. The aim is to predict this classification, given the multi-spectral values. In the sample database, the class of a pixel is coded as a number.

The Landsat satellite data is one of the many sources of information available for a scene. The interpretation of a scene by integrating spatial data of diverse types and resolutions including multispectral and radar data, maps indicating topography, land use etc. is expected to assume significant importance with the onset of an era characterised by integrative approaches to remote sensing (for example, NASA's Earth Observing System commencing this decade). Existing statistical methods are ill-equipped for handling such diverse data types. Note that this is not true for Landsat MSS data considered in isolation (as in this sample database). This data satisfies the important requirements of being numerical and at a single resolution, and standard maximum-likelihood classification performs very well. Consequently, for this data, it should be interesting to compare the performance of other methods against the statistical approach.

One frame of Landsat MSS imagery consists of four digital images of the same scene in different spectral bands. Two of these are in the visible region (corresponding approximately to green and red regions of the visible spectrum) and two are in the (near) infra-red. Each pixel is a 8-bit binary word, with 0 corresponding to black and 255 to white. The spatial resolution of a pixel is about 80m x 80m. Each image contains 2340 x 3380 such pixels.

The database is a (tiny) sub-area of a scene, consisting of 82 x 100 pixels. Each line of data corresponds to a 3x3 square neighbourhood of pixels completely contained within the 82x100 sub-area. Each line contains the pixel values in the four spectral bands (converted to ASCII) of each of the 9 pixels in the 3x3 neighbourhood and a number indicating the classification label of the central pixel. The number is a code for the following classes:

Number Class
1 red soil
2 cotton crop
3 grey soil
4 damp grey soil
5 soil with vegetation stubble
6 mixture class (all types present)
7 very damp grey soil

NB. There are no examples with class 6 in this dataset.

The data is given in random order and certain lines of data have been removed so you cannot reconstruct the original image from this dataset.

In each line of data the four spectral values for the top-left pixel are given first followed by the four spectral values for the top-middle pixel and then those for the top-right pixel, and so on with the pixels read out in sequence left-to-right and top-to-bottom. Thus, the four spectral values for the central pixel are given by attributes 17,18,19 and 20. If you like you can use only these four attributes, while ignoring the others. This avoids the problem which arises when a 3x3 neighbourhood straddles a boundary.


Attribute Information:

The attributes are numerical, in the range 0 to 255.


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Ken Tang and Ponnuthurai N. Suganthan and Xi Yao and A. Kai Qin. Linear dimensionalityreduction using relevance weighted LDA. School of Electrical and Electronic Engineering Nanyang Technological University. 2005. [View Context].

Giorgio Valentini. Random Aggregated and Bagged Ensembles of SVMs: An Empirical Bias?Variance Analysis. Multiple Classifier Systems. 2004. [View Context].

Xiaoli Z. Fern and Carla Brodley. Cluster Ensembles for High Dimensional Clustering: An Empirical Study. Journal of Machine Learning Research n, a. 2004. [View Context].

Jaakko Peltonen and Samuel Kaski. Discriminative Components of Data. IEEE. 2004. [View Context].

S. Augustine Su and Jennifer G. Dy. Automated hierarchical mixtures of probabilistic principal component analyzers. ICML. 2004. [View Context].

Jaakko Peltonen and Arto Klami and Samuel Kaski. Improved Learning of Riemannian Metrics for Exploratory Analysis. Improved Learning of Riemannian Metrics for Exploratory Analysis. Neural Networks. 2004. [View Context].

Fabian Hoti and Lasse Holmström. A semiparametric density estimation approach to pattern classification. Pattern Recognition, 37. 2004. [View Context].

Giorgio Valentini and Thomas G. Dietterich. Low Bias Bagged Support Vector Machines. ICML. 2003. [View Context].

Zoubin Ghahramani and Hyun-Chul Kim. Bayesian Classifier Combination. Gatsby Computational Neuroscience Unit University College London. 2003. [View Context].

Giorgio Valentini. Ensemble methods based on bias--variance analysis Theses Series DISI-TH-2003. Dipartimento di Informatica e Scienze dell'Informazione . 2003. [View Context].

Igor V. Tetko. Associative Neural Network. Neural Processing Letters, 16. 2002. [View Context].

Jaakko Peltonen and Arto Klami and Samuel Kaski. Learning More Accurate Metrics for Self-Organizing Maps. ICANN. 2002. [View Context].

Peter Sykacek and Stephen J. Roberts. Adaptive Classification by Variational Kalman Filtering. NIPS. 2002. [View Context].

Stephen D. Bay. Multivariate Discretization for Set Mining. Knowl. Inf. Syst, 3. 2001. [View Context].

Kagan Tumer and Joydeep Ghosh. Robust Combining of Disparate Classifiers through Order Statistics. CoRR, csLG/9905013. 1999. [View Context].

Kagan Tumer and Nikunj C. Oza. Decimated Input Ensembles for Improved Generalization. NASA Ames Research Center. 1999. [View Context].

Xavier Giannakopoulos and Juha Karhunen and Erkki Oja. An Experimental Comparison of Neural Algorithms for Independent Component Analysis and Blind Separation. Int. J. Neural Syst, 9. 1999. [View Context].

Cesar Guerra-Salcedo and L. Darrell Whitley. Genetic Approach to Feature Selection for Ensemble Creation. GECCO. 1999. [View Context].

Robert E. Schapire and Yoav Freund and Peter Bartlett and Wee Sun Lee. The Annals of Statistics, to appear. Boosting the Margin: A New Explanation for the Effectiveness of Voting Methods. AT&T Labs. 1998. [View Context].

Xavier Giannakopoulos and Juha Karhunen and Erkki Oja. A COMPARISON OF NEURAL ICA ALGORITHMS USING REAL-WORLD DATA. IDSIA. [View Context].

Adil M. Bagirov and Julien Ugon. An algorithm for computation of piecewise linear function separating two sets. CIAO, School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

Giorgio Valentini. An experimental bias--variance analysis of SVM ensembles based on resampling techniques. [View Context].

Cesar Guerra-Salcedo and Stephen Chen and Darrell Whitley and Sarah Smith. Fast and Accurate Feature Selection Using Hybrid Genetic Strategies. Department of Computer Science Colorado State University. [View Context].

Je Scott and Mahesan Niranjan and Richard W. Prager. Realisable Classifiers: Improving Operating Performance on Variable Cost Problems. Cambridge University Department of Engineering. [View Context].

Vikas Sindhwani and P. Bhattacharya and Subrata Rakshit. Information Theoretic Feature Crediting in Multiclass Support Vector Machines. [View Context].

Jaakko Peltonen and Arto Klami and Samuel Kaski. Learning Metrics for Information Visualization. Neural Networks Research Centre Helsinki University of Technology. [View Context].

C. esar and Cesar Guerra-Salcedo and Darrell Whitley. Feature Selection Mechanisms for Ensemble Creation : A Genetic Search Perspective. Department of Computer Science Colorado State University. [View Context].

Grigorios Tsoumakas and Ioannis P. Vlahavas. Fuzzy Meta-Learning: Preliminary Results. Greek Secretariat for Research and Technology. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/satimage/sat.trn"
,delimiter='\s+'
,names=['A_'+str(i) for i in range(1, 36)] + ['class']
)

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/satimage/sat.tst"
,delimiter='\s+'
,names=['A_'+str(i) for i in range(1, 36)] + ['class']
)


print(df_train.info())
print(df_test.info())
"""

#LOACL
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/statlog/satimage/sat.trn"
,delimiter='\s+'
,names=['A_'+str(i) for i in range(1, 36)] + ['class']
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/statlog/satimage/sat.tst"
,delimiter='\s+'
,names=['A_'+str(i) for i in range(1, 36)] + ['class']
)


print(df_train.info())
print(df_test.info())