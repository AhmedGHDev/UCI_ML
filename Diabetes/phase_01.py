import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This diabetes dataset is from AIM '94

Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

N/A

Area:

Life

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

20

Date Donated

N/A

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

742103


Source:

Michael Kahn, MD, PhD, Washington University, St. Louis, MO


Data Set Information:

Diabetes patient records were obtained from two sources: an automatic electronic recording device and paper records. The automatic device had an internal clock to timestamp events, whereas the paper records only provided "logical time" slots (breakfast, lunch, dinner, bedtime). For paper records, fixed times were assigned to breakfast (08:00), lunch (12:00), dinner (18:00), and bedtime (22:00). Thus paper records have fictitious uniform recording times whereas electronic records have more realistic time stamps.

Diabetes files consist of four fields per record. Each field is separated by a tab and each record is separated by a newline.

File Names and format:
(1) Date in MM-DD-YYYY format
(2) Time in XX:YY format
(3) Code
(4) Value

The Code field is deciphered as follows:

33 = Regular insulin dose
34 = NPH insulin dose
35 = UltraLente insulin dose
48 = Unspecified blood glucose measurement
57 = Unspecified blood glucose measurement
58 = Pre-breakfast blood glucose measurement
59 = Post-breakfast blood glucose measurement
60 = Pre-lunch blood glucose measurement
61 = Post-lunch blood glucose measurement
62 = Pre-supper blood glucose measurement
63 = Post-supper blood glucose measurement
64 = Pre-snack blood glucose measurement
65 = Hypoglycemic symptoms
66 = Typical meal ingestion
67 = More-than-usual meal ingestion
68 = Less-than-usual meal ingestion
69 = Typical exercise activity
70 = More-than-usual exercise activity
71 = Less-than-usual exercise activity
72 = Unspecified special event


Attribute Information:

Diabetes files consist of four fields per record. Each field is separated by a tab and each record is separated by a newline.

File Names and format:
(1) Date in MM-DD-YYYY format
(2) Time in XX:YY format
(3) Code
(4) Value


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Jeroen Eggermont and Joost N. Kok and Walter A. Kosters. Genetic Programming for data classification: partitioning the search space. SAC. 2004. [View Context].

Zhi-Hua Zhou and Yuan Jiang. NeC4.5: Neural Ensemble Based C4.5. IEEE Trans. Knowl. Data Eng, 16. 2004. [View Context].

Prem Melville and Raymond J. Mooney. Diverse ensembles for active learning. ICML. 2004. [View Context].

Michael L. Raymer and Travis E. Doom and Leslie A. Kuhn and William F. Punch. Knowledge discovery in medical and biological datasets using a hybrid Bayes classifier/evolutionary algorithm. IEEE Transactions on Systems, Man, and Cybernetics, Part B, 33. 2003. [View Context].

Eibe Frank and Mark Hall. Visualizing Class Probability Estimators. PKDD. 2003. [View Context].

Zhihua Zhang and James T. Kwok and Dit-Yan Yeung. Parametric Distance Metric Learning with Label Information. IJCAI. 2003. [View Context].

Peter Sykacek and Stephen J. Roberts. Adaptive Classification by Variational Kalman Filtering. NIPS. 2002. [View Context].

Kristin P. Bennett and Ayhan Demiriz and Richard Maclin. Exploiting unlabeled data in ensemble methods. KDD. 2002. [View Context].

Marina Skurichina and Ludmila Kuncheva and Robert P W Duin. Bagging and Boosting for the Nearest Mean Classifier: Effects of Sample Size on Diversity and Accuracy. Multiple Classifier Systems. 2002. [View Context].

Krzysztof Krawiec. Genetic Programming-based Construction of Features for Machine Learning and Knowledge Discovery Tasks. Institute of Computing Science, Poznan University of Technology. 2002. [View Context].

Ilya Blayvas and Ron Kimmel. Multiresolution Approximation for Classification. CS Dept. Technion. 2002. [View Context].

Jochen Garcke and Michael Griebel and Michael Thess. Data Mining with Sparse Grids. Computing, 67. 2001. [View Context].

Peter L. Hammer and Alexander Kogan and Bruno Simeone and Sandor Szedm'ak. R u t c o r Research R e p o r t. Rutgers Center for Operations Research Rutgers University. 2001. [View Context].

Robert Burbidge and Matthew Trotter and Bernard F. Buxton and Sean B. Holden. STAR - Sparsity through Automated Rejection. IWANN (1). 2001. [View Context].

Endre Boros and Peter Hammer and Toshihide Ibaraki and Alexander Kogan and Eddy Mayoraz and Ilya B. Muchnik. An Implementation of Logical Analysis of Data. IEEE Trans. Knowl. Data Eng, 12. 2000. [View Context].

Simon Tong and Daphne Koller. Restricted Bayes Optimal Classifiers. AAAI/IAAI. 2000. [View Context].

Marina Skurichina and Robert P W Duin. Boosting in Linear Discriminant Analysis. Multiple Classifier Systems. 2000. [View Context].

Chris Drummond and Robert C. Holte. Exploiting the Cost (In)sensitivity of Decision Tree Splitting Criteria. ICML. 2000. [View Context].

Mark A. Hall. Correlation-based Feature Selection for Discrete and Numeric Class Machine Learning. ICML. 2000. [View Context].

