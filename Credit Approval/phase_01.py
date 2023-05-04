import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data", names=["A"+str(i) for i in range(1,17)])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data", names=["A"+str(i) for i in range(1,17)])

print(df.info())