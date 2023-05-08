import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data contains a record of user interactions with the Entree Chicago restaurant recommendation system.


Data Set Characteristics:  

Transactional, Sequential

Number of Instances:

50672

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

N/A

Date Donated

2000-03-09

Associated Tasks:

Recommender-Systems

Missing Values?

Yes

Number of Web Hits:

116246


Source:

Original Owner and Donor:

Robin Burke
University of California, Irvine
Department of Information and Computer Science
Irvine, CA 92697

Now here:
http://josquin.cti.depaul.edu/~rburke/


Data Set Information:

This data records interactions with Entree Chicago restaurant recommendation system (originally [Web Link]) from September, 1996 to April, 1999. The data is organized into files roughly spanning a quarter year -- with Q3 1996 and Q2 1999 each only containing one month.

Each line in a session file represents a session of user interaction with the system. The (tab-separated) fields are as follows:

Date, IP, Entry point, Rated restaurant1, ..., Rated restaurantN, End point

1. Entry point:

Users can use a restaurant from any city as a entry point, but they always get recommendations for Chicago restaurants. The entry point therefore draws from a larger universe of restaurants than the rest of the data.
Entry points have the form nnnX, where nnn is a numeric restaurant ID and X is a character A-H that encodes the city.

A = Atlanta
B = Boston
C = Chicago
D = Los Angeles
E = New Orleans
F = New York
G = San Francisco
H = Washington DC

2. Rated Restaurant:

These are all Chicago restaurants.
These entries have the form nnnX, where nnn is a numeric restaurant ID and X is a character L-T that encodes the navigation operation.

L = browse (move from one restaurant in a list of recommendations to another)
M = cheaper (search for a restaurant like this one, but cheaper)
N = nicer ( " " , but nicer)
O = closer (unused in the production version of the system)
P = more traditional (search for a restaurant like this, but serving more traditional cuisine)
Q = more creative (search for a restaurant serving more creative cuisine)
R = more lively (search for a restaurant with a livelier atmosphere)
S = quieter (search for a restaurant with a quieter atmosphere)
T = change cuisine (search for a restaurant like this, but serving a different kind of food) Note that with this tweak, we would ideally like to know what cuisine the user wanted to change to, but this information was not recorded.

3. End point:

Just the numeric id for the (Chicago) restaurant that the user saw last. In our experiments, we are assuming that this was a good suggestion, but it is also possible that user just gives up.
Some potentially useful data is missing. In many cases, we don't know the starting point because the user input a set of selection criteria (such as "inexpensive traditional Mexican") using a form submission, rather than starting from a known restaurant. These queries were not recorded. This is denoted by a 0 in the entry point field. Some sessions do not have a known end point. This is marked by -1 in the end point field.


In addition to the user's interactions, there is also data linking the restaurant ID with its name and features such as "fabulous wine lists", "good for younger kids", and "Ethopian" cuisine. This data is stored by city (e.g. Atlanta, Boston, etc.) and is in the following format:

restaurant id [tab] restaurant name [tab] restaurant features (3 digits ids separated by spaces)



Attribute Information:

N/A


Relevant Papers:

Burke, R. The Wasabi Personal Shopper: A Case-Based Recommender System. In Proceedings of the 11th National Conference on Innovative Applications of Artificial Intelligence, pages 844-849. AAAI, 1999.
[Web Link]

Burke, R. Knowledge-based Recommender Systems. To appear in the Encyclopedia of Library and Information Science.


Papers That Cite This Data Set1:


Zoran Obradovic and Slobodan Vucetic. Challenges in Scientific Data Mining: Heterogeneous, Biased, and Large Samples. Center for Information Science and Technology Temple University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""