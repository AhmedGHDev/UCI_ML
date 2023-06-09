import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: CART book's waveform domains

Data Set Characteristics:  

Multivariate, Data-Generator

Number of Instances:

5000

Area:

Physical

Attribute Characteristics:

Real

Number of Attributes:

40

Date Donated

1988-11-10

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

73821


Source:

Original Owners:

Breiman,L., Friedman,J.H., Olshen,R.A., & Stone,C.J. (1984).
Classification and Regression Trees. Wadsworth International
Group: Belmont, California. (see pages 43-49).

Donor:

David Aha


Data Set Information:

Notes:
-- 3 classes of waves
-- 40 attributes, all of which include noise
-- The latter 19 attributes are all noise attributes with mean 0 and variance 1
-- See the book for details (49-55, 169)
-- waveform-+noise.data.Z contains 5000 instances


Attribute Information:

-- Each class is generated from a combination of 2 of 3 "base" waves
-- Each instance is generated f added noise (mean 0, variance 1) in each attribute
-- See the book for details (49-55, 169)


Relevant Papers:

Leo Breiman, Jerome H. Friedman, Adam Olshen, Jonathan Stone. "Classification and Regression Trees." 1984.
[Web Link]


Papers That Cite This Data Set1:


Giorgio Valentini. Random Aggregated and Bagged Ensembles of SVMs: An Empirical Bias?Variance Analysis. Multiple Classifier Systems. 2004. [View Context].

Zhi-Hua Zhou and W-D Wei and Gang Li and Honghua Dai. On the Size of Training Set and the Benefit from Ensemble. PAKDD. 2004. [View Context].

Eibe Frank and Mark Hall and Bernhard Pfahringer. Locally Weighted Naive Bayes. UAI. 2003. [View Context].

Giorgio Valentini and Thomas G. Dietterich. Low Bias Bagged Support Vector Machines. ICML. 2003. [View Context].

Joao Gama and Ricardo Rocha and Pedro Medas. Accurate decision trees for mining high-speed data streams. KDD. 2003. [View Context].

Giorgio Valentini. Ensemble methods based on bias--variance analysis Theses Series DISI-TH-2003. Dipartimento di Informatica e Scienze dell'Informazione . 2003. [View Context].

S. Sathiya Keerthi and Kaibo Duan and Shirish Krishnaj Shevade and Aun Neow Poo. A Fast Dual Algorithm for Kernel Logistic Regression. ICML. 2002. [View Context].

James Bailey and Thomas Manoukian and Kotagiri Ramamohanarao. Fast Algorithms for Mining Emerging Patterns. PKDD. 2002. [View Context].

Juan J. Rodr##guez and Carlos J. Alonso. Applying Boosting to Similarity Literals for Time Series Classification. Department of Informatics University of Valladolid, Spain. 2000. [View Context].

Juan J Rodríguez Diez and Carlos Alonso González and Henrik Boström. Learning First Order Logic Time Series Classifiers: Rules and Boosting. PKDD. 2000. [View Context].

Juan J. Rodr##guez and Carlos J. Alonso and Henrik Bostrom. Boosting Interval Based Literals. 2000. [View Context].

Bede Liu and Mingzeng Hu and Wynne Hsu. Multi-level organization and summarization of the discovered rules. KDD. 2000. [View Context].

Thomas G. Dietterich. An Experimental Comparison of Three Methods for Constructing Ensembles of Decision Trees: Bagging, Boosting, and Randomization. Machine Learning, 40. 2000. [View Context].

Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Khaled A. Alsabti and Sanjay Ranka and Vineet Singh. CLOUDS: A Decision Tree Classifier for Large Datasets. KDD. 1998. [View Context].

Kai Ming Ting and Boon Toh Low. Model Combination in the Multiple-Data-Batches Scenario. ECML. 1997. [View Context].

Nir Friedman and Moisés Goldszmidt. Discretizing Continuous Attributes While Learning Bayesian Networks. ICML. 1996. [View Context].

Ron Kohavi. Scaling Up the Accuracy of Naive-Bayes Classifiers: A Decision-Tree Hybrid. KDD. 1996. [View Context].

Tapio Elomaa and Juho Rousu. Finding Optimal Multi-Splits for Numerical Attributes in Decision Tree Learning. ESPRIT Working Group in Neural and Computational Learning. 1996. [View Context].

Dietrich Wettschereck and David W. Aha. Weighting Features. ICCBR. 1995. [View Context].

Thomas T. Osugi and M. S. EXPLORATION-BASED ACTIVE MACHINE LEARNING. Faculty of The Graduate College at the University of Nebraska In Partial Fulfillment of Requirements. [View Context].

Pierre Geurts. Extremely randomized trees. Technical report June 2003 University of Li#ege Department of Electrical Engineering and Computer Science Institut Monte#ore. [View Context].

Iñaki Inza and Pedro Larraaga and Ramon Etxeberria and Basilio Sierra. Feature Subset Selection by Bayesian networks based optimization. Dept. of Computer Science and Artificial Intelligence. University of the Basque Country. [View Context].

Kai Ming Ting and Boon Toh Low. Theory Combination: an alternative to Data Combination. University of Waikato. [View Context].

Matthias Scherf and W. Brauer. Feature Selection by Means of a Feature Weighting Approach. GSF - National Research Center for Environment and Health. [View Context].

Zhi-Hua Zhou and Xu-Ying Liu. Training Cost-Sensitive Neural Networks with Methods Addressing the Class Imbalance Problem. [View Context].

Giorgio Valentini. An experimental bias--variance analysis of SVM ensembles based on resampling techniques. [View Context].

Juan J. Rodr and guez Diez and Carlos J. Alonso. Learning Classification RBF Networks by Boosting. Lenguajes y Sistemas Inform#aticos. [View Context].

Zoran Obradovic and Slobodan Vucetic. Challenges in Scientific Data Mining: Heterogeneous, Biased, and Large Samples. Center for Information Science and Technology Temple University. [View Context].

Carlos J. Alonso Gonzalez and Juan J. Rodr and iguez Diez. Time Series Classification by Boosting Interval Based Literals. Grupo de Sistemas Inteligentes Departamento de Informatica Universidad de Valladolid. [View Context].

Juan J. Rodr##guez and Carlos J. Alonso and Henrik Bostrom. Learning First Order Logic Time Series Classifiers: Rules and Boosting. Grupo de Sistemas Inteligentes, Departamento de Inform#atica Universidad de Valladolid, Spain. [View Context].

Kai Ming Ting and Ian H. Witten. Stacked Generalization: when does it work. Department of Computer Science University of Waikato. [View Context].

Amund Tveit. Empirical Comparison of Accuracy and Performance for the MIPSVM classifier with Existing Classifiers. Division of Intelligent Systems Department of Computer and Information Science, Norwegian University of Science and Technology. [View Context].

Vikas Sindhwani and P. Bhattacharya and Subrata Rakshit. Information Theoretic Feature Crediting in Multiclass Support Vector Machines. [View Context].

Mohammed Waleed Kadous. Expanding the Scope of Concept Learning Using Metafeatures. School of Computer Science and Engineering, University of New South Wales. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""