import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The task is to train a network to discriminate between sonar signals bounced off a metal cylinder and those bounced off a roughly cylindrical rock.

Data Set Characteristics:  

Multivariate

Number of Instances:

208

Area:

Physical

Attribute Characteristics:

Real

Number of Attributes:

60

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

264418


Source:

The data set was contributed to the benchmark collection by Terry Sejnowski, now at the Salk Institute and the University of California at San Deigo. The data set was developed in collaboration with R. Paul Gorman of Allied-Signal Aerospace Technology Center.


Data Set Information:

The file "sonar.mines" contains 111 patterns obtained by bouncing sonar signals off a metal cylinder at various angles and under various conditions. The file "sonar.rocks" contains 97 patterns obtained from rocks under similar conditions. The transmitted sonar signal is a frequency-modulated chirp, rising in frequency. The data set contains signals obtained from a variety of different aspect angles, spanning 90 degrees for the cylinder and 180 degrees for the rock.

Each pattern is a set of 60 numbers in the range 0.0 to 1.0. Each number represents the energy within a particular frequency band, integrated over a certain period of time. The integration aperture for higher frequencies occur later in time, since these frequencies are transmitted later during the chirp.

The label associated with each record contains the letter "R" if the object is a rock and "M" if it is a mine (metal cylinder). The numbers in the labels are in increasing order of aspect angle, but they do not encode the angle directly.


Attribute Information:

N/A


Relevant Papers:

1. Gorman, R. P., and Sejnowski, T. J. (1988). "Analysis of Hidden Units in a Layered Network Trained to Classify Sonar Targets" in Neural Networks, Vol. 1, pp. 75-89.
[Web Link]


Papers That Cite This Data Set1:


Zhi-Hua Zhou and Yuan Jiang. NeC4.5: Neural Ensemble Based C4.5. IEEE Trans. Knowl. Data Eng, 16. 2004. [View Context].

Jianbin Tan and David L. Dowe. MML Inference of Oblique Decision Trees. Australian Conference on Artificial Intelligence. 2004. [View Context].

Dennis DeCoste. Anytime Query-Tuned Kernel Machines via Cholesky Factorization. SDM. 2003. [View Context].

Jeremy Kubica and Andrew Moore. Probabilistic Noise Identification and Data Cleaning. ICDM. 2003. [View Context].

Michail Vlachos and Carlotta Domeniconi and Dimitrios Gunopulos and George Kollios and Nick Koudas. Non-linear dimensionality reduction techniques for classification and visualization. KDD. 2002. [View Context].

Xavier Llor and David E. Goldberg and Ivan Traus and Ester Bernad i Mansilla. Accuracy, Parsimony, and Generality in Evolutionary Learning Systems via Multiobjective Selection. IWLCS. 2002. [View Context].

Fei Sha and Lawrence K. Saul and Daniel D. Lee. Multiplicative Updates for Nonnegative Quadratic Programming in Support Vector Machines. NIPS. 2002. [View Context].

Marina Skurichina and Ludmila Kuncheva and Robert P W Duin. Bagging and Boosting for the Nearest Mean Classifier: Effects of Sample Size on Diversity and Accuracy. Multiple Classifier Systems. 2002. [View Context].

Dennis DeCoste. Anytime Interval-Valued Outputs for Kernel Machines: Fast Support Vector Machine Classification via Distance Geometry. ICML. 2002. [View Context].

Ayhan Demiriz and Kristin P. Bennett and Mark J. Embrechts. A Genetic Algorithm Approach for Semi-Supervised Clustering. E-Business Department, Verizon Inc.. 2002. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Ensembles of Similarity-based Models. Intelligent Information Systems. 2001. [View Context].

Chris Drummond and Robert C. Holte. Exploiting the Cost (In)sensitivity of Decision Tree Splitting Criteria. ICML. 2000. [View Context].

Carlotta Domeniconi and Jing Peng and Dimitrios Gunopulos. An Adaptive Metric Machine for Pattern Classification. NIPS. 2000. [View Context].

Lorne Mason and Peter L. Bartlett and Jonathan Baxter. Improved Generalization Through Explicit Optimization of Margins. Machine Learning, 38. 2000. [View Context].

Kristin P. Bennett and Ayhan Demiriz and John Shawe-Taylor. A Column Generation Algorithm For Boosting. ICML. 2000. [View Context].

Chris Drummond and Robert C. Holte. Explicitly representing expected cost: an alternative to ROC representation. KDD. 2000. [View Context].

Juan J. Rodr##guez and Carlos J. Alonso and Henrik Bostrom. Boosting Interval Based Literals. 2000. [View Context].

Kagan Tumer and Joydeep Ghosh. Robust Combining of Disparate Classifiers through Order Statistics. CoRR, csLG/9905013. 1999. [View Context].

Chun-Nan Hsu and Hilmar Schuschel and Ya-Ting Yang. The ANNIGMA-Wrapper Approach to Neural Nets Feature Selection for Knowledge Discovery and Data Mining. Institute of Information Science. 1999. [View Context].

Art B. Owen. Tubular neighbors for regression and classification. Stanford University. 1999. [View Context].

Stavros J. Perantonis and Vassilis Virvilis. Input Feature Extraction for Multilayered Perceptrons Using Supervised Principal Component Analysis. Neural Processing Letters, 10. 1999. [View Context].

Jing Peng and Bir Bhanu. Feature Relevance Estimation for Image Databases. Multimedia Information Systems. 1999. [View Context].

Lorne Mason and Jonathan Baxter and Peter L. Bartlett and Marcus Frean. Boosting Algorithms as Gradient Descent. NIPS. 1999. [View Context].

