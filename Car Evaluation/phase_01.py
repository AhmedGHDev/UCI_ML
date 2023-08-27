import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data", names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/car/car.data", names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])

print(df.info())