Stavros J. Perantonis and Vassilis Virvilis. Input Feature Extraction for Multilayered Perceptrons Using Supervised Principal Component Analysis. Neural Processing Letters, 10. 1999. [View Context].

Art B. Owen. Tubular neighbors for regression and classification. Stanford University. 1999. [View Context].

Iñaki Inza and Pedro Larrañaga and Basilio Sierra and Ramon Etxeberria and Jose Antonio Lozano and Jos Manuel Peña. Representing the behaviour of supervised classification learning algorithms by Bayesian networks. Pattern Recognition Letters, 20. 1999. [View Context].

Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Thomas G. Dietterich. Approximate Statistical Test For Comparing Supervised Classification Learning Algorithms. Neural Computation, 10. 1998. [View Context].

Huan Liu and Rudy Setiono. Feature Transformation and Multivariate Decision Tree Induction. Discovery Science. 1998. [View Context].

Wojciech Kwedlo and Marek Kretowski. Discovery of Decision Rules from Databases: An Evolutionary Approach. PKDD. 1998. [View Context].

Jan C. Bioch and D. Meer and Rob Potharst. Bivariate Decision Trees. PKDD. 1997. [View Context].

Kristin P. Bennett and Erin J. Bredensteiner. A Parametric Optimization Method for Machine Learning. INFORMS Journal on Computing, 9. 1997. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Jennifer A. Blue and Kristin P. Bennett. Hybrid Extreme Point Tabu Search. Department of Mathematical Sciences Rensselaer Polytechnic Institute. 1996. [View Context].

Peter D. Turney. Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm. CoRR, csAI/9503102. 1995. [View Context].

Stefan R uping. A Simple Method For Estimating Conditional Probabilities For SVMs. CS Department, AI Unit Dortmund University. [View Context].

Adil M. Bagirov and John Yearwood. A new nonsmooth optimization algorithm for clustering. Centre for Informatics and Applied Optimization, School of Information Technology and Mathematical Sciences, University of Ballarat. [View Context].

Adil M. Bagirov and Alex Rubinov and A. N. Soukhojak and John Yearwood. Unsupervised and supervised data classification via nonsmooth and global optimization. School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].

Rudy Setiono and Huan Liu. Neural-Network Feature Selector. Department of Information Systems and Computer Science National University of Singapore. [View Context].

Charles Campbell and Nello Cristianini. Simple Learning Algorithms for Training Support Vector Machines. Dept. of Engineering Mathematics. [View Context].

Michael Lindenbaum and Shaul Markovitch and Dmitry Rusakov. Selective Sampling Using Random Field Modelling. [View Context].

Prem Melville and Raymond J. Mooney. Proceedings of the 21st International Conference on Machine Learning. Department of Computer Sciences. [View Context].

Fran ois Poulet. Cooperation between automatic algorithms, interactive algorithms and visualization tools for Visual Data Mining. ESIEA Recherche. [View Context].

Wl odzisl/aw Duch and Rudy Setiono and Jacek M. Zurada. Computational intelligence methods for rule-based data understanding. [View Context].

Liping Wei and Russ B. Altman. An Automated System for Generating Comparative Disease Profiles and Making Diagnoses. Section on Medical Informatics Stanford University School of Medicine, MSOB X215. [View Context].

Ilya Blayvas and Ron Kimmel. INVITED PAPER Special Issue on Multiresolution Analysis Machine Learning via Multiresolution Approximation. [View Context].

YongSeog Kim and W. Nick Street and Filippo Menczer. Optimal Ensemble Construction via Meta-Evolutionary Ensembles. Business Information Systems, Utah State University. [View Context].

Krzysztof Grabczewski and Wl/odzisl/aw Duch. THE SEPARABILITY OF SPLIT VALUE CRITERION. Department of Computer Methods, Nicolaus Copernicus University. [View Context].

Ilya Blayvas and Ron Kimmel. Efficient Classification via Multiresolution Training Set Approximation. CS Dept. Technion. [View Context].

Hussein A. Abbass. Pareto Neuro-Evolution: Constructing Ensemble of Neural Networks Using Multi-objective Optimization. Artificial Life and Adaptive Robotics (A.L.A.R.) Lab, School of Information Technology and Electrical Engineering, Australian Defence Force Academy. [View Context].

Matthias Scherf and W. Brauer. Feature Selection by Means of a Feature Weighting Approach. GSF - National Research Center for Environment and Health. [View Context].

Lena Kallin. Receiver operating characteristic (ROC) analysis Evaluating discriminance effects among decision support systems. Contents 1 The Theory of Receiver Operating Characteristic Curves 5. [View Context].

Rong-En Fan and P. -H Chen and C. -J Lin. Working Set Selection Using the Second Order Information for Training SVM. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Lawrence O. Hall and Nitesh V. Chawla and Kevin W. Bowyer. Combining Decision Trees Learned in Parallel. Department of Computer Science and Engineering, ENB 118 University of South Florida. [View Context].

Ahmed Hussain Khan and Intensive Care. Multiplier-Free Feedforward Networks. 174. [View Context].

Andrew Watkins and Jon Timmis and Lois C. Boggess. Artificial Immune Recognition System (AIRS): An ImmuneInspired Supervised Learning Algorithm. (abw5,jt6@kent.ac.uk) Computing Laboratory, University of Kent. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

