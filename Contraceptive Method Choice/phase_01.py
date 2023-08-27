import pandas as pd


#Step 00: Loading data

# attributes
"""
1. Wife's age (numerical)
2. Wife's education (categorical) 1=low, 2, 3, 4=high
3. Husband's education (categorical) 1=low, 2, 3, 4=high
4. Number of children ever born (numerical)
5. Wife's religion (binary) 0=Non-Islam, 1=Islam
6. Wife's now working? (binary) 0=Yes, 1=No
7. Husband's occupation (categorical) 1, 2, 3, 4
8. Standard-of-living index (categorical) 1=low, 2, 3, 4=high
9. Media exposure (binary) 0=Good, 1=Not good
10. Contraceptive method used (class attribute) 1=No-use, 2=Long-term, 3=Short-term
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data", names=['Wifes_age', 'Wifes_education', 'Husbands_education', 'Number_of_children_ever_born', 'Wifes_religion', 'Wifes_now_working?', 'Husbands_occupation', 'Standard-of-living_index', 'Media_exposure', 'Contraceptive_method_used'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data", names=['Wifes_age', 'Wifes_education', 'Husbands_education', 'Number_of_children_ever_born', 'Wifes_religion', 'Wifes_now_working?', 'Husbands_occupation', 'Standard-of-living_index', 'Media_exposure', 'Contraceptive_method_used'])

print(df.info())