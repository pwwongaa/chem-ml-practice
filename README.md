# 🧪 Chem ML Practice — Cheminformatics Learning Paradise

**A hands-on notebook playground for learning RDKit, QSAR, molecular machine learning and molecular deep learning.**

This repo is designed as a practical learning route rather than a one-off code dump. Each notebook focuses on one modelling idea, contains runnable examples, and includes practice exercises with TODO space plus reference answers.

> Build the full workflow: **SMILES → RDKit molecules → descriptors / fingerprints / graphs → ML models → plots → interpretation**.

---

## ✨ What you will learn

- 🧬 Parse SMILES and work with RDKit molecule objects.
- 📊 Calculate molecular descriptors and inspect chemical trends.
- 🤖 Build descriptor-based QSAR regression models.
- 🧩 Generate Morgan fingerprints and use similarity-style molecular features.
- 🎯 Convert molecular prediction into classification problems.
- 📈 Evaluate models with MAE, RMSE, R², ROC-AUC, PR-AUC and diagnostic plots.
- 🧠 Train neural-network models with PyTorch.
- 🕸️ Explore molecular graph learning with GNN-style workflows.
- 🧪 Compare manual RDKit pipelines with DeepChem-style workflows.

---

## 🧭 Project map

| Project | Notebook | Main idea | What it practises |
|---:|---|---|---|
| 1 | `01_rdkit_molecule_analyser.ipynb` | Basic RDKit molecule analysis | SMILES parsing, molecule drawing, atoms/bonds, descriptors, Lipinski rules, SMARTS patterns |
| 2 | `02_molecular_descriptors_qsar.ipynb` | Descriptor QSAR regression | Public/fallback solubility data, descriptor matrix, regression models, residual/error analysis |
| 3 | `03_morgan_fingerprint_qsar.ipynb` | Morgan fingerprint QSAR | ECFP-style vectors, Tanimoto similarity, fingerprint regression, applicability-domain thinking |
| 4 | `04_molecular_classification.ipynb` | Molecular classification | Binary labels, classifiers, ROC/PR curves, confusion matrix, threshold tuning |
| 5 | `05_deep_learning_chemistry.ipynb` | Molecular deep learning | PyTorch MLP, GNN workflow, DeepChem comparison, model-comparison plots |

---

## 🚀 Recommended learning route

Run the notebooks in order if you are starting from scratch:

1. **RDKit basics** — learn how molecules become Python objects.
2. **Descriptors** — turn molecules into numeric chemistry features.
3. **Fingerprints** — represent molecular substructures as bit vectors.
4. **Classification** — move from continuous prediction to class prediction.
5. **Neural networks** — compare MLP, graph and DeepChem-style approaches.

Each notebook is independent enough to run alone, but the concepts build naturally from Project 1 to Project 5.

---

## 🛠️ Installation

### Recommended: conda

RDKit is usually easiest with `conda-forge`.

```bash
conda env create -f environment.yml
conda activate chem-ml-practice
python -m ipykernel install --user --name chem-ml-practice --display-name "chem-ml-practice"
```

Then open Jupyter and select the `chem-ml-practice` kernel.

```bash
jupyter lab
```

### Minimal pip setup

This is usually enough for Projects 1–4:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Project 5 uses heavier deep-learning packages. See `requirements-optional.txt` for PyTorch Geometric and DeepChem-related dependencies.

---

## 🌐 Public data strategy

Projects 2–5 use a safe public-data strategy:

```text
try public solubility dataset
→ if network fails, use embedded demo data
→ clean SMILES and target values
→ randomly cap at 500 molecules
→ run downstream ML workflow
```

This keeps the notebooks usable in different environments:

- online laptops can use a larger public dataset;
- offline runs still work using the fallback demo table;
- the 500-molecule cap keeps descriptor calculation and model training lightweight.

---

## 🧪 Exercise style

The notebooks use a practical exercise layout:

```text
Exercise — task + guidance
TODO code cell — space to write your own solution
Answer — reference solution
```

The TODO cells are intentionally more open than simple fill-in-the-blank tasks. They are meant for modifying code, writing small functions, generating plots, comparing models and interpreting results.

---

## 📊 What makes this useful as a portfolio repo

This repo demonstrates a complete scientific ML workflow:

- chemical data parsing;
- feature engineering;
- model training;
- model comparison;
- validation plots;
- error analysis;
- public-data handling;
- fallback logic;
- reproducible notebooks;
- clear educational documentation.

It is suitable for showing practical skills in **cheminformatics, bioinformatics-adjacent ML, scientific Python and molecular modelling workflows**.

---

## 📁 Repository structure

```text
chem-ml-practice/
├── notebooks/                  # five main practice notebooks
├── src/                        # reusable helper functions
├── data/                       # small examples and data notes
├── docs/                       # learning notes, validation notes and data strategy
├── scripts/                    # notebook checking scripts
├── figures/                    # optional generated figures
├── outputs/                    # optional generated outputs
├── environment.yml             # conda environment
├── requirements.txt            # core pip dependencies
├── requirements-optional.txt   # optional deep-learning dependencies
├── LICENSE                     # MIT License
└── README.md
```

---

## ✅ Validation and safety checks

The release package is prepared with these checks:

- notebook outputs stripped;
- code cells syntax checked;
- common local paths removed;
- public/fallback data strategy documented;
- exercise and answer sections checked;
- Project 4 ROC/PR plotting block patched to avoid common state/import errors.

See `docs/VALIDATION.md` for details.

---

## ⚠️ Scope and limitations

These notebooks are for education, portfolio practice and prototyping.

They are **not** validated for clinical, regulatory, toxicology, commercial screening or safety-critical decision-making. Model performance depends on dataset quality, chemical coverage, train/test split strategy, molecular representation and target definition.

For stronger research-grade work, future extensions should add:

- scaffold split as the main validation split;
- external test sets;
- hyperparameter tuning;
- uncertainty estimation;
- repeated random seeds;
- better graph features;
- experiment tracking.

---

## 🧑‍💻 Author

Created by **Danny / pwwongaa** as a practical cheminformatics machine-learning learning repo.

---

## 📜 License

MIT License. See `LICENSE`.
