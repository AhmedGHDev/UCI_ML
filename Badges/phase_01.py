import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/badges/badges.data", names=['person_name'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/badges/badges.data", names=['person_name'])

print(df.info())