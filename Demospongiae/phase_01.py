import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Marine sponges of the Demospongiae class classification domain.


Data Set Characteristics:  

Multivariate

Number of Instances:

503

Area:

Life

Attribute Characteristics:

Integer

Number of Attributes:

N/A

Date Donated

2010-01-21

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

68817


Source:

Creator:

Eva Armengol, Enric Plaza, Marta Domingo and Iosune Uriz

Donor:

Santiago Ontanon (santi '@' iiia.csic.es)


Data Set Information:

This dataset contains 503 sponges belonging to the Demospongiae class collected from the Mediterranean (451 sponges) and Atlantic oceans (52 sponges). Each sponge is classified according to a hierarchy formed by: order, family, genus and specie. Each order is subdivided in several families. Each family is also divided in several genus, and each genus in several species:
- There are 7 different orders (between 42 to 117 sponges per order)
- 42 different families (1 to 43 sponges per family)
- 114 different genus (1 to 34 sponges per genus)
- 230 different species (1 to 15 sponges per specie)

Although classification at all these levels can be attempted, it has traditionally been used as a classification dataset, using 'order' as the target class. Moreover, a subset consisting of 280 sponges (orders astrophoricda, axinellida and hadromerida) is also commonly used.

The data set is relational and is provided in two alternative formats (which are equivalent):
- NOOS: NOOS is a lisp-like language to represent data as feature-terms. The following files contain the dataset in this format:
- sponge-ontology.noos: this defines the ontology (sorts and features)
- sponge-dm.noos: this file defines the different constants used in the examples
- sponge-cases-503.noos: this file contains the actual dataset
- Horn Clauses: the dataset is also provided as a set of prolog clauses, equivalent to the feature-term representation in NOOS. The file sponges-503.pl contains the dataset in this format. Each predicate with head 'sponge-problem' defines a different sponge.


Attribute Information:

Each sponge defines 2 attributes:
- description: which in itself defines up to 6 attributes (external-features, ecological-features, spikulate-skeleton, fibrous-skeleton, tracts-skeleton, and anatomy). Each of those attributes has additional attributes defined, and so on, forming a tree structure. The leaves of the tree contain both categorial as well as numerical features. Moreover, some features are multi-valued (i.e. a feature can contain more than one value)
- solution: this attribute has 4 additional attributes defined (order, family, genus and specie), which are the target attributes. As explained above, typically 'order' is used as the target class, since there are not enough examples to predict family, genus and specie accurately.

The trees representing the sponges vary in size: their depth varies form 5 to 8, and their number of leaves from 17 to 51.

A graphical representation of a sponge is shown in the file sponge-220.pdf as an example.


Relevant Papers:

Santiago Ontanon and Enric Plaza (2009) On Similarity Measures based on a Refinement Lattice. in ICCBR 2009, LNAI 5650, pp 240 - 255.

Eva Armengol, Enric Plaza: Lazy Induction of Descriptions for Relational Case-Based Learning. ECML 2001: 13-24

Eva Armengol, Enric Plaza: Similarity Assessment for Relational CBR. ICCBR 2001: 44-58



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""