import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: From G.Gong: CMU; Mostly Boolean or numeric-valued attribute types; Includes cost data (donated by Peter Turney)


Data Set Characteristics:  

Multivariate

Number of Instances:

155

Area:

Life

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

19

Date Donated

1988-11-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

360367


Source:

Creator:

unknown

Donor:

G.Gong (Carnegie-Mellon University) via
Bojan Cestnik
Jozef Stefan Institute
Jamova 39
61000 Ljubljana
Yugoslavia (tel.: (38)(+61) 214-399 ext.287) }


Data Set Information:

Please ask Gail Gong for further information on this database.


Attribute Information:

1. Class: DIE, LIVE
2. AGE: 10, 20, 30, 40, 50, 60, 70, 80
3. SEX: male, female
4. STEROID: no, yes
5. ANTIVIRALS: no, yes
6. FATIGUE: no, yes
7. MALAISE: no, yes
8. ANOREXIA: no, yes
9. LIVER BIG: no, yes
10. LIVER FIRM: no, yes
11. SPLEEN PALPABLE: no, yes
12. SPIDERS: no, yes
13. ASCITES: no, yes
14. VARICES: no, yes
15. BILIRUBIN: 0.39, 0.80, 1.20, 2.00, 3.00, 4.00
-- see the note below
16. ALK PHOSPHATE: 33, 80, 120, 160, 200, 250
17. SGOT: 13, 100, 200, 300, 400, 500,
18. ALBUMIN: 2.1, 3.0, 3.8, 4.5, 5.0, 6.0
19. PROTIME: 10, 20, 30, 40, 50, 60, 70, 80, 90
20. HISTOLOGY: no, yes

The BILIRUBIN attribute appears to be continuously-valued. I checked this with the donater, Bojan Cestnik, who replied:

