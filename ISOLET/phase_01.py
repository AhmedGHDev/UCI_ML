import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: Goal: Predict which letter-name was spoken--a simple classification task.

Data Set Characteristics:  

Multivariate

Number of Instances:

7797

Area:

Computer

Attribute Characteristics:

Real

Number of Attributes:

617

Date Donated

1994-09-12

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

152839


Source:

Creators:

Ron Cole and Mark Fanty
Department of Computer Science and Engineering,
Oregon Graduate Institute, Beaverton, OR 97006.
cole '@' cse.ogi.edu, fanty '@' cse.ogi.edu

Donor:

Tom Dietterich
Department of Computer Science
Oregon State University, Corvallis, OR 97331
tgd '@' cs.orst.edu


Data Set Information:

This data set was generated as follows. 150 subjects spoke the name of each letter of the alphabet twice. Hence, we have 52 training examples from each speaker. The speakers are grouped into sets of 30 speakers each, and are referred to as isolet1, isolet2, isolet3, isolet4, and isolet5. The data appears in isolet1+2+3+4.data in sequential order, first the speakers from isolet1, then isolet2, and so on. The test set, isolet5, is a separate file.

You will note that 3 examples are missing. I believe they were dropped due to difficulties in recording.

I believe this is a good domain for a noisy, perceptual task. It is also a very good domain for testing the scaling abilities of algorithms. For example, C4.5 on this domain is slower than backpropagation!

I have formatted the data for C4.5 and provided a C4.5-style names file as well.


Attribute Information:

The features are described in the paper by Cole and Fanty cited above. The features include spectral coefficients; contour features, sonorant features, pre-sonorant features, and post-sonorant features. Exact order of appearance of the features is not known.


Relevant Papers:

Fanty, M., Cole, R. (1991). Spoken letter recognition. In Lippman, R. P., Moody, J., and Touretzky, D. S. (Eds). Advances in Neural Information Processing Systems 3. San Mateo, CA: Morgan Kaufmann.
[Web Link]

Dietterich, T. G., Bakiri, G. (1991) Error-correcting output codes: A general method for improving multiclass inductive learning programs. Proceedings of the Ninth National Conference on Artificial Intelligence (AAAI-91), Anaheim, CA: AAAI Press.
[Web Link]

Dietterich, T. G., Bakiri, G. (1994) Solving Multiclass Learning Problems via Error-Correcting Output Codes. Available as URL: [Web Link]
[Web Link]


Papers That Cite This Data Set1:


Jaakko Peltonen and Samuel Kaski. Discriminative Components of Data. IEEE. 2004. [View Context].

Vassilis Athitsos and Stan Sclaroff. Boosting Nearest Neighbor Classifiers for Multiclass Recognition. Boston University Computer Science Tech. Report No, 2004-006. 2004. [View Context].

David Littau and Daniel Boley. Using Low-Memory Representations to Cluster Very Large Data Sets. SDM. 2003. [View Context].

Inderjit S. Dhillon and Dharmendra S. Modha and W. Scott Spangler. Class visualization of high-dimensional data with applications. Department of Computer Sciences, University of Texas. 2002. [View Context].

Erin L. Allwein and Robert E. Schapire and Yoram Singer. Reducing Multiclass to Binary: A Unifying Approach for Margin Classifiers. ICML. 2000. [View Context].

Khaled A. Alsabti and Sanjay Ranka and Vineet Singh. CLOUDS: A Decision Tree Classifier for Large Datasets. KDD. 1998. [View Context].

Hiroshi Shimodaira and Jun Okui and Mitsuru Nakai. Modified Minimum Classification Error Learning and Its Application to Neural Networks. SSPR/SPR. 1998. [View Context].

Thomas G. Dietterich and Ghulum Bakiri. Solving Multiclass Learning Problems via Error-Correcting Output Codes. CoRR, csAI/9501101. 1995. [View Context].

Shlomo Dubnov and Ran El and Yaniv Technion and Yoram Gdalyahu and Elad Schneidman and Naftali Tishby and Golan Yona. Clustering By Friends : A New Nonparametric Pairwise Distance Based Clustering Algorithm. Ben Gurion University. [View Context].

Jakub Zavrel. An Empirical Re-Examination of Weighted Voting for k-NN. Computational Linguistics. [View Context].

Hiroshi Shimodaira and Jun Okui and Mitsuru Nakai. IMPROVING THE GENERALIZATION PERFORMANCE OF THE MCE/GPD LEARNING. School of Information Science Japan Advanced Institute of Science and Technology Tatsunokuchi, Ishikawa. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""