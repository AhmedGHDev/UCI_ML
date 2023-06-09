import pandas as pd

# INFO
"""
Abstract: Data set containing values for six biomechanical features used to classify orthopaedic patients into 3 classes (normal, disk hernia or spondilolysthesis) or 2 classes (normal or abnormal).

Data Set Characteristics:  

Multivariate

Number of Instances:

310

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

6

Date Donated

2011-08-09

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

217462


Source:

Guilherme de Alencar Barreto (guilherme '@' deti.ufc.br) & Ajalmar RÃªgo da Rocha Neto (ajalmar '@' ifce.edu.br), Department of Teleinformatics Engineering, Federal University of CearÃ¡, Fortaleza, CearÃ¡, Brazil.

Henrique Antonio Fonseca da Mota Filho (hdamota '@' gmail.com), Hospital Monte Klinikum, Fortaleza, CearÃ¡, Brazil.


Data Set Information:

Biomedical data set built by Dr. Henrique da Mota during a medical residence period in the Group of Applied Research in Orthopaedics (GARO) of the Centre MÃ©dico-Chirurgical de RÃ©adaptation des Massues, Lyon, France. The data have been organized in two different but related classification tasks. The first task consists in classifying patients as belonging to one out of three categories: Normal (100 patients), Disk Hernia (60 patients) or Spondylolisthesis (150 patients). For the second task, the categories Disk Hernia and Spondylolisthesis were merged into a single category labelled as 'abnormal'. Thus, the second task consists in classifying patients as belonging to one out of two categories: Normal (100 patients) or Abnormal (210 patients). We provide files also for use within the WEKA environment.


Attribute Information:

Each patient is represented in the data set by six biomechanical attributes derived from the shape and orientation of the pelvis and lumbar spine (in this order): pelvic incidence, pelvic tilt, lumbar lordosis angle, sacral slope, pelvic radius and grade of spondylolisthesis. The following convention is used for the class labels: DH (Disk Hernia), Spondylolisthesis (SL), Normal (NO) and Abnormal (AB).


Relevant Papers:

(1) Berthonnaud, E., Dimnet, J., Roussouly, P. & Labelle, H. (2005). 'Analysis of the sagittal balance of the spine and pelvis using shape and orientation parameters', Journal of Spinal Disorders & Techniques, 18(1):40â€“47.

(2) Rocha Neto, A. R. & Barreto, G. A. (2009). 'On the Application of Ensembles of Classifiers to the Diagnosis of Pathologies of the Vertebral Column: A Comparative Analysis', IEEE Latin America Transactions, 7(4):487-496.

(3) Rocha Neto, A. R., Sousa, R., Barreto, G. A. & Cardoso, J. S. (2011). 'Diagnostic of Pathology on the Vertebral Column with Embedded Reject Optionâ€, Proceedings of the 5th Iberian Conference on Pattern Recognition and Image Analysis (IbPRIA'2011), Gran Canaria, Spain, Lecture Notes on Computer Science, vol. 6669, p. 588-595.



Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""