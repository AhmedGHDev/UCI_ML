import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king/krkopt.data", names=["White King file (column)", "White King rank (row)", "White Rook file", "White Rook rank", "Black King file", "Black King rank", "optimal depth-of-win for White"])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king/krkopt.data", names=["White King file (column)", "White King rank (row)", "White Rook file", "White Rook rank", "Black King file", "Black King rank", "optimal depth-of-win for White"])

print(df.info())