About the hepatitis database and BILIRUBIN problem I would like to say the following: BILIRUBIN is continuous attribute (= the number of it's "values" in the ASDOHEPA.DAT file is negative!!!); "values" are quoted because when speaking about the continuous attribute there is no such thing as all possible values. However, they represent so called "boundary" values; according to these "boundary" values the attribute can be discretized. At the same time, because of the continious attribute, one can perform some other test since the continuous information is preserved. I hope that these lines have at least roughly answered your question.


Relevant Papers:

Diaconis,P. & Efron,B. (1983). Computer-Intensive Methods in Statistics. Scientific American, Volume 248.
[Web Link]

Cestnik,G., Konenenko,I, & Bratko,I. (1987). Assistant-86: A Knowledge-Elicitation Tool for Sophisticated Users. In I.Bratko & N.Lavrac (Eds.) Progress in Machine Learning, 31-45, Sigma Press.
[Web Link]


Papers That Cite This Data Set1:


Amaury Habrard and Marc Bernard and Marc Sebban. IOS Press Detecting Irrelevant Subtrees to Improve Probabilistic Learning from Tree-structured Data. Fundamenta Informaticae. 2004. [View Context].

Jinyan Li and Limsoon Wong. Using Rules to Analyse Bio-medical Data: A Comparison between C4.5 and PCL. WAIM. 2003. [View Context].

Michael L. Raymer and Travis E. Doom and Leslie A. Kuhn and William F. Punch. Knowledge discovery in medical and biological datasets using a hybrid Bayes classifier/evolutionary algorithm. IEEE Transactions on Systems, Man, and Cybernetics, Part B, 33. 2003. [View Context].

Zhi-Hua Zhou and Yuan Jiang and Shifu Chen. Extracting symbolic rules from trained neural network ensembles. AI Commun, 16. 2003. [View Context].

Xiaoli Z. Fern and Carla Brodley. Boosting Lazy Decision Trees. ICML. 2003. [View Context].

Takashi Matsuda and Hiroshi Motoda and Tetsuya Yoshida and Takashi Washio. Mining Patterns from Structured Data by Beam-Wise Graph-Based Induction. Discovery Science. 2002. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski. Ensembles of Similarity-based Models. Intelligent Information Systems. 2001. [View Context].

Gary M. Weiss and Haym Hirsh. A Quantitative Study of Small Disjuncts: Experiments and Results. Department of Computer Science Rutgers University. 2000. [View Context].

Petri Kontkanen and Petri Myllym and Tomi Silander and Henry Tirri and Peter Gr. On predictive distributions and Bayesian networks. Department of Computer Science, Stanford University. 2000. [View Context].

David W. Opitz and Richard Maclin. Popular Ensemble Methods: An Empirical Study. J. Artif. Intell. Res. (JAIR, 11. 1999. [View Context].

Yk Huhtala and Juha Kärkkäinen and Pasi Porkka and Hannu Toivonen. Efficient Discovery of Functional and Approximate Dependencies Using Partitions. ICDE. 1998. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Floriana Esposito and Donato Malerba and Giovanni Semeraro. A Comparative Analysis of Methods for Pruning Decision Trees. IEEE Trans. Pattern Anal. Mach. Intell, 19. 1997. [View Context].

Ron Kohavi. The Power of Decision Tables. ECML. 1995. [View Context].

Peter D. Turney. Cost-Sensitive Classification: Empirical Evaluation of a Hybrid Genetic Decision Tree Induction Algorithm. CoRR, csAI/9503102. 1995. [View Context].

Christophe Giraud and Tony Martinez and Christophe G. Giraud-Carrier. University of Bristol Department of Computer Science ILA: Combining Inductive Learning with Prior Knowledge and Reasoning. 1995. [View Context].

Gabor Melli. A Lazy Model-Based Approach to On-Line Classification. University of British Columbia. 1989. [View Context].

Wl/odzisl/aw Duch and Rafal Adamczak and Geerd H. F Diercksen. Neural Networks from Similarity Based Perspective. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl/odzisl/aw Duch and Karol Grudzinski and Geerd H. F Diercksen. Minimal distance neural methods. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl odzisl and Rafal Adamczak and Krzysztof Grabczewski. Optimization of Logical Rules Derived by Neural Procedures. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Wl/odzisl/aw Duch and Rafal Adamczak and Geerd H. F Diercksen. Classification, Association and Pattern Completion using Neural Similarity Based Methods. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Elena Smirnova and Ida G. Sprinkhuizen-Kuyper and I. Nalbantis and b. ERIM and Universiteit Rotterdam. Unanimous Voting using Support Vector Machines. IKAT, Universiteit Maastricht. [View Context].

Rafael S. Parpinelli and Heitor S. Lopes and Alex Alves Freitas. An Ant Colony Based System for Data Mining: Applications to Medical Data. CEFET-PR, CPGEI Av. Sete de Setembro, 3165. [View Context].

Suresh K. Choubey and Jitender S. Deogun and Vijay V. Raghavan and Hayri Sever. A comparison of feature selection algorithms in the context of rough classifiers. [View Context].

Takao Mohri and Hidehiko Tanaka. An Optimal Weighting Criterion of Case Indexing for Both Numeric and Symbolic Attributes. Information Engineering Course, Faculty of Engineering The University of Tokyo. [View Context].

Wl/odzisl/aw Duch and Rafal/ Adamczak Email:duchraad@phys. uni. torun. pl. Statistical methods for construction of neural networks. Department of Computer Methods, Nicholas Copernicus University. [View Context].

Chris Drummond and Robert C. Holte. C4.5, Class Imbalance, and Cost Sensitivity: Why Under-Sampling beats Over-Sampling. Institute for Information Technology, National Research Council Canada. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Ida G. Sprinkhuizen-Kuyper and Elena Smirnova and I. Nalbantis. Reliability yields Information Gain. IKAT, Universiteit Maastricht. [View Context].

Christophe Giraud and Tony Martinez. ADYNAMIC INCREMENTAL NETWORK THAT LEARNS BY DISCRIMINATION. AA. [View Context].

Federico Divina and Elena Marchiori. Handling Continuous Attributes in an Evolutionary Inductive Learner. Department of Computer Science Vrije Universiteit. [View Context].

Zhi-Hua Zhou and Xu-Ying Liu. Training Cost-Sensitive Neural Networks with Methods Addressing the Class Imbalance Problem. [View Context].

Rafael S. Parpinelli and Heitor S. Lopes and Alex Alves Freitas. PART FOUR: ANT COLONY OPTIMIZATION AND IMMUNE SYSTEMS Chapter X An Ant Colony Algorithm for Classification Rule Discovery. CEFET-PR, Curitiba. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/hepatitis/hepatitis.data", names=['Class', 'AGE', 'SEX', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'MALAISE', 'ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM', 'SPLEEN_PALPABLE', 'SPIDERS', 'ASCITES', 'VARICES', 'BILIRUBIN', 'ALK_PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/hepatitis/hepatitis.data", names=['Class', 'AGE', 'SEX', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'MALAISE', 'ANOREXIA', 'LIVER_BIG', 'LIVER_FIRM', 'SPLEEN_PALPABLE', 'SPIDERS', 'ASCITES', 'VARICES', 'BILIRUBIN', 'ALK_PHOSPHATE', 'SGOT', 'ALBUMIN', 'PROTIME', 'HISTOLOGY'])

print(df.info())