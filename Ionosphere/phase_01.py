import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Classification of radar returns from the ionosphere


Data Set Characteristics:  

Multivariate

Number of Instances:

351

Area:

Physical

Attribute Characteristics:

Integer, Real

Number of Attributes:

34

Date Donated

1989-01-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

311460


Source:

Donor:

Vince Sigillito (vgs '@' aplcen.apl.jhu.edu)

Source:

Space Physics Group
Applied Physics Laboratory
Johns Hopkins University
Johns Hopkins Road
Laurel, MD 20723


Data Set Information:

This radar data was collected by a system in Goose Bay, Labrador. This system consists of a phased array of 16 high-frequency antennas with a total transmitted power on the order of 6.4 kilowatts. See the paper for more details. The targets were free electrons in the ionosphere. "Good" radar returns are those showing evidence of some type of structure in the ionosphere. "Bad" returns are those that do not; their signals pass through the ionosphere.

Received signals were processed using an autocorrelation function whose arguments are the time of a pulse and the pulse number. There were 17 pulse numbers for the Goose Bay system. Instances in this databse are described by 2 attributes per pulse number, corresponding to the complex values returned by the function resulting from the complex electromagnetic signal.


Attribute Information:

-- All 34 are continuous
-- The 35th attribute is either "good" or "bad" according to the definition summarized above. This is a binary classification task.


Relevant Papers:

Sigillito, V. G., Wing, S. P., Hutton, L. V., \& Baker, K. B. (1989). Classification of radar returns from the ionosphere using neural networks. Johns Hopkins APL Technical Digest, 10, 262-266.
[Web Link]


Papers That Cite This Data Set1:


Zhi-Hua Zhou and Yuan Jiang. NeC4.5: Neural Ensemble Based C4.5. IEEE Trans. Knowl. Data Eng, 16. 2004. [View Context].

Hyunsoo Kim and Se Hyun Park. Data Reduction in Support Vector Machines by a Kernelized Ionic Interaction Model. SDM. 2004. [View Context].

Glenn Fung and M. Murat Dundar and Jinbo Bi and Bharat Rao. A fast iterative algorithm for fisher discriminant using heterogeneous kernels. ICML. 2004. [View Context].

Predrag Radivojac and Zoran Obradovic and A. Keith Dunker and Slobodan Vucetic. Feature Selection Filters Based on the Permutation Test. ECML. 2004. [View Context].

Jeroen Eggermont and Joost N. Kok and Walter A. Kosters. Genetic Programming for data classification: partitioning the search space. SAC. 2004. [View Context].

Jennifer G. Dy and Carla Brodley. Feature Selection for Unsupervised Learning. Journal of Machine Learning Research, 5. 2004. [View Context].

Mikhail Bilenko and Sugato Basu and Raymond J. Mooney. Integrating constraints and metric learning in semi-supervised clustering. ICML. 2004. [View Context].

Michael L. Raymer and Travis E. Doom and Leslie A. Kuhn and William F. Punch. Knowledge discovery in medical and biological datasets using a hybrid Bayes classifier/evolutionary algorithm. IEEE Transactions on Systems, Man, and Cybernetics, Part B, 33. 2003. [View Context].

Dmitriy Fradkin and David Madigan. Experiments with random projections for machine learning. KDD. 2003. [View Context].

Marina Skurichina and Ludmila Kuncheva and Robert P W Duin. Bagging and Boosting for the Nearest Mean Classifier: Effects of Sample Size on Diversity and Accuracy. Multiple Classifier Systems. 2002. [View Context].

Robert Burbidge and Matthew Trotter and Bernard F. Buxton and Sean B. Holden. STAR - Sparsity through Automated Rejection. IWANN (1). 2001. [View Context].

Lorne Mason and Peter L. Bartlett and Jonathan Baxter. Improved Generalization Through Explicit Optimization of Margins. Machine Learning, 38. 2000. [View Context].

Justin Bradley and Kristin P. Bennett and Bennett A. Demiriz. Constrained K-Means Clustering. Microsoft Research Dept. of Mathematical Sciences One Microsoft Way Dept. of Decision Sciences and Eng. Sys. 2000. [View Context].

Jennifer G. Dy and Carla Brodley. Feature Subset Selection and Order Identification for Unsupervised Learning. ICML. 2000. [View Context].

P. S and Bradley K. P and Bennett A. Demiriz. Constrained K-Means Clustering. Microsoft Research Dept. of Mathematical Sciences One Microsoft Way Dept. of Decision Sciences and Eng. Sys. 2000. [View Context].

Juan J. Rodr##guez and Carlos J. Alonso and Henrik Bostrom. Boosting Interval Based Literals. 2000. [View Context].

Colin Campbell and Nello Cristianini and Alex J. Smola. Query Learning with Large Margin Classifiers. ICML. 2000. [View Context].

Marina Skurichina and Robert P W Duin. Boosting in Linear Discriminant Analysis. Multiple Classifier Systems. 2000. [View Context].

Art B. Owen. Tubular neighbors for regression and classification. Stanford University. 1999. [View Context].

Chun-Nan Hsu and Hilmar Schuschel and Ya-Ting Yang. The ANNIGMA-Wrapper Approach to Neural Nets Feature Selection for Knowledge Discovery and Data Mining. Institute of Information Science. 1999. [View Context].

Lorne Mason and Jonathan Baxter and Peter L. Bartlett and Marcus Frean. Boosting Algorithms as Gradient Descent. NIPS. 1999. [View Context].

Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Stephen D. Bay. Nearest neighbor classification from multiple feature subsets. Intell. Data Anal, 3. 1999. [View Context].

