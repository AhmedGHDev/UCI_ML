import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The goal is to learn to predict whether new molecules will be musks or non-musks

Data Set Characteristics:  

Multivariate

Number of Instances:

476

Area:

Physical

Attribute Characteristics:

Integer

Number of Attributes:

168

Date Donated

1994-09-12

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

84544


Source:

Creators:

AI Group at Arris Pharmaceutical Corporation
contact: David Chapman or Ajay Jain
Arris Pharmaceutical Corporation
385 Oyster Point Blvd.
South San Francisco, CA 94080
415-737-8600
zvona '@' arris.com, jain '@' arris.com

Donor:

Tom Dietterich
Department of Computer Science
Oregon State University
Corvallis, OR 97331
503-737-5559
tgd '@' cs.orst.edu


Data Set Information:

This dataset describes a set of 92 molecules of which 47 are judged by human experts to be musks and the remaining 45 molecules are judged to be non-musks. The goal is to learn to predict whether new molecules will be musks or non-musks. However, the 166 features that describe these molecules depend upon the exact shape, or conformation, of the molecule. Because bonds can rotate, a single molecule can adopt many different shapes. To generate this data set, the low-energy conformations of the molecules were generated and then filtered to remove highly similar conformations. This left 476 conformations. Then, a feature vector was extracted that describes each conformation.

This many-to-one relationship between feature vectors and molecules is called the "multiple instance problem". When learning a classifier for this data, the classifier should classify a molecule as "musk" if ANY of its conformations is classified as a musk. A molecule should be classified as "non-musk" if NONE of its conformations is classified as a musk.


Attribute Information:

molecule_name: Symbolic name of each molecule. Musks have names such as MUSK-188. Non-musks have names such as NON-MUSK-jp13.
conformation_name: Symbolic name of each conformation. These have the format MOL_ISO+CONF, where MOL is the molecule number, ISO is the stereoisomer number (usually 1), and CONF is the conformation number.
f1 through f162: These are "distance features" along rays (see paper cited above). The distances are measured in hundredths of Angstroms. The distances may be negative or positive, since they are actually measured relative to an origin placed along each ray. The origin was defined by a "consensus musk" surface that is no longer used. Hence, any experiments with the data should treat these feature values as lying on an arbitrary continuous scale. In particular, the algorithm should not make any use of the zero point or the sign of each feature value.
f163: This is the distance of the oxygen atom in the molecule to a designated point in 3-space. This is also called OXY-DIS.
f164: OXY-X: X-displacement from the designated point.
f165: OXY-Y: Y-displacement from the designated point.
f166: OXY-Z: Z-displacement from the designated point.
class: 0 => non-musk, 1 => musk

Please note that the molecule_name and conformation_name attributes should not be used to predict the class.


Relevant Papers:

Dietterich, T. G., Lathrop, R. H., Lozano-Perez, T. Solving the multiple-instance problem with axis-parallel rectangles. Artificial Intelligence.
[Web Link]


Papers That Cite This Data Set1:


Qingping Tao Ph. D. MAKING EFFICIENT LEARNING ALGORITHMS WITH EXPONENTIALLY MANY FEATURES. Qingping Tao A DISSERTATION Faculty of The Graduate College University of Nebraska In Partial Fulfillment of Requirements. 2004. [View Context].

Qingping Tao and Stephen Scott and N. V. Vinodchandran and Thomas T. Osugi. SVM-based generalized multiple-instance learning via approximate box counting. ICML. 2004. [View Context].

Giorgio Valentini. Random Aggregated and Bagged Ensembles of SVMs: An Empirical Bias?Variance Analysis. Multiple Classifier Systems. 2004. [View Context].

Giorgio Valentini and Thomas G. Dietterich. Low Bias Bagged Support Vector Machines. ICML. 2003. [View Context].

Giorgio Valentini. Ensemble methods based on bias--variance analysis Theses Series DISI-TH-2003. Dipartimento di Informatica e Scienze dell'Informazione . 2003. [View Context].

Zhi-Hua Zhou and Min-Ling Zhang. Ensembles of Multi-instance Learners. ECML. 2003. [View Context].

Stephen D. Bay. Combining Nearest Neighbor Classifiers Through Multiple Feature Subsets. ICML. 1998. [View Context].

Hendrik Blockeel and Luc De Raedt. Lookahead and Discretization in ILP. ILP. 1997. [View Context].

Giorgio Valentini. An experimental bias--variance analysis of SVM ensembles based on resampling techniques. [View Context].

Zhi-Hua Zhou and Min-Ling Zhang. Solving Multi-Instance Problems with Classifier Ensemble Based on Constructive Clustering. National Laboratory for Novel Software Technology. [View Context].

Hendrik Blockeel and Luc De Raedt. Top-down Induction of Logical Decision Trees. Katholieke Universiteit Leuven Department of Computer Science. [View Context].

Zhi-Hua Zhou and Hua Zhou. Multi-Instance Learning: A Survey. National Laboratory for Novel Software Technology. [View Context].

Zhi-Hua Zhou and Min-Ling Zhang. Neural Networks for Multi-Instance Learning. National Laboratory for Novel Software Technology, Nanjing University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
print(df.info())