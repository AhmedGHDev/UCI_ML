import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Dataset with electrical impedance measurements of freshly excised tissue samples from the breast.

Data Set Characteristics:  

Multivariate

Number of Instances:

106

Area:

Life

Attribute Characteristics:

Real

Number of Attributes:

10

Date Donated

2010-05-10

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

160903


Source:

JP Marques de Sá, INEB-Instituto de Engenharia Biomédica, Porto, Portugal; e-mail: jpmdesa '@' gmail.com
J Jossinet, inserm, Lyon, France


Data Set Information:

Impedance measurements were made at the frequencies: 15.625, 31.25, 62.5, 125, 250, 500, 1000 KHz
Impedance measurements of freshly excised breast tissue were made at the follwoing frequencies: 15.625, 31.25, 62.5, 125, 250, 500, 1000 KHz. These measurements plotted in the (real, -imaginary) plane constitute the impedance spectrum from where the breast tissue features are computed.
The dataset can be used for predicting the classification of either the original 6 classes or of 4 classes by merging together the fibro-adenoma, mastopathy and glandular classes whose discrimination is not important (they cannot be accurately discriminated anyway).


Attribute Information:

I0 Impedivity (ohm) at zero frequency
PA500 phase angle at 500 KHz
HFS high-frequency slope of phase angle
DA impedance distance between spectral ends
AREA area under spectrum
A/DA area normalized by DA
MAX IP maximum of the spectrum
DR distance between I0 and real part of the maximum frequency point
P length of the spectral curve
Class car(carcinoma), fad (fibro-adenoma), mas (mastopathy), gla (glandular), con (connective), adi (adipose). The


Relevant Papers:

Jossinet J (1996) Variability of impedivity in normal and pathological breast tissue. Med. & Biol. Eng. & Comput, 34: 346-350.
Silva JE, Marques de Sá JP, Jossinet J (2000) Classification of Breast Tissue by Electrical Impedance Spectroscopy. Med & Bio Eng & Computing, 38:26-30.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
#FROM URL
"""
xls = pd.ExcelFile('https://archive.ics.uci.edu/ml/machine-learning-databases/00192/BreastTissue.xls')
df = pd.read_excel(xls, 'Data')


print(df.info())
"""

#LOACL
xls = pd.ExcelFile('../ics.uci.edu/ml/machine-learning-databases/00192/BreastTissue.xls')
df = pd.read_excel(xls, 'Data')


print(df.info())