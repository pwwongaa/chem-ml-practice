# Project notes

## Project 1 — RDKit Molecule Analyser

Focus: molecule parsing, drawing, descriptor calculation, Lipinski checks and functional-group detection.

Use this notebook to understand the cheminformatics objects used by all later projects.

## Project 2 — Molecular Descriptors QSAR

Focus: descriptor-based regression. Molecules are converted into numerical descriptor tables, then classical ML models predict a continuous molecular property such as logS.

Key learning: features, train/test split, regression metrics, feature importance and residual analysis.

## Project 3 — Morgan Fingerprint QSAR

Focus: structural fingerprints. Morgan fingerprints encode local molecular substructures and can be used alone or combined with descriptors.

Key learning: fingerprint density, inactive-bit filtering, applicability domain, Tanimoto similarity and scaffold split challenge.

## Project 4 — Molecular Classification

Focus: classification rather than regression. Targets become class labels, so evaluation changes from RMSE/R2 to precision, recall, F1, ROC-AUC, PR-AUC and confusion matrices.

Key learning: class balance, probability thresholds and chemical error analysis.

## Project 5 — Deep Learning Chemistry

Focus: neural-network molecular prediction. The notebook includes fingerprint MLPs, graph neural network concepts and DeepChem-based workflows.

Key learning: PyTorch datasets, MLP regression/classification, GNN graph representation, optional DeepChem loaders and benchmark-style evaluation.
