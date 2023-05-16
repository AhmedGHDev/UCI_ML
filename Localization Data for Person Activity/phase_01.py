import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Data contains recordings of five people performing different activities. Each person wore four sensors (tags) while performing the same scenario five times.

Data Set Characteristics:  

Univariate, Sequential, Time-Series

Number of Instances:

164860

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

8

Date Donated

2010-11-03

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

132121


Source:

- Creators: Mitja Lustrek (mitja.lustrek '@' ijs.si), Bostjan Kaluza (bostjan.kaluza '@' ijs.si), Rok Piltaver (rok.piltaver '@' ijs.si), Jana Krivec (jana.krivec '@' ijs.si), Vedrana Vidulin (vedrana.vidulin '@' ijs.si)
- Jozef Stefan Institute, Jamova cesta 39, 1000 Ljubljana, Slovenija
- Donor: Bozidara Cvetkovic (boza.cvetkovic '@' ijs.si)
- Jozef Stefan Institute, Jamova cesta 39, 1000 Ljubljana, Slovenija
- Date received: October, 2010


Data Set Information:

People used for recording of the data were wearing four tags (ankle left, ankle right, belt and chest).
Each instance is a localization data for one of the tags. The tag can be identified by one of the attributes.


Attribute Information:

Instance example: A01,020-000-033-111,633790226057226795,27.05.2009 14:03:25:723,4.292500972747803,2.0738532543182373,1.36650812625885,walking

1) Sequence Name {A01,A02,A03,A04,A05,B01,B02,B03,B04,B05,C01,C02,C03,C04,C05,D01,D02,D03,D04,D05,E01,E02,E03,E04,E05} (Nominal)
- A, B, C, D, E = 5 people
2) Tag identificator {010-000-024-033,020-000-033-111,020-000-032-221,010-000-030-096} (Nominal)
- ANKLE_LEFT = 010-000-024-033
- ANKLE_RIGHT = 010-000-030-096
- CHEST = 020-000-033-111
- BELT = 020-000-032-221
3) timestamp (Numeric) all unique
4) date FORMAT = dd.MM.yyyy HH:mm:ss:SSS (Date)
5) x coordinate of the tag (Numeric)
6) y coordinate of the tag (Numeric)
7) z coordinate of the tag (Numeric)
8) activity {walking,falling,'lying down',lying,'sitting down',sitting,'standing up from lying','on all fours','sitting on the ground','standing up from sitting','standing up from sitting on the ground'} (Nominal)

Relevant Papers:

B. Kaluza, V. Mirchevska, E. Dovgan, M. Lustrek, M. Gams, An Agent-based Approach to Care in Independent Living, International Joint Conference on Ambient Intelligence (AmI-10), Malaga, Spain, In press



Citation Request:

B. Kaluza, V. Mirchevska, E. Dovgan, M. Lustrek, M. Gams, An Agent-based Approach to Care in Independent Living, International Joint Conference on Ambient Intelligence (AmI-10), Malaga, Spain, In press
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00196/ConfLongDemo_JSI.txt"
,names=["Sequence_Name", "Tag", "timestamp", "date", "x", "y", "z", "activity"]
)

print(df.info())
"""

#LOACL
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/00196/ConfLongDemo_JSI.txt"
,names=["Sequence_Name", "Tag", "timestamp", "date", "x", "y", "z", "activity"]
)

print(df.info())