import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The data were collected as the SCITOS G5 robot navigates through the room following the wall in a clockwise direction, for 4 rounds, using 24 ultrasound sensors arranged circularly around its 'waist'.

Data Set Characteristics:  

Multivariate, Sequential

Number of Instances:

5456

Area:

Computer

Attribute Characteristics:

Real

Number of Attributes:

24

Date Donated

2010-08-04

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

77879


Source:

(a) Creators: Ananda Freire, Marcus Veloso and Guilherme Barreto

Department of Teleinformatics Engineering

Federal University of CearÃ¡
Fortaleza, CearÃ¡, Brazil



(b) Donors of database: Ananda Freire (anandalf '@' gmail.com)
Guilherme Barreto (guilherme '@' deti.ufc.br)


Data Set Information:

The provided files comprise three different data sets. The first one contains the raw values of the measurements
of all 24 ultrasound sensors and the corresponding class label (see Section 7). Sensor readings are sampled at a
rate of 9 samples per second.

The second one contains four sensor readings named 'simplified distances' and the corresponding class label (see Section 7). These simplified distances are referred to as the 'front distance', 'left distance', 'right distance' and 'back distance'. They consist, respectively, of the minimum sensor readings among those within 60 degree arcs located at the front, left, right and back parts of the robot.

The third one contains only the front and left simplified distances and the corresponding class label.

It is worth mentioning that the 24 ultrasound readings and the simplified distances were collected at the same time step, so each file has the same number of rows (one for each sampling time step).

The wall-following task and data gathering were designed to test the hypothesis that this apparently simple navigation task is indeed a non-linearly separable classification task. Thus, linear classifiers, such as the Perceptron network, are not able to learn the task and command the robot around the room without collisions. Nonlinear neural classifiers, such as the MLP network, are able to learn the task and command the robot successfully without collisions.

If some kind of short-term memory mechanism is provided to the neural classifiers, their performances are improved in general. For example, if past inputs are provided together with current sensor readings, even the Perceptron becomes able to learn the task and command the robot succesfully. If a recurrent neural network, such as the Elman network, is used to learn the task, the resulting dynamical classifier is able to learn the task using less hidden neurons than the MLP network.

Files with different number of sensor readings were built in order to evaluate the performance of the classifiers with respect to the number of inputs.


Attribute Information:

Number of Attributes
-- sensor_readings_24.data: 24 numeric attributes and the class.
-- sensor_readings_4.data: 4 numeric attributes and the class.
-- sensor_readings_2.data: 2 numeric attributes and the class.



For Each Attribute:
-- File sensor_readings_24.data:
1. US1: ultrasound sensor at the front of the robot (reference angle: 180Â°) - (numeric: real)
2. US2: ultrasound reading (reference angle: -165Â°) - (numeric: real)
3. US3: ultrasound reading (reference angle: -150Â°) - (numeric: real)
4. US4: ultrasound reading (reference angle: -135Â°) - (numeric: real)
5. US5: ultrasound reading (reference angle: -120Â°) - (numeric: real)
6. US6: ultrasound reading (reference angle: -105Â°) - (numeric: real)
7. US7: ultrasound reading (reference angle: -90Â°) - (numeric: real)
8. US8: ultrasound reading (reference angle: -75Â°) - (numeric: real)
9. US9: ultrasound reading (reference angle: -60Â°) - (numeric: real)
10. US10: ultrasound reading (reference angle: -45Â°) - (numeric: real)
11. US11: ultrasound reading (reference angle: -30Â°) - (numeric: real)
12. US12: ultrasound reading (reference angle: -15Â°) - (numeric: real)
13. US13: reading of ultrasound sensor situated at the back of the robot (reference angle: 0Â°) - (numeric: real)
14. US14: ultrasound reading (reference angle: 15Â°) - (numeric: real)
15. US15: ultrasound reading (reference angle: 30Â°) - (numeric: real)
16. US16: ultrasound reading (reference angle: 45Â°) - (numeric: real)
17. US17: ultrasound reading (reference angle: 60Â°) - (numeric: real)
18. US18: ultrasound reading (reference angle: 75Â°) - (numeric: real)
19. US19: ultrasound reading (reference angle: 90Â°) - (numeric: real)
20. US20: ultrasound reading (reference angle: 105Â°) - (numeric: real)
21. US21: ultrasound reading (reference angle: 120Â°) - (numeric: real)
22. US22: ultrasound reading (reference angle: 135Â°) - (numeric: real)
23. US23: ultrasound reading (reference angle: 150Â°) - (numeric: real)
24. US24: ultrasound reading (reference angle: 165Â°) - (numeric: real)
25. Class:
-- Move-Forward
-- Slight-Right-Turn
-- Sharp-Right-Turn
-- Slight-Left-Turn

