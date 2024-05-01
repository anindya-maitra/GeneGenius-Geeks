# GeneGenius-Geeks
This repository is for the ACM kolkata  2024 competition. The project title is: "ANALYSIS OF SIGNALLING PATHWAYS FOR MULTIPLE FAULT SIMULATION AND DRUG THERAPY USING DYNAMIC BAYESIAN NETWORK BASED MODEL AND GPU-ACCELERATED BASED APPROACH"

# Approach
The objective of the project is to explore the use of GPU Acceleration in Drug
Application on Signaling Pathways Containing Multiple Faults utilizing Dynamic
Bayesian Networks for modelling and analysis.
It aims at modelling a Dynamic Bayesian Network (DBN) representing the Growth
Factor (GF) and MAPK Signalling pathways, introduce faults, apply drugs to the
faulty nodes and identify effective custom drugs for inhibition of faults.
The project aims to develop a scalable and efficient GPU-accelerated framework for
simulating DBNs that model temporal dependencies and interactions within
signaling pathways containing multiple faults. Compare the performance and
scalability of the GPU-accelerated and CPU-based methods. Demonstrate the
effectiveness of the proposed approach in identifying potential drug candidates for
pathway restoration.
DBNs provide a probabilistic framework for modeling and analysing the dynamics
of signaling pathways having multiple genetic faults on pathway behaviour.
However, as the number of faults and the size of the pathway increase, the
computational demands for analysis become substantial. Graphics Processing Units
(GPUs) offer massive parallel processing capabilities, making them well-suited for
this project.
Modeling of the DBN for GF and MAPK Signaling Pathways is done by using a
Directed Acyclic Graph(DAG). Each node and edge representing a Protein and the
Protein-Protein Interaction respectively. The Conditional Probability Data of each
node is also provided. The GF Proteins are the root nodes, the Transcription Factor
and Residual Proteins are the leaf nodes and the remaining proteins of the signaling
pathway are represented by the internal nodes. Faults are introduced by changing
the Conditional Probability Data of the Faulty Nodes and the Faulty Output Vector
is compared to the Faultless output of all 0’s. The Known Drugs are applied in
combination to their Inhibition Points and the corresponding Output Vectors are
generated. These are converted to encoded weight which is used for scoring.
Encoding is a computationally intensive task thus, GPU is implemented by the
PyCuda Library Module of Python. Customed drugs are simulated and compared
against the known drug combinations on the basis of the efficiency_scores.
GPU Accelerated Drug Application On Signaling Pathways Containing Multiple Faults Using
Dynamic Bayesian Networks
4
Optimization techniques are applied to the application of drugs to the faulty nodes.
The graphical representations of the optimized values help to achieve the same more
efficiently. The user interface is designed so that the user can inquiry the graphs and
plots related to the project in a simple, effective and efficient manner.
Parallel execution of independent drug application jobs would help us to obtain re-
sults in a much faster time frame. Custom nodes in the DBN are chosen as drug
inhibition points for more efficient results than known drugs.
