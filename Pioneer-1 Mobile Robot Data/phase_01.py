import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This dataset contains time series sensor readings of the Pioneer-1 mobile robot. The data is broken into "experiences" in which the robot takes action for some period of time and experiences a control

Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

N/A

Area:

Computer

Attribute Characteristics:

Categorical, Real

Number of Attributes:

N/A

Date Donated

1999-01-28

Associated Tasks:

N/A

Missing Values?

N/A

Number of Web Hits:

47616


Source:

Matthew D. Schmill, Paul R. Cohen
Experimental Knowledge Systems Laboratory
Department of Computer Science
Box 34610
University of Massachusetts, Amherst
Amherst, MA 01003-4610
schmill '@' cs.umass.edu, cohen '@' cs.umass.edu


Data Set Information:

The data were collected over a series of specifically designed trials. Our hope was to cover most of the types of sensory interactions that a Pioneer might be reasonably expected to encounter: things like passing by visible objects, pushing visible objects, crashing into walls, etc. Many of these interactions are repeated throughout the dataset.

This data was collected to serve as the basis for work in learning and conceptual development. Our first goal was to be able to have the robot cluster these experiences by their dynamics on their own into clusters of experiences with a common outcome.

Each data file contains time series data in which each row of data corresponds to a single observation of the sensor array. Included in each row are two additional variables, 'id' and 'description', which indicate the experience number that the observation belongs to, and a description of that experience, respectively. Observations within an experience are taken every 100ms.

The data is stored in three text files: one file for experiences in which the Pioneer was moving in a straight line, one in which it was turning in place, and one in which it was raising or lowering its gripper.

The description variable is a string of symbols. The string breaks down as follows:

"u" or "o" - unobstructed or obstructed
"x.xs" - activity lasted x.x seconds
activity - the activity and speed, if applicable, i.e. move100 = move forward at 100mm/sec
visual - objects in the visual array are listed in sequence. "cAHEAD" indicates an object visible to channel c directly AHEAD of the Pioneer.
[visual.X] - visual descriptions followed by a '.' and one character indicate that something special happens with the visible object. .V means the object Vanishes from sight during the activity. .D indicates that the object is Discovered (becomes visible) during the activity. .P indicates that the object is pushed.

An example: "u-3.5s-retr-100-aRIGHT.D" An unobstructed retreat (move) at -100 mm/sec for 3.5 seconds with an object being discovered in channel A.

It should be noted that, particularly with respect to the visual channels, the description may not be 100% accurate. Since the visual channels respond to colors that they are trained on (visual a=red, visual b=yellow, visual c=blue), it was possible, but infrequent, for some extraneous object in the environment generated a response in visual channels that were not supposed to show activity in a particular trial.

Rows are seperated by carriage returns, columns by commas.


Attribute Information:

TRIAL-ID : categorical, the trial id of the experience that the observation belongs to
DESCRIPTION : a symbolic description of the experience design
TIME-SECS : a reading of the Pioneer's internal clock, in seconds
BATTERY-LEVEL : a reading of battery level, in volts
SONAR-0 : sonar depth reading, in mm, of the left (90) pointing sonar
SONAR-1 : sonar depth reading, in mm, of a (15) pointing sonar
SONAR-2 : sonar depth reading, in mm, of a (7.5) pointing sonar
SONAR-3 : sonar depth reading, in mm, of a forward (0) pointing sonar
SONAR-4 : sonar depth reading, in mm, of a (-7.5) pointing sonar
SONAR-5 : sonar depth reading, in mm, of a (-15) pointing sonar
SONAR-6 : sonar depth reading, in mm, of a right (-90) pointing sonar
HEADING : heading reading, in degrees, from the robot's "true north"
R-WHEEL-VEL : right wheel velocity, in mm/sec
L-WHEEL-VEL : left wheel velocity, in mm/sec
TRANS-VEL : translational velocity, mm/sec
ROT-VEL : rotational velocity, mm/sec
R-STALL : right wheel stall sensor, binary (0/1)
L-STALL : left wheel stall sensor, binary (0/1)
ROBOT-STATUS : robot status, 2.0 = stationary, 3.0 = moving
GRIP-STATE : gripper state
GRIP-FRONT-BEAM : gripper break beam, binary, 1.0 = broken
GRIP-REAR-BEAM : gripper break beam, binary, 1.0 = broken
GRIP-BUMPER : gripper bumper, binary, 1.0 = in contact
VIS-A-AREA : area of dominant visible object for channel A, in pixels
VIS-A-X : X location of object in channel A on image plane, -140 ... 140
VIS-A-Y : Y location of channel A on image plane
VIS-A-H : height of object in channel A on plane, in pixels
VIS-A-W : width of object in A on image plane, in pixels
VIS-A-DIST : distance to object in channel A, in mm
VIS-B-AREA : area of dominant visible object for channel B, in pixels
VIS-B-X : X location of object in channel B on image plane, -140 ... 140
VIS-B-Y : Y location of channel B on image plane
VIS-B-H : height of object in channel B on plane, in pixels
VIS-B-W : width of object in B on image plane, in pixels
VIS-B-DIST : distance to object in channel B, in mm
VIS-C-AREA : area of dominant visible object for channel C, in pixels
VIS-C-X : X location of object in channel C on image plane, -140 ... 140
VIS-C-Y : Y location of channel C on image plane
VIS-C-H : height of object in C on image plane, in pixels
VIS-C-W : width of object in C on image plane, in pixels
VIS-C-DIST : distance to object in channel C, in mm

For the visual variables, when there is no visible object, width = 0, height = 0, area = 0, distance = 10000.0, Y = 0, X = 140.0. The sonars report 5201.0 as their maximum distance.


Relevant Papers:

Oates, Tim; Schmill, Matthew D. and Cohen, Paul R. Identifying Qualitatively Different Experiences: Experiments with a Mobile Robot.
[Web Link]

Schmill, Matthew D.; Oates, Tim; and Cohen, Paul R. Learned Models for Continuous Planning. Seventh International Workshop on Artificial Intelligence and Statistics.
[Web Link]



Citation Request:

The work represented here was funded by DARPA contracts F49620-97-1-0485 and N66001-96-C-8504.

For research use only.
"""