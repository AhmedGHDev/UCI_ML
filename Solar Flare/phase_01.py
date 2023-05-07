import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Each class attribute counts the number of solar flares of a certain class that occur in a 24 hour period


Data Set Characteristics:  

Multivariate

Number of Instances:

1389

Area:

Physical

Attribute Characteristics:

Categorical

Number of Attributes:

10

Date Donated

1989-03-01

Associated Tasks:

Regression

Missing Values?

No

Number of Web Hits:

202792


Source:

Donor:

Gary Bradshaw <gbradshaw '@' clipr.colorado.EDU>


Data Set Information:

Notes:

-- The database contains 3 potential classes, one for the number of times a certain type of solar flare occured in a 24 hour period.
-- Each instance represents captured features for 1 active region on the sun.
-- The data are divided into two sections. The second section (flare.data2) has had much more error correction applied to the it, and has consequently been treated as more reliable.


Attribute Information:

1. Code for class (modified Zurich class) (A,B,C,D,E,F,H)
2. Code for largest spot size (X,R,S,A,H,K)
3. Code for spot distribution (X,O,I,C)
4. Activity (1 = reduced, 2 = unchanged)
5. Evolution (1 = decay, 2 = no growth, 3 = growth)
6. Previous 24 hour flare activity code (1 = nothing as big as an M1, 2 = one M1, 3 = more activity than one M1)
7. Historically-complex (1 = Yes, 2 = No)
8. Did region become historically complex on this pass across the sun's disk (1 = yes, 2 = no)
9. Area (1 = small, 2 = large)
10. Area of the largest spot (1 = <=5, 2 = >5)

From all these predictors three classes of flares are predicted, which are represented in the last three columns.

11. C-class flares production by this region in the following 24 hours (common flares); Number
12. M-class flares production by this region in the following 24 hours (moderate flares); Number
13. X-class flares production by this region in the following 24 hours (severe flares); Number

Relevant Papers:

N/A


Papers That Cite This Data Set1:


Jinyan Li and Guozhu Dong and Kotagiri Ramamohanarao and Limsoon Wong. DeEPs: A New Instance-based Discovery and Classification System. Proceedings of the Fourth European Conference on Principles and Practice of Knowledge Discovery in Databases. 2001. [View Context].

Jinyan Li and Guozhu Dong and Kotagiri Ramamohanarao. Instance-Based Classification by Emerging Patterns. PKDD. 2000. [View Context].

Sally A. Goldman and Yan Zhou. Enhancing Supervised Learning with Unlabeled Data. ICML. 2000. [View Context].

Nir Friedman and Daphne Koller. Being Bayesian about Network Structure. UAI. 2000. [View Context].

Christophe G. Giraud-Carrier and Tony R. Martinez. An Integrated Framework for Learning and Reasoning. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

C. Titus Brown and Harry W. Bullen and Sean P. Kelly and Robert K. Xiao and Steven G. Satterfield and John G. Hagedorn and Judith E. Devaney. Visualization and Data Mining in an 3D Immersive Environment: Summer Project 2003. [View Context].

Nir Friedman and Daphne Koller (koller@cs. stanford. edu. A Bayesian Approach to Structure Discovery in Bayesian Networks. School of Computer Science & Engineering Hebrew University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/solar-flare/flare.data1"
,skiprows=1
,delimiter=' '
,names=['class', 'largest spot size', 'spot distribution', 'Activity', 'Evolution', 'Previous 24 hour flare activity', 'Historically-complex', 'historically complex on pass', 'Area', 'largest spot area', 'common flares', 'moderate flares', 'severe flares']
)

df_2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/solar-flare/flare.data1"
,skiprows=1
,delimiter=' '
,names=['class', 'largest spot size', 'spot distribution', 'Activity', 'Evolution', 'Previous 24 hour flare activity', 'Historically-complex', 'historically complex on pass', 'Area', 'largest spot area', 'common flares', 'moderate flares', 'severe flares']
)

df = pd.concat([df_1, df_2], axis=0)
print(df.info())
"""

#LOACL
import pandas
df_1 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/solar-flare/flare.data1"
,skiprows=1,delimiter=' ',names=['class', 'largest spot size', 'spot distribution', 'Activity', 'Evolution', 'Previous 24 hour flare activity', 'Historically-complex', 'historically complex on pass', 'Area', 'largest spot area', 'common flares', 'moderate flares', 'severe flares']
)

df_2 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/solar-flare/flare.data1",skiprows=1,delimiter=' ',names=['class', 'largest spot size', 'spot distribution', 'Activity', 'Evolution', 'Previous 24 hour flare activity', 'Historically-complex', 'historically complex on pass', 'Area', 'largest spot area', 'common flares', 'moderate flares', 'severe flares']
)

df = pd.concat([df_1, df_2], axis=0)
print(df.info())