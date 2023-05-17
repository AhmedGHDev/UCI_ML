import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The Physical Action Data Set includes 10 normal and 10 aggressive physical actions that measure the human activity. The data have been collected by 10 subjects using the Vicon 3D tracker.

Data Set Characteristics:  

Time-Series

Number of Instances:

3000

Area:

Physical

Attribute Characteristics:

Real

Number of Attributes:

27

Date Donated

2011-07-27

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

63648


Source:

Theo Theodoridis
School of Computer Science and Electronic Engineering
University of Essex
Wivenhoe Park, Colchester, CO4 3SQ, UK
ttheod '@' gmail.com
http://sites.google.com/site/ttheod/


Data Set Information:

1. Protocol:
Seven male and three female subjects (age 25 to 30), who have experienced aggression in scenarios such
as physical fighting, took part in the experiment. Throughout 20 individual experiments, each subject
had to perform ten normal and ten aggressive activities. Regarding the rights of the subjects involved,
ethical regulations have been followed based on the code of ethics of the British psychological society,
which explains the ethical legislations to conduct statistical experiments using human subjects. For safety
precaution issues, boxing hand wraps have been given to the subjects, and for the warm up the subjects
were instructed to familiarise with the bag by having a number of trial runs. The subjects were aware that
since their involvement in this series of experiments was voluntary, it was made clear that they could
withdraw at any time from the study.

2. Instrumentation:
The Essex robotic arena was the main experimental hall where the data collection took place. With area
4x5.5m, the ten subjects expressed normal and aggressive physical activities at random locations. For the
normal actions, a human partner has been used as a focus target attracting the attention from the subjects
so as to perform more realistic activity. For the aggressive actions, the subjects made use of a professional
kick-boxing standing bag, 1.75m tall, with a human figure drawn on its body. The bag has cylindrical shape
made from soft material, which could bounce when hit. All the activities have been recorded from random
starting positions so that to have a variety of spatial 3D data. The subjectsâ€™ performance has been recorded
by the Viconâ€™s nine ubiquitous cameras, interfacing human activity with spatial coordinate points. Based on
this context, the data acquisition process involved four reflectable markers placed on the forearms (elbows
and wrists), four on the forelegs (knees and ankles), and one on the top of the head.

3. Data Setup:
Each experimental trial has been taken separately for each physical activity. The duration of each action
was approximately ~10 seconds per subject, which corresponds to a time series of ~3000 samples, with
sampling frequency of 200Hz. Within this performance time, approximately 15 action trajectories were
extracted counting in average 15 normal (ex: handshaking), and 15 aggressive (ex: punching) actions.


Attribute Information:

Each file in the dataset contains in overall 28 columns (the 1st is a counter), and is organised as follows:

+---------+-------+---------------+---------------------+---------------------+---------------------+
| Segment | Head | L-Arm | R-Arm | L-Leg | R-Leg |
+---------+-------+-------+-------+----------+----------+----------+----------+----------+----------+
| Marker | m1 | m2 | m3 | m4 | m5 | m6 | m7 | m8 | m9 |
| Coords | x y z | x y z | x y z | x y z | x y z | x y z | x y z | x y z | x y z |
| Column | 1,2,3 | 4,5,6 | 7,8,9 | 10,11,12 | 13,14,15 | 16,17,18 | 19,20,21 | 22,23,24 | 25,26,27 |
+---------+-------+-------+-------+----------+----------+----------+----------+----------+----------+

Segment: A segment defines a body segment or limb.
- Head
- Left arm (L-Arm)
- Right arm (R-Arm)
- Left leg (L-Leg)
- Right leg (R-Leg)

Marker: A pair of markers (except the head) is attached at each body segment for 3D data acquisition.
- Arm markers: wrist (WRS), elbow (ELB)
- Leg markers: ankle (ANK), knee (KNE)

Coords: The 3 coordinates (x,y,z) define the 3D position of each marker in space.
- x: The x coordinate
- y: The y coordinate
- z: The z coordinate


Relevant Papers:

1. T. Theodoridis and H. Hu, Classifying Aggressive Actions of 3D Human Models Using
Dynamic ANNs for Mobile Robot Surveillance, IEEE International Conference on Robotics
and Biomimetics (Robio-2007), Dec. 15-18, 2007, pp. 371-376.

2. T. Theodoridis, A. Agapitos, H. Hu, and S. M. Lucas, Ubiquitous Robotics in Physical
Human Action Recognition: A Comparison Between Dynamic ANNs and GP, IEEE International
Conference on Robotics and Automation (ICRA-2008), May 19-23, 2008, pp. 3064-3069.

3. T. Theodoridis and H. Hu, A Fuzzy-Convolution Model for Physical Action and Behaviour
Pattern Recognition of 3D Time Series, IEEE Int. Conference on Robotics and Biomimetics
(Robio-2008), Feb. 21-26, 2009, pp. 407-412.

4. T. Theodoridis, A. Agapitos, H. Hu, and S. M. Lucas, Mechanical Feature Attributes for
Modeling and Pattern Classification of Physical Activities, IEEE International Conference
in Information and Automation (ICIA-2009), June 22-24, 2009, pp. 528-533.

5. T. Theodoridis, A. Agapitos, H. Hu, and S. M. Lucas, A QA-TSK Fuzzy Model versus Evolutionary
Decision Trees Towards Nonlinear Action Pattern Recognition, IEEE International Conference in
Information and Automation (ICIA-2010), June 20-23, 2010, pp. 1813-1818.

6. T. Theodoridis, P. Theodorakopoulos, and H. Hu, Evolving Aggressive Biomechanical Models with
Genetic Programming, IEEE/RSJ International Conference on Intelligent Robots and Systems,
(IROS-2010), Oct. 18-22, 2010, pp. 2495-2500.

7. T. Theodoridis, A. Agapitos, and H. Hu, A Gaussian Groundplan Projection Area Model for
Evolving Probabilistic Classifiers, GECCO Genetic and Evolutionary Computation Conference
(GECCO-2011), Jul. 12-16, 2011, pp. 1339-1346.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""