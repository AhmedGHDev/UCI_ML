import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: 1984 United Stated Congressional Voting Records; Classify as Republican or Democrat


Data Set Characteristics:  

Multivariate

Number of Instances:

435

Area:

Social

Attribute Characteristics:

Categorical

Number of Attributes:

16

Date Donated

1987-04-27

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

291115


Source:

Origin:

Congressional Quarterly Almanac, 98th Congress, 2nd session 1984, Volume XL: Congressional Quarterly Inc. Washington, D.C., 1985.

Donor:

Jeff Schlimmer (Jeffrey.Schlimmer '@' a.gp.cs.cmu.edu)


Data Set Information:

This data set includes votes for each of the U.S. House of Representatives Congressmen on the 16 key votes identified by the CQA. The CQA lists nine different types of votes: voted for, paired for, and announced for (these three simplified to yea), voted against, paired against, and announced against (these three simplified to nay), voted present, voted present to avoid conflict of interest, and did not vote or otherwise make a position known (these three simplified to an unknown disposition).


Attribute Information:

1. Class Name: 2 (democrat, republican)
2. handicapped-infants: 2 (y,n)
3. water-project-cost-sharing: 2 (y,n)
4. adoption-of-the-budget-resolution: 2 (y,n)
5. physician-fee-freeze: 2 (y,n)
6. el-salvador-aid: 2 (y,n)
7. religious-groups-in-schools: 2 (y,n)
8. anti-satellite-test-ban: 2 (y,n)
9. aid-to-nicaraguan-contras: 2 (y,n)
10. mx-missile: 2 (y,n)
11. immigration: 2 (y,n)
12. synfuels-corporation-cutback: 2 (y,n)
13. education-spending: 2 (y,n)
14. superfund-right-to-sue: 2 (y,n)
15. crime: 2 (y,n)
16. duty-free-exports: 2 (y,n)
17. export-administration-act-south-africa: 2 (y,n)


Relevant Papers:

Schlimmer, J. C. (1987). Concept acquisition through representational adjustment. Doctoral dissertation, Department of Information and Computer Science, University of California, Irvine, CA.
[Web Link]


Papers That Cite This Data Set1:


Aristides Gionis and Heikki Mannila and Panayiotis Tsaparas. Clustering Aggregation. ICDE. 2005. [View Context].

Daniel J. Lizotte and Omid Madani and Russell Greiner. Budgeted Learning of Naive-Bayes Classifiers. UAI. 2003. [View Context].

Julie Greensmith. New Frontiers For An Artificial Immune System. Digital Media Systems Laboratory HP Laboratories Bristol. 2003. [View Context].

Jonathan Eckstein and Peter L. Hammer and Ying Liu and Mikhail Nediak and Bruno Simeone. The Maximum Box Problem and its Application to Data Analysis. RUTCOR Rutgers Center for Operations Research Rutgers University. 2002. [View Context].

Daniel Barbar and Yi Li and Julia Couto. COOLCAT: an entropy-based algorithm for categorical clustering. CIKM. 2002. [View Context].

Federico Divina and Elena Marchiori. Evolutionary Concept Learning. GECCO. 2002. [View Context].

Robert M French and Nick Chater. Using Noise to Compute Error Surfaces in Connectionist Networks: A Novel Means of Reducing Catastrophic Forgetting. Neural Computation. 2002. [View Context].

Gary M. Weiss and Haym Hirsh. A Quantitative Study of Small Disjuncts: Experiments and Results. Department of Computer Science Rutgers University. 2000. [View Context].

Chun-Nan Hsu and Hilmar Schuschel and Ya-Ting Yang. The ANNIGMA-Wrapper Approach to Neural Nets Feature Selection for Knowledge Discovery and Data Mining. Institute of Information Science. 1999. [View Context].

Huan Liu and Rudy Setiono. Incremental Feature Selection. Appl. Intell, 9. 1998. [View Context].

Blai Bonet and Hector Geffner. Learning Sorting and Decision Trees with POMDPs. ICML. 1998. [View Context].

Eui-Hong Han and George Karypis and Vipin Kumar and Bamshad Mobasher. Clustering Based On Association Rule Hypergraphs. DMKD. 1997. [View Context].

Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja. Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF. Appl. Intell, 7. 1997. [View Context].

Erin J. Bredensteiner and Kristin P. Bennett. Feature Minimization within Decision Trees. National Science Foundation. 1996. [View Context].

Ron Kohavi and George H. John and Richard Long and David Manley and Karl Pfleger. MLC++: A Machine Learning Library in C. ICTAI. 1994. [View Context].

Igor Kononenko and Edvard Simec. Induction of decision trees using RELIEFF. University of Ljubljana, Faculty of electrical engineering & computer science. [View Context].

Daniel J. Lizotte. Library Release Form Name of Author. Budgeted Learning of Naive Bayes Classifiers. [View Context].

Daniel J. Lizotte and Omid Madani and Russell Greiner. Budgeted Learning, Part II: The Na#ve-Bayes Case. Department of Computing Science University of Alberta. [View Context].

Chotirat Ann and Dimitrios Gunopulos. Scaling up the Naive Bayesian Classifier: Using Decision Trees for Feature Selection. Computer Science Department University of California. [View Context].

Rudy Setiono and Huan Liu. Neural-Network Feature Selector. Department of Information Systems and Computer Science National University of Singapore. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data"
,names=['Class_Name', 'handicapped-infants', 'water-project-cost-sharing', 'adoption-of-the-budget-resolution', 'physician-fee-freeze', 'el-salvador-aid', 'religious-groups-in-schools', 'anti-satellite-test-ban', 'aid-to-nicaraguan-contras', 'mx-missile', 'immigration', 'synfuels-corporation-cutback', 'education-spending', 'superfund-right-to-sue', 'crime', 'duty-free-exports', 'export-administration-act-south-africa']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data"
,names=['Class_Name', 'handicapped-infants', 'water-project-cost-sharing', 'adoption-of-the-budget-resolution', 'physician-fee-freeze', 'el-salvador-aid', 'religious-groups-in-schools', 'anti-satellite-test-ban', 'aid-to-nicaraguan-contras', 'mx-missile', 'immigration', 'synfuels-corporation-cutback', 'education-spending', 'superfund-right-to-sue', 'crime', 'duty-free-exports', 'export-administration-act-south-africa']
)

print(df.info())