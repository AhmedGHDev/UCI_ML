import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Various Databases: Vehicle silhouttes, Landsat Sattelite, Shuttle, Australian Credit Approval, Heart Disease, Image Segmentation, German Credit

Data Set Characteristics:  

N/A

Number of Instances:

N/A

Area:

N/A

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

1992-10-01

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

57747


Source:

Origin:

The Stalog databases are a subset of the datasets used in the European Statlog project.

Donor:

Ross D. King
Department of Statistics and Modelling Science
University of Strathclyde
Glasgow G1 1XH
Scotland
U.K.
+44 41 552-4400 x 3033
Fax +44 41 552-4711
ross '@' turing.uk.ac


Data Set Information:

The databases available here were in used in the European StatLog project, which involves comparing the performances of machine learning, statistical, and neural network algorithms on data sets from real-world industrial areas including medicine, finance, image analysis, and engineering design. Not all of the databases used in the project are available in this repository.

Databases:

(a) Vehicle Silhouettes:

The original purpose was to find a method of distinguishing 3D objects within a 2D image by application of an ensemble of shape feature extractors to the 2D silhouettes of the objects.

(b) Landsat Satellite:

The database consists of the multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood. The aim is to predict this classification, given the multi-spectral values. In the sample database, the class of a pixel is coded as a number.

(c) Shuttle:

The shuttle dataset contains 9 attributes all of which are numerical. Approximately 80% of the data belongs to class 1.

(d) Australian Credit Approval:

This file concerns credit card applications. All attribute names and values have been changed to meaningless symbols to protect confidentiality of the data. This database exists elsewhere in the repository (Credit Screening Database) in a slightly different form.

(e) Heart Disease:

This dataset is a heart disease database similar to a database already present in the repository (Heart Disease databases) but in a slightly different form. This database contains 13 attributes (which have been extracted from a larger set of 75).

(f) Image Segmentation:

This dataset is an image segmentation database similar to a database already present in the repository (Image segmentation database) but in a slightly different form. The instances were drawn randomly from a database of 7 outdoor images. The images were handsegmented to create a classification for every pixel. Each instance is a 3x3 region.

(g) German Credit:

This dataset classifies people described by a set of attributes as good or bad credit risks. Comes in two formats (one all numeric). Also comes with a cost matrix.


Attribute Information:

N/A


Relevant Papers:

Feng,C., Sutherland,A., King,S., Muggleton,S. & Henery,R. (1993). Comparison of Machine Learning Classifiers to Statistics and Neural Networks. AI & Stats Conf. 93.
[Web Link]


Papers That Cite This Data Set1:


Wei-Chun Kao and Kai-Min Chung and Lucas Assun and Chih-Jen Lin. Decomposition Methods for Linear Support Vector Machines. Neural Computation, 16. 2004. [View Context].

Xiaoli Z. Fern and Carla Brodley. Cluster Ensembles for High Dimensional Clustering: An Empirical Study. Journal of Machine Learning Research n, a. 2004. [View Context].

Gavin Brown. Diversity in Neural Network Ensembles. The University of Birmingham. 2004. [View Context].

Jeroen Eggermont and Joost N. Kok and Walter A. Kosters. Genetic Programming for data classification: partitioning the search space. SAC. 2004. [View Context].

Zoubin Ghahramani and Hyun-Chul Kim. Bayesian Classifier Combination. Gatsby Computational Neuroscience Unit University College London. 2003. [View Context].

Bart Hamers and J. A. K Suykens. Coupled Transductive Ensemble Learning of Kernel Models. Bart De Moor. 2003. [View Context].

Jun Wang and Bin Yu and Les Gasser. Concept Tree Based Clustering Visualization with Shaded Similarity Matrices. ICDM. 2002. [View Context].

Ramesh Natarajan and Edwin P D Pednault. Segmented Regression Estimators for Massive Data Sets. SDM. 2002. [View Context].

Jochen Garcke and Michael Griebel and Michael Thess. Data Mining with Sparse Grids. Computing, 67. 2001. [View Context].

Avelino J. Gonzalez and Lawrence B. Holder and Diane J. Cook. Graph-Based Concept Learning. FLAIRS Conference. 2001. [View Context].

Edgar Acuna and Alex Rojas. Ensembles of classifiers based on Kernel density estimators. Department of Mathematics University of Puerto Rico. 2000. [View Context].

Haixun Wang and Carlo Zaniolo. CMP: A Fast Decision Tree Classifier Using Multivariate Predictions. ICDE. 2000. [View Context].

Cesar Guerra-Salcedo and L. Darrell Whitley. Genetic Approach to Feature Selection for Ensemble Creation. GECCO. 1999. [View Context].

Guido Lindner and Rudi Studer. AST: Support for Algorithm Selection with a CBR Approach. PKDD. 1999. [View Context].

