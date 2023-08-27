import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: A pen-based database with more than 11k isolated handwritten characters


Data Set Characteristics:  

Multivariate, Sequential

Number of Instances:

11640

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

N/A

Date Donated

2009-01-22

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

72158


Source:

F. Prat(*), M. J. Castro(+), D. Llorens(*), A. Marzal(*), and J. M. Vilar(*)

* Departamento de Lenguajes y Sistemas Informáticos
Universitat Jaume I (UJI), 12071 Castellón, SPAIN

+ Departamento de Sistemas Informáticos y Computación
Universidad Politécnica de Valencia (UPV), 46071 Valencia, SPAIN

fprat '@' lsi.uji.es
December 2008


Data Set Information:

We have created the UJIpenchars2 character database by collecting samples from 60 writers at two different sites in two phases:

1st phase, 11 writers, carried out at UJI.
2nd phase, 49 writers, carried out at UPV (44 writers) and UJI (5).
Each writer contributed with letters, digits, and other characters and two samples were collected for each pair writer/character.

The complete lexicon is as follows:
66 letters (33 per case):
The 52 ASCII letters.
The 14 Spanish non-ASCII letters:
Letter n with tilde (2 characters).
Vowels with acute accent (10 characters).
Letter u with diaeresis (2 characters).
The 10 digits.
Other 21 characters:
The 16 ASCII ones shown in the following line:
. , ; : ? ! ' ' ( ) % - @ $ < >
5 non-ASCII ones:
Inverted question and exclamation marks (2 characters).
Masculine and feminine ordinal indicators (2 characters).
The euro sign (1 character).
So the total number of samples in this database is 11640: 60 writers x (66+10+21) characters x 2 repetitions

UJIpenchars is a subset of UJIpenchars2 with only 1364 samples: the ASCII letters and digits collected at UJI during the 1st acquisition phase.

We have not defined a standard task for UJIpenchars2, but divided the writer set into two disjoint subsets in order to ease the definition of writer independent tasks:
40 'trn' writers:
The 11 1st phase UJI writers.
29 UPV writers.
20 'tst' writers:
The 5 2nd phase UJI writers.
15 UPV writers.
The distribution of our database consists of 2 files:
This 'uji2.names'.
The file 'ujipenchars2.txt' containing all the samples in a format described later.
The handwriting samples were collected on a Toshiba Portégé M400 Tablet PC using its cordless stylus. Each one of the 60 writers completed 2 non-consecutive sessions. In each session, the corresponding writer was asked to write one exemplar for each character in the lexicon. The acquisition program shows a set of boxes on the screen, one for each required character, and writers are told to write only inside those boxes.

Each acquisition box is approximately 13.6 millimetres wide and 20.4 millimetres tall and contais two horizontal guides at approximate distances of 7.5 and 12.7 millimetres from top, respectively.

Writers were instructed to clear the content of the corresponding box by using an on-screen button and try again whenever they made a mistake or were unhappy with the writing of any character. Subjects were monitored only when writing their first exemplars and every sample considered OK by its writer was accepted, even if some of its points lay out of the corresponding acquisition box.

Only X and Y coordinate information was recorded along the strokes by the acquisition program, without, for instance, pressure level values or timing information. Thus, in multi-stroke samples, no information at all was recorded between strokes. Both coordinates were expressed as integer ink units, with the origin lying at the top left corner of the corresponding acquisition box. X values grow left-to-right and Y values grow downwards.

Although we have employed the same acquisition program on identical hardware at UJI and UPV, we have observed that acquisition files seem to show that UPV samples have been collected using acquisition boxes larger than UJI ones. This is due to a different configuration parameter value that, at UPV, makes the acquisition program translate 1 millimetre into 152 ink units, instead of using the standard UJI ratio: 100 ink units per millimetre. If box homogenisation is needed, it can be easily achieved, for instance, by dividing UPV coordinate values by 1.52.

We have also observed that runs of consecutive points with identical coordinates were frequently acquired inside strokes; such runs were preserved in this database, so it is up to its users to decide whether to avoid them by an appropriate preprocessing step or not.

Although it is a paper mainly devoted to UJIpenchars,

      D. Llorens et al.: 'The UJIpenchars Database: A Pen-Based Database of Isolated Handwritten Characters'
      Proc. of the 6th International Conference on Language Resources and Evaluation. 2008.

contains useful information about UJIpenchars2. It can be found in [Web Link].

Attribute Information:

The file 'ujipenchars2.txt' is a text one with a simple format where all database samples are represented. Because some non-ASCII characters are needed, UTF-8 encoding is employed.

In order to describe how attributes are represented in 'ujipenchars2.txt', it is worth explaining the general syntax of the file first. From the higher-level point of view, this file is composed of comment lines and sample representations.

A comment line is one beginning with two slashes. In 'ujipenchars2.txt', we have employed comment lines for two purposes:

Prior to the set of samples corresponding to each site, a comment acts as a reminder of the number of ink units per length unit on the Tablet PC screen, so these two comments can be found in 'ujipenchars2.txt':
      // UJI: 100 units per millimetre 

      // UPV: 152 units per millimetre

Prior to each sample representation, an ASCII comment tells you which character it represents. For ASCII characters (for instance, an uppercase u), comments may look like this:
      // ASCII char: U

For non-ASCII characters (for instance, a lowercase o with acute accent), the character identity is represented by means of its HTML entity name:
      // Non-ASCII char: oacute 
A sample representation is composed of a header line followed by the representation of its *sequence of strokes*, where the header line consists of three blank-separated elements: the word 'WORD', the representation of the *character identity*, and the *session identifier*. For instance, a semicolon sample representation may look like this:
           WORD ; trn_UJI_W03-01

             NUMSTROKES 2

             POINTS 9 # 541 1001 541 1001 540 987 540 987 530 977 530 977 530 977 530 977 530 977

             POINTS 8 # 518 1227 500 1257 480 1291 470 1309 465 1318 458 1330 458 1330 471 1312

A detailed description on how information about each attribute is represented in 'ujipenchars2.txt' follows:
Character identity: It is represented by the character itself (';' in the previous example), one out of 97 possibilities. Remember that UTF-8 encoding is employed, so non-ASCII characters need more than a byte to be encoded.

Session identifier: It is composed by a long writer identifier ('trn_UJI_W03' in the previous example) and a repetition number ('01' or '02') separated by a hyphen, where a long writer identifier consists of three elements separated by underscores:
A writer set identifier, 'trn' (writers for training) or 'tst' (writers for test).
A site identifier, 'UJI' or 'UPV'.
A short writer identifier, like 'W03' in the previous example. Writers are numbered from 1 to 60.

Sequence of strokes: Its representation consists of a number of lines where individual elements are separated by blanks. The elements of the first line are the word 'NUMSTROKES' and an unsigned integer representing the number of strokes in the sample. This number varies from 1 to 5 in 'ujipenchars2.txt'. And, for each stroke, a line represents its points with the following elements:
The word 'POINTS'.
An unsigned integer representing the number of points in the stroke.
A hash character.
For each point in the stroke, two integers representing its X and Y coordinates in ink units. Remember that X values grow left-to-right, Y values grow downwards, and the ratio of length to ink units varies from site to site. Moreover, we have observed some negative coordinate values in 'ujipenchars2.txt'.

Relevant Papers:

D. Llorens et al., 'The UJIpenchars Database: A Pen-Based Database of Isolated Handwritten Characters'
Proc. of the 6th International Conference on Language Resources and Evaluation. 2008.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""