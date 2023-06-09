import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: KEGG Metabolic pathways modeled as directed relation network. Variety of graphical features presented.

Data Set Characteristics:  

Multivariate, Univariate, Text

Number of Instances:

53414

Area:

Life

Attribute Characteristics:

Integer, Real

Number of Attributes:

24

Date Donated

2011-11-28

Associated Tasks:

Classification, Regression, Clustering

Missing Values?

N/A

Number of Web Hits:

70767


Source:

1. Muhammad Naeem, Centre of Research in Data Engineering(CORDE) & Department of Computer Science, MAJU Islamabad Pakistan, (naeems.naeem '@' gmail.com).
2. Sohail Asghar, Director/Associate Professor University Institute of IT PMAS-Arid Agriculture University, Rawalpindi, Pakistan Centre of Research in Data Engineering (CORDE), (sohail.asghar '@' gmail.com)


Data Set Information:

KEGG Metabolic pathways can be realized into network. Two kinds of network / graph can be formed. These include Reaction Network and Relation Network. In Reaction network, Substrate or Product compound are considered as Node and genes are treated as edge. Whereas in the relation network, Substrate and Product componds are considered as Edges while enzyme and genes are placed as nodes. We tool large number of metabolic pathways from KEGG XML. They were modeled into the graph as described above. With the help of Cytoscape tool, variety of network features were compunted.


Attribute Information:

a) Pathway text
b) Nodes integer (min:2, max:116)
c) Edges integer (min:1, max:606)
d) Connected Components integer (min:1, max:13)
e) Network Diameter integer (min:1, max:30)
f) Network Radius integer (min:1, max:2)
g) Shortest Path integer (min:1, max:3277)
h) Characteristic Path Length real (min:1, [Web Link])
i) Avg.num.Neighbours real (min:1, [Web Link])
j) Isolated Nodes integer (min:0, max:1)
k) Number of Self Loops integer (min:0, max:0)
l) Multi-edge Node Pair integer (min:0, max:57)
m) NeighborhoodConnectivity real (min:1, [Web Link])
n) Outdegree real (min:0.5, [Web Link])
o) Stress real (min:0, [Web Link])
p) SelfLoops integer (min:0, max:0)
q) PartnerOfMultiEdgedNodePairs real (min:0, [Web Link])
r) EdgeCount real (min:1, [Web Link])
s) BetweennessCentrality real (min:0, [Web Link])
t) Indegree real (min:0.5, [Web Link])
u) Eccentricity real ([Web Link], [Web Link])
v) ClosenessCentrality real ([Web Link], max:1)
w) AverageShortestPathLength real ([Web Link], [Web Link])
x) ClusteringCoefficient real (min:0, [Web Link])


Relevant Papers:

Shannon,P., Markiel,A., Ozier,O., Baliga,N.S., Wang,J.T.,Ramage,D., Amin,N., Schwikowski,B. and Ideker,T. (2003) Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome Res., 13, 2498â€“2504.



Citation Request:

Naeem M,Asghar S, Centre of Research in Data Engineering Islamabad Pakistan, naeems.naeem '@' gmail.com, sohail.asg '@' gmail.com
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00220/Relation%20Network%20(Directed).data"
,names=['Pathway', 'Nodes', 'Edges', 'Connected_Components', 'Network_Diameter', 'Network_Radius', 'Shortest_Path', 'Characteristic_Path_Length', 'Avg.num.Neighbours', 'Isolated_Nodes', 'Number_of_Self_Loops', 'Multi-edge_Node_Pair', 'NeighborhoodConnectivity', 'Outdegree', 'Stress', 'SelfLoops', 'PartnerOfMultiEdgedNodePairs', 'EdgeCount', 'BetweennessCentrality', 'Indegree', 'Eccentricity', 'ClosenessCentrality', 'AverageShortestPathLength', 'ClusteringCoefficient']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00220/Relation Network (Directed).data"
,names=['Pathway', 'Nodes', 'Edges', 'Connected_Components', 'Network_Diameter', 'Network_Radius', 'Shortest_Path', 'Characteristic_Path_Length', 'Avg.num.Neighbours', 'Isolated_Nodes', 'Number_of_Self_Loops', 'Multi-edge_Node_Pair', 'NeighborhoodConnectivity', 'Outdegree', 'Stress', 'SelfLoops', 'PartnerOfMultiEdgedNodePairs', 'EdgeCount', 'BetweennessCentrality', 'Indegree', 'Eccentricity', 'ClosenessCentrality', 'AverageShortestPathLength', 'ClusteringCoefficient']
)

print(df.info())