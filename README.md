# Chem Machine Learning Practice

A five-notebook practice repository for cheminformatics, QSAR, molecular machine learning and molecular deep learning. The project is designed as a compact learning portfolio: each notebook is independent, runnable and focused on one modelling idea.

## What this repo demonstrates

- RDKit-based molecule parsing, drawing, descriptor calculation and functional-group checks.
- Descriptor-based QSAR regression with model comparison and diagnostic plots.
- Morgan fingerprint QSAR, applicability-domain analysis and scaffold-aware evaluation.
- Molecular classification with ROC-AUC, PR-AUC, confusion matrices and threshold tuning.
- Deep learning chemistry workflows using PyTorch, PyTorch Geometric-style GNNs and DeepChem data loaders.

## Project map

| Project | Notebook | Main concept | Typical target |
|---|---|---|---|
| 1 | `01_rdkit_molecule_analyser.ipynb` | RDKit molecule analysis | descriptors, Lipinski rules, functional groups |
| 2 | `02_molecular_descriptors_qsar.ipynb` | Descriptor-based QSAR | ESOL logS regression |
| 3 | `03_morgan_fingerprint_qsar.ipynb` | Morgan fingerprint QSAR | logS regression and applicability domain |
| 4 | `04_molecular_classification.ipynb` | Molecular classification | high/low solubility or other binary labels |
| 5 | `05_deep_learning_chemistry.ipynb` | Molecular deep learning | MLP, GNN and DeepChem workflows |

## Learning route

Run the notebooks in order if you are learning from scratch:

1. **Project 1:** Learn how SMILES become RDKit molecule objects and descriptors.
2. **Project 2:** Use descriptors as features for classical QSAR regression.
3. **Project 3:** Use Morgan fingerprints and compare them with descriptors.
4. **Project 4:** Change the problem type from regression to classification.
5. **Project 5:** Replace classical ML with neural-network and graph-learning workflows.

## Installation

Conda is recommended because RDKit is easiest to install from conda-forge.

```bash
conda env create -f environment.yml
conda activate chem-ml-practice
python -m ipykernel install --user --name chem-ml-practice --display-name "chem-ml-practice"
```

Minimal pip setup may also work for Projects 1-4:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Optional deep-learning packages for Project 5 are listed in `requirements-optional.txt`. DeepChem and PyTorch Geometric can be environment-sensitive, especially on Python 3.12 or different CUDA builds. If an optional dependency fails, Projects 1-4 and the PyTorch MLP parts can still be used.

## Data

The notebooks use small embedded examples and public educational datasets, including ESOL/Delaney and Tox21 via public URLs or DeepChem loaders where available. The repository does not include private, commercial or sensitive datasets.

## Validation and safety checks

This repo package was prepared with these checks:

- Notebook outputs stripped to avoid leaking local runtime paths.
- Notebook code cells syntax-checked.
- Repository scanned for common secret patterns.
- Repository scanned for common local path patterns.
- English-only documentation and notebook comments.

See `docs/VALIDATION.md` for details.

## Scope and limitations

These notebooks are for education, portfolio practice and prototyping. They are not validated for clinical, regulatory, commercial screening or safety-critical molecular decision making. Model performance depends on dataset quality, train/test split strategy, chemical domain and target definition.

## Repository structure

```text
chem-machine-learning-practice/
├── notebooks/                  # five independent practice notebooks
├── src/                        # reusable cheminformatics helper functions
├── data/                       # small public/example data only
├── docs/                       # validation notes and project notes
├── scripts/                    # notebook syntax and safety checks
├── figures/                    # optional generated figures
├── outputs/                    # optional generated CSV/model outputs
├── environment.yml             # conda environment
├── requirements.txt            # core pip dependencies
├── requirements-optional.txt   # optional DL/DeepChem dependencies
├── LICENSE                     # MIT License
└── README.md
```

## License

MIT License. See `LICENSE`.
