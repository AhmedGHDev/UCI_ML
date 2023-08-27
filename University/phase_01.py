import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Data in original (LISP-readable) form


Data Set Characteristics:  

Multivariate

Number of Instances:

285

Area:

N/A

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

17

Date Donated

1988-07-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

292767


Source:

Original Owner:

unknown

Donor:

Steve Souders <souders '@' ads.com>


Data Set Information:

Format: Each observation concerns one university. In some cases, more information is provided about the attribute (e.g., units or domain). Some duplicates may exist and a single observation may have more than one value for a given attribute (esp. academic emphasis).

It appears that several attributes could serve as a distinguished class attribute for this database. The data file remains in the state as given to us by Steve Souders. It is a LISP readable file with a few relevant functions at the end of the data file. The info on missing data values have not been calculated. We hope to get to this in the future.


Attribute Information:

1. University-name
2. State
3. location
4. Control
5. number-of-students
6. male:female (ratio)
7. student:faculty (ratio)
8. sat-verbal
9. sat-math
10. expenses
11. percent-financial-aid
12. number-of-applicants
13. percent-admittance
14. percent-enrolled
15. academics
16. social
17. quality-of-life
18. academic-emphasis


Relevant Papers:

Lebowitz M. "Concept learning in a rich input domain : generalization-based memory." Machine Learning, Vol 2, No 2, September 1987.
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

names=['University-name', 'State', 'location', 'Control', 'number-of-students', 'male', 'student', 'sat-verbal', 'sat-math', 'expenses', 'percent-financial-aid', 'number-of-applicants', 'percent-admittance', 'percent-enrolled', 'academics', 'social', 'quality-of-life', 'academic-emphasis']