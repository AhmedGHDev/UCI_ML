import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Michalski's famous soybean disease database


Data Set Characteristics:  

Multivariate

Number of Instances:

47

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

35

Date Donated

1987-01-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

126017


Source:

Origin:

Michalski,R.S.
Learning by being told and learning from examples: an experimental comparison of the two methodes of knowledge acquisition in the context of developing an expert system for soybean desease diagnoiss",
International Journal of Policy Analysis and Information Systems, 1980, 4(2), 125-161.

Donor:

Doug Fisher (dfisher%vuse '@' uunet.uucp)


Data Set Information:

A small subset of the original soybean database. See the reference for Fisher and Schlimmer in soybean-large.names for more information.

Steven Souders wrote:

> Figure 15 in the Michalski and Stepp paper (PAMI-82) says that the
> discriminant values for the attribute CONDITION OF FRUIT PODS for the
> classes Rhizoctonia Root Rot and Phytophthora Rot are "few or none"
> and "irrelevant" respectively. However, in the SOYBEAN-SMALL dataset
> I got from UCI, the value for this attribute is "dna" (does not apply)
> for both classes. I show the actual data below for cases D3
> (Rhizoctonia Root Rot) and D4 (Phytophthora Rot). According to the
> attribute names given in soybean-large.names, FRUIT-PODS is attribute
> #28. If you look at column 28 in the data below (marked with arrows)
> you'll notice that all cases of D3 and D4 have the same value. Thus,
> the SOYBEAN-SMALL dataset from UCI could NOT have produced the results
> in the Michalski and Stepp paper.

I do not have that paper, but have found what is probably a later variation of that figure in Stepp's dissertation, which lists the value "normal" for the first 2 classes and "irrelevant" for the latter 2 classes. I believe that "irrelevant" is used here as a synonym for "not-applicable", "dna", and "does-not-apply". I believe that there is a mis-print in the figure he read in their PAMI-83 article.

I have checked over each attribute value in this database. It corresponds exactly with the copies listed in both Stepp's and Fisher's dissertations.


Attribute Information:

1. date: april,may,june,july,august,september,october,?.
2. plant-stand: normal,lt-normal,?.
3. precip: lt-norm,norm,gt-norm,?.
4. temp: lt-norm,norm,gt-norm,?.
5. hail: yes,no,?.
6. crop-hist: diff-lst-year,same-lst-yr,same-lst-two-yrs,
same-lst-sev-yrs,?.
7. area-damaged: scattered,low-areas,upper-areas,whole-field,?.
8. severity: minor,pot-severe,severe,?.
9. seed-tmt: none,fungicide,other,?.
10. germination: 90-100%,80-89%,lt-80%,?.
11. plant-growth: norm,abnorm,?.
12. leaves: norm,abnorm.
13. leafspots-halo: absent,yellow-halos,no-yellow-halos,?.
14. leafspots-marg: w-s-marg,no-w-s-marg,dna,?.
15. leafspot-size: lt-1/8,gt-1/8,dna,?.
16. leaf-shread: absent,present,?.
17. leaf-malf: absent,present,?.
18. leaf-mild: absent,upper-surf,lower-surf,?.
19. stem: norm,abnorm,?.
20. lodging: yes,no,?.
21. stem-cankers: absent,below-soil,above-soil,above-sec-nde,?.
22. canker-lesion: dna,brown,dk-brown-blk,tan,?.
23. fruiting-bodies: absent,present,?.
24. external decay: absent,firm-and-dry,watery,?.
25. mycelium: absent,present,?.
26. int-discolor: none,brown,black,?.
27. sclerotia: absent,present,?.
28. fruit-pods: norm,diseased,few-present,dna,?.
29. fruit spots: absent,colored,brown-w/blk-specks,distort,dna,?.
30. seed: norm,abnorm,?.
31. mold-growth: absent,present,?.
32. seed-discolor: absent,present,?.
33. seed-size: norm,lt-norm,?.
34. shriveling: absent,present,?.
35. roots: norm,rotted,galls-cysts,?.


Relevant Papers:

Tan, M., & Eshelman, L. (1988). Using weighted networks to represent classification knowledge in noisy domains. Proceedings of the Fifth International Conference on Machine Learning (pp. 121-134). Ann Arbor, Michigan: Morgan Kaufmann.
[Web Link]

