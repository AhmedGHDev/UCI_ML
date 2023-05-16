import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: 15 months worth of daily data (440 daily records) that describes the occupancy rate, between 0 and 1, of different car lanes of the San Francisco bay area freeways across time.

Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

440

Area:

Computer

Attribute Characteristics:

Real

Number of Attributes:

138672

Date Donated

2011-05-22

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

92853


Source:

Source: California Department of Transportation, www.pems.dot.ca.gov
Creator: Marco Cuturi, Kyoto University, mcuturi '@' i.kyoto-u.ac.jp


Data Set Information:

We have downloaded 15 months worth of daily data from the California Department of Transportation PEMS website, [Web Link], The data describes the occupancy
rate, between 0 and 1, of different car lanes of San Francisco bay area freeways. The measurements cover the period from Jan. 1st 2008 to Mar. 30th 2009 and are sampled every 10 minutes. We consider each day in this database as a single time series of dimension 963 (the number of sensors which functioned consistently throughout the studied period) and length 6 x 24=144. We remove public holidays from the dataset, as well
as two days with anomalies (March 8th 2009 and March 9th 2008) where all sensors were muted between 2:00 and 3:00 AM. This results in a database of 440 time series.

The task we propose on this dataset is to classify each observed day as the correct day of the week, from Monday to Sunday, e.g. label it with an integer in {1,2,3,4,5,6,7}.

I will keep separate copies of this database on my website in a Matlab format. If you use Matlab, it might be more convenient to consider these .mat files directly.

Data-Format
-------------

There are two files for each fold, the data file and the labels file. We have split the 440 time series between train and test folds, but you are of course free to merge them to consider a different cross validation setting.
- The PEMS_train textfile has 263 lines. Each line describes a time-series provided as a matrix. The matrix syntax is that of Matlab, e.g. [ a b ; c d] is the matrix with row vectors [a b] and [c d] in that order. Each matrix describes the different occupancies rates (963 lines, one for each station/detector) sampled every 10 minutes during the day (144 columns).
- The PEMS_trainlabel text describes, for each day of measurements described above, the day of the week on which the data was sampled, namely an integer between 1 (Mon.) and 7 (Sun.).

- PEMS_test and PEMS_testlabels are formatted in the same way, except that there are 173 test instances.

- The permutation that I used to shuffle the dataset is given in the randperm file. If you need to rearrange the data so that it follows the calendar order, you should merge train and test samples and reorder them using the inverse permutation of randperm.


Attribute Information:

Each attribute describes the measurement of the occupancy rate (between 0 and 1) of a captor location as recorded by a measuring station, at a given timestamp in time during the day. The ID of each station is given in the stations_list text file. For more information on the location (GPS, Highway, Direction) of each station please refer to the PEMS website. There are 963 (stations) x 144 (timestamps) = 138.672 attributes for each record.


Relevant Papers:

M. Cuturi, Fast Global Alignment Kernels, Proceedings of the Intern. Conference on Machine Learning 2011.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
from zipfile import ZipFile
import io
from urllib.request import urlopen
import pandas as pd

# ['PEMS_test', 'PEMS_testlabels', 'PEMS_train', 'PEMS_trainlabels', 'randperm', 'stations_list']
r = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/00204/PEMS-SF.zip")
r = r.read()
file = ZipFile(io.BytesIO(r))

df_train_x = pd.read_csv(file.open('PEMS_train')
, demlimiter='\s+'
, encoding='latin1'
)

df_train_y = pd.read_csv(file.open('PEMS_trainlabels')
, demlimiter='\s+'
, encoding='latin1'
)

df_test_x = pd.read_csv(file.open('PEMS_test')
, demlimiter='\s+'
, encoding='latin1'
)

df_test_y = pd.read_csv(file.open('PEMS_testlabels')
, demlimiter='\s+'
, encoding='latin1'
)

print(df_train_x.info())
print(df_train_y.info())
print(df_test_x.info())
print(df_test_y.info())
"""

#LOACL
from zipfile import ZipFile
import pandas as pd

# ['PEMS_test', 'PEMS_testlabels', 'PEMS_train', 'PEMS_trainlabels', 'randperm', 'stations_list']

file = ZipFile("../ics.uci.edu/ml/machine-learning-databases/00204/PEMS-SF.zip")

df_train_x = pd.read_csv(file.open('PEMS_train')
, demlimiter='\s+'
, encoding='latin1'
)

df_train_y = pd.read_csv(file.open('PEMS_trainlabels')
, demlimiter='\s+'
, encoding='latin1'
)

df_test_x = pd.read_csv(file.open('PEMS_test')
, demlimiter='\s+'
, encoding='latin1'
)

df_test_y = pd.read_csv(file.open('PEMS_testlabels')
, demlimiter='\s+'
, encoding='latin1'
)

print(df_train_x.info())
print(df_train_y.info())
print(df_test_x.info())
print(df_test_y.info())