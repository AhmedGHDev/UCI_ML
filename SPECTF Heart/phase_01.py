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

Integer

Number of Attributes:

44

Date Donated

2001-10-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

119343


Source:

Original owners:

1. Krzysztof J. Cios, Lukasz A. Kurgan
University of Colorado at Denver, Denver, CO 80217, U.S.A.
Krys.Cios '@' cudenver.edu

2. Lucy S. Goodenday
Medical College of Ohio, OH, U.S.A.

Donors:

Lukasz A.Kurgan, Krzysztof J. Cios


Data Set Information:

The dataset describes diagnosing of cardiac Single Proton Emission Computed Tomography (SPECT) images. Each of the patients is classified into two categories: normal and abnormal. The database of 267 SPECT image sets (patients) was processed to extract features that summarize the original SPECT images. As a result, 44 continuous feature pattern was created for each patient. The CLIP3 algorithm was used to generate classification rules from these patterns. The CLIP3 algorithm generated rules that were 77.0% accurate (as compared with cardilogists' diagnoses).

SPECTF is a good data set for testing ML algorithms; it has 267 instances that are descibed by 45 attributes.

Predicted attribute: OVERALL_DIAGNOSIS (binary)

NOTE: See the SPECT heart data for binary data for the same classification task.


Attribute Information:

1. OVERALL_DIAGNOSIS: 0,1 (class attribute, binary)
2. F1R: continuous (count in ROI (region of interest) 1 in rest)
3. F1S: continuous (count in ROI 1 in stress)
4. F2R: continuous (count in ROI 2 in rest)
5. F2S: continuous (count in ROI 2 in stress)
6. F3R: continuous (count in ROI 3 in rest)
7. F3S: continuous (count in ROI 3 in stress)
8. F4R: continuous (count in ROI 4 in rest)
9. F4S: continuous (count in ROI 4 in stress)
10. F5R: continuous (count in ROI 5 in rest)
11. F5S: continuous (count in ROI 5 in stress)
12. F6R: continuous (count in ROI 6 in rest)
13. F6S: continuous (count in ROI 6 in stress)
14. F7R: continuous (count in ROI 7 in rest)
15. F7S: continuous (count in ROI 7 in stress)
16. F8R: continuous (count in ROI 8 in rest)
17. F8S: continuous (count in ROI 8 in stress)
18. F9R: continuous (count in ROI 9 in rest)
19. F9S: continuous (count in ROI 9 in stress)
20. F10R: continuous (count in ROI 10 in rest)
21. F10S: continuous (count in ROI 10 in stress)
22. F11R: continuous (count in ROI 11 in rest)
23. F11S: continuous (count in ROI 11 in stress)
24. F12R: continuous (count in ROI 12 in rest)
25. F12S: continuous (count in ROI 12 in stress)
26. F13R: continuous (count in ROI 13 in rest)
27. F13S: continuous (count in ROI 13 in stress)
28. F14R: continuous (count in ROI 14 in rest)
29. F14S: continuous (count in ROI 14 in stress)
30. F15R: continuous (count in ROI 15 in rest)
31. F15S: continuous (count in ROI 15 in stress)
32. F16R: continuous (count in ROI 16 in rest)
33. F16S: continuous (count in ROI 16 in stress)
34. F17R: continuous (count in ROI 17 in rest)
35. F17S: continuous (count in ROI 17 in stress)
36. F18R: continuous (count in ROI 18 in rest)
37. F18S: continuous (count in ROI 18 in stress)
38. F19R: continuous (count in ROI 19 in rest)
39. F19S: continuous (count in ROI 19 in stress)
40. F20R: continuous (count in ROI 20 in rest)
41. F20S: continuous (count in ROI 20 in stress)
42. F21R: continuous (count in ROI 21 in rest)
43. F21S: continuous (count in ROI 21 in stress)
44. F22R: continuous (count in ROI 22 in rest)
45. F22S: continuous (count in ROI 22 in stress)
- all continuous attributes have integer values from the 0 to 100
- dataset is divided into:
-- training data ("SPECTF.train" 80 instances)
-- testing data ("SPECTF.test" 187 instances)


Relevant Papers:

Kurgan, L.A., Cios, K.J., Tadeusiewicz, R., Ogiela, M. & Goodenday, L.S. "Knowledge Discovery Approach to Automated Cardiac SPECT Diagnosis" Artificial Intelligence in Medicine, vol. 23:2, pp 149-169, Oct 2001
[Web Link]

Cios, K.J., Wedding, D.K. & Liu, N. CLIP3: cover learning using integer programming. Kybernetes, 26:4-5, pp 513-536, 1997

Cios K. J. & Kurgan L. Hybrid Inductive Machine Learning: An Overview of CLIP Algorithms, In: Jain L.C., and Kacprzyk J. (Eds). New Learning Paradigms in Soft Computing, Physica-Verlag (Springer), 2001
[Web Link]


Papers That Cite This Data Set1:


Carlotta Domeniconi and Bojun Yan. Nearest Neighbor Ensemble. ICPR (1). 2004. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df_train = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.train"
,names=['OVERALL_DIAGNOSIS', 'F1R', 'F1S', 'F2R', 'F2S', 'F3R', 'F3S', 'F4R', 'F4S', 'F5R', 'F5S', 'F6R', 'F6S', 'F7R', 'F7S', 'F8R', 'F8S', 'F9R', 'F9S', 'F10R', 'F10S', 'F11R', 'F11S', 'F12R', 'F12S', 'F13R', 'F13S', 'F14R', 'F14S', 'F15R', 'F15S', 'F16R', 'F16S', 'F17R', 'F17S', 'F18R', 'F18S', 'F19R', 'F19S', 'F20R', 'F20S', 'F21R', 'F21S', 'F22R', 'F22S']
)


