import pandas as pd


#Step 00: Loading data
#FROM URL

# INFO
"""
Abstract: The data set contains 15 classes of 24 instances each. Each class references to a hand movement type in LIBRAS (Portuguese name 'LÍngua BRAsileira de Sinais', oficial brazilian signal language).


Data Set Characteristics:  

Multivariate, Sequential

Number of Instances:

360

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

91

Date Donated

2009-08-17

Associated Tasks:

Classification, Clustering

Missing Values?

N/A

Number of Web Hits:

101559


Source:

Creators:
Daniel Baptista Dias (Dias, D.B.)
Sarajane Marques Peres (Peres, S. M.)
Helton Hideraldo Bíscaro (Bíscaro. H. H.)
{danielbdias,heltonhb, sarajane} at usp.br

Donor:
University of São Paulo - Brazil


Data Set Information:

The dataset (movement_libras) contains 15 classes of 24 instances each, where each class references to a hand movement type in LIBRAS.

In the video pre-processing, a time normalization is carried out selecting 45 frames from each video, in according
to an uniform distribution. In each frame, the centroid pixels of the segmented objects (the hand) are found, which
compose the discrete version of the curve F with 45 points. All curves are normalized in the unitary space.

In order to prepare these movements to be analysed by algorithms, we have carried out a mapping operation, that is, each
curve F is mapped in a representation with 90 features, with representing the coordinates of movement.

Some sub-datasets are offered in order to support comparisons of results.


Attribute Information:

90 numeric (double) and 1 for the class (integer)


Relevant Papers:

DIAS, D. B.; MADEO, R. C. B.; ROCHA, T.; BÍSCARO, H. H.; PERES, S. M..
Hand Movement Recognition for Brazilian Sign Language: A Study Using Distance-Based Neural Networks.
In: 2009 International Joint Conference on Neural Networks, 2009, Atlanta, GA.
Proceedings of 2009 International Joint Conference on Neural Networks. Eau Claire, WI, USA : Documation LLC, 2009. p. 697-704.
Digital Object Identifier 10.1109/IJCNN.2009.5178917



Citation Request:

Please refer to the Machine Learning Repository's citation policy.
"""

"""
import pandas as pd
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/libras/movement_libras.data"
,names=['F_'+str(i) for i in range(1, 91)] + ['class']
)

print(df.info())
"""

#LOACL
import pandas as pd
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/libras/movement_libras.data"
,names=['F_'+str(i) for i in range(1, 91)] + ['class']
)

print(df.info())