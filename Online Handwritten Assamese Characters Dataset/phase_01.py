import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This is a dataset of 8235 online handwritten assamese characters. The â€œonlineâ€ process involves capturing of data as text is written on a digitizing tablet with an electronic pen.

Data Set Characteristics:  

Multivariate, Sequential

Number of Instances:

8235

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

N/A

Date Donated

2011-04-01

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

56478


Source:

Creators:
Udayan BaruahÂ¹ Â² and Shyamanta M HazarikaÂ¹

1. Department of Computer Science and Engineering
Tezpur University
Assam, India, 784028.
udayanbaruah '@' yahoo.co.in
shyamanta '@' ieee.org

2. Department of Information Technology
Sikkim Manipal Institute of Technology
Sikkim, India, 737136.
udayanbaruah '@' yahoo.co.in

Donor:

Udayan Baruah
Department of Information Technology
Sikkim Manipal Institute of Technology
Sikkim, India, 737136.
udayanbaruah '@' yahoo.co.in


Data Set Information:

A dataset of online handwritten assamese characters by collecting samples from 45 writers is created. Each writer contributed 52 basic characters, 10 numerals and 121 assamese conjunct consonants. The total number of entries corresponding to each writer is 183 (= 52 characters + 10 numerals + 121 conjunct consonants). The total number of samples in the dataset is 8235 ( = 45 Ã— 183 ).

The handwriting samples were collected on an iball 8060U external digitizing tablet connected to a laptop using its cordless digital stylus pen. The data acquisition program consists of a GUI which shows a box on the screen along with other controls. The writers are instructed to write only inside the acquisition box. The acquisition program records the handwriting as a stream of (X, Y) coordinate points using the appropriate pen position sensor along with the pen-up/pen-down switching. No pressure level was recorded.

The distribution of the dataset consists of 45 folders (one for each writer) and a â€œData_Table.pdfâ€ file. This file contains information about the character id (ID), character name (Label) and actual shape of the character (Char).

Each folder contains 183 text files corresponding to the 183 characters written by a single writer. Each file is named based on the pair (M, N). The text file â€œM.N.txtâ€ represents the character with ID â€œMâ€ written by the writer with ID â€œNâ€. For instance the file â€œ132.10.txtâ€ represents the character with ID â€œ132â€ written by the writer with ID â€œ10â€.


Attribute Information:

1. Character Name: The first line of each sample is â€œCHARACTER_NAME: Characterâ€. The â€œCharacterâ€ is the Name of any one of the 183 characters listed below:

Here â€œID [i]â€ represents the name of the character with the ID â€œiâ€.

