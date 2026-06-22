# Chem Machine Learning Practice

This repository contains my practical notebooks for learning and applying machine learning in chemistry and cheminformatics. The aim is to build a clean portfolio of reproducible examples covering molecular representation, descriptor calculation, exploratory analysis, QSAR-style modelling and basic deep learning workflows for chemical data.

## Focus areas

* Molecular parsing and standardisation using RDKit
* SMILES-based molecule handling
* Molecular descriptors, fingerprints and physicochemical features
* Exploratory data analysis for chemical datasets
* QSAR-style regression and classification models
* Model evaluation using appropriate metrics
* Visualisation of chemical structures and model outputs
* Reproducible Jupyter notebook workflows

## Planned notebook sequence

| Notebook                               | Topic                               | Main skills demonstrated                              |
| -------------------------------------- | ----------------------------------- | ----------------------------------------------------- |
| `01_rdkit_molecule_analyser.ipynb`     | Basic molecule loading and analysis | SMILES parsing, structure display, descriptors        |
| `02_molecular_descriptors.ipynb`       | Descriptor calculation              | LogP, molecular weight, H-bond donors/acceptors, TPSA |
| `03_qsar_regression_baseline.ipynb`    | Regression modelling                | Feature engineering, train/test split, RMSE, R²       |
| `04_molecular_classification.ipynb`    | Classification modelling            | Fingerprints, classifiers, accuracy, ROC-AUC          |
| `05_deep_learning_for_molecules.ipynb` | Introductory deep learning          | Neural network baseline for chemical features         |

## Example skills shown

This repository demonstrates practical experience in:

* Python
* RDKit
* pandas / NumPy
* scikit-learn
* matplotlib
* Jupyter notebooks
* Molecular descriptors
* Chemical data cleaning
* Machine learning model evaluation

## Repository structure

```text
chem-machine-learning-practice/
├── notebooks/          # Main learning notebooks
├── src/                # Reusable helper functions
├── data/               # Small public example datasets only
├── figures/            # Exported plots and molecule images
├── environment.yml     # Conda environment
├── requirements.txt    # Python package list
└── README.md
```

## Setup

Create the environment with Conda:

```bash
conda env create -f environment.yml
conda activate chem-ml
```

Or install core packages with pip:

```bash
pip install -r requirements.txt
```

## Notes

The notebooks in this repository are for learning, demonstration and portfolio purposes. Any datasets used should be public, synthetic or small example datasets. Large datasets, private files, API keys and unpublished research data should not be committed to the repository.

## Status

Work in progress. More notebooks will be added as I continue developing my chemistry machine learning and cheminformatics workflow.
