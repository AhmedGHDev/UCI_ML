import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: This data consists of 640 black and white face images of people taken with varying pose (straight, left, right, up), expression (neutral, happy, sad, angry), eyes (wearing sunglasses or not), and size


Data Set Characteristics:  

Image

Number of Instances:

640

Area:

N/A

Attribute Characteristics:

Integer

Number of Attributes:

N/A

Date Donated

1999-06-24

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

178080


Source:

Original Owner and Donor:

Tom Mitchell
School of Computer Science
Carnegie Mellon University
tom.mitchell '@' cmu.edu
http://www.cs.cmu.edu/~tom/


Data Set Information:

Each image can be characterized by the pose, expression, eyes, and size. There are 32 images for each person capturing every combination of features.

To view the images, you can use the program xv.

The image data can be found in /faces. This directory contains 20 subdirectories, one for each person, named by userid. Each of these directories contains several different face images of the same person.

You will be interested in the images with the following naming convention:

.pgm
is the user id of the person in the image, and this field has 20 values: an2i, at33, boland, bpm, ch4f, cheyer, choon, danieln, glickman, karyadi, kawamura, kk49, megak, mitchell, night, phoebe, saavik, steffi, sz24, and tammo.
is the head position of the person, and this field has 4 values: straight, left, right, up.
is the facial expression of the person, and this field has 4 values: neutral, happy, sad, angry.
is the eye state of the person, and this field has 2 values: open, sunglasses.
is the scale of the image, and this field has 3 values: 1, 2, and 4. 1 indicates a full-resolution image (128 columns by 120 rows); 2 indicates a half-resolution image (64 by 60); 4 indicates a quarter-resolution image (32 by 30).
If you've been looking closely in the image directories, you may notice that some images have a .bad suffix rather than the .pgm suffix. As it turns out, 16 of the 640 images taken have glitches due to problems with the camera setup; these are the .bad images. Some people had more glitches than others, but everyone who got ``faced'' should have at least 28 good face images (out of the 32 variations possible, discounting scale).

More information and C code for loading the images is available here: [Web Link].


Attribute Information:

N/A


Relevant Papers:

T. Mitchell. Machine Learning, McGraw Hill, 1997.



Papers That Cite This Data Set1:


Xiaofeng He and Partha Niyogi. Locality Preserving Projections. NIPS. 2003. [View Context].

Marina Meila and Michael I. Jordan. Learning with Mixtures of Trees. Journal of Machine Learning Research, 1. 2000. [View Context].



Citation Request:

You may use this material free of charge for any educational purpose, provided attribution is given in any lectures or publications that make use of this material.
"""