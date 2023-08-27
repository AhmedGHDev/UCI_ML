import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: These highly imbalanced bioassay datasets are from the differing types of screening that can be performed using HTS technology. 21 datasets were created from 12 bioassays.

Data Set Characteristics:  

Multivariate

Number of Instances:

N/A

Area:

Life

Attribute Characteristics:

Integer, Real

Number of Attributes:

N/A

Date Donated

2011-03-29

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

50503


Source:

Virtual Screening of Bioassay Data
Amanda C Schierz,Smart Technology Research Centre, Bournemouth University, Talbot Campus, Poole, Dorset, BH12 5BB, UK
Journal of Cheminformatics 2009, 1:21 doi:10.1186/1758-2946-1-21



Data Set Information:

21 bioassay datasets generated from Pubchem. Both Primary and confirmatory bioassays (12 bioassays, 21 mixes)The data is provided in the same train/test split as the original paper. The compound IDs have been provided in separate files in case people wish to generate their own molecular representation. The order of the compound Ids is the same as the data files.

â€¢ AID362 details the results of a primary screening bioassay for Formylpeptide Receptor Ligand Binding University from the New Mexico Center for Molecular Discovery. It is a relatively small dataset with 4279 compounds and with a ratio of 1 active to 70 inactive compounds (1.4% minority class). The compounds were selected on the basis of preliminary virtual screening of approximately 480,000 drug-like small molecules from Chemical Diversity Laboratories.

â€¢ AID456 is a primary screen assay from the Burnham Center for Chemical Genomics for inhibition of TNFa induced VCAM-1 cell surface expression and consists of 9,982 compounds with a ratio of 1 active compound to 368 inactive compounds (0.27% minority). The compounds have been selected for their known drug-like properties and 9,431 meet the Rule of 5 [19].

â€¢ AID688 is the result of a primary screen for Yeast eIF2B from the Penn Center for Molecular Discovery and contains activity information of 27,198 compounds with a ratio of 1 active compound to 108 inactive compounds (0.91% minority). The screen is a reporter-gene assay and 25,656 of the compounds have known drug-like properties.

â€¢ AID604 is a primary screening bioassay for Rho kinase 2 inhibitors from the Scripps Research Institute Molecular Screening Center. The bioassay contains activity information of 59,788 compounds with a ratio of 1 active compound to 281 inactive compounds (1.4%). 57,546 of the compounds have known drug-like properties.

â€¢ AID373 is a primary screen from the Scripps Research Institute Molecular Screening Center for endothelial differentiation, sphingolipid G-protein-coupled receptor, 3. 59,788 compounds were screened with a ratio of 1 active compound to 963 inactive compounds (0.1%). 57,546 of the compounds screened had known drug-like properties.

â€¢ AID746 is a primary screen from the Scripps Research Institute Molecular Screening Center for Mitogen-activated protein kinase. 59,788 compounds were screened with a ratio of 1 active compound to 162 inactive compounds (0.61%). 57,546 of the compounds screened had known drug-like properties.

â€¢ AID687 is the result of a primary screen for coagulation factor XI from the Penn Center for Molecular Discovery and contains activity information of 33,067 compounds with a ratio of 1 active compound to 350 inactive compounds (0.28% minority). 30,353 of the compounds screened had known drug-like properties.

â€¢ AID1608 is a different type of screening assay that was used to identify compounds that prevent HttQ103-induced cell death. National Institute of Neurological Disorders and Stroke Approved Drug Program. The compounds that prevent a release of a certain chemical into the growth medium are labelled as active and the remaining compounds are labelled as having inconclusive activity. AID1608 is a small dataset with 1,033 compounds and a ratio of 1 active to 14 inconclusive compounds (6.58% minority class).

â€¢ AID644 confirmatory screen of AID604

â€¢ AID1284 confirmatory screen of AID746

â€¢ AID439 confirmatory screen of AID373

â€¢ AID721 confirmatory screen of AID746



Attribute Information:

Each attribute has been fully described in the Open Access publication. The data is a mixture of boolean, integer and real values. Only 2 class - Active and Inactive. Highly Imbalanced.


Relevant Papers:

Citations for paper:

The use of classification trees for bioinformatics
Xiang Chen, Minghui Wang, Heping Zhang: 6 JAN 2011
DOI: 10.1002/widm.14

Consensus model for identification of novel PI3K inhibitors in large chemical library
Chin Yee Liew, Xiao Hua Ma and Chun Wei Yap
Journal of Computer-Aided Molecular Design
Volume 24, Number 2, 131-141, DOI: 10.1007/s10822-010-9321-0

Genetic Algorithm-Neural Network (GANN): a study of neural network activation functions and depth of genetic algorithm search applied to feature selection
Dong Ling Tong and Robert Mintram
International Journal of Machine Learning and Cybernetics
Volume 1, Numbers 1-4, 75-87, DOI: 10.1007/s13042-010-0004-x






Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
#FROM URL
"""
import pandas as pd
from zipfile import ZipFile
import requests, zipfile, io
zip_file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00209/Schierz_Bioassay.zip'
file_name="ad.data"
r = requests.get(zip_file_url)
zip_file = zipfile.ZipFile(io.BytesIO(r.content))
dfs = {text_file.filename.split('/')[-1].split('.')[0]+"_df": pd.read_csv(zip_file.open(text_file.filename)) for text_file in zip_file.infolist() if text_file.filename.endswith('.csv')}

print(df.info())
"""

#LOACL
import zipfile
zip_file = zipfile.ZipFile('../ics.uci.edu/ml/machine-learning-databases/00209/Schierz_Bioassay.zip')
dfs = {text_file.filename.split('/')[-1].split('.')[0]+"_df": pd.read_csv(zip_file.open(text_file.filename)) for text_file in zip_file.infolist() if text_file.filename.endswith('.csv')}

print(dfs.keys())
print(dfs[list(dfs.keys())[0]].info())