Ljupco Todorovski and Saso Dzeroski. Experiments in Meta-level Learning with ILP. PKDD. 1999. [View Context].

Art B. Owen. Tubular neighbors for regression and classification. Stanford University. 1999. [View Context].

Robert E. Schapire and Yoav Freund and Peter Bartlett and Wee Sun Lee. The Annals of Statistics, to appear. Boosting the Margin: A New Explanation for the Effectiveness of Voting Methods. AT&T Labs. 1998. [View Context].

Khaled A. Alsabti and Sanjay Ranka and Vineet Singh. CLOUDS: A Decision Tree Classifier for Large Datasets. KDD. 1998. [View Context].

Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja. Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF. Appl. Intell, 7. 1997. [View Context].

Oya Ekin and Peter L. Hammer and Alexander Kogan and Pawel Winter. Distance-Based Classification Methods. e p o r t RUTCOR ffl Rutgers Center for Operations Research ffl Rutgers University. 1996. [View Context].

Georgios Paliouras and David S. Brée. The Effect of Numeric Features on the Scalability of Inductive Learning Programs. ECML. 1995. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Ron Kohavi and George H. John and Richard Long and David Manley and Karl Pfleger. MLC++: A Machine Learning Library in C. ICTAI. 1994. [View Context].

Krzysztof Grabczewski and Wl/odzisl/aw Duch. THE SEPARABILITY OF SPLIT VALUE CRITERION. Department of Computer Methods, Nicolaus Copernicus University. [View Context].

C. esar and Cesar Guerra-Salcedo and Darrell Whitley. Feature Selection Mechanisms for Ensemble Creation : A Genetic Search Perspective. Department of Computer Science Colorado State University. [View Context].

Elena Smirnova and Ida G. Sprinkhuizen-Kuyper and I. Nalbantis and b. ERIM and Universiteit Rotterdam. Unanimous Voting using Support Vector Machines. IKAT, Universiteit Maastricht. [View Context].

Ron Kohavi and Barry G. Becker and Dan Sommerfield. Improving Simple Bayes. Data Mining and Visualization Group Silicon Graphics, Inc. [View Context].

Wl odzisl and aw Duch. Control and Cybernetics. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl odzisl/aw Duch and Rudy Setiono and Jacek M. Zurada. Computational intelligence methods for rule-based data understanding. [View Context].

Wl/odzisl/aw Duch and Rafal/ Adamczak Email:duchraad@phys. uni. torun. pl. Statistical methods for construction of neural networks. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Chih-Wei Hsu and Cheng-Ru Lin. A Comparison of Methods for Multi-class Support Vector Machines. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Wl/odzisl/aw Duch. Support Vector Neural Training. Index Terms--. [View Context].

Alexander K. Seewald. Meta-Learning for Stacked Classification. Austrian Research Institute for Artificial Intelligence. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Meta-learning: searching in the model space. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Kuan-ming Lin and Chih-Jen Lin. A Study on Reduced Support Vector Machines. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Je Scott and Mahesan Niranjan and Richard W. Prager. Realisable Classifiers: Improving Operating Performance on Variable Cost Problems. Cambridge University Department of Engineering. [View Context].

Yishay Mansour. Pessimistic decision tree pruning based on tree size. Computer Science Dept. Tel-Aviv University. [View Context].

Guido Lindner and Rudi Studer. Algorithm Selection Support for Classification. DaimlerChrysler AG, Research & Technology FT3/KL. [View Context].

Ron Kohavi and George H. John. Automatic Parameter Selection by Minimizing Estimated Error. Computer Science Dept. Stanford University. [View Context].

Iñaki Inza and Pedro Larraaga and Ramon Etxeberria and Basilio Sierra. Feature Subset Selection by Bayesian networks based optimization. Dept. of Computer Science and Artificial Intelligence. University of the Basque Country. [View Context].

Ron Kohavi and George John and Richard Long and David Manley and Karl Pfleger. Appears in Tools with AI '94. Computer Science Department Stanford University. [View Context].

H. -T Lin and C. -J Lin. A Study on Sigmoid Kernels for SVM and the Training of non-PSD Kernels by SMO-type Methods. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Jun Wang. Classification Visualization with Shaded Similarity Matrix. Bei Yu Les Gasser Graduate School of Library and Information Science University of Illinois at Urbana-Champaign. [View Context].

Rong-En Fan and P. -H Chen and C. -J Lin. Working Set Selection Using the Second Order Information for Training SVM. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Wl odzisl/aw Duch and Karol Grudzinski. Search and global minimization in similarity-based methods. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl odzisl and aw Duch. Committees of Undemocratic Competent Models. School of Computer Engineering Nanyang Technological University. [View Context].



Citation Request:

Any publications based on these datasets should include an acknowledgment of the original sources of the datasets.
"""