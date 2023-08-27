import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Data giving characteristics of each ORF (potential gene) in the E. coli genome. Sequence, homology (similarity to other genes) and structural information, and function (if known) are provided.


Data Set Characteristics:  

Relational

Number of Instances:

N/A

Area:

Life

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

2001-07-14

Associated Tasks:

N/A

Missing Values?

Yes

Number of Web Hits:

57849


Source:

Original Owner and Donor:

Ross D. King
Department of Computer Science,
University of Wales Aberystwyth,
SY23 3DB, Wales
rdk '@' aber.ac.uk
http://users.aber.ac.uk/rdk


Data Set Information:

The data was collected from several sources, including GenProtEC ([Web Link]) and SWISSPROT ([Web Link]). Structure prediction was made by PROF ([Web Link]). Homology search was provided by PSI-BLAST ([Web Link]).

The data is in Datalog format. Missing values are not explicit, but some genes have more relationships than others.

E. coli genes (ORFs) are related to each other by the predicate ecoli_to_ecoli(EcoliNumber,E-value,Psi-blast_iteration). They are related to other (SWISSPROT) proteins by the predicate e_val(AccNo,E-value). All the data for a single gene (ORF) is enclosed between delimiters of the form:

begin(model(EcoliNumber)).
end(model(EcoliNumber)).

The gene functional classes are in a hierarchy. See [Web Link] (note: the classes may have changed since original data collection).

There are two datalog files: ecoli_data.pl and ecoli_functions.pl

1. ecoli_functions.pl

Lists classes and ORF functions. Lines are of the following form:

class(5,1,1,'Colicin-related functions').
class(5,1,'Laterally acquirred elements').
class(5,'Extrachromosomal').

Arguments are up to 3 numbers (describing class at up to 3 different levels), followed by a string class description. For example:

function(ecoli210,7,0,0,'b0217','putative aminopeptidase').

Arguments are ORF number, exactly 3 class numbers, gene name (or blattner number if no gene name), ORF description.

2. ecoli_data.pl

Data for each ORF (gene) is delimited by

begin(model(ecoliX)).
end(model(ecoliX)).

where X is the ORF number. Other predicates are as follows (examples):
ecoli_orf(ecoliX). % X is ORF number
ecoli_mol_wt(176624.1). % float
ecoli_theo_pI(5.81). %float
ecoli_atomic_comp(c,7940). % {c,h,n,o,s} , int
ecoli_aliphatic_index(69.57). % float
ecoli_hydro(-0.549). % float
sec_struc(1,c,2). % int (start), {a,b,c}, int (length)
sec_struc_coil(1,2). % int (start), int (length)
sec_struc_beta(1,5). % int (start), int (length)
sec_struc_alpha(1,7). % int (start), int (length)
sequence_length(255). % int
amino_acid_ratio(a,8.9). % amino_acid_char, float
amino_acids(ecoli3013,a,70). % ORF_num, amino_acid_char, int
amino_acid_pair_ratio(a,a,9.0). % amino_acid_char, amino_acid_char, float
amino_acid_pairs(a,a,7). % amino_acid_char, amino_acid_char, int
ecoli_to_ecoli(1170,1.0e-105,5). % ORF_num, double (e-value), int (iteration)
e_val(o42893,2.0e-99). % accession_number, double (e-value)
psi_iter(o42893,5). % accession_number, int (iteration)
species(p52494,'candida_albicans__yeast_'). % accession_number, string
mol_wt(p52494,104022). % accession_number, int
classification(p52494,candida). % accession_number, name
keyword(p25195,'plasmid'). % accession_number, string



Attribute Information:

N/A


Relevant Papers:

King, R. and Karwath, A. and Clare, A. and Dehaspe, L. (2001). The Utility of Different Representations of Protein Sequence for Predicting Functional Class, Bioinformatics, 17(5), pages 445--454.
[Web Link]


Papers That Cite This Data Set1:


Aik Choon Tan and David Gilbert. An Empirical Comparison of Supervised Machine Learning Techniques in Bioinformatics. APBC. 2003. [View Context].

Mukund Deshpande and George Karypis. Evaluation of Techniques for Classifying Biological Sequences. PAKDD. 2002. [View Context].

Mark A. Hall. Department of Computer Science Hamilton, NewZealand Correlation-based Feature Selection for Machine Learning. Doctor of Philosophy at The University of Waikato. 1999. [View Context].

Paul Horton and Kenta Nakai. Better Prediction of Protein Cellular Localization Sites with the it k Nearest Neighbors Classifier. ISMB. 1997. [View Context].

. Prototype Selection for Composite Nearest Neighbor Classifiers. Department of Computer Science University of Massachusetts. 1997. [View Context].

Andrew Watkins and Jon Timmis and Lois C. Boggess. Artificial Immune Recognition System (AIRS): An ImmuneInspired Supervised Learning Algorithm. (abw5,jt6@kent.ac.uk) Computing Laboratory, University of Kent. [View Context].

Gaurav Marwah and Lois C. Boggess. Artificial Immune Systems for Classification : Some Issues. Department of Computer Science Mississippi State University. [View Context].



Citation Request:

Usage Restrictions:
Copyright 2000 by R. D. King, A. Karwath, A. Clare, L. Dehaspe

There are no restrictions data usage. This data is provided "as is" and without any express or implied warranties, including, without limitation, the implied warranties of merchantibility and fitness for a particular purpose.

Citation Requests:
Please cite King et al. (2000).

Acknowledgements:
This work was supported by the following grants: G78/6609, BIF08765, GR/L62849 and by PharmaDM, Ambachtenlaan, 54/D, B-3001 Leuven, Belgium
"""