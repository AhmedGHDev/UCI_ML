import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: 1593 handwritten digits from around 80 persons were scanned, stretched in a rectangular box 16x16 in a gray scale of 256 values.


Data Set Characteristics:  

Multivariate

Number of Instances:

1593

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

256

Date Donated

2008-11-11

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

157772


Source:

The dataset was created by Tactile Srl, Brescia, Italy (http://www.tattile.it) and donated in 1994 to Semeion Research Center of Sciences of Communication, Rome, Italy (http://www.semeion.it), for machine learning research.

For any questions, e-mail Massimo Buscema (m.buscema '@' semeion.it) or Stefano Terzi (s.terzi '@' semeion.it)


Data Set Information:

1593 handwritten digits from around 80 persons were scanned, stretched in a rectangular box 16x16 in a gray scale of 256 values.Then each pixel of each image was scaled into a bolean (1/0) value using a fixed threshold.

Each person wrote on a paper all the digits from 0 to 9, twice. The commitment was to write the digit the first time in the normal way (trying to write each digit accurately) and the second time in a fast way (with no accuracy).

The best validation protocol for this dataset seems to be a 5x2CV, 50% Tune (Train +Test) and completly blind 50% Validation


Attribute Information:

This dataset consists of 1593 records (rows) and 256 attributes (columns).

Each record represents a handwritten digit, orginally scanned with a resolution of 256 grays scale (28).

Each pixel of the each original scanned image was first stretched, and after scaled between 0 and 1 (setting to 0 every pixel whose value was under tha value 127 of the grey scale (127 included) and setting to 1 each pixel whose orinal value in the grey scale was over 127).

Finally, each binary image was scaled again into a 16x16 square box (the final 256 binary attributes).


Relevant Papers:

M Buscema, MetaNet: The Theory of Independent Judges, in Substance Use & Misuse 33(2)1998, pp 439-461.



Citation Request:

Semeion Research Center of Sciences of Communication, via Sersale 117, 00128 Rome, Italy
Tattile Via Gaetano Donizetti, 1-3-5,25030 Mairano (Brescia), Italy.
"""

#FROM URL
"""
import pandas as pd
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/semeion/semeion.data"
,delimiter='\s+'
,names=['PX_'+str(i) for i in range(0, 266)]
)

print(df.info())
"""

#LOACL
import pandas as pd
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/semeion/semeion.data"
,delimiter='\s+'
,names=['PX_'+str(i) for i in range(0, 266)]
)

print(df.info())