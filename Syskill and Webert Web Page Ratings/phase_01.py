import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This database contains HTML source of web pages plus the ratings of a single user on these web pages. Web pages are on four seperate subjects (Bands- recording artists; Goats; Sheep; and BioMedical)

Data Set Characteristics:  

Multivariate, Text

Number of Instances:

332

Area:

Computer

Attribute Characteristics:

Categorical

Number of Attributes:

5

Date Donated

1998-10-20

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

80834


Source:

Michael Pazzani
Department of Information and Computer Science,
University of California, Irvine
Irvine, CA 92697-3425
pazzani '@' ics.uci.edu
http://www.ics.uci.edu/~pazzani


Data Set Information:

The HTML source of a web page is given. Users looked at each web page and inidated on a 3 point scale (hot medium cold) 50-100 pages per domain. However, this is realistic because we want to learn user profiles from as few examples as possible so that users have an incentitive to rate pages.


Attribute Information:

Each subject is in a separate directory. Within each directory, there is an file named "index". The index contains information on the other files. Each entry is a line of the form:

file-name | rating | url | date-rated | title

where file-name is the name of a file (usually an integer), rating is hot, medium, or cold. There are so few medium's that mediums are usually merged with cold in experiments.

The other fields aren't used in learning, but they are collected by the interface for other purposes. They are the url of the html source, the date rated and the title of the web oage.


Relevant Papers:

Pazzani M., Billsus, D. (1997). Learning and Revising User Profiles: The identification of interesting web sites. Machine Learning 27, 313-331
[Web Link]

Pazzani, M., Muramatsu J., Billsus, D. (1996). Syskill & Webert: Identifying interesting web sites. Proceedings of the National Conference on Artificial Intelligence, Portland, OR. PDF
[Web Link]


Papers That Cite This Data Set1:


Stephen D. Bay and Dennis F. Kibler and Michael J. Pazzani and Padhraic Smyth. The UCI KDD Archive of Large Data Sets for Data Mining Research and Experimentation. SIGKDD Explorations, 2. 2000. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""