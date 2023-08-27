import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset represents a set of possible advertisements on Internet pages.


Data Set Characteristics:  

Multivariate

Number of Instances:

3279

Area:

Computer

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

1558

Date Donated

1998-07-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

416403


Source:

Creator & donor:

Nicholas Kushmerick <nick '@' ucd.ie>


Data Set Information:

This dataset represents a set of possible advertisements on Internet pages. The features encode the geometry of the image (if available) as well as phrases occuring in the URL, the image's URL and alt text, the anchor text, and words occuring near the anchor text. The task is to predict whether an image is an advertisement ("ad") or not ("nonad").


Attribute Information:

(3 continous; others binary; this is the "STANDARD encoding" mentioned in the [Kushmerick, 99].)

One or more of the three continous features are missing in 28% of the instances; missing values should be interpreted as "unknown".


Relevant Papers:

N. Kushmerick (1999). "Learning to remove Internet advertisements", 3rd Int Conf Autonomous Agents. Available at www.cs.ucd.ie/staff/nick/research/[Web Link].
[Web Link]


Papers That Cite This Data Set1:


Dmitriy Fradkin and David Madigan. Experiments with random projections for machine learning. KDD. 2003. [View Context].

Sergio A. Alvarez and Takeshi Kawato and Carolina Ruiz. Mining over loosely coupled data sources using neural experts. Computer Science Dept. Boston College. [View Context].

Shay Cohen and Eytan Ruppin and Gideon Dror. Feature Selection Based on the Shapley Value. School of Computer Sciences Tel-Aviv University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#ONLINE
# you need to dwonload: pip install requests
"""
import pandas as pd
from zipfile import ZipFile
import requests, zipfile, io
zip_file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/internet_ads/ad-dataset.zip'
r = requests.get(zip_file_url)
zip_file = zipfile.ZipFile(io.BytesIO(r.content))
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename)) for text_file in zip_file.infolist() if text_file.filename.endswith('.data')}
df = dfs["ad.data"]
df.info()
"""

# LOCAL
import zipfile, io
zip_file_path = '../ics.uci.edu/ml/machine-learning-databases/internet_ads/ad-dataset.zip'
zip_file = zipfile.ZipFile(zip_file_path)
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename)) for text_file in zip_file.infolist() if text_file.filename.endswith('.data')}
df = dfs["ad.data"]
df.info()
