# Chem Machine Learning Practice

This repository contains practical learning notebooks for chemistry-focused machine learning and cheminformatics.

The current notebooks are starter placeholders. They are intended to be replaced or expanded with real project notebooks covering RDKit, molecular descriptors, QSAR-style modelling, molecular classification and introductory deep learning for chemical data.

## Main aims

- Practise cheminformatics workflows using Python and RDKit
- Convert SMILES strings into molecular objects and features
- Build descriptor and fingerprint datasets
- Train baseline machine learning models for molecular prediction tasks
- Show reproducible notebook-based chemistry ML practice
- Develop a GitHub portfolio for cheminformatics and scientific machine learning

## Repository structure

```text
chem-machine-learning-practice/
├── README.md
├── notebooks/
│   ├── 01_rdkit_molecule_analyser.ipynb
│   ├── 02_molecular_descriptors.ipynb
│   ├── 03_qsar_regression_baseline.ipynb
│   ├── 04_molecular_classification.ipynb
│   └── 05_deep_learning_for_molecules.ipynb
├── src/
│   └── chem_ml_utils.py
├── data/
│   ├── README.md
│   └── example_molecules.csv
├── figures/
├── environment.yml
├── requirements.txt
└── .gitignore
```

## Notebook plan

| Notebook | Purpose |
|---|---|
| `01_rdkit_molecule_analyser.ipynb` | Load SMILES, create RDKit molecules and inspect basic properties |
| `02_molecular_descriptors.ipynb` | Calculate molecular descriptors and build a feature table |
| `03_qsar_regression_baseline.ipynb` | Train a simple regression model using molecular descriptors |
| `04_molecular_classification.ipynb` | Train a simple classifier using descriptors or fingerprints |
| `05_deep_learning_for_molecules.ipynb` | Build an introductory neural-network workflow for molecular features |

## Setup with Conda

```bash
conda env create -f environment.yml
conda activate chem-ml
```

## Setup with pip

```bash
pip install -r requirements.txt
```

RDKit is usually easiest to install via Conda using the `conda-forge` channel.

## Suggested GitHub topics

```text
cheminformatics
machine-learning
chemistry
rdkit
qsar
molecular-descriptors
python
jupyter-notebook
scikit-learn
deep-learning
```

## Data note

Only small public, synthetic or educational example datasets should be committed. Do not upload private research data, proprietary datasets, API keys, credentials or large raw files.

## Status

Work in progress. The starter notebooks are intentionally minimal and will be expanded as the project develops.