ID [1] = â€œAâ€
ID [2] = â€œAAâ€
ID [3] = â€œEâ€
ID [4] = â€œEEâ€
ID [5] = â€œUâ€
ID [6] = â€œUUâ€
ID [7] = â€œREEâ€
ID [8] = â€œAEâ€
ID [9] = â€œOIâ€
ID [10] = â€œOâ€
ID [11] = â€œOUâ€
ID [12] = â€œKAâ€
ID [13] = â€œKHAâ€
ID [14] = â€œGAâ€
ID [15] = â€œGHAâ€
ID [16] = â€œNGâ€
ID [17] = â€œCAâ€
ID [18] = â€œCCAâ€
ID [19] = â€œJAâ€
ID [20] = â€œJHAâ€
ID [21] = â€œNIYAâ€
ID [22] = â€œMTAâ€
ID [23] = â€œMTHAâ€
ID [24] = â€œMDAâ€
ID [25] = â€œMDHAâ€
ID [26] = â€œMNAâ€
ID [27] = â€œTAâ€
ID [28] = â€œTHAâ€
ID [29] = â€œDAâ€
ID [30] = â€œDHAâ€
ID [31] = â€œNAâ€
ID [32] = â€œPAâ€
ID [33] = â€œPHAâ€
ID [34] = â€œBAâ€
ID [35] = â€œBHAâ€
ID [36] = â€œMAâ€
ID [37] = â€œAJAâ€
ID [38] = â€œRAâ€
ID [39] = â€œLAâ€
ID [40] = â€œWAâ€
ID [41] = â€œTXAâ€
ID [42] = â€œMXAâ€
ID [43] = â€œDXAâ€
ID [44] = â€œHAâ€
ID [45] = â€œKHYAâ€
ID [46] = â€œAYAâ€
ID [47] = â€œDRAâ€
ID [48] = â€œDHRAâ€
ID [49] = â€œKTAâ€
ID [50] = â€œANSRâ€
ID [51] = â€œBXGâ€
ID [52] = â€œCBNâ€
ID [53] = â€œKKâ€
ID [54] = â€œKTâ€
ID [55] = â€œKTTâ€
ID [56] = â€œKSâ€
ID [57] = â€œKLâ€
ID [58] = â€œKMâ€
ID [59] = â€œGLâ€
ID [60] = â€œCCâ€
ID [61] = â€œCCCâ€
ID [62] = â€œJJâ€
ID [63] = â€œJBâ€
ID [64] = â€œBJâ€
ID [65] = â€œGNâ€
ID [66] = â€œTNâ€
ID [67] = â€œJJBâ€
ID [68] = â€œLGâ€
ID [69] = â€œTTâ€
ID [70] = â€œGDHâ€
ID [71] = â€œGMâ€
ID [72] = â€œGHNâ€
ID [73] = â€œMDDâ€
ID [74] = â€œNTâ€
ID [75] = â€œNNâ€
ID [76] = â€œNMMâ€
ID [77] = â€œTTTâ€
ID [78] = â€œTTBâ€
ID [79] = â€œTMâ€
ID [80] = â€œTRâ€
ID [81] = â€œNTTâ€
ID [82] = â€œRRGâ€
ID [83] = â€œNDDâ€
ID [84] = â€œNTHâ€
ID [85] = â€œNDHâ€
ID [86] = â€œNNNâ€
ID [87] = â€œNBâ€
ID [88] = â€œNSâ€
ID [89] = â€œNMâ€
ID [90] = â€œDBâ€
ID [91] = â€œQJâ€
ID [92] = â€œPTTâ€
ID [93] = â€œPLâ€
ID [94] = â€œDVâ€
ID [95] = â€œBLâ€
ID [96] = â€œBDâ€
ID [97] = â€œTBâ€
ID [98] = â€œMMâ€
ID [99] = â€œMVâ€
ID [100] = â€œMPâ€
ID [101] = â€œMNâ€
ID [102] = â€œNTRâ€
ID [103] = â€œMBâ€
ID [104] = â€œLKâ€
ID [105] = â€œMNDâ€
ID [106] = â€œFKâ€
ID [107] = â€œLDâ€
ID [108] = â€œLLâ€
ID [109] = â€œLPâ€
ID [110] = â€œLTâ€
ID [111] = â€œSNâ€
ID [112] = â€œSCâ€
ID [113] = â€œSMâ€
ID [114] = â€œSBâ€
ID [115] = â€œFNâ€
ID [116] = â€œFTâ€
ID [117] = â€œSKâ€
ID [118] = â€œSSTHâ€
ID [119] = â€œSSMâ€
ID [120] = â€œSSNâ€
ID [121] = â€œSSBâ€
ID [122] = â€œSTâ€
ID [123] = â€œSPâ€
ID [124] = â€œSPHâ€
ID [125] = â€œSTHâ€
ID [126] = â€œSKHâ€
ID [127] = â€œNGGâ€
ID [128] = â€œNGCâ€
ID [129] = â€œFPâ€
ID [130] = â€œNGNâ€
ID [131] = â€œXMâ€
ID [132] = â€œNGJâ€
ID [133] = â€œMNTHâ€
ID [134] = â€œNGKâ€
ID [135] = â€œKRâ€
ID [136] = â€œTRUâ€
ID [137] = â€œBHRâ€
ID [138] = â€œTHBâ€
ID [139] = â€œDGâ€
ID [140] = â€œDGHâ€
ID [141] = â€œDDâ€
ID [142] = â€œDDHâ€
ID [143] = â€œHRâ€
ID [144] = â€œGGUâ€
ID [145] = â€œGGNâ€
ID [146] = â€œNKHâ€
ID [147] = â€œNGHâ€
ID [148] = â€œNGKHâ€
ID [149] = â€œTTHâ€
ID [150] = â€œPNâ€
ID [151] = â€œHNâ€
ID [152] = â€œXNâ€
ID [153] = â€œMFâ€
ID [154] = â€œBBâ€
ID [155] = â€œLBâ€
ID [156] = â€œLMâ€
ID [157] = â€œBHMâ€
ID [158] = â€œMLâ€
ID [159] = â€œSLâ€
ID [160] = â€œPSâ€
ID [161] = â€œKHRâ€
ID [162] = â€œGRâ€
ID [163] = â€œGHRâ€
ID [164] = â€œJRâ€
ID [165] = â€œTRRâ€
ID [166] = â€œDRRâ€
ID [167] = â€œDHRRâ€
ID [168] = â€œPRRâ€
ID [169] = â€œBRRâ€
ID [170] = â€œMRRâ€
ID [171] = â€œTSRâ€
ID [172] = â€œDSRâ€
ID [173] = â€œHRRâ€
ID [174] = â€œSUNYAâ€
ID [175] = â€œEKâ€
ID [176] = â€œDUIâ€
ID [177] = â€œTINIâ€
ID [178] = â€œCARIâ€
ID [179] = â€œPACâ€
ID [180] = â€œCAYâ€
ID [181] = â€œXATâ€
ID [182] = â€œATHâ€
ID [183] = â€œNAAâ€

2. The total number of strokes in the sample: The total number of strokes used to write a character is represented by the line â€œSTROKE_COUNT: Numberâ€, where â€œNumberâ€ is an integer value.

3. Sequence of Strokes: Each stroke begins with the â€œPEN_DOWNâ€ information and there is a â€œPEN_UPâ€ information followed by the â€œPEN_DOWNâ€ information between two consecutive strokes. The end of a sample is represented by the â€œPEN_UPâ€ information followed by the â€œEND_CHARACTER: Characterâ€ information. Each stroke consists of a sequence of X and Y coordinates values which are given in the first and the second columns respectively. Corresponding to each pair of values of X and Y coordinates, there are â€œSTYLUS_STATEâ€ and â€œSTROKEâ€ information given in the third and the fourth columns respectively. â€œSTYLUS_STATEâ€ is either 1 or 0. Corresponding to each recorded (X, Y) point, â€œSTYLUS_STATEâ€ is 1 and corresponding to the â€œPEN_UPâ€ information â€œSTYLUS_STATEâ€ is 0. â€œSTYLUS_STATEâ€ is kept blank corresponding to each â€œPEN_DOWNâ€ information. The â€œSTROKEâ€ information represents the serial number of a constituent stroke of a sample. The value of X grows left-to-right and that of Y grows downwards. Coordinates are integer numbers ranging from 0 to 4392 for X and 0 to 4868 for Y respectively.


Relevant Papers:

Provide references to papers that have cited this data set in the past (if any).



Citation Request:

U. Baruah, S. M. Hazarika, "A Dataset of Online Handwritten Assamese Characters", Journal of Information Processing Systems, vol. 11, no. 3, pp. 325-341, 2015.
"""