import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The dataset consists of measurements of fetal heart rate (FHR) and uterine contraction (UC) features on cardiotocograms classified by expert obstetricians.

Data Set Characteristics:  

Multivariate

Number of Instances:

2126

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

23

Date Donated

2010-09-07

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

237136


Source:

Marques de SÃ¡, J.P., jpmdesa '@' gmail.com, Biomedical Engineering Institute, Porto, Portugal.
Bernardes, J., joaobern '@' med.up.pt, Faculty of Medicine, University of Porto, Portugal.
Ayres de Campos, D., sisporto '@' med.up.pt, Faculty of Medicine, University of Porto, Portugal.


Data Set Information:

2126 fetal cardiotocograms (CTGs) were automatically processed and the respective diagnostic features measured. The CTGs were also classified by three expert obstetricians and a consensus classification label assigned to each of them. Classification was both with respect to a morphologic pattern (A, B, C. ...) and to a fetal state (N, S, P). Therefore the dataset can be used either for 10-class or 3-class experiments.


Attribute Information:

LB - FHR baseline (beats per minute)
AC - # of accelerations per second
FM - # of fetal movements per second
UC - # of uterine contractions per second
DL - # of light decelerations per second
DS - # of severe decelerations per second
DP - # of prolongued decelerations per second
ASTV - percentage of time with abnormal short term variability
MSTV - mean value of short term variability
ALTV - percentage of time with abnormal long term variability
MLTV - mean value of long term variability
Width - width of FHR histogram
Min - minimum of FHR histogram
Max - Maximum of FHR histogram
Nmax - # of histogram peaks
Nzeros - # of histogram zeros
Mode - histogram mode
Mean - histogram mean
Median - histogram median
Variance - histogram variance
Tendency - histogram tendency
CLASS - FHR pattern class code (1 to 10)
NSP - fetal state class code (N=normal; S=suspect; P=pathologic)


Relevant Papers:

Ayres de Campos et al. (2000) SisPorto 2.0 A Program for Automated Analysis of Cardiotocograms. J Matern Fetal Med 5:311-318



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
import pandas as pd
xls = pd.ExcelFile('https://archive.ics.uci.edu/ml/machine-learning-databases/00193/CTG.xls')
df = pd.read_excel(xls, 'Data')


print(df.info())
"""

#LOACL
import pandas as pd
xls = pd.ExcelFile('../ics.uci.edu/ml/machine-learning-databases/00193/CTG.xls')
df = pd.read_excel(xls, 'Data')


print(df.info())