import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Predicting the Cellular Localization Sites of Proteins


Data Set Characteristics:  

Multivariate

Number of Instances:

1484

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

374532


Source:

Creator and Maintainer:

Kenta Nakai
Institue of Molecular and Cellular Biology
Osaka, University
1-3 Yamada-oka, Suita 565 Japan
nakai '@' imcb.osaka-u.ac.jp
http://www.imcb.osaka-u.ac.jp/nakai/psort.html

Donor:

Paul Horton (paulh '@' cs.berkeley.edu)


Data Set Information:

Predicted Attribute: Localization site of protein. ( non-numeric ).

The references below describe a predecessor to this dataset and its development. They also give results (not cross-validated) for classification by a rule-based expert system with that version of the dataset.

Reference: "Expert Sytem for Predicting Protein Localization Sites in Gram-Negative Bacteria", Kenta Nakai & Minoru Kanehisa, PROTEINS: Structure, Function, and Genetics 11:95-110, 1991.

Reference: "A Knowledge Base for Predicting Protein Localization Sites in Eukaryotic Cells", Kenta Nakai & Minoru Kanehisa, Genomics 14:897-911, 1992.


Attribute Information:

1. Sequence Name: Accession number for the SWISS-PROT database
2. mcg: McGeoch's method for signal sequence recognition.
3. gvh: von Heijne's method for signal sequence recognition.
4. alm: Score of the ALOM membrane spanning region prediction program.
5. mit: Score of discriminant analysis of the amino acid content of the N-terminal region (20 residues long) of mitochondrial and non-mitochondrial proteins.
6. erl: Presence of "HDEL" substring (thought to act as a signal for retention in the endoplasmic reticulum lumen). Binary attribute.
7. pox: Peroxisomal targeting signal in the C-terminus.
8. vac: Score of discriminant analysis of the amino acid content of vacuolar and extracellular proteins.
9. nuc: Score of discriminant analysis of nuclear localization signals of nuclear and non-nuclear proteins.


Relevant Papers:

Paul Horton & Kenta Nakai, "A Probablistic Classification System for Predicting the Cellular Localization Sites of Proteins", Intelligent Systems in Molecular Biology, 109-115. St. Louis, USA 1996.
[Web Link]

The references below describe a predecessor to this dataset and its development. They also give results (not cross-validated) for classification by a rule-based expert system with that version of the dataset:

Kenta Nakai & Minoru Kanehisa, "Expert Sytem for Predicting Protein Localization Sites in Gram-Negative Bacteria", PROTEINS: Structure, Function, and Genetics 11:95-110, 1991.

Kenta Nakai & Minoru Kanehisa, "A Knowledge Base for Predicting Protein Localization Sites in Eukaryotic Cells", Genomics 14:897-911, 1992.
[Web Link]


Papers That Cite This Data Set1:


Vassilis Athitsos and Stan Sclaroff. Boosting Nearest Neighbor Classifiers for Multiclass Recognition. Boston University Computer Science Tech. Report No, 2004-006. 2004. [View Context].

Samuel Kaski and Jaakko Peltonen. Informative Discriminant Analysis. ICML. 2003. [View Context].

Dmitry Pavlov and Alexandrin Popescul and David M. Pennock and Lyle H. Ungar. Mixtures of Conditional Maximum Entropy Models. ICML. 2003. [View Context].

Aik Choon Tan and David Gilbert. An Empirical Comparison of Supervised Machine Learning Techniques in Bioinformatics. APBC. 2003. [View Context].

Nitesh V. Chawla and Kevin W. Bowyer and Lawrence O. Hall and W. Philip Kegelmeyer. SMOTE: Synthetic Minority Over-sampling Technique. J. Artif. Intell. Res. (JAIR, 16. 2002. [View Context].

Manoranjan Dash and Kiseok Choi and Peter Scheuermann and Huan Liu. Feature Selection for Clustering - A Filter Solution. ICDM. 2002. [View Context].

Erin L. Allwein and Robert E. Schapire and Yoram Singer. Reducing Multiclass to Binary: A Unifying Approach for Margin Classifiers. ICML. 2000. [View Context].

Paul Horton and Kenta Nakai. Better Prediction of Protein Cellular Localization Sites with the it k Nearest Neighbors Classifier. ISMB. 1997. [View Context].

Johannes Furnkranz. Round Robin Rule Learning. Austrian Research Institute for Artificial Intelligence. [View Context].

Gaurav Marwah and Lois C. Boggess. Artificial Immune Systems for Classification : Some Issues. Department of Computer Science Mississippi State University. [View Context].

Alain Rakotomamonjy. Analysis of SVM regression bounds for variable ranking. P.S.I CNRS FRE 2645, INSA de Rouen Avenue de l'Universite. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/yeast/yeast.data"
,delimiter='\s+'
,names=['Sequence_Name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/yeast/yeast.data"
,delimiter='\s+'
,names=['Sequence_Name', 'mcg', 'gvh', 'alm', 'mit', 'erl', 'pox', 'vac', 'nuc']
)

print(df.info())