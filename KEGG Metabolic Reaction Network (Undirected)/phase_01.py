import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: KEGG Metabolic pathways modeled as un-directed reaction network. Variety of graphical features presented.

Data Set Characteristics:  

Multivariate, Univariate, Text

Number of Instances:

65554

Area:

Life

Attribute Characteristics:

Integer, Real

Number of Attributes:

29

Date Donated

2011-11-28

Associated Tasks:

Classification, Regression, Clustering

Missing Values?

Yes

Number of Web Hits:

66491


Source:

1. Muhammad Naeem, Centre of Research in Data Engineering(CORDE) & Department of Computer Science, MAJU Islamabad Pakistan(naeems.naeem '@' gmail.com).
2. Sohail Asghar, Director/Associate Professor University Institute of IT PMAS-Arid Agriculture University,Rawalpindi Pakistan, Centre of Research in Data Engineering (CORDE),(sohail.asghar '@' gmail.com)


Data Set Information:

KEGG Metabolic pathways can be realized into network. Two kinds of network / graph can be formed. These include Reaction Network and Relation Network. In Reaction network, Substrate or Product compound are considered as Node and genes are treated as edge. Whereas in the relation network, Substrate and Product componds are considered as Edges while enzyme and genes are placed as nodes. We tool large number of metabolic pathways from KEGG XML. They were modeled into the graph as described above. With the help of Cytoscape tool, variety of network features were compunted.


Attribute Information:


a) Pathway text
b) Connected Components Integer (min:1, max:39 )
c) Diameter Integer (min:1, max:46 )
d) Radius Integer (min:1, max:13 )
e) Centralization Integer (min:0, max:1 )
f) Shortest Path Integer (min:2, max:23420 )
g) Characteristic Path Length Integer (min:1, [Web Link] )
h) Avg.num.Neighbours real ([Web Link], [Web Link])
i) Density real ([Web Link], max:1)
j) Heterogeneity real (min:0, [Web Link])
k) Isolated Nodes Integer (min:0, max:3)
l) Number of Self Loops Integer (min:0, max:4)
m) Multi-edge Node Pair Integer (min:0, max:220)
n) NeighborhoodConnectivity real ([Web Link], [Web Link])
o) NumberOfDirectedEdges real ([Web Link], [Web Link])
p) Stress real (min:0, [Web Link])
q) SelfLoops real (min:0, [Web Link])
r) Partner Of MultiEdged NodePairs Integer (min:0, max:3)
s) Degree real (min:1, [Web Link])
t) TopologicalCoefficient real (min:0, max:1)
u) BetweennessCentrality real (min:0, [Web Link])
v) Radiality real ([Web Link], max:30744573457 )
w) Eccentricity real ([Web Link], [Web Link])
x) NumberOfUndirectedEdges real (min:0, [Web Link])
y) ClosenessCentrality real ([Web Link], max:1)
z) AverageShortestPathLength real ([Web Link], [Web Link] )
aa) ClusteringCoefficient real (min:0, max:1)
bb) nodeCount Integer (min:2, max:232)
cc) edgeCount Integer (min:1, max:444)


Relevant Papers:

Shannon,P., Markiel,A., Ozier,O., Baliga,N.S., Wang,J.T.,Ramage,D., Amin,N., Schwikowski,B. and Ideker,T. (2003) Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome Res., 13, 2498â€“2504.



Citation Request:

Naeem M,Asghar S, Centre of Research in Data Engineering Islamabad Pakistan, naeems.naeem '@' gmail.com, sohail.asg '@' gmail.com
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00221/Reaction%20Network%20(Undirected).data"
,
names=['Pathway', 'Connected_Components', 'Diameter', 'Radius', 'Centralization', 'Shortest_Path', 'Characteristic_Path_Length', 'Avg.num.Neighbours', 'Density', 'Heterogeneity', 'Isolated_Nodes', 'Number_of_Self_Loops', 'Multi-edge_Node_Pair', 'NeighborhoodConnectivity', 'NumberOfDirectedEdges', 'Stress', 'SelfLoops', 'Partner_Of_MultiEdged_NodePairs', 'Degree', 'TopologicalCoefficient', 'BetweennessCentrality', 'Radiality', 'Eccentricity', 'NumberOfUndirectedEdges', 'ClosenessCentrality', 'AverageShortestPathLength', 'ClusteringCoefficient', 'nodeCount', 'edgeCount']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00221/Reaction Network (Undirected).data"
,
names=['Pathway', 'Connected_Components', 'Diameter', 'Radius', 'Centralization', 'Shortest_Path', 'Characteristic_Path_Length', 'Avg.num.Neighbours', 'Density', 'Heterogeneity', 'Isolated_Nodes', 'Number_of_Self_Loops', 'Multi-edge_Node_Pair', 'NeighborhoodConnectivity', 'NumberOfDirectedEdges', 'Stress', 'SelfLoops', 'Partner_Of_MultiEdged_NodePairs', 'Degree', 'TopologicalCoefficient', 'BetweennessCentrality', 'Radiality', 'Eccentricity', 'NumberOfUndirectedEdges', 'ClosenessCentrality', 'AverageShortestPathLength', 'ClusteringCoefficient', 'nodeCount', 'edgeCount']
)

print(df.info())