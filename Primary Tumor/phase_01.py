import pandas as pd


#Step 00: Loading data

# INFO
"""
Abstract: From Ljubljana Oncology Institute

Data Set Characteristics:  

Multivariate

Number of Instances:

339

Area:

Life

Attribute Characteristics:

Categorical

Number of Attributes:

17

Date Donated

1988-11-01

Associated Tasks:

Classification

Missing Values?

Yes

Number of Web Hits:

177515


Source:

Donors:

1. Igor Kononenko,
University E.Kardelj
Faculty for electrical engineering
Trzaska 25
61000 Ljubljana (tel.: (38)(+61) 265-161

2. Bojan Cestnik
Jozef Stefan Institute
Jamova 39
61000 Ljubljana
Yugoslavia (tel.: (38)(+61) 214-399 ext.287)


Data Set Information:

This is one of three domains provided by the Oncology Institutenthat has repeatedly appeared in the machine learning literature.

(See also breast-cancer and lymphography.)


Attribute Information:

--- NOTE: All attribute values in the database have been entered as numeric values corresponding to their index in the list of attribute values for that attribute domain as given below.
1. class: lung, head & neck, esophasus, thyroid, stomach, duoden & sm.int, colon, rectum, anus, salivary glands, pancreas, gallblader, liver, kidney, bladder, testis, prostate, ovary, corpus uteri, cervix uteri, vagina, breast
2. age: <30, 30-59, >=60
3. sex: male, female
4. histologic-type: epidermoid, adeno, anaplastic
5. degree-of-diffe: well, fairly, poorly
6. bone: yes, no
7. bone-marrow: yes, no
8. lung: yes, no
9. pleura: yes, no
10. peritoneum: yes, no
11. liver: yes, no
12. brain: yes, no
13. skin: yes, no
14. neck: yes, no
15. supraclavicular: yes, no
16. axillar: yes, no
17. mediastinum: yes, no
18. abdominal: yes, no


Relevant Papers:

Cestnik,G., Konenenko,I, & Bratko,I. (1987). Assistant-86: A Knowledge-Elicitation Tool for Sophisticated Users. In I.Bratko & N.Lavrac (Eds.) Progress in Machine Learning, 31-45, Sigma Press.
[Web Link]

Clark,P. & Niblett,T. (1987). Induction in Noisy Domains. In I.Bratko & N.Lavrac (Eds.) Progress in Machine Learning, 11-30, Sigma Press.
[Web Link]

Michalski,R., Mozetic,I. Hong,J., & Lavrac,N. (1986). The Multi-Purpose Incremental Learning System AQ15 and its Testing Applications to Three Medical Domains. In Proceedings of the Fifth National Conference on Artificial Intelligence, 1041-1045. Philadelphia, PA: Morgan Kaufmann.
[Web Link]


Papers That Cite This Data Set1:


Xavier Llor and David E. Goldberg and Ivan Traus and Ester Bernad i Mansilla. Accuracy, Parsimony, and Generality in Evolutionary Learning Systems via Multiobjective Selection. IWLCS. 2002. [View Context].

Remco R. Bouckaert. Accuracy bounds for ensembles under 0 { 1 loss. Xtal Mountain Information Technology & Computer Science Department, University of Waikato. 2002. [View Context].

Igor Kononenko and Edvard Simec and Marko Robnik-Sikonja. Overcoming the Myopia of Inductive Learning Algorithms with RELIEFF. Appl. Intell, 7. 1997. [View Context].

Pedro Domingos. Control-Sensitive Feature Selection for Lazy Learners. Artif. Intell. Rev, 11. 1997. [View Context].

Kamal Ali and Michael J. Pazzani. Error Reduction through Learning Multiple Descriptions. Machine Learning, 24. 1996. [View Context].

Geoffrey I. Webb. OPUS: An Efficient Admissible Algorithm for Unordered Search. J. Artif. Intell. Res. (JAIR, 3. 1995. [View Context].

Geoffrey I Webb. Learning Decision Lists by Prepending Inferred Rules. School of Computing and Mathematics Deakin University. [View Context].

Alexander K. Seewald. Dissertation Towards Understanding Stacking Studies of a General Ensemble Learning Scheme ausgefuhrt zum Zwecke der Erlangung des akademischen Grades eines Doktors der technischen Naturwissenschaften. [View Context].



Citation Request:

This primary tumor domain was obtained from the University Medical Centre, Institute of Oncology, Ljubljana, Yugoslavia. Thanks go to M. Zwitter and M. Soklic for providing the data. Please include this citation if you plan to use this database.
"""

#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/primary-tumor/primary-tumor.data",names=['class', 'age', 'sex', 'histologic-type', 'degree-of-diffe', 'bone', 'bone-marrow', 'lung', 'pleura', 'peritoneum', 'liver', 'brain', 'skin', 'neck', 'supraclavicular', 'axillar', 'mediastinum', 'abdominal'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/primary-tumor/primary-tumor.data",names=['class', 'age', 'sex', 'histologic-type', 'degree-of-diffe', 'bone', 'bone-marrow', 'lung', 'pleura', 'peritoneum', 'liver', 'brain', 'skin', 'neck', 'supraclavicular', 'axillar', 'mediastinum', 'abdominal'])

print(df.info())