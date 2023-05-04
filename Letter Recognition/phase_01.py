import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Database of character image features; try to identify the letter

Data Set Characteristics:  

Multivariate

Number of Instances:

20000

Area:

Computer

Attribute Characteristics:

Integer

Number of Attributes:

16

Date Donated

1991-01-01

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

490115


Source:

Creator:

David J. Slate
Odesta Corporation; 1890 Maple Ave; Suite 115; Evanston, IL 60201

Donor:

David J. Slate (dave '@' math.nwu.edu) (708) 491-3867


Data Set Information:

The objective is to identify each of a large number of black-and-white rectangular pixel displays as one of the 26 capital letters in the English alphabet. The character images were based on 20 different fonts and each letter within these 20 fonts was randomly distorted to produce a file of 20,000 unique stimuli. Each stimulus was converted into 16 primitive numerical attributes (statistical moments and edge counts) which were then scaled to fit into a range of integer values from 0 through 15. We typically train on the first 16000 items and then use the resulting model to predict the letter category for the remaining 4000. See the article cited above for more details.


Attribute Information:

1. lettr capital letter (26 values from A to Z)
2. x-box horizontal position of box (integer)
3. y-box vertical position of box (integer)
4. width width of box (integer)
5. high height of box (integer)
6. onpix total # on pixels (integer)
7. x-bar mean x of on pixels in box (integer)
8. y-bar mean y of on pixels in box (integer)
9. x2bar mean x variance (integer)
10. y2bar mean y variance (integer)
11. xybar mean x y correlation (integer)
12. x2ybr mean of x * x * y (integer)
13. xy2br mean of x * y * y (integer)
14. x-ege mean edge count left to right (integer)
15. xegvy correlation of x-ege with y (integer)
16. y-ege mean edge count bottom to top (integer)
17. yegvx correlation of y-ege with x (integer)


Relevant Papers:

P. W. Frey and D. J. Slate. "Letter Recognition Using Holland-style Adaptive Classifiers". (Machine Learning Vol 6 #2 March 91)
[Web Link]


Papers That Cite This Data Set1:


Jaakko Peltonen and Arto Klami and Samuel Kaski. Improved Learning of Riemannian Metrics for Exploratory Analysis. Improved Learning of Riemannian Metrics for Exploratory Analysis. Neural Networks. 2004. [View Context].

Xiaoli Z. Fern and Carla Brodley. Cluster Ensembles for High Dimensional Clustering: An Empirical Study. Journal of Machine Learning Research n, a. 2004. [View Context].

Giorgio Valentini. Ensemble methods based on bias--variance analysis Theses Series DISI-TH-2003. Dipartimento di Informatica e Scienze dell'Informazione . 2003. [View Context].

Dmitry Pavlov and Alexandrin Popescul and David M. Pennock and Lyle H. Ungar. Mixtures of Conditional Maximum Entropy Models. ICML. 2003. [View Context].

Kristin P. Bennett and Ayhan Demiriz and Richard Maclin. Exploiting unlabeled data in ensemble methods. KDD. 2002. [View Context].

Stephen D. Bay. Nearest neighbor classification from multiple feature subsets. Intell. Data Anal, 3. 1999. [View Context].

Thomas G. Dietterich. Approximate Statistical Test For Comparing Supervised Classification Learning Algorithms. Neural Computation, 10. 1998. [View Context].

Thomas G. Dietterich and Ghulum Bakiri. Solving Multiclass Learning Problems via Error-Correcting Output Codes. CoRR, csAI/9501101. 1995. [View Context].

Georgios Paliouras and David S. Brée. The Effect of Numeric Features on the Scalability of Inductive Learning Programs. ECML. 1995. [View Context].

Miguel Moreira and Alain Hertz and Eddy Mayoraz. Data binarization by discriminant elimination. Proceedings of the ICML-99 Workshop: From Machine Learning to. [View Context].

Arto Klami and Samuel Kaski and Ty n ohjaaja and Janne Sinkkonen. HELSINKI UNIVERSITY OF TECHNOLOGY Department of Engineering Physics and Mathematics Arto Klami Regularized Discriminative Clustering. Regularized Discriminative Clustering. [View Context].

Shailesh Kumar and Melba Crawford and Joydeep Ghosh. A versatile framework for labelling imagery with a large number of classes. Department of Electrical and Computer Engineering. [View Context].

Amund Tveit. Empirical Comparison of Accuracy and Performance for the MIPSVM classifier with Existing Classifiers. Division of Intelligent Systems Department of Computer and Information Science, Norwegian University of Science and Technology. [View Context].

Hirotaka Inoue and Hiroyuki Narihisa. Incremental Learning with Self-Organizing Neural Grove. Department of Electrical Engineering and Information Science, Kure National College of Technology. [View Context].

Jaakko Peltonen and Arto Klami and Samuel Kaski. Learning Metrics for Information Visualization. Neural Networks Research Centre Helsinki University of Technology. [View Context].

Adil M. Bagirov and Julien Ugon. An algorithm for computation of piecewise linear function separating two sets. CIAO, School of Information Technology and Mathematical Sciences, The University of Ballarat. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data", names=['lettr_capital_letter', 'x-box_horizontal_position_of_box', 'y-box_vertical_position_of_box', 'width_width_of_box', 'high_height_of_box', 'onpix_total_#_on_pixels', 'x-bar_mean_x_of_on_pixels_in_box', 'y-bar_mean_y_of_on_pixels_in_box', 'x2bar_mean_x_variance', 'y2bar_mean_y_variance', 'xybar_mean_x_y_correlation', 'x2ybr_mean_of_x_*_x_*_y', 'xy2br_mean_of_x_*_y_*_y', 'x-ege_mean_edge_count_left_to_right', 'xegvy_correlation_of_x-ege_with_y', 'y-ege_mean_edge_count_bottom_to_top', 'yegvx_correlation_of_y-ege_with_x'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/letter-recognition/letter-recognition.data", names=['lettr_capital_letter', 'x-box_horizontal_position_of_box', 'y-box_vertical_position_of_box', 'width_width_of_box', 'high_height_of_box', 'onpix_total_#_on_pixels', 'x-bar_mean_x_of_on_pixels_in_box', 'y-bar_mean_y_of_on_pixels_in_box', 'x2bar_mean_x_variance', 'y2bar_mean_y_variance', 'xybar_mean_x_y_correlation', 'x2ybr_mean_of_x_*_x_*_y', 'xy2br_mean_of_x_*_y_*_y', 'x-ege_mean_edge_count_left_to_right', 'xegvy_correlation_of_x-ege_with_y', 'y-ege_mean_edge_count_bottom_to_top', 'yegvx_correlation_of_y-ege_with_x'])

print(df.info())