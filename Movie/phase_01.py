import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data set contains a list of over 10000 films including many older, odd, and cult films. There is information on actors, casts, directors, producers, studios, etc.


Data Set Characteristics:  

Multivariate, Relational

Number of Instances:

10000

Area:

N/A

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

1999-07-07

Associated Tasks:

N/A

Missing Values?

Yes

Number of Web Hits:

270466


Source:

Original Owner and Donor

Gio Wiederhold
Stanford University
650-725-8363
gio '@' cs.stanford.edu


Data Set Information:

The data is stored in relational form across several files. The central file (MAIN) is a list of movies, each with a unique identifier. These identifiers may change in successive versions. The actors (CAST) for those movies are listed with their roles in a distinct file. More information about individual actors (ACTORS) is in a third file. All directors in MAIN are listed in a fourth file (PEOPLE), with a number of important producers, writers, and cinematographers. A fifth file (REMAKES) links movies that were copied to a substantial extent from each other. The sixth file (STUDIOS) provides some information about studios shown in MAIN.

The original motivation was for database class exercises, to replace the boring `manager of the toy-department' queries. Note that the CASTS, refering MAIN and ACTORS is logically identical to the inventory file refering to suppliers and assemblies in the the standard bill-of-materials problems. Personal interests caused the database to be made complete for all Hitchcock movies and TV episodes. Related films by type and actor were added gradually.

Subsequent research on temporal databases caused date fields (years only) to be added. It allows testing, say, if the dates-of-work of an ACTOR match the dates of the MAIN films that the CAST relation shows. Object-oriented database features could be tested with fields having multiple and two-level values, as documented in DOC.

The entries were gradually collected during course work starting about 1975 and are still being updated. Most of the entries were manual. The DOC file lists some of the reference works used. Corrections and additions continue to be appreciated.

Detailed descriptions of the fields and their formats is provided in doc.html.

Missing Values:

Outside of key fields, missing values are common. Their encoding is described in DOC. Sometimes the data seems to be unavailable, sometimes it hasn't been entered. Some information, as `lived-with' is inherently incomplete.

Censored Data:

Minor actors are ignored.

Dependencies:

Every MAIN film must have a director in PEOPLE. About 50 pseudo director names ahve been listed in PEOPLE to allow interesting films to with (yet) unknown directors to be entered. Every CASTS entry must relate to a MAIN film entry. Every ACTOR should appear in some CASTS entry, but not vice versa. See DOC for more type information.

Other Relevant Information:

Films are listed, if known, with their original language title. An Alt(T: ) field provides English translations, where known.

Data Format:

The current files are in HTML, to allow easy parsing to other formats. An XML version is being considered.

The approximate file sizes are:
DOC ....... 50K
MAIN ...... 1 145K 11 400 entries
PEOPLE .... 355K 3 290 entries
CASTS ..... 4 340K 46 000 entries
ACTORS .... 811K 6 800 entries
REMAKES ... 135K 1 278 entries
STUDIOS ... 26K 200 entries


Attribute Information:

N/A


Relevant Papers:

N/A


Papers That Cite This Data Set1:


Harsha Nagesh and Sanjay Goil and Alok N. Choudhary. Adaptive Grids for Clustering Massive Data Sets. Department of Energy ASCI. [View Context].



Citation Request:

Copyright held by Gio Wiederhold, 1990-1999. This data may not be used for commercial resale.

Please acknowledge the source when used: Gio Wiederhold, Stanford University.
"""