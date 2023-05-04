import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/adult-stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df3 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small+adult-stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df4 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df = pd.concat([df1, df2, df3, df4], axis=0)


print(df.info())
"""

#LOACL
import pandas
df1 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/balloons/adult+stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df2 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/balloons/adult-stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df3 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small+adult-stretch.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df4 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/balloons/yellow-small.data", 
                 names=['Class Name', 'Left-Weight', 'Left-Distance', 'Right-Weight', 'Right-Distance'])

df = pd.concat([df1, df2, df3, df4], axis=0)

print(df.info())