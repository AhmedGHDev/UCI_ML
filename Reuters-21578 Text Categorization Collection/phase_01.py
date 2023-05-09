import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This is a collection of documents that appeared on Reuters newswire in 1987. The documents were assembled and indexed with categories.

Data Set Characteristics:  

Text

Number of Instances:

21578

Area:

N/A

Attribute Characteristics:

Categorical

Number of Attributes:

5

Date Donated

1997-09-26

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

247303


Source:

David D. Lewis
AT&T Labs - Research
lewis '@' research.att.com

Documents came from Reuters newswire in 1987.


Data Set Information:

From the original readme file (please consult it for more information):
-------------------------
The documents in the Reuters-21578 collection appeared on the Reuters newswire in 1987. The documents were assembled and indexed with categories by personnel from Reuters Ltd. (Sam Dobbins, Mike Topliss, Steve Weinstein) and Carnegie Group, Inc. (Peggy Andersen, Monica Cellio, Phil Hayes, Laura Knecht, Irene Nirenburg) in 1987.

In 1990, the documents were made available by Reuters and CGI for research purposes to the Information Retrieval Laboratory (W. Bruce Croft, Director) of the Computer and Information Science Department at the University of Massachusetts at Amherst. Formatting of the documents and production of associated data files was done in 1990 by David D. Lewis and Stephen Harding at the Information Retrieval Laboratory.

Further formatting and data file production was done in 1991 and 1992 by David D. Lewis and Peter Shoemaker at the Center for Information and Language Studies, University of Chicago. This version of the data was made available for anonymous FTP as "Reuters-22173, Distribution 1.0" in January 1993. From 1993 through 1996, Distribution 1.0 was hosted at a succession of FTP sites maintained by the Center for Intelligent Information Retrieval (W. Bruce Croft, Director) of the Computer Science Department at the University of Massachusetts at Amherst.

At the ACM SIGIR '96 conference in August, 1996 a group of text categorization researchers discussed how published results on Reuters-22173 could be made more comparable across studies. It was decided that a new version of collection should be produced with less ambiguous formatting, and including documentation carefully spelling out standard methods of using the collection. The opportunity would also be used to correct a variety of typographical and other errors in the categorization and formatting of the collection.

Steve Finch and David D. Lewis did this cleanup of the collection September through November of 1996, relying heavily on Finch's SGML-tagged version of the collection from an earlier study. One result of the re-examination of the collection was the removal of 595 documents which were exact duplicates (based on identity of timestamps down to the second) of other documents in the collection. The new collection therefore has only 21,578 documents, and thus is called the Reuters-21578 collection. This README describes version 1.0 of this new collection, which we refer to as "Reuters-21578, Distribution 1.0".

In preparing the collection and documentation we have benefited from discussions with Eric Brown, William Cohen, Fred Damerau, Yoram Singer, Amit Singhal, and Yiming Yang, among many others.

We thank all the people and organizations listed above for their efforts and support, without which this collection would not exist.


Attribute Information:

Reuters-21578, Distribution 1.0 includes five files (all-exchanges-strings.lc.txt, all-orgs-strings.lc.txt, all-people-strings.lc.txt, all-places-strings.lc.txt, and all-topics-strings.lc.txt) which list the names of *all* legal categories in each set. A sixth file, cat-descriptions_120396.txt gives some additional information on the category sets.


Relevant Papers:

Chidanand Apt, Fred Damerau, Sholom M. Weiss. "Automated Learning of Decision Rules for Text Categorization." ACM Transactions on Information Systems, 1994.
[Web Link]

Chidanand Apt, Fred Damerau, Sholom M. Weiss, "Toward Language Independent Automated Learning of Text Categorization Models." SIGIR 1994.
[Web Link]

Philip J. Hayes, Peggy M. Anderson, rene B. Nirenburg, Linda M. Schmandt. "TCS: A Shell for Content-Based Text Categorization." IEEE Conference on Artificial Intelligence Applications, 1990.
[Web Link]

Philip J. Hayes and Steven P. Weinstein. "CONSTRUE/TIS: A System for Content-Based Indexing of a Database of News Stories." Second Annual Conference on Innovative Applications of Artificial Intelligence, 1990.
[Web Link]


Papers That Cite This Data Set1:


Manuel Oliveira. Library Release Form Name of Author: Stanley Robson de Medeiros Oliveira Title of Thesis: Data Transformation For Privacy-Preserving Data Mining Degree: Doctor of Philosophy Year this Degree Granted. University of Alberta Library. 2005. [View Context].

David Littau and Daniel Boley. Using Low-Memory Representations to Cluster Very Large Data Sets. SDM. 2003. [View Context].

Bianca Zadrozny and Charles Elkan. Transforming classifier scores into accurate multiclass probability estimates. KDD. 2002. [View Context].

Vijay S. Iyengar and Chidanand Apt and Tong Zhang. Active learning using adaptive resampling. KDD. 2000. [View Context].

Dmitry Pavlov and Jianchang Mao and Byron Dom. Scaling-Up Support Vector Machines Using Boosting Algorithm. ICPR. 2000. [View Context].

Daphne Koller and Mehran Sahami. Toward Optimal Feature Selection. ICML. 1996. [View Context].

Omid Madani and David M. Pennock and Gary William Flake. Co-Validation: Using Model Disagreement to Validate Classification Algorithms. Yahoo! Research Labs. [View Context].

Thomas T. Osugi and M. S. EXPLORATION-BASED ACTIVE MACHINE LEARNING. Faculty of The Graduate College at the University of Nebraska In Partial Fulfillment of Requirements. [View Context].

Vikas Sindhwani and P. Bhattacharya and Subrata Rakshit. Information Theoretic Feature Crediting in Multiclass Support Vector Machines. [View Context].



Citation Request:

The copyright for the text of newswire articles and Reuters annotations in the Reuters-21578 collection resides with Reuters Ltd. Reuters Ltd. and Carnegie Group, Inc. have agreed to allow the free distribution of this data *for research purposes only*.

If you publish results based on this data set, please acknowledge its use, refer to the data set by the name "Reuters-21578, Distribution 1.0", and inform your readers of the current location of the data set (see "Availability & Questions").
"""