Stavros J. Perantonis and Vassilis Virvilis. Input Feature Extraction for Multilayered Perceptrons Using Supervised Principal Component Analysis. Neural Processing Letters, 10. 1999. [View Context].

David M J Tax and Robert P W Duin. Support vector domain description. Pattern Recognition Letters, 20. 1999. [View Context].

Richard Maclin. Boosting Classifiers Regionally. AAAI/IAAI. 1998. [View Context].

Robert E. Schapire and Yoav Freund and Peter Bartlett and Wee Sun Lee. The Annals of Statistics, to appear. Boosting the Margin: A New Explanation for the Effectiveness of Voting Methods. AT&T Labs. 1998. [View Context].

Lorne Mason and Peter L. Bartlett and Jonathan Baxter. Direct Optimization of Margins Improves Generalization in Combined Classifiers. NIPS. 1998. [View Context].

Kristin P. Bennett and Erin J. Bredensteiner. A Parametric Optimization Method for Machine Learning. INFORMS Journal on Computing, 9. 1997. [View Context].

Aynur Akkus and H. Altay Güvenir. K Nearest Neighbor Classification on Feature Projections. ICML. 1996. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski and Geerd H. F Diercksen. Minimal distance neural methods. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Andrew Watkins and Jon Timmis and Lois C. Boggess. Artificial Immune Recognition System (AIRS): An ImmuneInspired Supervised Learning Algorithm. (abw5,jt6@kent.ac.uk) Computing Laboratory, University of Kent. [View Context].

Aynur Akku and H. Altay Guvenir. Weighting Features in k Nearest Neighbor Classification on Feature Projections. Department of Computer Engineering and Information Science Bilkent University. [View Context].

Krzysztof Grabczewski and Wl/odzisl/aw Duch. THE SEPARABILITY OF SPLIT VALUE CRITERION. Department of Computer Methods, Nicolaus Copernicus University. [View Context].

Christos Emmanouilidis and A. Hunter and Dr J. MacIntyre. A Multiobjective Evolutionary Setting for Feature Selection and a Commonality-Based Crossover Operator. Centre for Adaptive Systems, School of Computing, Engineering and Technology University of Sunderland. [View Context].

Chiranjib Bhattacharyya. Robust Classification of noisy data using Second Order Cone Programming approach. Dept. Computer Science and Automation, Indian Institute of Science. [View Context].

Ayhan Demiriz and Kristin P. Bennett. Chapter 1 OPTIMIZATIONAPPROACHESTOSEMI-SUPERVISED LEARNING. Department of Decision Sciences and Engineering Systems & Department of Mathematical Sciences, Rensselaer Polytechnic Institute. [View Context].

Isabelle Alvarez and Stephan Bernard. Ranking Cases with Decision Trees: a Geometric Method that Preserves Intelligibility. [View Context].

Christos Dimitrakakis and Samy Bengioy. Online Policy Adaptation for Ensemble Classifiers. IDIAP. [View Context].

Rajesh Parekh and Jihoon Yang and Vasant Honavar. Constructive Neural-Network Learning Algorithms for Pattern Classification. [View Context].

Alain Rakotomamonjy. Leave-One-Out errors in Bipartite Ranking SVM. PSI CNRS FRE2645 INSA de Rouen Avenue de l'universite. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Meta-learning: searching in the model space. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Charles Campbell and Nello Cristianini. Simple Learning Algorithms for Training Support Vector Machines. Dept. of Engineering Mathematics. [View Context].

Federico Divina and Elena Marchiori. Knowledge-Based Evolutionary Search for Inductive Concept Learning. Vrije Universiteit of Amsterdam. [View Context].

K. A. J Doherty and Rolf Adams and Neil Davey. Unsupervised Learning with Normalised Data and Non-Euclidean Norms. University of Hertfordshire. [View Context].

Michael Lindenbaum and Shaul Markovitch and Dmitry Rusakov. Selective Sampling Using Random Field Modelling. [View Context].

Christos Emmanouilidis and Anthony Hunter. A Comparison of Crossover Operators in Neural Network Feature Selection with Multiobjective Evolutionary Algorithms. Centre for Adaptive Systems, School of Computing, Engineering and Technology University of Sunderland. [View Context].

Chiranjib Bhattacharyya and Pannagadatta K. S and Alexander J. Smola. A Second order Cone Programming Formulation for Classifying Missing Data. Department of Computer Science and Automation Indian Institute of Science. [View Context].

Perry Moerland. Mixtures of latent variable models for density estimation and classification. E S E A R C H R E P R O R T I D I A P D a l l e M o l l e I n s t i t u t e f o r Pe r cep t ua l A r t i f i c i a l Intelligence . [View Context].

Markus Breitenbach and Rodney Nielsen and Gregory Z. Grudic. Probabilistic Random Forests: Predicting Data Point Specific Misclassification Probabilities. Department of Computer Science University of Colorado. [View Context].

Federico Divina and Elena Marchiori. Handling Continuous Attributes in an Evolutionary Inductive Learner. Department of Computer Science Vrije Universiteit. [View Context].

Glenn Fung and Sathyakama Sandilya and R. Bharat Rao. Rule extraction from Linear Support Vector Machines. Computer-Aided Diagnosis & Therapy, Siemens Medical Solutions, Inc. [View Context].

Karthik Ramakrishnan. UNIVERSITY OF MINNESOTA. [View Context].

Michalis K. Titsias and Aristidis Likas. Shared Kernel Models for Class Conditional Density Estimation. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data" ,names=[str(i) for i in range(1,35)]+["class"])

print(df.info())

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data" ,names=[str(i) for i in range(1,35)]+["class"])

print(df.info())