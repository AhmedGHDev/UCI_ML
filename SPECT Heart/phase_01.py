import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Data on cardiac Single Proton Emission Computed Tomography (SPECT) images. Each patient classified into two categories: normal and abnormal.


Data Set Characteristics:  

Multivariate

Number of Instances:

267

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

22

Date Donated

2001-10-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

244478


Source:

Original Owners:

Krzysztof J. Cios, Lukasz A. Kurgan
University of Colorado at Denver, Denver, CO 80217, U.S.A.
Krys.Cios '@' cudenver.edu
Lucy S. Goodenday
Medical College of Ohio, OH, U.S.A.

Donors:

Lukasz A.Kurgan, Krzysztof J. Cios


Data Set Information:

The dataset describes diagnosing of cardiac Single Proton Emission Computed Tomography (SPECT) images. Each of the patients is classified into two categories: normal and abnormal. The database of 267 SPECT image sets (patients) was processed to extract features that summarize the original SPECT images. As a result, 44 continuous feature pattern was created for each patient. The pattern was further processed to obtain 22 binary feature patterns. The CLIP3 algorithm was used to generate classification rules from these patterns. The CLIP3 algorithm generated rules that were 84.0% accurate (as compared with cardilogists' diagnoses).

SPECT is a good data set for testing ML algorithms; it has 267 instances that are descibed by 23 binary attributes


Attribute Information:

1. OVERALL_DIAGNOSIS: 0,1 (class attribute, binary)
2. F1: 0,1 (the partial diagnosis 1, binary)
3. F2: 0,1 (the partial diagnosis 2, binary)
4. F3: 0,1 (the partial diagnosis 3, binary)
5. F4: 0,1 (the partial diagnosis 4, binary)
6. F5: 0,1 (the partial diagnosis 5, binary)
7. F6: 0,1 (the partial diagnosis 6, binary)
8. F7: 0,1 (the partial diagnosis 7, binary)
9. F8: 0,1 (the partial diagnosis 8, binary)
10. F9: 0,1 (the partial diagnosis 9, binary)
11. F10: 0,1 (the partial diagnosis 10, binary)
12. F11: 0,1 (the partial diagnosis 11, binary)
13. F12: 0,1 (the partial diagnosis 12, binary)
14. F13: 0,1 (the partial diagnosis 13, binary)
15. F14: 0,1 (the partial diagnosis 14, binary)
16. F15: 0,1 (the partial diagnosis 15, binary)
17. F16: 0,1 (the partial diagnosis 16, binary)
18. F17: 0,1 (the partial diagnosis 17, binary)
19. F18: 0,1 (the partial diagnosis 18, binary)
20. F19: 0,1 (the partial diagnosis 19, binary)
21. F20: 0,1 (the partial diagnosis 20, binary)
22. F21: 0,1 (the partial diagnosis 21, binary)
23. F22: 0,1 (the partial diagnosis 22, binary)
- dataset is divided into:
-- training data ("SPECT.train" 80 instances)
-- testing data ("SPECT.test" 187 instances)


Relevant Papers:

Kurgan, L.A., Cios, K.J., Tadeusiewicz, R., Ogiela, M. & Goodenday, L.S. "Knowledge Discovery Approach to Automated Cardiac SPECT Diagnosis" Artificial Intelligence in Medicine, vol. 23:2, pp 149-169, Oct 2001
[Web Link]

Cios, K.J., Wedding, D.K. & Liu, N. CLIP3: cover learning using integer programming. Kybernetes, 26:4-5, pp 513-536, 1997

Cios K. J. & Kurgan L. Hybrid Inductive Machine Learning: An Overview of CLIP Algorithms, In: Jain L.C., and Kacprzyk J. (Eds). New Learning Paradigms in Soft Computing, Physica-Verlag (Springer), 2001
[Web Link]


Papers That Cite This Data Set1:


Rich Caruana and Alexandru Niculescu-Mizil. An Empirical Evaluation of Supervised Learning for ROC Area. ROCAI. 2004. [View Context].

Michael G. Madden. Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. CoRR, csLG/0211003. 2002. [View Context].

Lukasz A. Kurgan and Waldemar Swiercz and Krzysztof J. Cios. Semantic Mapping of XML Tags Using Inductive Machine Learning. ICMLA. 2002. [View Context].

M. A. Galway and Michael G. Madden. DEPARTMENT OF INFORMATION TECHNOLOGY technical report NUIG-IT-011002 Evaluation of the Performance of the Markov Blanket Bayesian Classifier Algorithm. Department of Information Technology National University of Ireland, Galway. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECT.train"
,names=['OVERALL_DIAGNOSIS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22']
)


df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECT.test"
,names=['OVERALL_DIAGNOSIS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22']
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
import pandas
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/spect/SPECT.train"
,names=['OVERALL_DIAGNOSIS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22']
)


df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/spect/SPECT.test"
,names=['OVERALL_DIAGNOSIS', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22']
)

print(df_train.info())
print(df_test.info())