-- File sensor_readings_4.data:
1. SD_front: minimum sensor reading within a 60 degree arc located at the front of the robot - (numeric: real)
2. SD_left: minimum sensor reading within a 60 degree arc located at the left of the robot - (numeric: real)
3. SD_right: minimum sensor reading within a 60 degree arc located at the right of the robot - (numeric: real)
4. SD_back: minimum sensor reading within a 60 degree arc located at the back of the robot - (numeric: real)
5. Class:
-- Move-Forward
-- Slight-Right-Turn
-- Sharp-Right-Turn
-- Slight-Left-Turn

-- File sensor_readings_2.data:
1. SD_front: minimum sensor reading within a 60 degree arc located at the front of the robot - (numeric: real)
2. SD_left: minimum sensor reading within a 60 degree arc located at the left of the robot - (numeric: real)
3. Class:
-- Move-Forward
-- Slight-Right-Turn
-- Sharp-Right-Turn
-- Slight-Left-Turn


Relevant Papers:

Ananda L. Freire, Guilherme A. Barreto, Marcus Veloso and Antonio T. Varela (2009),
'Short-Term Memory Mechanisms in Neural Network Learning of Robot Navigation
Tasks: A Case Study'. Proceedings of the 6th Latin American Robotics Symposium (LARS'2009),
ValparaÃ­so-Chile, pages 1-6, DOI: 10.1109/LARS.2009.5418323



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
from zipfile import ZipFile
import requests, zipfile, io
zip_file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00194/AllData.zip'
r = requests.get(zip_file_url)
zip_file = zipfile.ZipFile(io.BytesIO(r.content))

df_2 = pd.read_csv(zip_file.open("sensor_readings_2.data"), names=['SD_front', 'SD_left', 'Class'])
df_4 = pd.read_csv(zip_file.open("sensor_readings_4.data"), names=['SD_front', 'SD_left', 'SD_right', 'SD_back', 'Class'])
df_24 = pd.read_csv(zip_file.open("sensor_readings_24.data"), names=['US1', 'US2', 'US3', 'US4', 'US5', 'US6', 'US7', 'US8', 'US9', 'US10', 'US11', 'US12', 'US13', 'US14', 'US15', 'US16', 'US17', 'US18', 'US19', 'US20', 'US21', 'US22', 'US23', 'US24', 'Class'])

print(df_2.info())
print(df_4.info())
print(df_24.info())
"""

#LOACL
from zipfile import ZipFile
import zipfile
zip_file = zipfile.ZipFile('../ics.uci.edu/ml/machine-learning-databases/00194/AllData.zip')

df_2 = pd.read_csv(zip_file.open("sensor_readings_2.data"), names=['SD_front', 'SD_left', 'Class'])
df_4 = pd.read_csv(zip_file.open("sensor_readings_4.data"), names=['SD_front', 'SD_left', 'SD_right', 'SD_back', 'Class'])
df_24 = pd.read_csv(zip_file.open("sensor_readings_24.data"), names=['US1', 'US2', 'US3', 'US4', 'US5', 'US6', 'US7', 'US8', 'US9', 'US10', 'US11', 'US12', 'US13', 'US14', 'US15', 'US16', 'US17', 'US18', 'US19', 'US20', 'US21', 'US22', 'US23', 'US24', 'Class'])

print(df_2.info())
print(df_4.info())
print(df_24.info())