df_test = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.test"
,names=['OVERALL_DIAGNOSIS', 'F1R', 'F1S', 'F2R', 'F2S', 'F3R', 'F3S', 'F4R', 'F4S', 'F5R', 'F5S', 'F6R', 'F6S', 'F7R', 'F7S', 'F8R', 'F8S', 'F9R', 'F9S', 'F10R', 'F10S', 'F11R', 'F11S', 'F12R', 'F12S', 'F13R', 'F13S', 'F14R', 'F14S', 'F15R', 'F15S', 'F16R', 'F16S', 'F17R', 'F17S', 'F18R', 'F18S', 'F19R', 'F19S', 'F20R', 'F20S', 'F21R', 'F21S', 'F22R', 'F22S']
)

print(df_train.info())
print(df_test.info())
"""

#LOACL
import pandas
df_train = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.train"
,names=['OVERALL_DIAGNOSIS', 'F1R', 'F1S', 'F2R', 'F2S', 'F3R', 'F3S', 'F4R', 'F4S', 'F5R', 'F5S', 'F6R', 'F6S', 'F7R', 'F7S', 'F8R', 'F8S', 'F9R', 'F9S', 'F10R', 'F10S', 'F11R', 'F11S', 'F12R', 'F12S', 'F13R', 'F13S', 'F14R', 'F14S', 'F15R', 'F15S', 'F16R', 'F16S', 'F17R', 'F17S', 'F18R', 'F18S', 'F19R', 'F19S', 'F20R', 'F20S', 'F21R', 'F21S', 'F22R', 'F22S']
)


df_test = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/spect/SPECTF.test"
,names=['OVERALL_DIAGNOSIS', 'F1R', 'F1S', 'F2R', 'F2S', 'F3R', 'F3S', 'F4R', 'F4S', 'F5R', 'F5S', 'F6R', 'F6S', 'F7R', 'F7S', 'F8R', 'F8S', 'F9R', 'F9S', 'F10R', 'F10S', 'F11R', 'F11S', 'F12R', 'F12S', 'F13R', 'F13S', 'F14R', 'F14S', 'F15R', 'F15S', 'F16R', 'F16S', 'F17R', 'F17S', 'F18R', 'F18S', 'F19R', 'F19S', 'F20R', 'F20S', 'F21R', 'F21S', 'F22R', 'F22S']
)

print(df_train.info())
print(df_test.info())