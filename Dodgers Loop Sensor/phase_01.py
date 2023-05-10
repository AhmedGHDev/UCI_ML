import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Loop sensor data was collected for the Glendale on ramp for the 101 North freeway in Los Angeles


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

50400

Area:

N/A

Attribute Characteristics:

Categorical, Integer

Number of Attributes:

3

Date Donated

2006-12-01

Associated Tasks:

N/A

Missing Values?

Yes

Number of Web Hits:

89924


Source:

Creator and Maintainer:
Jon Hutchins
UCI
johutchi '@' uci.edu

Donor: PeMS


Data Set Information:

This loop sensor data was collected for the Glendale on ramp for the 101 North freeway in Los Angeles. It is close enough to the stadium to see unusual traffic after a Dodgers game, but not so close and heavily used by game traffic so that the signal for the extra traffic is overly obvious.

NOTE: This is an on ramp near the stadium so event traffic BEGINS at or near the END of the event time.

The observations were taken over 25 weeks, 288 time slices per day (5 minute count aggregates).

The goal is to predict the presence of a baseball game at Dodgers stadium


Attribute Information:

1. Date: MM/DD/YY
2. Time: (H)H:MM (military time)
3. Count: Number of cars measured for the previous five minutes
Rows: Each five minute time slice is represented by one row

For .events file:
1. Date: MM/DD/YY
2. Begin event time: HH:MM:SS (military)
3. End event time: HH:MM:SS (military)
4. Game attendance
5. Away team
6. W/L score


Relevant Papers:

"Adaptive event detection with time-varying Poisson processes"
A. Ihler, J. Hutchins, and P. Smyth
Proceedings of the 12th ACM SIGKDD Conference (KDD-06), August 2006.



Citation Request:

These loop sensor measurements were obtained from the Freeway Performance Measurement System (PeMS), "[Web Link]" Please include this citation if you plan to use this database.
"""

#FROM URL
"""
df_data  = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/Dodgers.data"
,names=['Date_Time', 'Count']
)

df_events = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/event-detection/Dodgers.events"
,encoding = 'unicode_escape'
,names=['Date', 'Begin_event_time', 'End_event_time', 'Game_attendance', 'Away_team', 'W/L score']
)

print(df_data.info())
print(df_events.info())
"""

#LOACL
df_data  = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/event-detection/Dodgers.data"
,names=['Date_Time', 'Count']
)

df_events = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/event-detection/Dodgers.events"
,encoding = 'unicode_escape'
,names=['Date', 'Begin_event_time', 'End_event_time', 'Game_attendance', 'Away_team', 'W/L score']
)

print(df_data.info())
print(df_events.info())