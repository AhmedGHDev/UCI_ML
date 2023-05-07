import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: 2 data formats (structured, one-instance-per-line)


Data Set Characteristics:  

Multivariate

Number of Instances:

10

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

32

Date Donated

1994-06-24

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

204601


Source:

Original owners:

Ryszard S. Michalski (michalski '@' aic.gmu.edu) and Robert Stepp

Donor:

GMU, Center for AI, Software Librarian, Eric E. Bloedorn (bloedorn '@' aic.gmu.edu)



Data Set Information:

Notes:

- Additional "background" knowledge is supplied that provides a partial ordering on some of the attribute values.

- We are providing this dataset both in its original form and in a form similar to the more typical propositional datasets in our repository. Since the trains dataset records relations between attributes, this transformation was somewhat challenging. However, it may shed some insight on this problem for people who are more familiar with the simple one-instance-per-line dataset format.

Hierarchy of values:

if (cshape is one of {openrect,opentrap,ushaped,dblopnrect}
then cshape is opentop

if (cshape is one of {hexagon,ellipse,closedrect,jaggedtop,slopetop, engine}
then cshape closedtop

Prediction task: Determine concise decision rules distinguishing trains traveling east from those traveling west.


Attribute Information:

The following format was used for the "transformed" dataset representation as found in trains.transformed.data (one instance per line):

1. Number_of_cars (integer in [3-5])
2. Number_of_different_loads (integer in [1-4])
3-22: 5 attributes for each of cars 2 through 5: (20 attributes total)
- num_wheels (integer in [2-3])
- length (short or long)
- shape (closedrect, dblopnrect, ellipse, engine, hexagon, jaggedtop, openrect, opentrap, slopetop, ushaped)
- num_loads (integer in [0-3])
- load_shape (circlelod, hexagonlod, rectanglod, trianglod)
23-32: 10 Boolean attributes describing whether 2 types of loads are on adjacent cars of the train
- Rectangle_next_to_rectangle (0 if false, 1 if true)
- Rectangle_next_to_triangle (0 if false, 1 if true)
- Rectangle_next_to_hexagon (0 if false, 1 if true)
- Rectangle_next_to_circle (0 if false, 1 if true)
- Triangle_next_to_triangle (0 if false, 1 if true)
- Triangle_next_to_hexagon (0 if false, 1 if true)
- Triangle_next_to_circle (0 if false, 1 if true)
- Hexagon_next_to_hexagon (0 if false, 1 if true)
- Hexagon_next_to_circle (0 if false, 1 if true)
- Circle_next_to_circle (0 if false, 1 if true)
33. Class attribute (east or west)

The number of cars vary between 3 and 5. Therefore, attributes referring to properties of cars that do not exist (such as the 5 attriubutes for the "5th" car when the train has fewer than 5 cars) are assigned a value of "-".


Relevant Papers:

R.S. Michalski and J.B. Larson "Inductive Inference of VL Decision Rules" In Proceedings of the Workshop in Pattern-Directed Inference Systems, Hawaii, May 1977.
[Web Link]

Stepp, R.E. and Michalski, R.S. "Conceptual Clustering: Inventing Goal-Oriented Classifications of Structured Objects" In R.S. Michalski, J.G. Carbonell, and T.M. Mitchell (Eds.) "Machine Learning: An Artificial Intelligence Approach, Volume II". Los Altos, Ca: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Daan Fierens and Jan Ramon and Hendrik Blockeel and Maurice Bruynooghe. A Comparison of Approaches for Learning Probability Trees. Department of Computer Science. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""