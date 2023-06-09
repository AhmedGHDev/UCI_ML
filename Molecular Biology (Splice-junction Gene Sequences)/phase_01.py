import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Primate splice-junction gene sequences (DNA) with associated imperfect domain theory


Data Set Characteristics:  

Sequential, Domain-Theory

Number of Instances:

3190

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

61

Date Donated

1992-01-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

122590


Source:

Creators:

1. All examples taken from Genbank 64.1 (ftp site: genbank.bio.net)
2. Categories "ei" and "ie" include every "split-gene" for primates in Genbank 64.1
3. non-splice examples taken from sequences known not to include a splicing site

Donor:

G. Towell, M. Noordewier, and J. Shavlik,
{towell,shavlik}@cs.wisc.edu, noordewi '@' cs.rutgers.edu


Data Set Information:

Problem Description:

Splice junctions are points on a DNA sequence at which `superfluous' DNA is removed during the process of protein creation in higher organisms. The problem posed in this dataset is to recognize, given a sequence of DNA, the boundaries between exons (the parts of the DNA sequence retained after splicing) and introns (the parts of the DNA sequence that are spliced out). This problem consists of two subtasks: recognizing exon/intron boundaries (referred to as EI sites), and recognizing intron/exon boundaries (IE sites). (In the biological community, IE borders are referred to a ``acceptors'' while EI borders are referred to as ``donors''.)

This dataset has been developed to help evaluate a "hybrid" learning algorithm (KBANN) that uses examples to inductively refine preexisting knowledge. Using a "ten-fold cross-validation" methodology on 1000 examples randomly selected from the complete set of 3190, the following error rates were produced by various ML algorithms (all experiments run at the Univ of Wisconsin, sometimes with local implementations of published algorithms).

System -- Neither -- EI -- IE
---------------------------------------------------
KBANN -- 4.62 -- 7.56 -- 8.47
BACKPROP -- 5.29 -- 5.74 -- 10.75
PEBLS -- 6.86 -- 8.18 -- 7.55
PERCEPTRON -- 3.99 -- 16.32 -- 17.41
ID3 -- 8.84 -- 10.58 -- 13.99
COBWEB -- 11.80 -- 15.04 -- 9.46
Near. Neighbor -- 31.11 -- 11.65 -- 9.09


Attribute Information:

1. One of {n ei ie}, indicating the class.
2. The instance name.
3-62. The remaining 60 fields are the sequence, starting at position -30 and ending at position +30. Each of these fields is almost always filled by one of {a, g, t, c}. Other characters indicate ambiguity among the standard characters according to the following table:

character: meaning
D: A or G or T
N: A or G or C or T
S: C or G
R: A or G


Relevant Papers:

M. O. Noordewier and G. G. Towell and J. W. Shavlik, 1991; "Training Knowledge-Based Neural Networks to Recognize Genes in DNA Sequences". Advances in Neural Information Processing Systems, volume 3, Morgan Kaufmann.
[Web Link]

G. G. Towell and J. W. Shavlik and M. W. Craven, 1991; "Constructive Induction in Knowledge-Based Neural Networks", In Proceedings of the Eighth International Machine Learning Workshop, Morgan Kaufmann.
[Web Link]

G. G. Towell, 1991; "Symbolic Knowledge and Neural Networks: Insertion, Refinement, and Extraction", PhD Thesis, University of Wisconsin - Madison.
[Web Link]

G. G. Towell and J. W. Shavlik, 1992; "Interpretation of Artificial Neural Networks: Mapping Knowledge-based Neural Networks into Rules", In Advances in Neural Information Processing Systems, volume 4, Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Jinyan Li and Limsoon Wong. Using Rules to Analyse Bio-medical Data: A Comparison between C4.5 and PCL. WAIM. 2003. [View Context].

S. Sathiya Keerthi and Kaibo Duan and Shirish Krishnaj Shevade and Aun Neow Poo. A Fast Dual Algorithm for Kernel Logistic Regression. ICML. 2002. [View Context].

Michael G. Madden. Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. CoRR, csLG/0211003. 2002. [View Context].

Xiaojin Zhu. Label Propagation for Eukaryotic Splice Junction Identification. 2002. [View Context].

Mukund Deshpande and George Karypis. Evaluation of Techniques for Classifying Biological Sequences. PAKDD. 2002. [View Context].

Susanne Hoche and Stefan Wrobel. Scaling Boosting by Margin-Based Inclusionof Features and Relations. ECML. 2002. [View Context].

Jinyan Li and Kotagiri Ramamohanarao and Guozhu Dong. Combining the Strength of Pattern Frequency and Distance for Classification. PAKDD. 2001. [View Context].

Jinyan Li and Guozhu Dong and Kotagiri Ramamohanarao and Limsoon Wong. DeEPs: A New Instance-based Discovery and Classification System. Proceedings of the Fourth European Conference on Principles and Practice of Knowledge Discovery in Databases. 2001. [View Context].

Jinyan Li and Guozhu Dong and Kotagiri Ramamohanarao. Instance-Based Classification by Emerging Patterns. PKDD. 2000. [View Context].

Thomas G. Dietterich. An Experimental Comparison of Three Methods for Constructing Ensembles of Decision Trees: Bagging, Boosting, and Randomization. Machine Learning, 40. 2000. [View Context].

Marina Meila and Michael I. Jordan. Learning with Mixtures of Trees. Journal of Machine Learning Research, 1. 2000. [View Context].

Yoav Freund and Lorne Mason. The Alternating Decision Tree Learning Algorithm. ICML. 1999. [View Context].

Lorne Mason and Jonathan Baxter and Peter L. Bartlett and Marcus Frean. Boosting Algorithms as Gradient Descent. NIPS. 1999. [View Context].

Kagan Tumer and Nikunj C. Oza. Decimated Input Ensembles for Improved Generalization. NASA Ames Research Center. 1999. [View Context].

Blaz Zupan and Marko Bohanec and Janez Dem#sar and Ivan Bratko. Learning by Discovering Concept Hierarchies. Artif. Intell, 109. 1999. [View Context].

Kai Ming Ting and Ian H. Witten. Issues in Stacked Generalization. J. Artif. Intell. Res. (JAIR, 10. 1999. [View Context].

Andreas L. Prodromidis. On the Management of Distributed Learning Agents Ph.D. Thesis Proposal CUCS-032-97. Department of Computer Science Columbia University. 1998. [View Context].

Manoranjan Dash and Huan Liu. Hybrid Search of Feature Subsets. PRICAI. 1998. [View Context].

Adam J. Grove and Dale Schuurmans. Boosting in the Limit: Maximizing the Margin of Learned Ensembles. AAAI/IAAI. 1998. [View Context].

Foster J. Provost and Tom Fawcett and Ron Kohavi. The Case against Accuracy Estimation for Comparing Induction Algorithms. ICML. 1998. [View Context].

Kai Ming Ting and Boon Toh Low. Model Combination in the Multiple-Data-Batches Scenario. ECML. 1997. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Gustavo E. A and Gustavo E A P A Batista and Ronaldo C. Prati and Maria Carolina Monard. A Study of the Behavior of Several Methods for Balancing Machine Learning Training Data. Instituto de Ci ^ encias Matem aticas e de Computac~ ao. [View Context].

Kai Ming Ting and Boon Toh Low. Theory Combination: an alternative to Data Combination. University of Waikato. [View Context].

Rudy Setiono. Extracting M-of-N Rules from Trained Neural Networks. School of Computing National University of Singapore. [View Context].

Rong-En Fan and P. -H Chen and C. -J Lin. Working Set Selection Using the Second Order Information for Training SVM. Department of Computer Science and Information Engineering National Taiwan University. [View Context].

M. A. Galway and Michael G. Madden. DEPARTMENT OF INFORMATION TECHNOLOGY technical report NUIG-IT-011002 Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. Department of Information Technology National University of Ireland, Galway. [View Context].

Pedro Domingos. Using Partitioning to Speed Up Specific-to-General Rule Induction. Department of Information and Computer Science University of California, Irvine. [View Context].

Kai Ming Ting and Ian H. Witten. Stacked Generalization: when does it work. Department of Computer Science University of Waikato. [View Context].

Cesar Guerra-Salcedo and Stephen Chen and Darrell Whitley and Sarah Smith. Fast and Accurate Feature Selection Using Hybrid Genetic Strategies. Department of Computer Science Colorado State University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/molecular-biology/splice-junction-gene-sequences/splice.data", names=['class', 'instance_name', 'sequence'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/molecular-biology/splice-junction-gene-sequences/splice.data", names=['class', 'instance_name', 'sequence'])

print(df.info())