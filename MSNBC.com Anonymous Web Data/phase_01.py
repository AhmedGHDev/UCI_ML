import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data describes the page visits of users who visited msnbc.com on September 28, 1999. Visits are recorded at the level of URL category (see description) and are recorded in time order.

Data Set Characteristics:  

Sequential

Number of Instances:

989818

Area:

Computer

Attribute Characteristics:

Categorical

Number of Attributes:

N/A

Date Donated

N/A

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

95460


Source:

David Heckerman (heckerma '@' microsoft.com)


Data Set Information:

The data comes from Internet Information Server (IIS) logs for msnbc.com and news-related portions of msn.com for the entire day of September, 28, 1999 (Pacific Standard Time). Each sequence in the dataset corresponds to page views of a user during that twenty-four hour period. Each event in the sequence corresponds to a user's request for a page. Requests are not recorded at the finest level of detail---that is, at the level of URL, but rather, they are recorded at the level of page category (as determined by a site administrator). The categories are "frontpage", "news", "tech", "local", "opinion", "on-air", "misc", "weather", "health", "living", "business", "sports", "summary", "bbs" (bulletin board service), "travel", "msn-news", and "msn-sports". Any page requests served via a caching mechanism were not recorded in the server logs and, hence, not present in the data.

Other Relevant Information:

* Number of users: 989818
* Average number of vitis per user: 5.7
* Number of URLs per category: 10 to 5000


Attribute Information:

Each category is associated--in order--with an integer starting with "1". For example, "frontpage" is associated with 1, "news" with 2, and "tech" with 3. Each row below "% Sequences:" describes the hits--in order--of a single user. For example, the first user hits "frontpage" twice, and the second user hits "news" once.


Relevant Papers:

I. Cadez, D. Heckerman, C. Meek, P. Smyth, S. White, "Visualization of navigation patterns on a Web site using model-based clustering," Journal of Data Mining and Knowledge Discovery.
[Web Link]



Citation Request:

This data is avaliable thanks to msnbc.com
"""