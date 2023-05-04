import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Topic: human subjects study

Data Set Characteristics:  

Multivariate

Number of Instances:

160

Area:

Social

Attribute Characteristics:

Categorical

Number of Attributes:

5

Date Donated

1989-03-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

128363


Source:

Creators:

Barbara and Frederick Hayes-Roth

Donor:

David W. Aha (aha '@' ics.uci.edu) (714) 856-8779


Data Set Information:

This database contains 5 numeric-valued attributes. Only a subset of 3 are used during testing (the latter 3). Furthermore, only 2 of the 3 concepts are "used" during testing (i.e., those with the prototypes 000 and 111). I've mapped all values to their zero-indexing equivalents.

Some instances could be placed in either category 0 or 1. I've followed the authors' suggestion, placing them in each category with equal probability.

I've replaced the actual values of the attributes (i.e., hobby has values chess, sports and stamps) with numeric values. I think this is how the authors' did this when testing the categorization models described in the paper. I find this unfair. While the subjects were able to bring background knowledge to bear on the attribute values and their relationships, the algorithms were provided with no such knowledge. I'm uncertain whether the 2 distractor attributes (name and hobby) are presented to the authors' algorithms during testing. However, it is clear that only the age, educational status, and marital status attributes are given during the human subjects' transfer tests.


Attribute Information:

-- 1. name: distinct for each instance and represented numerically
-- 2. hobby: nominal values ranging between 1 and 3
-- 3. age: nominal values ranging between 1 and 4
-- 4. educational level: nominal values ranging between 1 and 4
-- 5. marital status: nominal values ranging between 1 and 4
-- 6. class: nominal value between 1 and 3


Relevant Papers:

Hayes-Roth, B., & Hayes-Roth, F. (1977). Concept learning and the recognition and classification of exemplars. Journal of Verbal Learning and Verbal Behavior, 16, 321-338.
[Web Link]

Anderson, J.R., & Kline, P.J. (1979). A learning system and its psychological implications. In Proceedings of the Sixth International Joint Conference on Artificial Intelligence (pp. 16-21). Tokyo, Japan: Morgan Kaufmann.

Aha, D.W. (1989). Incremental learning of independent, overlapping, and graded concept descriptions with an instance-based process framework.Manuscript submitted for publication.


Papers That Cite This Data Set1:


Yuan Jiang and Zhi-Hua Zhou. Editing Training Data for kNN Classifiers with Neural Network Ensemble. ISNN (1). 2004. [View Context].

Bob Ricks and Dan Ventura. Training a Quantum Neural Network. NIPS. 2003. [View Context].

Gabor Melli. A Lazy Model-Based Approach to On-Line Classification. University of British Columbia. 1989. [View Context].

Anthony D. Griffiths and Derek Bridge. A Yardstick for the Evaluation of Case-Based Classifiers. Department of Computer Science, University of York. [View Context].

Jerome H. Friedman and Ron Kohavi and Youngkeol Yun. To appear in AAAI-96 Lazy Decision Trees. Statistics Department and Stanford Linear Accelerator Center Stanford University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data",names=['name', 'hobby', 'age', 'educational_level', 'marital_status', 'class'])

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.test",names=['name', 'hobby', 'age', 'educational_level', 'marital_status'])

print(df.info())
"""

#LOACL
import pandas

df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data",names=['name', 'hobby', 'age', 'educational_level', 'marital_status', 'class'])

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.test",names=['name', 'hobby', 'age', 'educational_level', 'marital_status'])

print(df.info())
print(df_test.info())