Ayhan Demiriz and Kristin P. Bennett and Mark J. Embrechts. Semi-Supervised Clustering Using Genetic Algorithms. Dept. 1999. [View Context].

Hiroshi Shimodaira and Jun Okui and Mitsuru Nakai. Modified Minimum Classification Error Learning and Its Application to Neural Networks. SSPR/SPR. 1998. [View Context].

Richard Maclin. Boosting Classifiers Regionally. AAAI/IAAI. 1998. [View Context].

Lorne Mason and Peter L. Bartlett and Jonathan Baxter. Direct Optimization of Margins Improves Generalization in Combined Classifiers. NIPS. 1998. [View Context].

Thomas G. Dietterich. Machine-Learning Research. AI Magazine, 18. 1997. [View Context].

Richard Maclin and David W. Opitz. An Empirical Evaluation of Bagging and Boosting. AAAI/IAAI. 1997. [View Context].

Perry Moerland and E. Fiesler and I. Ubarretxena-Belandia. Martigny - Valais - Suisse Discrete All-Positive Multilayer Perceptrons for Optical Implementation. E S E A R C H R E P R O R T I D I A P. 1997. [View Context].

Erin J. Bredensteiner and Kristin P. Bennett. Feature Minimization within Decision Trees. National Science Foundation. 1996. [View Context].

Andrew Watkins and Jon Timmis and Lois C. Boggess. Artificial Immune Recognition System (AIRS): An ImmuneInspired Supervised Learning Algorithm. (abw5,jt6@kent.ac.uk) Computing Laboratory, University of Kent. [View Context].

Perry Moerland and E. Fiesler and I. Ubarretxena-Belandia. Incorporating LCLV Non-Linearities in Optical Multilayer Neural Networks. Preprint of an article published in Applied Optics. [View Context].

Maria Salamo and Elisabet Golobardes. Analysing Rough Sets weighting methods for Case-Based Reasoning Systems. Enginyeria i Arquitectura La Salle. [View Context].

Jakub Zavrel. An Empirical Re-Examination of Weighted Voting for k-NN. Computational Linguistics. [View Context].

Rudy Setiono and Huan Liu. Neural-Network Feature Selector. Department of Information Systems and Computer Science National University of Singapore. [View Context].

Wl/odzisl/aw Duch and Jerzy J. Korczak. Optimization and global minimization methods suitable for neural networks. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Christos Emmanouilidis and A. Hunter and Dr J. MacIntyre. A Multiobjective Evolutionary Setting for Feature Selection and a Commonality-Based Crossover Operator. Centre for Adaptive Systems, School of Computing, Engineering and Technology University of Sunderland. [View Context].

Elena Smirnova and Ida G. Sprinkhuizen-Kuyper and I. Nalbantis and b. ERIM and Universiteit Rotterdam. Unanimous Voting using Support Vector Machines. IKAT, Universiteit Maastricht. [View Context].

Alain Rakotomamonjy. Leave-One-Out errors in Bipartite Ranking SVM. PSI CNRS FRE2645 INSA de Rouen Avenue de l'universite. [View Context].

Hiroshi Shimodaira and Jun Okui and Mitsuru Nakai. IMPROVING THE GENERALIZATION PERFORMANCE OF THE MCE/GPD LEARNING. School of Information Science Japan Advanced Institute of Science and Technology Tatsunokuchi, Ishikawa. [View Context].

Charles Campbell and Nello Cristianini. Simple Learning Algorithms for Training Support Vector Machines. Dept. of Engineering Mathematics. [View Context].

Ayhan Demiriz and Kristin P. Bennett. Chapter 1 OPTIMIZATIONAPPROACHESTOSEMI-SUPERVISED LEARNING. Department of Decision Sciences and Engineering Systems & Department of Mathematical Sciences, Rensselaer Polytechnic Institute. [View Context].

Ronaldo C. Prati and Peter A. Flach. ROCCER: A ROC convex hull rule learning algorithm. Institute of Mathematics and Computer Science at University of So Paulo. [View Context].

Perry Moerland. Mixtures of latent variable models for density estimation and classification. E S E A R C H R E P R O R T I D I A P D a l l e M o l l e I n s t i t u t e f o r Pe r cep t ua l A r t i f i c i a l Intelligence . [View Context].

Stefan Aeberhard and O. de Vel and Danny Coomans. New Fast Algorithms for Variable Selection based on Classifier Performance. James Cook University. [View Context].

Kristin P. Bennett and Erin J. Bredensteiner. Geometry in Learning. Department of Mathematical Sciences Rensselaer Polytechnic Institute. [View Context].

Carlotta Domeniconi and Bojun Yan. On Error Correlation and Accuracy of Nearest Neighbor Ensemble Classifiers. Information and Software Engineering Department George Mason University. [View Context].

Chris Drummond and Robert C. Holte. C4.5, Class Imbalance, and Cost Sensitivity: Why Under-Sampling beats Over-Sampling. Institute for Information Technology, National Research Council Canada. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

ESEARCH R and D. R. Ort and Perry Moerland and E. Fiesler and I. Ubarretxena-Belandia. Multilayer Perceptrons for Optical Implementation. Optical Engineering, ol. [View Context].

Yin Zhang and W. Nick Street. Bagging with Adaptive Costs. Management Sciences Department University of Iowa Iowa City. [View Context].

Chiranjib Bhattacharyya. Robust Classification of noisy data using Second Order Cone Programming approach. Dept. Computer Science and Automation, Indian Institute of Science. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
,names=['E_'+str(i) for i in range(1, 61)]+['class']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
,names=['E_'+str(i) for i in range(1, 61)]+['class']
)

print(df.info())