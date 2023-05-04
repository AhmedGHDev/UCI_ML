import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: From Collective Bargaining Review

Data Set Characteristics:  

Multivariate

Number of Instances:

57

Area:

Social

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

16

Date Donated

1988-11-01

Associated Tasks:

N/A

Missing Values?

No

Number of Web Hits:

102187


Source:

Creators:

Collective Barganing Review, montly publication,
Labour Canada, Industrial Relations Information Service,
Ottawa, Ontario, K1A 0J2, Canada, (819) 997-3117

The data includes all collective agreements reached in the business and personal services sector for locals with at least 500 members (teachers, nurses, university staff, police, etc) in Canada in 87 and first quarter of 88.

Donor:

Stan Matwin, Computer Science Dept
University of Ottawa,
34 Somerset East, K1N 9B4, (stan '@' uotcsi2.bitnet)


Data Set Information:

Data was used to test 2 tier approach with learning from positive and negative examples


Attribute Information:

1. dur: duration of agreement
[1..7]
2 wage1.wage : wage increase in first year of contract
[2.0 .. 7.0]
3 wage2.wage : wage increase in second year of contract
[2.0 .. 7.0]
4 wage3.wage : wage increase in third year of contract
[2.0 .. 7.0]
5 cola : cost of living allowance
[none, tcf, tc]
6 hours.hrs : number of working hours during week
[35 .. 40]
7 pension : employer contributions to pension plan
[none, ret_allw, empl_contr]
8 stby_pay : standby pay
[2 .. 25]
9 shift_diff : shift differencial : supplement for work on II and III shift
[1 .. 25]
10 educ_allw.boolean : education allowance
[true false]
11 holidays : number of statutory holidays
[9 .. 15]
12 vacation : number of paid vacation days
[ba, avg, gnr]
13 lngtrm_disabil.boolean : employer's help during employee longterm disability
[true , false]
14 dntl_ins : employers contribution towards the dental plan
[none, half, full]
15 bereavement.boolean : employer's financial contribution towards the covering the costs of bereavement
[true , false]
16 empl_hplan : employer's contribution towards the health plan
[none, half, full]


Relevant Papers:

Bergadano, F., Matwin, S., Michalski, R., Zhang, J., Measuring Quality of Concept Descriptions, Procs. of the 3rd European Working Sessions on Learning, Glasgow, October 1988.
[Web Link]

Bergadano, F., Matwin, S., Michalski, R., Zhang, J.,Representing and Acquiring Imprecise and Context-dependent Concepts in Knowledge-based Systems, Procs. of ISMIS'88, North Holland, 1988.
[Web Link]


Papers That Cite This Data Set1:


Rudy Setiono. Feedforward Neural Network Construction Using Cross Validation. Neural Computation, 13. 2001. [View Context].

Endre Boros and Peter Hammer and Toshihide Ibaraki and Alexander Kogan and Eddy Mayoraz and Ilya B. Muchnik. An Implementation of Logical Analysis of Data. IEEE Trans. Knowl. Data Eng, 12. 2000. [View Context].

Gary M. Weiss and Haym Hirsh. A Quantitative Study of Small Disjuncts: Experiments and Results. Department of Computer Science Rutgers University. 2000. [View Context].

Lorne Mason and Jonathan Baxter and Peter L. Bartlett and Marcus Frean. Boosting Algorithms as Gradient Descent. NIPS. 1999. [View Context].

Richard Maclin. Boosting Classifiers Regionally. AAAI/IAAI. 1998. [View Context].

Huan Liu and Rudy Setiono. A Probabilistic Approach to Feature Selection - A Filter Solution. ICML. 1996. [View Context].

Oya Ekin and Peter L. Hammer and Alexander Kogan and Pawel Winter. Distance-Based Classification Methods. e p o r t RUTCOR ffl Rutgers Center for Operations Research ffl Rutgers University. 1996. [View Context].

George H. John and Ron Kohavi and Karl Pfleger. Irrelevant Features and the Subset Selection Problem. ICML. 1994. [View Context].

Ron Kohavi and George H. John. Automatic Parameter Selection by Minimizing Estimated Error. Computer Science Dept. Stanford University. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

YongSeog Kim and W. Nick Street and Filippo Menczer. Optimal Ensemble Construction via Meta-Evolutionary Ensembles. Business Information Systems, Utah State University. [View Context].

Ida G. Sprinkhuizen-Kuyper and Elena Smirnova and I. Nalbantis. Reliability yields Information Gain. IKAT, Universiteit Maastricht. [View Context].

Chris Drummond and Robert C. Holte. C4.5, Class Imbalance, and Cost Sensitivity: Why Under-Sampling beats Over-Sampling. Institute for Information Technology, National Research Council Canada. [View Context].

Huan Liu and Rudy Setiono. To appear in Proceedings of IEA-AIE96 FEATURE SELECTION AND CLASSIFICATION -- A PROBABILISTIC WRAPPER APPROACH. Department of Information Systems and Computer Science National University of Singapore. [View Context].

John G. Cleary and Leonard E. Trigg. Experiences with OB1, An Optimal Bayes Decision Tree Learner. Department of Computer Science University of Waikato. [View Context].

Alexander K. Seewald. Meta-Learning for Stacked Classification. Austrian Research Institute for Artificial Intelligence. [View Context].

Karthik Ramakrishnan. UNIVERSITY OF MINNESOTA. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/labor-negotiations/C4.5/labor-neg.data"
, names=['dur', 'wage1_wage', 'wage2_wage', 'wage3_wage', 'cola', 'hours_hrs', 'pension', 'stby_pay', 'shift_diff', 'educ_allw_boolean', 'holidays', 'vacation', 'lngtrm_disabil_boolean', 'dntl_ins', 'bereavement_boolean', 'empl_hplan']
)

df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/labor-negotiations/C4.5/labor-neg.test"
, names=['dur', 'wage1_wage', 'wage2_wage', 'wage3_wage', 'cola', 'hours_hrs', 'pension', 'stby_pay', 'shift_diff', 'educ_allw_boolean', 'holidays', 'vacation', 'lngtrm_disabil_boolean', 'dntl_ins', 'bereavement_boolean', 'empl_hplan']
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
import pandas
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/labor-negotiations/C4.5/labor-neg.data"
, names=['dur', 'wage1_wage', 'wage2_wage', 'wage3_wage', 'cola', 'hours_hrs', 'pension', 'stby_pay', 'shift_diff', 'educ_allw_boolean', 'holidays', 'vacation', 'lngtrm_disabil_boolean', 'dntl_ins', 'bereavement_boolean', 'empl_hplan']
)

df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/labor-negotiations/C4.5/labor-neg.test"
, names=['dur', 'wage1_wage', 'wage2_wage', 'wage3_wage', 'cola', 'hours_hrs', 'pension', 'stby_pay', 'shift_diff', 'educ_allw_boolean', 'holidays', 'vacation', 'lngtrm_disabil_boolean', 'dntl_ins', 'bereavement_boolean', 'empl_hplan']
)

print(df_train.info())
print(df_test.info())