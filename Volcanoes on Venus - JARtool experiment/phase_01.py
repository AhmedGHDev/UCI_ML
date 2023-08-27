import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: The JARtool project was a pioneering effort to develop an automatic system for cataloging small volcanoes in the large set of Venus images returned by the Magellan spacecraft.


Data Set Characteristics:  

Image

Number of Instances:

N/A

Area:

Physical

Attribute Characteristics:

N/A

Number of Attributes:

N/A

Date Donated

N/A

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

61644


Source:

Michael C. Burl
MS 126-347, JPL
4800 Oak Grove Drive
Pasadena, CA 91109
(818) 393-5345
Michael.C.Burl '@' jpl.nasa.gov
http://www-aig.jpl.nasa.gov/mls/home/burl/


Data Set Information:

The data was collected by the Magellan spacecraft over an approximately four year period from 1990--1994. The objective of the mission was to obtain global mapping of the surface of Venus using synthetic aperture radar (SAR). A more detailed discussion of the mission and objectives is available at JPL's Magellan webpage.

There are some spatial dependencies. For example, background patches from with in a single image are likely to be more similar than background patches taken across different images.

In addition to the images, there are "ground truth" files that specify the locations of volcanoes within the images. The quotes around "ground truth" are intended as a reminder that there is no absolute ground truth for this data set. No one has been to Venus and the image quality does not permit 100%, unambiguous identification of the volcanoes, even by human experts. There are labels that provide some measure of subjective uncertainty (1 = definitely a volcano, 2 = probably, 3 = possibly, 4 = only a pit is visible). See reference [Smyth95] for more information on the labeling uncertainty problem.

There are also files that specify the exact set of experiments using in the published evaluations of the JARtool system.

The image files are in a format called VIEW. This format consists of two files, a binary file with extension .sdt (the image data) and an ascii file with extension .spr (header information). There is a MATLAB utility function included in the data package that can be used to read the data. If you want to use something other than Matlab, you are on your own, but the format is fairly simple and can be understood by looking at the Matlab code.

The labeling files are provided in two forms. The .lxyr files are simple space-separated ascii containing label, x-location of center, y-location of center, and radius.


Attribute Information:

The images are 1024X1024 pixels. The pixel values are in the range [0,255]. The pixel value is related to the amount of energy backscattered to the radar from a given spatial location. Higher pixel values indicate greater backscatter. Lower pixel values indicate lesser backscatter. Both topography and surface roughness relative to the radar wavelength affect the amount of backscatter.


Relevant Papers:

G.H. Pettengill, P.G. Ford, W.T.K. Johnson, R.K. Raney, L.A. Soderblom, "Magellan: Radar Performance and Data Products", Science, 252:260-265 (1991).
[Web Link]

R.S. Saunders, A.J. Spear, P.C. Allin, R.S. Austin, A.L. Berman, R.C. Chandlee, J. Clark, A.V. Decharon, E.M. Dejong, "Magellan Mission Summary", J. of Geophysical Research Planets, 97(E8):13067-13090, (1992).
[Web Link]

M.C. Burl, L. Asker, P. Smyth, U. Fayyad, P. Perona, L. Crumpler, and J. Aubele, "Learning to Recognize Volcanoes on Venus", Machine Learning, (March 1998).
[Web Link]

P. Smyth, M.C. Burl, U.M. Fayyad, and P. Perona, Chapter: "Knowledge Discovery in Large Image Databases: Dealing with Uncertainties in Ground Truth", In Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, Menlo Park, CA, (1995).
[Web Link]



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""