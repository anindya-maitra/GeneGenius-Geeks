# GeneGenius-Geeks
This repository is for the ACM kolkata  2024 competition. The project title is: "ANALYSIS OF SIGNALLING PATHWAYS FOR MULTIPLE FAULT SIMULATION AND DRUG THERAPY USING DYNAMIC BAYESIAN NETWORK BASED MODEL AND GPU-ACCELERATED BASED APPROACH"

# Approach
Our project investigates cell growth regulation and its disruptions, leading to uncontrolled cell division and apoptosis- key features of cancerous conditions. We use Dynamic Bayesian Networks (DBNs) to model these disruptions and simulate the intricate dynamics of cancer. Our ultimate aim is to develop a GPU-accelerated drug application that can identify and target multiple faults in signaling pathways, leading to the discovery of custom drug combinations that effectively inhibit these faults. This enables the discovery of custom drug combinations that effectively inhibit them. Modelling these faults reveals the complexity of concurrent dysfunctions. Cell growth regulation is a highly complex process controlled by a multitude of signaling pathways that ensure balanced cell proliferation and programmed cell death (apoptosis). When these pathways malfunction, it can result in cancer, characterized by uncontrolled cell growth and evasion of apoptosis. Traditional approaches to understanding and treating these conditions have often fallen short due to the complexity and concurrent nature of multiple pathway disruptions. Thus, there is a critical need for more sophisticated computational methods to model these conditions and develop effective treatments. So, we develop GPU-accelerated drug applications using DBNs to identify and target multiple faults in modelled pathways, discover custom drug combinations for inhibition, and enhance drug efficacy in treating cancer. The efficiency_score parameter identifies optimized drug combinations without prior knowledge of specific malfunctions. GPU acceleration enhances speed and efficiency for identifying drug combinations that score higher than known ones for pathway restoration and control of untriggered cell division. One of the significant advantages of our approach is its ability to uncover synergistic effects between drugs that might be missed by traditional screening methods. Cancer treatment often requires a combination of drugs to tackle the disease's multifaceted nature, and our method is particularly adept at identifying such combinations. By simulating the concurrent effects of multiple drugs on the modelled pathways, we can pinpoint interactions that lead to enhanced therapeutic outcomes. The implications of our work extend beyond just identifying effective drug combinations. By providing a more nuanced understanding of the multiple fault dynamics within signaling pathways, our models can offer insights into the underlying mechanisms of cancer progression. This knowledge can inform the development of new therapeutic strategies and guide experimental research. Thus, our approach offers improved drug efficacy in treating conditions like cancer, potentially leading to more effective therapies.

# Hierarchy of modules
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/4875139b-0b6b-44f1-864f-97e705b38ec5)

# Proposed Solution
1. Dynamic Bayesian Network Modeling
Modeling of the Dynamic Bayesian Network for Growth Factor Signaling Pathway and MAPK Signaling Pathway using a Directed Acyclic Graph and corresponding Conditional Probabilities related to it.
1.1	Obtain related data and model the Dynamic Bayesian Network
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/5765a81c-2035-4e92-b8e4-2b45d2c935fb)
1.2	Find the Unique Input Vector
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/4f226f7f-9eb2-40de-b531-5c0772685c8b)
2.	Fault Modeling
Faults are introduced in the Signaling pathway by changing the Conditional Probability Data of the Internal Faulty Nodes and the Faulty Output Vector is compared to the Faultless output of all 0’s.
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/24f6e9b6-e5f0-4a00-9eff-2fd7e0fe903c)
3. Application of Known Drugs
The Known Drugs are applied in combination to their Inhibition Points that are the faulty internal nodes and the corresponding Output Vectors are generated.
3.1.	Application of drugs to faulty nodes and data generation 
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/3a6abe56-a091-4cfb-887f-b303a69730f2)
3.2.	Encoding and Parallelization
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/b7361f85-3fa3-4ff9-b3e3-60c737a922e8)
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/e0a7fd5f-b647-4fa6-bad2-028f255fcdb2)
3.3.	Scoring
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/2ea7f969-916d-411d-b673-ebbf3e21bb66)
4.	Searching for Custom Drugs Inhibition Points
Customed drugs are simulated and compared against the known drug combinations on the basis of the efficiency_scores.
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/955d1f9f-bbd3-4d1c-befe-76271cbf5b1d)
5.	Optimization
Optimization techniques are applied to the application of drugs to the faulty nodes. The graphical representations of the optimized values help to achieve the same more efficiently.
FLOWCHART:
![image](https://github.com/anindya-maitra/GeneGenius-Geeks/assets/85032238/2d330f55-2ed0-44a2-9bc0-defff2c837c0)
