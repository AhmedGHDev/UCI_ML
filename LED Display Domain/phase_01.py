import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: From Classification and Regression Trees book; We provide here 2 C programs for generating sample databases

Data Set Characteristics:  

Multivariate, Data-Generator

Number of Instances:

N/A

Area:

Computer

Attribute Characteristics:

Categorical

Number of Attributes:

7

Date Donated

1988-11-10

Associated Tasks:

Classification

Missing Values?

No

Number of Web Hits:

86026


Source:

Original Source:

Breiman,L., Friedman,J.H., Olshen,R.A., & Stone,C.J. (1984).
Classification and Regression Trees. Wadsworth International Group: Belmont, California. (see pages 43-49).

Donor:

David Aha


Data Set Information:

This simple domain contains 7 Boolean attributes and 10 concepts, the set of decimal digits. Recall that LED displays contain 7 light-emitting diodes -- hence the reason for 7 attributes. The problem would be easy if not for the introduction of noise. In this case, each attribute value has the 10% probability of having its value inverted.

It's valuable to know the optimal Bayes rate for these databases. In this case, the misclassification rate is 26% (74% classification accuracy).


Attribute Information:

-- All attribute values are either 0 or 1, according to whether the corresponding light is on or not for the decimal digit.
-- Each attribute (excluding the class attribute, which is an integer ranging between 0 and 9 inclusive) has a 10% percent chance of being inverted.


Relevant Papers:

Breiman,L., Friedman,J.H., Olshen,R.A., & Stone,C.J. Classification and Regression Trees. Wadsworth International Group: Belmont, California. 1984. (see pages 43-49).
[Web Link]

Quinlan,J.R. (1987). Simplifying Decision Trees. In International Journal of Man-Machine Studies.
[Web Link]

Tan,M. & Eshelman,L. (1988). Using Weighted Networks to Represent Classification Knowledge in Noisy Domains. In Proceedings of the 5th International Conference on Machine Learning, 121-134, Ann Arbor, Michigan: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Joao Gama and Ricardo Rocha and Pedro Medas. Accurate decision trees for mining high-speed data streams. KDD. 2003. [View Context].

Tim Leunig and D. Stott Parker. Empirical comparisons of various voting methods in bagging. KDD. 2003. [View Context].

Xavier Llor and David E. Goldberg and Ivan Traus and Ester Bernad i Mansilla. Accuracy, Parsimony, and Generality in Evolutionary Learning Systems via Multiobjective Selection. IWLCS. 2002. [View Context].

Xavier Llor and David E. Goldberg. Minimal Achievable Error in the LED. Illinois Genetic Algorithms Laboratory University of Illinois at Urbana-Champaign. 2002. [View Context].

Huan Liu and Rudy Setiono. Incremental Feature Selection. Appl. Intell, 9. 1998. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Ramon Sangesa and Ulises Cortes. Possibilistic Conditional Dependency, Similarity and Information Measures: an application to causal network recovery. Departament de Llenguatges i Sistemes Informtics Departament de Llenguatges i Sistemes Informtics Technical University of Catalonia Technical University of Catalonia. [View Context].

Vikas Sindhwani and P. Bhattacharya and Subrata Rakshit. Information Theoretic Feature Crediting in Multiclass Support Vector Machines. [View Context].

Maria Salamo and Elisabet Golobardes. Analysing Rough Sets weighting methods for Case-Based Reasoning Systems. Enginyeria i Arquitectura La Salle. [View Context].



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""