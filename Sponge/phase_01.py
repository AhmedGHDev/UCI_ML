import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Data on sponges; Attributes in spanish


Data Set Characteristics:  

Multivariate

Number of Instances:

76

Area:

Life

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

45

Date Donated

N/A

Associated Tasks:

Clustering

Missing Values?

Yes

Number of Web Hits:

118495


Source:

Creators:

Iosune Uriz and Marta Domingo
Centre d'Estudis Aban\c{c}ats de Blanes (CSIC)
Cami de Santa Barbara. Blanes (Girona). Spain

Donor:

Javier B\'ejar and Ulises Cort\'es (bejar '@' lsi.upc.es)
Dept. Llenguatges i Sistemes Inform\`atics;
Universitat Politecnica de Catalunya. Barcelona; Spain


Data Set Information:

These are atlantic-mediterranean marine sponges that belong to O.Hadromerida (Demospongiae.Porifera).


Attribute Information:

27 attributes are non-numeric and nominal.
15 attributes are boolean and take the values (NO SI).
3 attributes are numeric and take natural numbers.


Relevant Papers:

Domingo, M. "Aplicaci\'o de t\`ecniques de I.A. (LINNEO) a la classificaci\'o sistem\`atica: O.Hadromerida (Demospongiae.Porifera). Master Thesis. Departament d'ecologia. Universitat de Barcelona.

Martin, M and Sanguesa, R. and Cor\'es "Biasing induction with previous knowledge for knowledge acquisition in imprecise domains''. Les syst\`emes experts et leus applications. Onzi\'emes Journ\'ees Internationales. Avignon'91. Vol 1. pp. 359-370. Avignon, France. 1991.

Martin, M. and Sanguesa, R. and Cort\'es U. "Knowledge acquisition combining analytical and empirical techniques''. Proceedings of the Eighth International Workshop of Machine Learning. ML 91. pp 657-661. Evanston, Illinois, USA 1991.
[Web Link]

Bejar, J. and Cort\'es, U. "LINNEO+: Herramienta para la adquisicion de conocimiento y generacion de reglas de clasificaci\'on en dominios poco estructurados''. Proceedings del III Congreso Iberoamericano de Inteligencia Artificial. IBERAMIA 92. pp 471-482. La Habana (Cuba).
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/sponge/sponge.data"
,names=['X_'+str(i) for i in range(1, 46)]
)

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/sponge/sponge.data"
,names=['X_'+str(i) for i in range(1, 46)]
)

print(df.info())