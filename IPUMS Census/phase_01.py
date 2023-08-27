import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df_s97 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_s98 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_s99 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)

df_97 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_98 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_99 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)


print(df_99.info())
"""

#LOACL
df_s97 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_s98 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_s99 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/s.ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)

df_97 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_98 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)
df_99 = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/ipums-mld/ipums.la.97.gz"
,compression='gzip'
,names=['X_'+str(i) for i in range(1, 62)]
)


print(df_99.info())