Fisher,D.H. & Schlimmer,J.C. (1988). Concept Simplification and Predictive Accuracy. Proceedings of the Fifth International Conference on Machine Learning (pp. 22-28). Ann Arbor, Michigan: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Yuan Jiang and Zhi-Hua Zhou. Editing Training Data for kNN Classifiers with Neural Network Ensemble. ISNN (1). 2004. [View Context].

Rich Caruana and Alexandru Niculescu-Mizil. An Empirical Evaluation of Supervised Learning for ROC Area. ROCAI. 2004. [View Context].

Prem Melville and Raymond J. Mooney. Diverse ensembles for active learning. ICML. 2004. [View Context].

Rich Caruana and Alexandru Niculescu-Mizil and Geoff Crew and Alex Ksikes. Ensemble selection from libraries of models. ICML. 2004. [View Context].

Rich Caruana and Alexandru Niculescu-Mizil. Data Mining in Metric Space: An Empirical Analysis of Supervised Learning Performance Criteria. ROCAI. 2004. [View Context].

Vassilis Athitsos and Stan Sclaroff. Boosting Nearest Neighbor Classifiers for Multiclass Recognition. Boston University Computer Science Tech. Report No, 2004-006. 2004. [View Context].

Geoffrey Holmes and Bernhard Pfahringer and Richard Kirkby and Eibe Frank and Mark A. Hall. Multiclass Alternating Decision Trees. ECML. 2002. [View Context].

Subramani Mani and Marco Porta and Suzanne McDermott. Building Bayesian Network Models in Medicine: the MENTOR Experience. Center for Biomedical Informatics University of Pittsburgh. 2002. [View Context].

Marco Porta and Subramani Mani and Suzanne McDermott. MENTOR: Building Bayesian Network Models in Medicine CSCE Technical Report TR-2002-016. Department of Computer Science and Engineering University of South Carolina. 2002. [View Context].

Bianca Zadrozny. Reducing multiclass to binary by coupling probability estimates. NIPS. 2001. [View Context].

Rudy Setiono. Feedforward Neural Network Construction Using Cross Validation. Neural Computation, 13. 2001. [View Context].

Nikunj C. Oza and Stuart J. Russell. Experimental comparisons of online and batch versions of bagging and boosting. KDD. 2001. [View Context].

Kiri Wagstaff and Claire Cardie. Clustering with Instance-level Constraints. ICML. 2000. [View Context].

Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

Manoranjan Dash and Huan Liu. Hybrid Search of Feature Subsets. PRICAI. 1998. [View Context].

Huan Liu and Rudy Setiono. Incremental Feature Selection. Appl. Intell, 9. 1998. [View Context].

Hendrik Blockeel and Luc De Raedt and Jan Ramon. Top-Down Induction of Clustering Trees. ICML. 1998. [View Context].

Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja. Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF. Appl. Intell, 7. 1997. [View Context].

Nir Friedman and Dan Geiger and Moisés Goldszmidt. Bayesian Network Classifiers. Machine Learning, 29. 1997. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Guszti Bartfai. VICTORIA UNIVERSITY OF WELLINGTON Te Whare Wananga o te Upoko o te Ika a Maui. Department of Computer Science PO Box 600. 1996. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Geoffrey I. Webb. OPUS: An Efficient Admissible Algorithm for Unordered Search. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

Ron Kohavi. A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection. IJCAI. 1995. [View Context].

Thomas G. Dietterich and Ghulum Bakiri. Solving Multiclass Learning Problems via Error-Correcting Output Codes. CoRR, csAI/9501101. 1995. [View Context].

Christophe Giraud and Tony Martinez and Christophe G. Giraud-Carrier. University of Bristol Department of Computer Science ILA: Combining Inductive Learning with Prior Knowledge and Reasoning. 1995. [View Context].

Jitender S. Deogun and Vijay V. Raghavan and Hayri Sever. Exploiting Upper Approximation in the Rough Set Methodology. KDD. 1995. [View Context].

Geoffrey I. Webb. OPUS: A systematic search algorithm and its application to categorical attribute-value datadriven machine learning. School of Computing and Mathematics, Deakin University. 1993. [View Context].

Suresh K. Choubey and Jitender S. Deogun and Vijay V. Raghavan and Hayri Sever. A comparison of feature selection algorithms in the context of rough classifiers. [View Context].

