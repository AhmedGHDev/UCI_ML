import pandas as pd


#Step 00: Loading data
# INFO
"""
Abstract: This data contains protein localization sites


Data Set Characteristics:  

Multivariate

Number of Instances:

336

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

8

Date Donated

1996-09-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

306695


Source:

Creator and Maintainer:

Kenta Nakai
Institue of Molecular and Cellular Biology
Osaka, University
1-3 Yamada-oka, Suita 565 Japan
nakai '@' imcb.osaka-u.ac.jp
http://www.imcb.osaka-u.ac.jp/nakai/psort.html\

Donor:

Paul Horton (paulh '@' cs.berkeley.edu)

See also: yeast database


Data Set Information:

The references below describe a predecessor to this dataset and its development. They also give results (not cross-validated) for classification by a rule-based expert system with that version of the dataset.

Reference: "Expert Sytem for Predicting Protein Localization Sites in Gram-Negative Bacteria", Kenta Nakai & Minoru Kanehisa, PROTEINS: Structure, Function, and Genetics 11:95-110, 1991.

Reference: "A Knowledge Base for Predicting Protein Localization Sites in Eukaryotic Cells", Kenta Nakai & Minoru Kanehisa, Genomics 14:897-911, 1992.


Attribute Information:

1. Sequence Name: Accession number for the SWISS-PROT database
2. mcg: McGeoch's method for signal sequence recognition.
3. gvh: von Heijne's method for signal sequence recognition.
4. lip: von Heijne's Signal Peptidase II consensus sequence score. Binary attribute.
5. chg: Presence of charge on N-terminus of predicted lipoproteins. Binary attribute.
6. aac: score of discriminant analysis of the amino acid content of outer membrane and periplasmic proteins.
7. alm1: score of the ALOM membrane spanning region prediction program.
8. alm2: score of ALOM program after excluding putative cleavable signal regions from the sequence.


Relevant Papers:

Paul Horton & Kenta Nakai. "A Probablistic Classification System for Predicting the Cellular Localization Sites of Proteins".Intelligent Systems in Molecular Biology, 109-115. St. Louis, USA 1996.
[Web Link]


Papers That Cite This Data Set1:


Xiaoyong Chai and Li Deng and Qiang Yang and Charles X. Ling. Test-Cost Sensitive Naive Bayes Classification. ICDM. 2004. [View Context].

Vassilis Athitsos and Stan Sclaroff. Boosting Nearest Neighbor Classifiers for Multiclass Recognition. Boston University Computer Science Tech. Report No, 2004-006. 2004. [View Context].

Charles X. Ling and Qiang Yang and Jianning Wang and Shichao Zhang. Decision trees with minimal costs. ICML. 2004. [View Context].

Aik Choon Tan and David Gilbert. An Empirical Comparison of Supervised Machine Learning Techniques in Bioinformatics. APBC. 2003. [View Context].

Mukund Deshpande and George Karypis. Evaluation of Techniques for Classifying Biological Sequences. PAKDD. 2002. [View Context].

Huajie Zhang and Charles X. Ling. An Improved Learning Algorithm for Augmented Naive Bayes. PAKDD. 2001. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Paul Horton and Kenta Nakai. Better Prediction of Protein Cellular Localization Sites with the it k Nearest Neighbors Classifier. ISMB. 1997. [View Context].

Chotirat Ann and Dimitrios Gunopulos. Scaling up the Naive Bayesian Classifier: Using Decision Trees for Feature Selection. Computer Science Department University of California. [View Context].

Andrew Watkins and Jon Timmis and Lois C. Boggess. Artificial Immune Recognition System (AIRS): An ImmuneInspired Supervised Learning Algorithm. (abw5,jt6@kent.ac.uk) Computing Laboratory, University of Kent. [View Context].

Gaurav Marwah and Lois C. Boggess. Artificial Immune Systems for Classification : Some Issues. Department of Computer Science Mississippi State University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data" ,delimiter="\s+" ,names=['Sequence_Name', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data" ,delimiter="\s+" ,names=['Sequence_Name', 'mcg', 'gvh', 'lip', 'chg', 'aac', 'alm1', 'alm2'])

print(df.info())