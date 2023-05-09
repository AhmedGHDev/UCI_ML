import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset is a heart disease database similar to a database already present in the repository (Heart Disease databases) but in a slightly different form


Data Set Characteristics:  

Multivariate

Number of Instances:

270

Area:

Life

Attribute Characteristics:

Categorical, Real

Number of Attributes:

13

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

304366


Source:

N/A


Data Set Information:

Cost Matrix

_______ abse pres
absence 0 1
presence 5 0

where the rows represent the true values and the columns the predicted.


Attribute Information:


Attribute Information:
------------------------
-- 1. age
-- 2. sex
-- 3. chest pain type (4 values)
-- 4. resting blood pressure
-- 5. serum cholesterol in mg/dl
-- 6. fasting blood sugar > 120 mg/dl
-- 7. resting electrocardiographic results (values 0,1,2)
-- 8. maximum heart rate achieved
-- 9. exercise induced angina
-- 10. oldpeak = ST depression induced by exercise relative to rest
-- 11. the slope of the peak exercise ST segment
-- 12. number of major vessels (0-3) colored by flourosopy
-- 13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

Attributes types
-----------------

Real: 1,4,5,8,10,12
Ordered:11,
Binary: 2,6,9
Nominal:7,3,13

Variable to be predicted
------------------------
Absence (1) or presence (2) of heart disease


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Gavin Brown. Diversity in Neural Network Ensembles. The University of Birmingham. 2004. [View Context].

Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja. Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF. Appl. Intell, 7. 1997. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Elena Smirnova and Ida G. Sprinkhuizen-Kuyper and I. Nalbantis and b. ERIM and Universiteit Rotterdam. Unanimous Voting using Support Vector Machines. IKAT, Universiteit Maastricht. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/heart/heart.dat"
,names=['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'serum_cholesterol_mg/dl', 'fasting_blood_sugar_>_120_mg/dl', 'resting_electrocardiographic', 'maximum_heart_rate', 'exercise', 'oldpeak', 'peak_exercise_ST_segment_slope', 'major_vessels', 'thal']
,delimiter='\s+'
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/statlog/heart/heart.dat"
,names=['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'serum_cholesterol_mg/dl', 'fasting_blood_sugar_>_120_mg/dl', 'resting_electrocardiographic', 'maximum_heart_rate', 'exercise', 'oldpeak', 'peak_exercise_ST_segment_slope', 'major_vessels', 'thal']
,delimiter='\s+'
)

print(df.info())