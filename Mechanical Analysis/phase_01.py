import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Fault diagnosis problem of electromechanical devices; also PUMPS DATA SET is newer version with domain theory and results

Data Set Characteristics:  

Multivariate

Number of Instances:

209

Area:

Computer

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

8

Date Donated

1990-06-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

130498


Source:

Original Owners of Database:

1. F. Bergadano, A. Giordana, L. Saitta
University of Torino, Italy
Corso Svizzera 185, Torino - tel. (39) 11 7712002
e-mail: bergadan '@' itoinfo.bitnet

2. F. Bracadori, D. De Marchi
Sogesta, Localita' Crocicchio, Urbino, Italy

Donor:

Enichem (Eni), Ravenna through Sogesta (Eni), Urbino.


Data Set Information:

F. Bergadano supplied this database. Each instance contains many components, each of which has 8 attributes. Different instances in this database have different numbers of components. It was impossible to put one instance on one line. He originally had one instance per file, but this makes it difficult to ftp them (imagine ftp'ing 222 or so files!). I bundled the set of 209 instances into a single data file, prefixing each with the line:

===== Instance number 1: =====

where "n" is a number in [1,221]. However, they are NOT, repeat NOT in sequential order. Twelve (12) of the instances are missing. Bergadano supplied these additional 12 instances (numbers 8,12,32,33,66,69,73,152,167,194,203,208) in a "notused" sub-directory. I bundled these up with the same format in the "notused-instances" file.

A quick scan of their file didn't reveal what the purpose is for these twelve instances.


Attribute Information:

0 - dummy (always 1) - used for numbering - ignore
1 - class - classification (1..6, the same for components of one example)
2 - # - component number (integer)
3 - sup - support in the machine where measure was taken (1..4)
4 - cpm - frequency of the measure (integer)
5 - mis - measure (real)
6 - misr - earlier measure (real)
7 - dir - filter, type of the measure and direction:
{vo=,
va=,
vv=,
ao=,
aa=,
av=,
io=,
ia=,
iv=}
8 - omega - rpm of the machine (integer, the same for components of one example)


Relevant Papers:

F. Bergadano, A. Giordana, L. Saitta, F. Brancadori, D. De Marchi: "Integrated Learning in a real Domain" Proc. VII ML Conference, Austin TX, 1990 (pages 322-329)
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