Takao Mohri and Hidehiko Tanaka. An Optimal Weighting Criterion of Case Indexing for Both Numeric and Symbolic Attributes. Information Engineering Course, Faculty of Engineering The University of Tokyo. [View Context].

Nikunj C. Oza and Stuart J. Russell. Online Bagging and Boosting. Computer Science Division University of California. [View Context].

Perry Moerland. A Comparison of Mixture Models for Density Estimation. IDIAP. [View Context].

Zhi-Hua Zhou and Yang Yu. Ensembling Local Learners Through Multimodal Perturbation. [View Context].

Geoffrey I Webb. Generality is more significant than complexity: Toward an alternative to Occam's Razor. School of Computing and Mathematics Deakin University. [View Context].

Sherrie L. W and Zijian Zheng. A BENCHMARK FOR CLASSIFIER LEARNING. Basser Department of Computer Science The University of Sydney. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Chotirat Ann and Dimitrios Gunopulos. Scaling up the Naive Bayesian Classifier: Using Decision Trees for Feature Selection. Computer Science Department University of California. [View Context].

Zhi-Hua Zhou and Xu-Ying Liu. Training Cost-Sensitive Neural Networks with Methods Addressing the Class Imbalance Problem. [View Context].

Prem Melville and Raymond J. Mooney. Proceedings of the 21st International Conference on Machine Learning. Department of Computer Sciences. [View Context].

Jarinee Chattratichart and John Darlington and Moustafa Ghanem and Yang Guo and Harold Huning and Martin Kohler and Janjao Sutiwaraphun and Hing Wing and Dan Yang. Large Scale Data Mining: The Challenges and The Solutions. Department of Computing. [View Context].

Daichi Mochihashi and Gen-ichiro Kikui and Kenji Kita. Learning Nonstructural Distance Metric by Minimum Cluster Distortions. ATR Spoken Language Translation research laboratories. [View Context].

Miguel Moreira and Alain Hertz and Eddy Mayoraz. Data binarization by discriminant elimination. Proceedings of the ICML-99 Workshop: From Machine Learning to. [View Context].

Igor Kononenko and Edvard Simec. Induction of decision trees using RELIEFF. University of Ljubljana, Faculty of electrical engineering & computer science. [View Context].

BayesianClassifi552 Pat Langley and Wayne Iba. In Proceedings of the Tenth National ConferenceonArtifi256 Intelligence( 42840. Lambda Kevin Thompson. [View Context].

YongSeog Kim and W. Nick Street and Filippo Menczer. Optimal Ensemble Construction via Meta-Evolutionary Ensembles. Business Information Systems, Utah State University. [View Context].

Iñaki Inza and Pedro Larraaga and Basilio Sierra. Bayesian networks for feature subset selection. Department of Computer Sciences and Artificial Intelligence. [View Context].

Perry Moerland. Mixtures of latent variable models for density estimation and classification. E S E A R C H R E P R O R T I D I A P D a l l e M o l l e I n s t i t u t e f o r Pe r cep t ua l A r t i f i c i a l Intelligence . [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/soybean/soybean-small.data"
,names=['date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist', 'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth', 'leaves', 'leafspots-halo', 'leafspots-marg', 'leafspot-size', 'leaf-shread', 'leaf-malf', 'leaf-mild', 'stem', 'lodging', 'stem-cankers', 'canker-lesion', 'fruiting-bodies', 'external_decay', 'mycelium', 'int-discolor', 'sclerotia', 'fruit-pods', 'fruit_spots', 'seed', 'mold-growth', 'seed-discolor', 'seed-size', 'shriveling', 'roots']
)


print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/soybean/soybean-small.data"
,names=['date', 'plant-stand', 'precip', 'temp', 'hail', 'crop-hist', 'area-damaged', 'severity', 'seed-tmt', 'germination', 'plant-growth', 'leaves', 'leafspots-halo', 'leafspots-marg', 'leafspot-size', 'leaf-shread', 'leaf-malf', 'leaf-mild', 'stem', 'lodging', 'stem-cankers', 'canker-lesion', 'fruiting-bodies', 'external_decay', 'mycelium', 'int-discolor', 'sclerotia', 'fruit-pods', 'fruit_spots', 'seed', 'mold-growth', 'seed-discolor', 'seed-size', 'shriveling', 'roots']
)

print(df.info())