import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Artificial, 7 classes of animals


Data Set Characteristics:  

Multivariate

Number of Instances:

101

Area:

Life

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

17

Date Donated

1990-05-15

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

449228


Source:

Creator:

Richard Forsyth

Donor:

Richard S. Forsyth
8 Grosvenor Avenue
Mapperley Park
Nottingham NG3 5DX
0602-621676


Data Set Information:

A simple database containing 17 Boolean-valued attributes. The "type" attribute appears to be the class attribute. Here is a breakdown of which animals are in which type: (I find it unusual that there are 2 instances of "frog" and one of "girl"!)

Class# -- Set of animals:
====== ====================================================
1 -- (41) aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, girl, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby,wolf
2 -- (20) chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren
3 -- (5) pitviper, seasnake, slowworm, tortoise, tuatara
4 -- (13) bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna
5 -- (4) frog, frog, newt, toad
6 -- (8) flea, gnat, honeybee, housefly, ladybird, moth, termite, wasp
7 -- (10) clam, crab, crayfish, lobster, octopus, scorpion, seawasp, slug, starfish, worm


Attribute Information:

1. animal name: Unique for each instance
2. hair: Boolean
3. feathers: Boolean
4. eggs: Boolean
5. milk: Boolean
6. airborne: Boolean
7. aquatic: Boolean
8. predator: Boolean
9. toothed: Boolean
10. backbone: Boolean
11. breathes: Boolean
12. venomous: Boolean
13. fins: Boolean
14. legs: Numeric (set of values: {0,2,4,5,6,8})
15. tail: Boolean
16. domestic: Boolean
17. catsize: Boolean
18. type: Numeric (integer values in range [1,7])


Relevant Papers:

Forsyth's PC/BEAGLE User's Guide.


Papers That Cite This Data Set1:


Yuan Jiang and Zhi-Hua Zhou. Editing Training Data for kNN Classifiers with Neural Network Ensemble. ISNN (1). 2004. [View Context].

Mikko Koivisto and Kismat Sood. Exact Bayesian Structure Discovery in Bayesian Networks. Journal of Machine Learning Research, 5. 2004. [View Context].

Eibe Frank and Stefan Kramer. Ensembles of nested dichotomies for multi-class problems. ICML. 2004. [View Context].

Eibe Frank and Mark Hall and Bernhard Pfahringer. Locally Weighted Naive Bayes. UAI. 2003. [View Context].

Huan Liu and Hiroshi Motoda and Lei Yu. Feature Selection with Selective Sampling. ICML. 2002. [View Context].

Michael Bain. Structured Features from Concept Lattices for Unsupervised Learning and Classification. Australian Joint Conference on Artificial Intelligence. 2002. [View Context].

Mukund Deshpande and George Karypis. Using conjunction of attribute values for classification. CIKM. 2002. [View Context].

Neil Davey and Rod Adams and Mary J. George. The Architecture and Performance of a Stochastic Competitive Evolutionary Neural Tree Network. Appl. Intell, 12. 2000. [View Context].

Manoranjan Dash and Huan Liu. Hybrid Search of Feature Subsets. PRICAI. 1998. [View Context].

D. Randall Wilson and Tony R. Martinez. Heterogeneous Radial Basis Function Networks. Proceedings of the International Conference on Neural Networks (ICNN. 1996. [View Context].

Guszti Bartfai. VICTORIA UNIVERSITY OF WELLINGTON Te Whare Wananga o te Upoko o te Ika a Maui. Department of Computer Science PO Box 600. 1996. [View Context].

Christophe Giraud and Tony Martinez and Christophe G. Giraud-Carrier. University of Bristol Department of Computer Science ILA: Combining Inductive Learning with Prior Knowledge and Reasoning. 1995. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].

Christophe G. Giraud-Carrier and Tony Martinez. AN INCREMENTAL LEARNING MODEL FOR COMMONSENSE REASONING. Department of Computer Science Brigham Young University. [View Context].

Jun Wang. Classification Visualization with Shaded Similarity Matrix. Bei Yu Les Gasser Graduate School of Library and Information Science University of Illinois at Urbana-Champaign. [View Context].

Mehmet Dalkilic and Arijit Sengupta. A Logic-theoretic classifier called Circle. School of Informatics Center for Genomics and BioInformatics Indiana University. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data"
,names=['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data"
,names=['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']
)

print(df.info())