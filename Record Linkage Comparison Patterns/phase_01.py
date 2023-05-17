import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Element-wise comparison of records with personal data from a record linkage setting. The task is to decide from a comparison pattern whether the underlying records belong to one person.

Data Set Characteristics:  

Multivariate

Number of Instances:

5749132

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

12

Date Donated

2011-03-10

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

93366


Source:

The underlying records stem from the epidemiological cancer registry of the
German state of North Rhine-Westphalia (Epidemiologisches Krebsregister NRW,
http://www.krebsregister.nrw.de). Creation of comparison patterns and
assignment of matching status were undertaken by staff members of
the Institute for Medical Biostatistics, Epidemiology and Informatics (IMBEI)
at the University Medical Center of the Johannes Gutenberg University in Mainz,
Germany (http://www.imbei.uni-mainz.de).


Data Set Information:

The records represent individual data including first and family name, sex, date of birth and postal code, which were collected through iterative insertions in the course of several years. The comparison patterns in this data set are based on a sample of 100.000 records dating from 2005 to 2008. Data pairs were classified as 'match' or 'non-match' during an extensive manual review where several documentarists were involved. The resulting classification formed the basis for assessing the quality of the
registryâ€™s own record linkage procedure.

In order to limit the amount of patterns, a blocking procedure was applied,
which selects only record pairs that meet specific agreement conditions. The
results of the following six blocking iterations were merged together:

1. Phonetic equality of first name and family name, equality of date of birth.
2. Phonetic equality of first name, equality of day of birth.
3. Phonetic equality of first name, equality of month of birth.
4. Phonetic equality of first name, equality of year of birth.
5. Equality of complete date of birth.
6. Phonetic equality of family name, equality of sex.

This procedure resulted in 5.749.132 record pairs, of which 20.931 are matches.

The data set is split into 10 blocks of (approximately) equal size and ratio
of matches to non-matches.

The separate file frequencies.csv contains for every predictive attribute
the average number of values in the underlying records. These values can, for example,
be used as u-probabilities in weight-based record linkage following the
framework of Fellegi and Sunter.


Attribute Information:

1. id_1: internal identifier of first record.
2. id_2: internal identifier of second record.
3. cmp_fname_c1: agreement of first name, first component
4. cmp_fname_c2: agreement of first name, second component
5. cmp_lname_c1: agreement of family name, first component
6. cmp_lname_c2: agreement of family name, second component
7. cmp_sex: agreement sex
8. cmp_bd: agreement of date of birth, day component
9. cmp_bm: agreement of date of birth, month component
10. cmp_by: agreement of date of birth, year component
11. cmp_plz: agreement of postal code
12. is_match: matching status (TRUE for matches, FALSE for non-matches)

The agreement of name components is measured as a real number in the interval [0,1], where 0 denotes maximal disagreement and 1 equality of the underlying values. For the other comparisons, only the values 0 (not equal) and 1 (equal) are used.

is_match is the outcome variable. id_1 and id_2 are not used for prediction but could be used to construct connected components from the found matches.


Relevant Papers:

1. Irene Schmidtmann, Gael Hammer, Murat Sariyar, Aslihan Gerhold-Ay:
Evaluation des Krebsregisters NRW Schwerpunkt Record Linkage. Technical
Report, IMBEI 2009.
[Web Link]
-- Describes the external evaluation of the registry's record linkage
procedures.
-- The comparison patterns in this data set were created in course of
this evaluation.

2. Murat Sariyar, Andreas Borg, Klaus Pommerening:
Controlling false match rates in record linkage using extreme value theory.
Journal of Biomedical Informatics, 2011 (in press).
-- Predicted attribute: matching status (boolean).
-- Results:
-- A new approach for estimating the false match rate in record
linkage by methods of Extreme Value Theory (EVT).
-- The model eliminates the need for labelled training data while
achieving only slighter lower accuracy compared to a procedure
that has knowledge about the matching status.



Citation Request:

Please refer to the Epidemiological Cancer Registry of North Rhine-Westphalia ('Epidemiologisches Krebsregister') and to one of the mentioned papers when using this data set in a publication.
"""
#FROM URL
"""
import pandas as pd
from zipfile import ZipFile
import requests, zipfile, io
zip_file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00210/donation.zip'
r = requests.get(zip_file_url)
zip_file = zipfile.ZipFile(io.BytesIO(r.content))
dfs = dict()
for text_file in zip_file.infolist():
  if text_file.filename.endswith('.csv'):
    dfs[text_file.filename.split('/')[-1].split('.')[0]+"_df"] = pd.read_csv(zip_file.open(text_file.filename))
  if text_file.filename.endswith('.zip'):
    temp_zip_file = zipfile.ZipFile(zip_file.open(text_file.filename))
    for temp_text_file in temp_zip_file.infolist():
      if temp_text_file.filename.endswith('.csv'):
        dfs[temp_text_file.filename.split('/')[-1].split('.')[0]+"_df"] = pd.read_csv(temp_zip_file.open(temp_text_file.filename))

dfs.keys()
dfs[list(dfs.keys())[0]].info()
"""

#LOACL
import zipfile
zip_file = zipfile.ZipFile('../ics.uci.edu/ml/machine-learning-databases/00210/donation.zip')
dfs = dict()
for text_file in zip_file.infolist():
  if text_file.filename.endswith('.csv'):
    dfs[text_file.filename.split('/')[-1].split('.')[0]+"_df"] = pd.read_csv(zip_file.open(text_file.filename))
  if text_file.filename.endswith('.zip'):
    temp_zip_file = zipfile.ZipFile(zip_file.open(text_file.filename))
    for temp_text_file in temp_zip_file.infolist():
      if temp_text_file.filename.endswith('.csv'):
        dfs[temp_text_file.filename.split('/')[-1].split('.')[0]+"_df"] = pd.read_csv(temp_zip_file.open(temp_text_file.filename))

dfs.keys()
dfs[list(dfs.keys())[0]].info()