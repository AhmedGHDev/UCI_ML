import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data arises from a large study to examine EEG correlates of genetic predisposition to alcoholism. It contains measurements from 64 electrodes placed on the scalp sampled at 256 Hz


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

122

Area:

Life

Attribute Characteristics:

Categorical, Integer, Real

Number of Attributes:

4

Date Donated

1999-10-13

Associated Tasks:

N/A

Missing Values?

Yes

Number of Web Hits:

289955


Source:

Original Owner:

Henri Begleiter
Neurodynamics Laboratory,
State University of New York Health Center
Brooklyn, New York

Donor:

Lester Ingber
POB 06440 Sears Tower
Chicago, IL 60606
ingber '@' ingber.com
http://www.ingber.com/



Data Set Information:

This data arises from a large study to examine EEG correlates of genetic predisposition to alcoholism. It contains measurements from 64 electrodes placed on subject's scalps which were sampled at 256 Hz (3.9-msec epoch) for 1 second.

There were two groups of subjects: alcoholic and control. Each subject was exposed to either a single stimulus (S1) or to two stimuli (S1 and S2) which were pictures of objects chosen from the 1980 Snodgrass and Vanderwart picture set. When two stimuli were shown, they were presented in either a matched condition where S1 was identical to S2 or in a non-matched condition where S1 differed from S2.

Shown here are example plots of a control ([Web Link]) and alcoholic ([Web Link]) subject. The plots indicate voltage, time, and channel and are averaged over 10 trials for the single stimulus condition.

There were 122 subjects and each subject completed 120 trials where different stimuli were shown. The electrode positions were located at standard sites (Standard Electrode Position Nomenclature, American Electroencephalographic Association 1990). Zhang et al. (1995) describes in detail the data collection process.

There are three versions of the EEG data set.

1. The Small Data Set
The small data set (smni97_eeg_data.tar.gz) contains data for the 2 subjects, alcoholic a_co2a0000364 and control c_co2c0000337. For each of the 3 matching paradigms, c_1 (one presentation only), c_m (match to previous presentation) and c_n (no-match to previous presentation), 10 runs are shown.

2. The Large Data Set
The large data set (SMNI_CMI_TRAIN.tar.gz and SMNI_CMI_TEST.tar.gz) contains data for 10 alcoholic and 10 control subjects, with 10 runs per subject per paradigm. The test data used the same 10 alcoholic and 10 control subjects as with the training data, but with 10 out-of-sample runs per subject per paradigm.

3. The Full Data Set
This data set contains all 120 trials for 122 subjects. The entire set of data is about 700 MBytes.

NOTE: There are 17 trials with empty files in co2c1000367. Some trials have "err" notices, e.g., search/grep for "err" and see "S2 match err" or "S2 nomatch err" etc.


Attribute Information:

Each trial is stored in its own file and will appear in the following format.

# co2a0000364.rd
# 120 trials, 64 chans, 416 samples 368 post_stim samples
# 3.906000 msecs uV
# S1 obj , trial 0
# FP1 chan 0
0 FP1 0 -8.921
0 FP1 1 -8.433
0 FP1 2 -2.574
0 FP1 3 5.239
0 FP1 4 11.587
0 FP1 5 14.028
...

The first four lines are header information. Line 1 contains the subject identifier and indicates if the subject was an alcholic (a) or control (c) subject by the fourth letter. Line 4 identifies the matching conditions: a single object shown (S1 obj), object 2 shown in a matching condition (S2 match), and object 2 shown in a non matching condition (S2 nomatch).

Line 5 identifies the start of the data from sensor FP1. The four columns of data are: the trial number, sensor position, sample number (0-255), and sensor value (in micro volts).



Relevant Papers:

X.L. Zhang, H. Begleiter, B. Porjesz, W. Wang, and A. Litke. (1995). "Event related potentials during object recognition tasks". Brain Research Bulletin. Volume 38. Number 6. Pages 531-538.
[Web Link]

L. Ingber. (1997). Statistical mechanics of neocortical interactions: Canonical momenta indicators of electroencephalography. Physical Review E. Volume 55. Number 4. Pages 4578-4593.
[Web Link]

L. Ingber. (1998). Statistical mechanics of neocortical interactions: Training and testing canonical momenta indicators of EEG. Mathematical Computer Modelling. Volume 27. Number 3. Pages 33-64.
[Web Link]

J. G. Snodgrss and M. Vanderwart. (1980). "A standardized set of 260 pictures: norms for the naming agreement, familiarity, and visual complexity." Journal of Experimental Psychology: Human Learning and Memory. Volume 6. Pages 174-215.
[Web Link]


Papers That Cite This Data Set1:


Peter Sykacek and Stephen J. Roberts. Adaptive Classification by Variational Kalman Filtering. NIPS. 2002. [View Context].

Stephen D. Bay and Dennis F. Kibler and Michael J. Pazzani and Padhraic Smyth. The UCI KDD Archive of Large Data Sets for Data Mining Research and Experimentation. SIGKDD Explorations, 2. 2000. [View Context].



Citation Request:

There are no usage restrictions on this data.

Acknowledgments for this data should made to Henri Begleiter at the Neurodynamics Laboratory at the State University of New York Health Center at Brooklyn.

Plots are courtesy of Roger Gabriel.
"""